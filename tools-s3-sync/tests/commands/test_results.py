import pytest
from snovak.commands.results import SyncCommandResult

def test_initial_count():
    result = SyncCommandResult()
    assert result.get_synced_files_count() == 0, "Initial count should be zero"

def test_increment_synced():
    result = SyncCommandResult()
    result.increment_synced()
    assert result.get_synced_files_count() == 1, "Incrementing once should result in a count of 1"

def test_increment_synced_by_specific_number():
    result = SyncCommandResult()
    result.increment_synced(5)
    assert result.get_synced_files_count() == 5, "Incrementing by 5 should result in a count of 5"

def test_multiple_increments():
    result = SyncCommandResult()
    result.increment_synced(3)
    result.increment_synced(4)
    assert result.get_synced_files_count() == 7, "Incrementing by 3 and 4 should result in a total count of 7"
