from _typeshed import Incomplete
from watchdog.events import FileSystemEvent as FileSystemEvent, FileSystemEventHandler

logger: Incomplete

class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event: FileSystemEvent): ...

def restart_file() -> None: ...
