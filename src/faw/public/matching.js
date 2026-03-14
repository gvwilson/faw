// src/styles.css
var styles_default = ".faw { padding: 4px 0; }\n\n.faw-question { font-size: 1.1em; font-weight: 600; margin-bottom: 12px; }\n.faw-instructions { font-size: 0.9em; color: var(--muted-foreground); margin-bottom: 12px; }\n\n.faw-btn {\n  padding: 10px 20px; border: none; border-radius: var(--radius);\n  font: inherit; font-weight: 600; cursor: pointer;\n}\n.faw-btn-primary { background: var(--primary); color: var(--primary-foreground); }\n.faw-btn-primary:hover:not(:disabled) { opacity: 0.9; }\n.faw-btn-secondary { background: var(--secondary); color: var(--secondary-foreground); border: 1px solid var(--border); }\n.faw-btn-secondary:hover:not(:disabled) { opacity: 0.85; }\n.faw-btn:disabled { opacity: 0.45; cursor: not-allowed; }\n\n.faw-feedback { font-weight: 600; margin-top: 12px; }\n.faw-correct { color: #28a745; }\n.faw-incorrect { color: var(--destructive); }\n\n.faw-options { margin-bottom: 12px; }\n.faw-option {\n  padding: 10px; margin: 6px 0;\n  border: 2px solid var(--border); border-radius: var(--radius);\n  cursor: pointer; transition: background .2s, border-color .2s;\n}\n.faw-option:hover:not(.faw-answered) { background: var(--accent); border-color: var(--primary); }\n.faw-option.faw-answered { cursor: not-allowed; }\n.faw-option.faw-correct { background: #d4edda; border-color: #28a745; }\n.faw-option.faw-incorrect { background: #f8d7da; border-color: var(--destructive); }\n.faw-option.faw-faded { opacity: .5; }\n.faw-explanation {\n  padding: 10px; margin-top: 10px;\n  background: var(--muted); border-left: 4px solid var(--primary); border-radius: var(--radius);\n}\n\n.faw-matching-three-col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 16px; }\n.faw-column { display: flex; flex-direction: column; gap: 10px; }\n.faw-item-fixed {\n  padding: 10px; background: var(--accent); border: 2px solid var(--primary);\n  border-radius: var(--radius); font-weight: 500;\n}\n.faw-item-fixed.faw-correct { background: #d4edda; border-color: #28a745; }\n.faw-item-fixed.faw-incorrect { background: #f8d7da; border-color: var(--destructive); }\n.faw-drop-zone {\n  padding: 10px; min-height: 40px; background: var(--muted);\n  border: 2px dashed var(--border); border-radius: var(--radius);\n  text-align: center; color: var(--muted-foreground); font-style: italic;\n  cursor: pointer; transition: all .2s;\n}\n.faw-drop-zone.faw-filled { background: var(--secondary); border-style: solid; color: inherit; font-style: normal; font-weight: 500; }\n.faw-drop-zone.faw-drop-target, .faw-label-drop-zone.faw-drop-target { background: #fff9c4; border-color: #fbc02d; }\n.faw-drop-zone.faw-correct { background: #d4edda; border-color: #28a745; }\n.faw-drop-zone.faw-incorrect { background: #f8d7da; border-color: var(--destructive); }\n.faw-item-draggable {\n  padding: 10px; background: #fff3e0; border: 2px solid #ff9800;\n  border-radius: var(--radius); font-weight: 500;\n}\n\n.faw-ordering-items { margin-bottom: 16px; }\n.faw-ordering-item {\n  display: flex; align-items: center; gap: 10px;\n  margin-bottom: 6px; padding: 10px;\n  border: 2px solid var(--border); border-radius: var(--radius);\n}\n.faw-ordering-item.faw-drop-target { background: #fff9c4; border-style: dashed; }\n.faw-ordering-item.faw-correct { background: #d4edda; border-color: #28a745; }\n.faw-ordering-item.faw-incorrect { background: #f8d7da; border-color: var(--destructive); }\n.faw-ordering-text { flex: 1; }\n\n.faw-ordering-item, .faw-item-draggable, .faw-label-num, .faw-label-badge { cursor: grab; }\n.faw-ordering-item:active, .faw-item-draggable:active, .faw-label-num:active, .faw-label-badge:active { cursor: grabbing; }\n.faw-ordering-item.faw-dragging, .faw-item-draggable.faw-dragging, .faw-label-num.faw-dragging, .faw-label-badge.faw-dragging { opacity: .5; }\n\n.faw-position, .faw-label-num {\n  min-width: 30px; height: 30px; background: var(--primary); color: var(--primary-foreground);\n  border-radius: 50%; display: flex; align-items: center;\n  justify-content: center; font-weight: 600; flex-shrink: 0;\n}\n.faw-label-badge {\n  min-width: 24px; height: 24px; background: var(--primary); color: var(--primary-foreground);\n  border-radius: 50%; display: flex; align-items: center;\n  justify-content: center; font-size: 0.8em; font-weight: 600; flex-shrink: 0;\n}\n.faw-label-badge.faw-correct { background: #28a745; color: white; }\n.faw-label-badge.faw-incorrect { background: var(--destructive); color: white; }\n\n.faw-labeling-area { display: grid; grid-template-columns: 1fr 2fr; gap: 16px; margin-bottom: 16px; }\n.faw-labeling-labels, .faw-labeling-text { display: flex; flex-direction: column; gap: 10px; }\n.faw-labeling-title { font-weight: 600; color: var(--muted-foreground); margin-bottom: 6px; }\n.faw-label-item { display: flex; align-items: center; gap: 8px; padding: 6px; border-radius: var(--radius); }\n.faw-text-lines { display: flex; flex-direction: column; gap: 8px; }\n.faw-text-line { display: flex; align-items: flex-start; gap: 8px; }\n.faw-label-drop-zone {\n  min-width: 60px; min-height: 30px; padding: 4px;\n  background: var(--muted); border: 2px dashed var(--border); border-radius: var(--radius);\n  display: flex; flex-wrap: wrap; gap: 4px; align-content: flex-start; flex-shrink: 0;\n}\n.faw-text-content { flex: 1; padding: 4px 0; line-height: 1.5; }\n\n.faw-card {\n  min-height: 140px; padding: 32px 20px; border-radius: var(--radius);\n  display: flex; align-items: center; justify-content: center;\n  font-size: 1.2em; text-align: center; margin-bottom: 12px; transition: all .3s;\n}\n.faw-card-front { background: var(--accent); border: 2px solid var(--primary); }\n.faw-card-back  { background: var(--muted); border: 2px solid var(--border); }\n.faw-rating-btns { display: flex; gap: 8px; margin-bottom: 12px; }\n.faw-progress { height: 6px; background: var(--muted); border-radius: 4px; margin-bottom: 10px; }\n.faw-progress-fill { height: 100%; background: var(--primary); border-radius: 4px; transition: width .3s; }\n\n.faw-cm-workspace {\n  position: relative; height: 360px;\n  border: 1px solid var(--border); border-radius: var(--radius);\n  margin-bottom: 12px; overflow: hidden; background: var(--muted);\n}\n.faw-cm-svg { position: absolute; top: 0; left: 0; width: 100%; height: 100%; overflow: visible; }\n.faw-cm-node {\n  position: absolute; transform: translate(-50%, -50%);\n  padding: 8px 14px; background: var(--card); border: 2px solid var(--primary);\n  border-radius: var(--radius); cursor: move; user-select: none;\n  font-weight: 500; z-index: 1; white-space: nowrap;\n}\n.faw-cm-node.faw-cm-pending { box-shadow: 0 0 0 3px var(--primary); background: var(--accent); }\n.faw-cm-terms { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 10px; }\n.faw-cm-term {\n  padding: 5px 14px; border: 2px solid var(--border); border-radius: 20px;\n  background: var(--muted); cursor: pointer; font: inherit; font-size: 0.9em; transition: all .15s;\n}\n.faw-cm-term:hover:not(:disabled) { border-color: var(--primary); background: var(--accent); }\n.faw-cm-term.faw-cm-term-selected { background: var(--primary); color: var(--primary-foreground); border-color: var(--primary); }\n.faw-cm-term:disabled { opacity: 0.45; cursor: not-allowed; }\n.faw-cm-edge-list { display: flex; flex-direction: column; gap: 4px; margin-bottom: 10px; }\n.faw-cm-edge-row {\n  display: flex; align-items: center; gap: 6px;\n  padding: 4px 8px; background: var(--muted); border-radius: var(--radius); font-size: 0.9em;\n}\n.faw-cm-edge-label { padding: 2px 8px; background: var(--accent); border-radius: 10px; font-size: 0.85em; font-weight: 500; }\n.faw-cm-edge-remove { margin-left: auto; background: none; border: none; cursor: pointer; color: var(--muted-foreground); padding: 2px 4px; border-radius: 4px; }\n.faw-cm-edge-remove:hover { color: #dc3545; background: #f8d7da; }\n";

