- Subcommands:
    + new (in addition to current newproj functionality, ask about git and an upstream URL)
    + list - Show table of current projects and meta-data
    + archive - Set status
    + delete - Remove this project
    + grep - Search notes and resource folder
    + set-status - Update status for specified project
    + get-status - Show current status for all (or specified)
    + register - Add existing project to projects
    + sync - Ensure projects state and project metadata match
    + get-tags - Get tags, if they exist
    + set-tags - Update tags, in metadata and state
    + get-keys - Get keys, if they exist
    + set-keys - Set keys, in metadata and state
    + notes
        - init
        - add
        - delete
        - list
        - delete
        - archive
    + resources
        - location - print location
        - browse - open in file browser
        - terminal - run terminal at resource location
    + time
        - start - Add time entry
        - stop - Finish time entry
        - cancel - Cancel a time entry
        - edit - Edit a time entry
        - status - List current time entry
        - log - Get time entries (switches to filter on project or timespan)
    + containers
        - new
        - status
        - start
        - stop
        - delete
        - shell

- Configuration options:
    + Notes root directory
    + Resources root directory
    + Note template
    + Editor command
    + Folder command

- State maintenance:
    + XXX file in configuration directory
        * Includes metadata state from `.md` files
    + Combines with configuration options

- Default template:
    + Add path to resource root directory
    + If git is used, include URL of repository

- Enhancements:
    + Custom states
    + Metadata editor
    + Plugins for each facet
        * Time tracking: watson, plain text, ...
        * Resources: folders, git, ...
        * Notes: plain text, ...
    + Plugin APIs for each facet