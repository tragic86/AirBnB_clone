#!/usr/bin.python3
import cmd, sys, shlex
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
	prompt = '(hbnb) '

	def do_echo(self, arg):
		'''Simply echos back the argument'''
		print(HBNBCommand.parse(arg))

	def do_create(self, arg):
		'''Create new instance of a class

			Usage: create <classname>
		'''
		argv = HBNBCommand.parse(arg)
		valid = HBNBCommand.checkargs(1, argv)
		if valid == 0:
			return

		constructor = argv[0] + '()'
		instance = eval(constructor)
		print(instance)

	def do_EOF(self, arg):
		'''Represents end of file'''
		return True

	def do_quit(self, arg):
		'''Quit command to exit the program'''
		return True

	def emptyline(self):
		pass

	@staticmethod
	def checkargs(argc, argv):
		'''Ensures arguments are valid

			Args:
				argc = amount of args expected
				argv = list of args

		   Returns:
		   		0 for failure, 1 for success
		'''
		if argc >= 1:
			if len(argv) == 0:
				print("** class name missing **")
				return 0

			classes = ('BaseModel', 'User', 'State'
						'City', 'Amenity', 'Place',
						'Review')

			if argv[0] not in classes:
				print("** class doesn't exist **")
				return 0

		if argc >= 2:
			if len(argv) == 1:
				print("** instance id missing **")
				return 0
			# search for instance, and report
			# ** no instance found **

		if argc >= 3:
			if len(argv) == 2:
				print("** attribute name missing **")
				return 0

			if len(argv) == 3:
				print("** value missing **")
				return 0
		return 1

	@staticmethod
	def parse(arg):
		'''Convert string into list of arguments'''
		return tuple(shlex.split(arg))


if __name__ == '__main__':
	HBNBCommand().cmdloop()