// src/matching.js
function mk(tag, cls, txt) {
  const el = document.createElement(tag);
  if (cls) el.className = cls;
  if (txt !== void 0) el.textContent = txt;
  return el;
}
function render({ model, el }) {
  const s = mk("style");
  s.textContent = styles_default;
  el.appendChild(s);
  const container = mk("div", "faw");
  container.appendChild(mk("div", "faw-question", model.get("question")));
  container.appendChild(mk("div", "faw-instructions", "Drag labels from the right column to match with items on the left:"));
  const left = model.get("left"), right = model.get("right");
  const correctMap = Object.fromEntries(Object.entries(model.get("correct_matches")).map(([k, v]) => [+k, +v]));
  const matches = {};
  let submitted = false;
  const grid = mk("div", "faw-matching-three-col");
  const leftCol = mk("div", "faw-column"), midCol = mk("div", "faw-column"), rightCol = mk("div", "faw-column");
  const leftItems = left.map((text) => {
    const d = mk("div", "faw-item-fixed", text);
    leftCol.appendChild(d);
    return d;
  });
  const zones = left.map((_, li) => {
    const z = mk("div", "faw-drop-zone", "(drop here)");
    z.addEventListener("dragover", (e) => {
      if (submitted) return;
      e.preventDefault();
      z.classList.add("faw-drop-target");
    });
    z.addEventListener("dragleave", () => z.classList.remove("faw-drop-target"));
    z.addEventListener("drop", (e) => {
      if (submitted) return;
      e.preventDefault();
      z.classList.remove("faw-drop-target");
      const ri = parseInt(e.dataTransfer.getData("text/plain"));
      z.textContent = right[ri];
      z.className = "faw-drop-zone faw-filled";
      matches[li] = ri;
      sync();
      z.addEventListener("click", () => {
        if (submitted) return;
        z.textContent = "(drop here)";
        z.className = "faw-drop-zone";
        delete matches[li];
        sync();
      });
    });
    midCol.appendChild(z);
    return z;
  });
  right.forEach((text, i) => {
    const d = mk("div", "faw-item-draggable", text);
    d.draggable = true;
    d.addEventListener("dragstart", (e) => {
      if (submitted) return;
      d.classList.add("faw-dragging");
      e.dataTransfer.effectAllowed = "copy";
      e.dataTransfer.setData("text/plain", i);
    });
    d.addEventListener("dragend", () => d.classList.remove("faw-dragging"));
    rightCol.appendChild(d);
  });
  grid.append(leftCol, midCol, rightCol);
  container.appendChild(grid);
  const submitBtn = mk("button", "faw-btn faw-btn-primary", "Check Answers");
  submitBtn.style.marginBottom = "16px";
  submitBtn.addEventListener("click", () => {
    if (submitted) return;
    if (Object.keys(matches).length !== left.length) {
      alert("Please match all items before checking answers.");
      return;
    }
    submitted = true;
    submitBtn.disabled = true;
    rightCol.querySelectorAll(".faw-item-draggable").forEach((d) => {
      d.draggable = false;
      d.style.cssText = "cursor:default;opacity:.5";
    });
    let score = 0;
    zones.forEach((z, li) => {
      const ok = matches[li] === correctMap[li];
      if (ok) score++;
      leftItems[li].classList.add(ok ? "faw-correct" : "faw-incorrect");
      z.classList.add(ok ? "faw-correct" : "faw-incorrect");
      z.appendChild(mk("span", ok ? "faw-correct" : "faw-incorrect", ok ? " \u2713" : " \u2717"));
    });
    container.appendChild(mk("div", `faw-feedback ${score === left.length ? "faw-correct" : "faw-incorrect"}`, `Score: ${score}/${left.length} correct`));
    model.set("value", { matches, correct: score === left.length, score, total: left.length });
    model.save_changes();
  });
  container.appendChild(submitBtn);
  el.appendChild(container);
  function sync() {
    model.set("value", { matches, correct: false, score: 0, total: left.length });
    model.save_changes();
  }
}
var matching_default = { render };
export {
  matching_default as default
};
//# sourceMappingURL=matching.js.map
