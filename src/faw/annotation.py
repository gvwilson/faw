"""Annotation Widget for Marimo"""

import anywidget
from pathlib import Path
import traitlets


class AnnotationWidget(anywidget.AnyWidget):
    """
    An image annotation widget where students drag labels onto hotspots.

    Students drag numbered labels from a sidebar and drop them onto the
    correct regions of an image. On submission each placement is scored
    by checking whether it falls within the target radius of the correct
    hotspot.

    Attributes:
        question (str): The question text to display
        image_url (str): URL (or data URI) of the image to annotate
        labels (list): List of label strings
        targets (list): List of dicts with 'x', 'y', 'radius' keys, each in
                        percent of the image dimensions; index i is the target
                        for labels[i]
        value (dict): Current state with 'placed', 'results', 'score',
                      'total', and 'correct' keys
    """

    _esm = Path(__file__).parent / "static" / "annotation.js"

    question = traitlets.Unicode("").tag(sync=True)
    image_url = traitlets.Unicode("").tag(sync=True)
    labels = traitlets.List(trait=traitlets.Unicode()).tag(sync=True)
    targets = traitlets.List(trait=traitlets.Dict()).tag(sync=True)
    value = traitlets.Dict(default_value=None, allow_none=True).tag(sync=True)

    def __init__(self, question: str, image_url: str, labels: list[str],
                 targets: list[dict], **kwargs):
        """
        Initialize an annotation widget.

        Args:
            question: The question text
            image_url: URL or data URI of the image
            labels: List of label strings
            targets: List of dicts, one per label, each with keys:
                     'x' (float): horizontal centre of target in % of image width
                     'y' (float): vertical centre of target in % of image height
                     'radius' (float): acceptance radius in % (Euclidean distance
                                       in percentage-coordinate space)
        """
        super().__init__(**kwargs)
        self.question = question
        self.image_url = image_url
        self.labels = labels
        self.targets = targets
