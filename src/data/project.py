import pickle
import logging
import typing

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
    _container_driver: str
    _resource_driver: str
    _note_driver: str
    _time_driver: str

    def __init__(self,
                 name: str,
                 status: ProjectStatus = ProjectStatus.in_progress,
                 keywords: list[str] = None,
                 tags: list[str] = None,
                 notes: list[Path] = None,
                 resource: Path = None,
                 containers: list[str] = None,
                 note_driver: str = None,
                 resource_driver: str = None,
                 container_driver: str = None,
                 time_driver: str = None):
        self._name = name
        self._status = status
        self._keywords = keywords
        self._tags = tags
        self._notes = notes
        self._note_driver = note_driver
        self._resource = resource
        self._resource_driver = resource_driver
        self._containers = containers
        self._container_driver = container_driver
        self._time_driver = time_driver


class ProjectsState:
    _projects: dict[str, Project]
    _runtime_state: dict[str, typing.Any]

    def __init__(self, runtime_state):
        self._projects = dict()
        self._runtime_state = runtime_state

    def load(self):
        state_file = self._runtime_state['config_directory'].joinpath('projects.pickle')
        try:
            with open(state_file, 'rb') as f:
                self._projects = pickle.load(f)
        except IOError:
            self._projects = dict()
        return self

    def save(self) -> None:
        state_file = self._runtime_state['config_directory'].joinpath('projects.pickle')
        with open(state_file, 'wb') as f:
            pickle.dump(self._projects, f, pickle.HIGHEST_PROTOCOL)

    def add_project(self, new_project: Project) -> None:
        self._projects[new_project._name] = new_project
        self.save()

    def list(self):
        return self._projects.keys()
