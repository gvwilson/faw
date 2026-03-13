"""
Example Marimo Notebook: Education Widgets Demo

This notebook demonstrates all three educational widgets.
Run with: marimo edit example_notebook.py
"""

import marimo

__generated_with = "0.19.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    from faw import (
        AnnotationWidget,
        ConceptMapWidget,
        FlashcardWidget,
        LabelingWidget,
        MatchingWidget,
        MultipleChoiceWidget,
        OrderingWidget,
    )

    return (
        AnnotationWidget,
        ConceptMapWidget,
        FlashcardWidget,
        LabelingWidget,
        MatchingWidget,
        MultipleChoiceWidget,
        OrderingWidget,
    )


@app.cell
def _(mo):
    mo.md("""
    # Educational Widgets Demo

    This notebook demonstrates interactive self-test questions.
    """)
    return


# ---------------------------------------------------------------------------
# Annotation
# ---------------------------------------------------------------------------

@app.cell
def _(mo):
    annotation_reset = mo.ui.button(label="↺ Reset")
    mo.vstack([mo.md("## Annotation Question"), annotation_reset])
    return (annotation_reset,)


@app.cell
def _(AnnotationWidget, annotation_reset, mo):
    import urllib.parse

    _ = annotation_reset.value
    # Each labeled element is an explicit rect+text box so target centres
    # are exact pixel coordinates, not font-metric estimates.
    # SVG: 560 × 180, viewBox ensures correct scaling as a responsive <img>.
    # Box centres (px): for=(38,41), item=(111,41), collection=(257,41), process(item)=(171,129)
    # Target %: x = centre_x/560, y = centre_y/180
    _svg = (
        '<svg xmlns="http://www.w3.org/2000/svg"'
        ' viewBox="0 0 560 180" width="560" height="180"'
        ' font-family="monospace" font-size="18">'
        '<rect width="560" height="180" fill="#1e1e1e" rx="6"/>'
        # "for" keyword box  (x=12, w=52 → centre_x=38)
        '<rect x="12" y="22" width="52" height="38" rx="4"'
        ' fill="#1f3a52" stroke="#569cd6" stroke-width="2"/>'
        '<text x="38" y="47" text-anchor="middle"'
        ' fill="#569cd6" font-weight="bold">for</text>'
        # "item" loop-variable box  (x=82, w=58 → centre_x=111)
        '<rect x="82" y="22" width="58" height="38" rx="4"'
        ' fill="#1a3a2a" stroke="#9cdcfe" stroke-width="2"/>'
        '<text x="111" y="47" text-anchor="middle" fill="#9cdcfe">item</text>'
        # "in" — unlabeled, plain text
        '<text x="155" y="47" fill="#569cd6">in</text>'
        # "collection" iterable box  (x=190, w=134 → centre_x=257)
        '<rect x="190" y="22" width="134" height="38" rx="4"'
        ' fill="#1a3a3a" stroke="#4ec9b0" stroke-width="2"/>'
        '<text x="257" y="47" text-anchor="middle" fill="#4ec9b0">collection</text>'
        '<text x="334" y="47" fill="#d4d4d4">:</text>'
        # "process(item)" loop-body box  (x=82, w=178 → centre_x=171)
        '<rect x="82" y="110" width="178" height="38" rx="4"'
        ' fill="#2a2a1a" stroke="#dcdcaa" stroke-width="2"/>'
        '<text x="171" y="135" text-anchor="middle"'
        ' fill="#dcdcaa">process(item)</text>'
        '</svg>'
    )
    _image_url = "data:image/svg+xml," + urllib.parse.quote(_svg)
    annotation_question = mo.ui.anywidget(
        AnnotationWidget(
            question="Drag each label to the matching part of the for-loop:",
            image_url=_image_url,
            labels=["keyword", "loop variable", "iterable", "loop body"],
            targets=[
                # x = centre_x / 560,  y = centre_y / 180
                {"x":  6.8, "y": 22.8, "radius":  5},  # "for"      (38, 41)
                {"x": 19.8, "y": 22.8, "radius":  6},  # "item"    (111, 41)
                {"x": 45.9, "y": 22.8, "radius": 12},  # "collection" (257, 41)
                {"x": 30.5, "y": 71.7, "radius": 12},  # "process(item)" (171, 129)
            ],
        )
    )
    annotation_question
    return (annotation_question, urllib)


@app.cell
def _(annotation_question, mo):
    _val = annotation_question.value.get("value") or {}
    _total = _val.get("total", 0)
    _msg = f"Score: {_val['score']}/{_total}" if _total > 0 else "Not submitted yet"
    mo.md(f"**{_msg}**")
    return


# ---------------------------------------------------------------------------
# Concept Map
# ---------------------------------------------------------------------------

@app.cell
def _(mo):
    concept_map_reset = mo.ui.button(label="↺ Reset")
    mo.vstack([mo.md("## Concept Map"), concept_map_reset])
    return (concept_map_reset,)


