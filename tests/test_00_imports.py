"""Test Importing the package works."""
import pytest


@pytest.mark.test_package
def test_import():
    """Test imporint package works."""
    from translator_template.main import spool_file  # pylint: disable=import-outside-toplevel, unused-import
    assert True
