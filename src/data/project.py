import pickle
import logging
import typing

from enum import Enum, EnumMeta
from rich.console import Console

_logger = logging.getLogger(__name__)


class ProjectStatusMeta(EnumMeta):
    def __str__(cls):
        lines = [f"Project status choices:"]
        for member in cls:
            lines.append(f"- {member.name}")
        return '\n'.join(lines)


class ProjectStatus(str, Enum, metaclass=ProjectStatusMeta):
    pending = 'pending'
    in_progress = 'in-progress'
    waiting = 'waiting'
    done = 'done'
    archived = 'archived'
    dropped = 'dropped'


class Project:
    _name: str
    _tags: list[str]
    _status: ProjectStatus
    _container_driver: str
    _resource_driver: str
    _note_driver: str
    _time_driver: str
    _task_driver: str

    def __init__(self,
                 name: str,
                 status: ProjectStatus = ProjectStatus.in_progress,
                 tags: list[str] = None,
                 note_driver: str = None,
                 resource_driver: str = None,
                 container_driver: str = None,
                 time_driver: str = None,
                 task_driver: str = None):
        self._name = name
        self._status = status
        self._tags = tags
        self._note_driver = note_driver
        self._resource_driver = resource_driver
        self._container_driver = container_driver
        self._time_driver = time_driver
        self._task_driver = task_driver

    def info(self):
        console = Console()
        # name
        console.print(f'Name: [not bold]{self._name}[/not bold]', style='bold')
        # status
        console.print(f'Status: [not bold]{self._status}[/not bold]', style='bold')
        # tags
        if self._tags:
            console.print('Tags:', style='bold')
            for tag in self._tags:
                console.print(f' - {tag}')
        # notes
        if self._note_driver:
            console.print(f'Notes [not bold][{self._note_driver}][/not bold]:', style='bold')

        # resources

        # containers

        # time

        # tasks


class ProjectsState:
    _projects: dict[str, Project]
    _runtime_state: dict[str, typing.Any]

    def __init__(self, runtime_state):
        self._projects = {}
        self._runtime_state = runtime_state
        if runtime_state['debug']:
            _logger.setLevel(logging.DEBUG)

    def info(self):
        # TODO: This needs fixed once project info is done
        ret = ''
        for project in self._projects:
            ret += f'{self._projects[project]}\n'
        return ret

    def __getitem__(self, name):
        _logger.debug(f'Called __getitem__ with {name}')
        _logger.debug(f'{type(self._projects[name])}')
        return self._projects[name]

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

    def exists(self, name):
        return name in self._projects
