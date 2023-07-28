import json
import logging

from enum import Enum
from pathlib import Path


_logger = logging.getLogger(__name__)


class ProjectStatus(str, Enum):
    pending = 'pending'
    in_progress = 'in-progress'
    waiting = 'waiting'
    done = 'done'
    archived = 'archived'
    dropped = 'dropped'


class Project:
    _name: str
    _keywords: list[str]
    _tags: list[str]
    _notes: list[Path]
    _resource: Path
    _containers: list[str]
    _status: ProjectStatus
    _parent: str

    def __init__(self,
                 name: str,
                 parent: str = None,
                 status: ProjectStatus = ProjectStatus.in_progress,
                 keywords: list[str] = None,
                 tags: list[str] = None,
                 notes: list[Path] = None,
                 resource: Path = None,
                 containers: list[str] = None):
        self._name = name
        self._parent = parent
        self._status = status
        self._keywords = keywords
        self._tags = tags
        self._notes = notes
        self._resource = resource
        self._containers = containers


class ProjectsState:
    _projects: dict[str, Project]
    _config_directory: Path
    _debug: bool = False

    def __init__(self):
        self._projects = dict()

    def toJson(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)

    def load(self) -> None:
        state_file = self._config_directory.joinpath('projects.state')
        try:
            with open(state_file, 'r') as f:
                self._projects = json.loads(f.read())
        except IOError:
            _logger.WARNING('Projects state file does not exist, starting fresh')
            self._projects = dict()

    def save(self) -> None:
        print('Saving projects state')
        with open(self._config_directory.joinpath('projects.state'), 'w') as f:
            f.write(json.dumps(self.toJson()), indent=4)

    def add_project(self, new_project: Project) -> None:
        self._projects[new_project._name] = new_project

    @property
    def config_directory(self) -> Path:
        return self._config_directory

    @config_directory.setter
    def config_directory(self, config_directory: Path) -> None:
        self._config_directory = config_directory

    def set_debug(self, debug: bool) -> None:
        self._debug = debug
        if self._debug:
            _logger.setLevel(logging.DEBUG)