@app.cell
def _(ConceptMapWidget, concept_map_reset, mo):
    _ = concept_map_reset.value
    concept_map = mo.ui.anywidget(
        ConceptMapWidget(
            question="Map the relationships between these Python concepts:",
            concepts=["function", "parameter", "argument", "return value", "call site"],
            terms=["defines", "accepts", "supplies", "produces", "invokes"],
            correct_edges=[
                {"from": "function", "to": "parameter", "label": "accepts"},
                {"from": "function", "to": "return value", "label": "produces"},
                {"from": "call site", "to": "argument", "label": "supplies"},
                {"from": "argument", "to": "parameter", "label": "defines"},
                {"from": "call site", "to": "function", "label": "invokes"},
            ],
        )
    )
    concept_map
    return (concept_map,)


@app.cell
def _(concept_map, mo):
    def concept_map_msg(widget):
        val = widget.value.get("value") or {}
        score = val.get("score")
        total = val.get("total", 5)
        if score is None:
            return "Draw connections between concepts to see your score."
        msg = f"**{score}/{total}** correct connection{'s' if total != 1 else ''}"
        if val.get("correct"):
            msg += " — complete!"
        return msg

    mo.md(concept_map_msg(concept_map))
    return


# ---------------------------------------------------------------------------
# Flashcard Deck
# ---------------------------------------------------------------------------

@app.cell
def _(mo):
    flashcard_reset = mo.ui.button(label="↺ Reset")
    mo.vstack([mo.md("## Flashcard Deck"), flashcard_reset])
    return (flashcard_reset,)


@app.cell
def _(FlashcardWidget, flashcard_reset, mo):
    _ = flashcard_reset.value
    flashcard_deck = mo.ui.anywidget(
        FlashcardWidget(
            question="Python Concepts — rate yourself on each card:",
            cards=[
                {
                    "front": "What does a list comprehension look like?",
                    "back": "[expr for item in iterable if condition] — e.g., [x**2 for x in range(10) if x % 2 == 0]",
                },
                {
                    "front": "What is the difference between a list and a tuple?",
                    "back": "Lists are mutable (can be changed after creation); tuples are immutable (cannot be changed).",
                },
                {
                    "front": "What does the `*args` parameter do in a function definition?",
                    "back": "It collects any number of positional arguments into a tuple named `args`.",
                },
                {
                    "front": "What is a Python generator?",
                    "back": "A function that uses `yield` to produce values one at a time, pausing between each, without building the full sequence in memory.",
                },
                {
                    "front": "What does `if __name__ == '__main__':` do?",
                    "back": "It runs the indented code only when the file is executed directly, not when it is imported as a module.",
                },
                {
                    "front": "What is the difference between `is` and `==` in Python?",
                    "back": "`==` tests value equality; `is` tests identity (whether two names refer to the exact same object in memory).",
                },
            ],
            shuffle=True,
        )
    )
    flashcard_deck
    return (flashcard_deck,)


@app.cell
def _(flashcard_deck, mo):
    def flashcard_progress(widget):
        val = widget.value.get("value") or {}
        results = val.get("results", {})
        counts = {"got_it": 0, "almost": 0, "no": 0}
        for r in results.values():
            counts[r["rating"]] = counts.get(r["rating"], 0) + 1
        return len(results), counts, val.get("complete", False)

    _rated, _counts, _complete = flashcard_progress(flashcard_deck)
    mo.md(f"""
    **Progress:** {_rated} card(s) rated —
    ✓ Got it: {_counts["got_it"]} &nbsp;
    ~ Almost: {_counts["almost"]} &nbsp;
    ✗ No: {_counts["no"]}
    {"&nbsp; 🎉 Deck complete!" if _complete else ""}
    """)
    return


# ---------------------------------------------------------------------------
# Labeling
# ---------------------------------------------------------------------------

@app.cell
def _(mo):
    labeling_reset = mo.ui.button(label="↺ Reset")
    mo.vstack([mo.md("## Labeling Question"), labeling_reset])
    return (labeling_reset,)


@app.cell
def _(LabelingWidget, labeling_reset, mo):
    _ = labeling_reset.value
    labeling_question = mo.ui.anywidget(
        LabelingWidget(
            question="Label the parts of this Python code:",
            labels=[
                "Variable declaration",
                "Function call",
                "String literal",
                "Arithmetic operation",
            ],
            text_lines=[
                "name = 'Alice'",
                "age = 25",
                "result = age + 5",
                "print(name)",
            ],
            correct_labels={
                0: [0, 2],  # Line 0: labels 0 and 2
                1: [0],     # Line 1: label 0
                2: [0, 3],  # Line 2: labels 0 and 3
                3: [1],     # Line 3: label 1
            },
        )
    )
    labeling_question
    return (labeling_question,)


