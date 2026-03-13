"""Unit tests for AnnotationWidget."""

import pytest
from faw import AnnotationWidget

IMAGE_URL = "data:image/svg+xml,<svg/>"

LABELS = ["keyword", "loop variable", "iterable", "loop body"]

TARGETS = [
    {"x": 6.5,  "y": 34.0, "radius": 6},
    {"x": 16.5, "y": 34.0, "radius": 7},
    {"x": 37.8, "y": 34.0, "radius": 11},
    {"x": 19.8, "y": 72.0, "radius": 13},
]


class TestAnnotationWidget:
    def test_initialization(self):
        w = AnnotationWidget(
            question="Label the diagram:",
            image_url=IMAGE_URL,
            labels=LABELS,
            targets=TARGETS,
        )
        assert w.question == "Label the diagram:"
        assert w.image_url == IMAGE_URL
        assert w.labels == LABELS
        assert w.targets == TARGETS
        assert w.value is None

    def test_label_count_matches_target_count(self):
        w = AnnotationWidget(
            question="Q", image_url=IMAGE_URL, labels=LABELS, targets=TARGETS
        )
        assert len(w.labels) == len(w.targets)

    def test_target_structure(self):
        w = AnnotationWidget(
            question="Q", image_url=IMAGE_URL, labels=LABELS, targets=TARGETS
        )
        for t in w.targets:
            assert "x" in t
            assert "y" in t
            assert "radius" in t

    def test_target_coordinates_in_range(self):
        w = AnnotationWidget(
            question="Q", image_url=IMAGE_URL, labels=LABELS, targets=TARGETS
        )
        for t in w.targets:
            assert 0 <= t["x"] <= 100
            assert 0 <= t["y"] <= 100
            assert t["radius"] > 0

    def test_single_label(self):
        w = AnnotationWidget(
            question="Q",
            image_url=IMAGE_URL,
            labels=["nucleus"],
            targets=[{"x": 50.0, "y": 50.0, "radius": 10}],
        )
        assert len(w.labels) == 1
        assert w.labels[0] == "nucleus"

    def test_value_update_in_progress(self):
        w = AnnotationWidget(
            question="Q", image_url=IMAGE_URL, labels=LABELS, targets=TARGETS
        )
        w.value = {
            "placed": {0: {"x": 6.0, "y": 34.0}},
            "score": 0,
            "total": 4,
            "correct": False,
        }
        assert w.value["score"] == 0
        assert w.value["correct"] is False

    def test_value_update_all_correct(self):
        w = AnnotationWidget(
            question="Q", image_url=IMAGE_URL, labels=LABELS, targets=TARGETS
        )
        w.value = {
            "results": {i: {"placed": {"x": t["x"], "y": t["y"]}, "correct": True}
                        for i, t in enumerate(TARGETS)},
            "score": 4,
            "total": 4,
            "correct": True,
        }
        assert w.value["correct"] is True
        assert w.value["score"] == 4

    def test_value_update_partial(self):
        w = AnnotationWidget(
            question="Q", image_url=IMAGE_URL, labels=LABELS, targets=TARGETS
        )
        w.value = {
            "results": {
                0: {"placed": {"x": 6.5, "y": 34.0}, "correct": True},
                1: {"placed": {"x": 50.0, "y": 50.0}, "correct": False},
                2: {"placed": None, "correct": False},
                3: {"placed": None, "correct": False},
            },
            "score": 1,
            "total": 4,
            "correct": False,
        }
        assert w.value["score"] == 1
        assert w.value["total"] == 4
        assert w.value["correct"] is False

    def test_value_update_none_placed(self):
        w = AnnotationWidget(
            question="Q", image_url=IMAGE_URL, labels=LABELS, targets=TARGETS
        )
        w.value = {
            "results": {i: {"placed": None, "correct": False} for i in range(4)},
            "score": 0,
            "total": 4,
            "correct": False,
        }
        assert w.value["score"] == 0
        for i in range(4):
            assert w.value["results"][i]["placed"] is None

    def test_image_url_stored(self):
        url = "https://example.com/diagram.png"
        w = AnnotationWidget(
            question="Q",
            image_url=url,
            labels=["part A"],
            targets=[{"x": 25.0, "y": 25.0, "radius": 8}],
        )
        assert w.image_url == url

    def test_independent_instances(self):
        w1 = AnnotationWidget(
            question="Q1", image_url=IMAGE_URL,
            labels=["a"], targets=[{"x": 10, "y": 10, "radius": 5}],
        )
        w2 = AnnotationWidget(
            question="Q2", image_url=IMAGE_URL,
            labels=["b", "c"], targets=[{"x": 20, "y": 20, "radius": 5},
                                        {"x": 80, "y": 80, "radius": 5}],
        )
        assert w1.question != w2.question
        assert len(w1.labels) != len(w2.labels)
        assert w1.value is None
        assert w2.value is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
