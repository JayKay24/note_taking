# -*- coding: utf-8 -*-
"""
This example uses docopt with the built in cmd module to demonstrate an 
interactive command application.
Usage:
    note_app create <content>...
    note_app view <note_id>
    note_app delete <note_id>
    note_app list
    note_app search <query_string>...
    note_app (-i | --interactive)
    note_app (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit
"""
import sys
import cmd
from docopt import docopt, DocoptExit
from classes.note_take import NoteTake

note_take = NoteTake()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn
    
class MyInteractive (cmd.Cmd):
    prompt = '(note_app) '
    file = None
    
    @docopt_cmd
    def do_create_note(self, args):
        """Usage: create <content>..."""
        
        content = args['<content>']
        content = ' '.join(content)
        note_take.create_note(content)
        
    @docopt_cmd
    def do_view_note(self, args):
        """Usage: view <note_id>"""
        
        note_id = int(args['<note_id>'])
        note_take.view_note(note_id)
        
    @docopt_cmd
    def do_delete_note(self, args):
        """Usage: delete <note_id>"""
        
        note_id = int(args['<note_id>'])
        note_take.delete_note(note_id)
        
    @docopt_cmd
    def do_list_notes(self, args):
        """Usage: list"""
        
        note_take.list_notes()
        
    @docopt_cmd
    def do_search_notes(self, args):
        """Usage: search <query_string>..."""
        
        query_string = args['<query_string>']
        query_string = ' '.join(query_string)
        note_take.search_notes(query_string)
        
    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        
        print("Good Bye!")
        exit()      
opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:
    
    MyInteractive().cmdloop()
print(opt)