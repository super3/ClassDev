#!/usr/bin/env python
# Filename: assign1.py
# Project Github: http://github.com/super3/ClassDev
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

class FileOp:
	def __init__(self, ini_file, op_file):
		"""A nice little class to make everything nice."""
		self.table = self.in_file(ini_file)
		self.op_table = self.in_file(op_file)

	def in_file(self, filename):
		"""Read a file into a table."""
		table = []
		for line in open(filename, 'r'):
			if line == ":":
				return table
			table.append(str(line))
		return table

	def out_file(self, filename, txt):
		f = open(filename, 'w+')
		f.write(txt)
		f.close()

	def add_op(self, word):
		"""Add a word to the list."""
		if self.check(word):
			return "DUPLICATE"
		else:
			self.table.append(word)
			return "ADDED"

	def remove_op(self, word):
		"""Remove a word from the list."""
		if self.check(word):
			self.table.remove(word)
			return "DELETED"
		else:
			return "SKIP - NOT EXIST"

	def check_op(self, word):
		if self.check(word):
			return "YES"
		else:
			return "NO"

	def check(self, word):
		for item in self.table:
			if word == item:
				return True
		return False

	def print_op(self):
		output = ""
		for item in self.table:
			output += item
		return output

	def run(self, outfile):
		output = ""
		for word in self.op_table:
			if word[0] == "?":
				output += word.strip('\n').ljust(15) + " " + self.check_op(word[2:]) + "\n"
			elif word[0] == "+":
				output += word.strip('\n').ljust(15) + " " + self.add_op(word[2:]) + "\n"
			elif word[0] == "-":
				output += word.strip('\n').ljust(15) + " " + self.remove_op(word[2:]) + "\n"
			elif word[0] == "*":
				output += "*\n"+ self.print_op() 
			else:
				output += word.strip('\n') , "UNRECOGNIZED"
		self.out_file(outfile, output)

 

assign1 = FileOp('initial_file.txt', 'operation_file.txt')
assign1.run('result.txt')