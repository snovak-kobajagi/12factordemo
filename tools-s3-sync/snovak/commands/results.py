class SyncCommandResult:
    def __init__(self):
        self._synced_files_count = 0

    def increment_synced(self, count: int = 1):
        self._synced_files_count += count

    def get_synced_files_count(self) -> int:
        return self._synced_files_count

