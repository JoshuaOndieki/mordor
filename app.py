"""
    Usage:
        add <new_skill>
        skills --list
        complete <skill>
        progress
"""

from docopt import docopt,DocoptExit
from functions import Mordor,skills




def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    os.system("clear")
    print(__doc__)


class MORDOR(cmd.Cmd):
    prompt = "MORDOR $$$"

    @docopt_cmd
    def do_add_skills(self, arg):
        """Usage: add <skill>"""
        skill=arg["<skill>"]
        print(add_skill(skill))

    @docopt_cmd
    def do_list_skills(self, arg):
        """Usage: skills --list"""
        print(view_skills())

    @docopt_cmd
    def do_complete_skill(self, arg):
        """Usage: complete <skill>"""
        skill=arg["<skill>"]
        print(complete_skill(skill))

    @docopt_cmd
    def do_progress(self, arg):
        """Usage: progress"""

        print(progress(skills))



    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit"""
        os.system('clear')
        print ('Mordor has quit')
        exit()


if __name__ == "__main__":
    try:
        intro()
        MORDOR().cmdloop()
    except KeyboardInterrupt:
        os.system("clear")
        print('Mordor has quit')