@app.cell
def _(labeling_question, mo):
    _val = labeling_question.value.get("value") or {}
    _total = _val.get("total", 0)
    _msg = f"Score: {_val['score']}/{_total}" if _total > 0 else "Not submitted yet"
    mo.md(f"**{_msg}**")
    return


# ---------------------------------------------------------------------------
# Matching
# ---------------------------------------------------------------------------

@app.cell
def _(mo):
    matching_reset = mo.ui.button(label="↺ Reset")
    mo.vstack([mo.md("## Matching Question"), matching_reset])
    return (matching_reset,)


@app.cell
def _(MatchingWidget, matching_reset, mo):
    _ = matching_reset.value
    matching_question = mo.ui.anywidget(
        MatchingWidget(
            question="Match the programming languages to their primary paradigms:",
            left=["Python", "Haskell", "C", "SQL"],
            right=["Functional", "Procedural", "Multi-paradigm", "Declarative"],
            correct_matches={0: 2, 1: 0, 2: 1, 3: 3},
        )
    )
    matching_question
    return (matching_question,)


@app.cell
def _(matching_question, mo):
    _val = matching_question.value.get("value") or {}
    _msg = f"Score: {_val['score']}/{_val['total']}" if _val else "Not answered yet"
    mo.md(f"**{_msg}**")
    return


# ---------------------------------------------------------------------------
# Multiple Choice
# ---------------------------------------------------------------------------

@app.cell
def _(mo):
    multiple_choice_reset = mo.ui.button(label="↺ Reset")
    mo.vstack([mo.md("## Multiple Choice Question"), multiple_choice_reset])
    return (multiple_choice_reset,)


@app.cell
def _(MultipleChoiceWidget, mo, multiple_choice_reset):
    _ = multiple_choice_reset.value
    multiple_choice_question = mo.ui.anywidget(
        MultipleChoiceWidget(
            question="What is the capital of France?",
            options=["London", "Berlin", "Paris", "Madrid"],
            correct_answer=2,
            explanation="Paris has been the capital of France since the 12th century.",
        )
    )
    multiple_choice_question
    return (multiple_choice_question,)


@app.cell
def _(mo, multiple_choice_question):
    _val = multiple_choice_question.value.get("value") or {}
    if _val.get("answered"):
        _msg = "Score: 1/1" if _val.get("correct") else "Score: 0/1"
    else:
        _msg = "Not answered yet"
    mo.md(f"**{_msg}**")
    return


# ---------------------------------------------------------------------------
# Ordering
# ---------------------------------------------------------------------------

@app.cell
def _(mo):
    ordering_reset = mo.ui.button(label="↺ Reset")
    mo.vstack([mo.md("## Ordering Question"), ordering_reset])
    return (ordering_reset,)


@app.cell
def _(OrderingWidget, mo, ordering_reset):
    _ = ordering_reset.value
    ordering_question = mo.ui.anywidget(
        OrderingWidget(
            question="Arrange these steps of the scientific method in the correct order:",
            items=[
                "Ask a question",
                "Do background research",
                "Construct a hypothesis",
                "Test with an experiment",
                "Analyze data",
                "Draw conclusions",
            ],
            shuffle=True,
        )
    )
    ordering_question
    return (ordering_question,)


@app.cell
def _(mo, ordering_question):
    _val = ordering_question.value.get("value") or {}
    if _val.get("correct") is not None and _val.get("order"):
        _msg = "Score: 1/1" if _val.get("correct") else "Score: 0/1"
    else:
        _msg = "Not answered yet"
    mo.md(f"**{_msg}**")
    return


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

@app.cell
def _(mo):
    mo.md("""
    ---

    ## Quiz Results Summary

    You can access the values from all widgets to create a summary or scoring system.
    """)
    return


@app.cell
def _(
    annotation_question,
    concept_map,
    flashcard_deck,
    matching_question,
    multiple_choice_question,
    mo,
    ordering_question,
):
    def widget_val(widget):
        return widget.value.get("value") or {}

    def calculate_score():
        score = 0
        total = 0
        for val, answered_key, correct_key in [
            (widget_val(annotation_question), "score", "correct"),
            (widget_val(concept_map), "score", "correct"),
            (widget_val(matching_question), "score", "correct"),
            (widget_val(multiple_choice_question), "answered", "correct"),
            (widget_val(ordering_question), "order", "correct"),
        ]:
            if val.get(answered_key) is not None and val.get(answered_key) is not False:
                total += 1
                if val.get(correct_key):
                    score += 1
        fc = widget_val(flashcard_deck)
        if fc.get("results"):
            total += 1
            if fc.get("complete"):
                score += 1
        return score, total

    score, total = calculate_score()
    mo.md(f"""
    ### Current Score: {score}/{total}

    {"🎉 Perfect score!" if score == total and total > 0 else "Keep going!" if total > 0 else "Answer the questions above to see your score."}
    """)
    return


if __name__ == "__main__":
    app.run()
