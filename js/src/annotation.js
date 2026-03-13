import styles from './styles.css';

function mk(tag, cls, txt) {
  const el = document.createElement(tag);
  if (cls) el.className = cls;
  if (txt !== undefined) el.textContent = txt;
  return el;
}

function render({ model, el }) {
  const s = mk('style'); s.textContent = styles; el.appendChild(s);
  const container = mk('div', 'faw');
  container.appendChild(mk('div', 'faw-question', model.get('question')));
  container.appendChild(mk('div', 'faw-instructions', 'Drag labels onto the image. Click a placed label to remove it.'));

  const labels = model.get('labels');
  const targets = model.get('targets');
  const placed = {};   // labelIndex -> {x, y} in % of image dimensions
  let submitted = false;

  const area = mk('div', 'faw-annotation-area');

  // --- Sidebar ---
  const labelsCol = mk('div', 'faw-annotation-labels');
  labelsCol.appendChild(mk('div', 'faw-labeling-title', 'Labels:'));
  labels.forEach((text, li) => {
    const chip = mk('div', 'faw-annotation-chip');
    chip.draggable = true;
    chip.append(mk('span', 'faw-label-num', li + 1), mk('span', 'faw-label-text', text));
    chip.addEventListener('dragstart', e => {
      if (submitted) return;
      e.dataTransfer.effectAllowed = 'copy';
      e.dataTransfer.setData('text/plain', String(li));
      chip.classList.add('faw-dragging');
    });
    chip.addEventListener('dragend', () => chip.classList.remove('faw-dragging'));
    labelsCol.appendChild(chip);
  });

  // --- Image wrapper ---
  const imgWrapper = mk('div', 'faw-annotation-image-wrapper');
  const img = mk('img');
  img.src = model.get('image_url');
  img.className = 'faw-annotation-img';
  img.draggable = false;
  imgWrapper.appendChild(img);

  imgWrapper.addEventListener('dragover', e => {
    if (submitted) return;
    e.preventDefault();
    imgWrapper.classList.add('faw-drop-target');
  });
  imgWrapper.addEventListener('dragleave', e => {
    if (e.relatedTarget && imgWrapper.contains(e.relatedTarget)) return;
    imgWrapper.classList.remove('faw-drop-target');
  });
  imgWrapper.addEventListener('drop', e => {
    if (submitted) return;
    e.preventDefault();
    imgWrapper.classList.remove('faw-drop-target');
    const li = parseInt(e.dataTransfer.getData('text/plain'));
    const rect = imgWrapper.getBoundingClientRect();
    placed[li] = {
      x: (e.clientX - rect.left) / rect.width * 100,
      y: (e.clientY - rect.top) / rect.height * 100,
    };
    renderBadges();
    sync();
  });

  function renderBadges() {
    imgWrapper.querySelectorAll('.faw-annotation-badge').forEach(b => b.remove());
    Object.entries(placed).forEach(([li, pos]) => {
      li = parseInt(li);
      const badge = mk('div', 'faw-annotation-badge', li + 1);
      badge.style.left = pos.x + '%';
      badge.style.top = pos.y + '%';
      badge.title = labels[li];
      badge.draggable = true;
      badge.addEventListener('dragstart', e => {
        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('text/plain', String(li));
        badge.classList.add('faw-dragging');
        e.stopPropagation();
      });
      badge.addEventListener('dragend', () => badge.classList.remove('faw-dragging'));
      badge.addEventListener('click', () => { delete placed[li]; renderBadges(); sync(); });
      imgWrapper.appendChild(badge);
    });
  }

  area.append(labelsCol, imgWrapper);
  container.appendChild(area);

  // --- Submit ---
  const submitBtn = mk('button', 'faw-btn faw-btn-primary', 'Check Annotations');
  submitBtn.style.marginTop = '16px';
  submitBtn.addEventListener('click', () => {
    if (submitted) return;
    submitted = true;
    submitBtn.disabled = true;

    let score = 0;
    const total = labels.length;
    const results = {};
    labels.forEach((_, li) => {
      const pos = placed[li];
      const target = targets[li];
      let correct = false;
      if (pos && target) {
        const dx = pos.x - target.x, dy = pos.y - target.y;
        correct = Math.sqrt(dx * dx + dy * dy) <= target.radius;
      }
      if (correct) score++;
      results[li] = { placed: pos || null, correct };
    });

    // Replace badges with scored versions and show target markers
    imgWrapper.querySelectorAll('.faw-annotation-badge, .faw-annotation-target').forEach(b => b.remove());
    labels.forEach((text, li) => {
      const target = targets[li];
      const tgt = mk('div', 'faw-annotation-target');
      tgt.style.left = target.x + '%';
      tgt.style.top = target.y + '%';
      tgt.title = text;
      imgWrapper.appendChild(tgt);
      const pos = placed[li];
      if (pos) {
        const badge = mk('div', `faw-annotation-badge ${results[li].correct ? 'faw-correct' : 'faw-incorrect'}`, li + 1);
        badge.style.left = pos.x + '%';
        badge.style.top = pos.y + '%';
        badge.title = text;
        imgWrapper.appendChild(badge);
      }
    });

    const pct = total ? Math.round(score / total * 100) : 0;
    container.appendChild(mk('div', `faw-feedback ${score === total ? 'faw-correct' : 'faw-incorrect'}`,
      `Score: ${score}/${total} correct (${pct}%)`));
    model.set('value', { results, score, total, correct: score === total });
    model.save_changes();
  });

  container.appendChild(submitBtn);
  el.appendChild(container);

  function sync() {
    if (!submitted) {
      model.set('value', { placed, score: 0, total: labels.length, correct: false });
      model.save_changes();
    }
  }
}

export default { render };
