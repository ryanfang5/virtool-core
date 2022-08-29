from virtool_core.models.samples import Sample
import pytest


@pytest.fixture
def mock_sample():
    return {
        "all_read": True,
        "all_write": False,
        "artifacts": [],
        "caches": [],
        "created_at": "2015-10-06T20:00:00Z",
        "format": "fastq",
        "group": "none",
        "group_read": True,
        "group_write": False,
        "hold": True,
        "host": "",
        "id": "bf1b993c",
        "is_legacy": False,
        "isolate": "",
        "labels": [{"color": "#FF0000", "description": "", "id": 1, "name": "bug"}],
        "library_type": "normal",
        "locale": "",
        "name": "Foobar",
        "notes": "",
        "nuvs": False,
        "paired": False,
        "pathoscope": False,
        "quality": None,
        "reads": [],
        "ready": False,
        "subtractions": [{"id": "apple", "name": "Apple"}],
        "user": {
            "administrator": False,
            "handle": "bob",
            "id": "test",
        },
    }


def test_sample(mock_sample):
    """
    Tests that no errors are thrown when using the Sample model.
    """

    Sample(**mock_sample)
