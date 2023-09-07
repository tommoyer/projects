- Subcommands:
    + new
        * p new <project>
    + list - Show table of current projects and meta-data
        * p list
    + archive - Set status
        * p archive <project>
    + delete - Remove this project
        * p delete <project>
    + grep - Search notes and resource folder. Options to limit to a project or parent
        * p grep [--project <project>] [--parent <parent>] <search>
    + set-status - Update status for specified project
        * p set-status <project>
    + get-status - Show current status for all (or specified)
        * p get-status [<project>]
    + get-tags - Get tags, if they exist
        * p get-tags <project>
    + set-tags - Update tags, in metadata and state
        * p set-tags <project>
    + add-tag
        * p add-tag <project>
    + remove-tag
        * p remove-tag <project>
    + notes <project> [<subcommand>], if no subcommand call info
    + resources <project> [<subcommand>], if no subcommand call info
    + time <project> [<subcommand>], if no subcommand call info
    + containers <project> [<subcommand>], if no subcommand call info
    + tasks <project> [<subcommand>], if no subcommand call info

- Enhancements:
    + Custom states
    + Metadata editor
    + Reports
    + Dashboard
    + GUI
    + Plugin for Gnome/Systray
    + Look at rich and textual for other fun stuff
        * https://github.com/Textualize/rich
        * https://github.com/Textualize/textual