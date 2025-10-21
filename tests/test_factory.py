import pytest

from reports.average import AverageRating
from reports.factory import get_average_rating


def test_get_average_rating_returns_true_instance():
    result = get_average_rating("average-rating")
    assert isinstance(result, AverageRating)


def test_get_average_rating_raises_unknown_report():
    with pytest.raises(ValueError, match="Unknown report type"):
        get_average_rating("fake-report")
