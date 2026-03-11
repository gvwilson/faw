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

  const opts = mk('div', 'faw-options');
  const options = model.get('options');
  const correct = model.get('correct_answer');
  let answered = false;

  const feedbackEl = mk('div'); feedbackEl.style.display = 'none';
  const explanationEl = mk('div'); explanationEl.style.display = 'none';

  options.forEach((text, i) => {
    const div = mk('div', 'faw-option');
    const radio = mk('input'); radio.type = 'radio'; radio.name = 'answer'; radio.value = i; radio.id = `opt-${i}`; radio.style.marginRight = '10px';
    const lbl = mk('label'); lbl.htmlFor = `opt-${i}`; lbl.textContent = text; lbl.style.cursor = 'pointer';
    div.append(radio, lbl);

    const select = () => {
      if (answered) return;
      radio.checked = true;
      answered = true;
      [...opts.children].forEach((opt, j) => {
        opt.classList.add('faw-answered', j === correct ? 'faw-correct' : j === i ? 'faw-incorrect' : 'faw-faded');
      });
      const ok = i === correct;
      feedbackEl.textContent = ok ? '✓ Correct!' : '✗ Incorrect';
      feedbackEl.className = `faw-feedback ${ok ? 'faw-correct' : 'faw-incorrect'}`;
      feedbackEl.style.display = 'block';
      const expl = model.get('explanation');
      if (expl) { explanationEl.textContent = expl; explanationEl.className = 'faw-explanation'; explanationEl.style.display = 'block'; }
      model.set('value', { selected: i, correct: ok, answered: true });
      model.save_changes();
    };

    div.addEventListener('click', select);
    radio.addEventListener('change', select);
    opts.appendChild(div);
  });

  container.append(opts, feedbackEl, explanationEl);
  el.appendChild(container);
}

export default { render };
