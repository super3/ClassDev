#!/usr/bin/env python
# Filename: assign2.py
# Project Github: http://github.com/super3/ClassDev
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

table = []

#IDENTIFIER, PREDEFINED, LITERAL, MISC

table.append( ("APROG", "IDENTIFIER") )
table.append( ("I", "IDENTIFIER") )
table.append( ("J", "IDENTIFIER") )
table.append( ("K", "IDENTIFIER") )
table.append( ("PI", "IDENTIFIER") )

table.append( ("1", "CONSTANT") )
table.append( ("2", "CONSTANT") )
table.append( ("3", "CONSTANT") )
table.append( ("4", "CONSTANT") )
table.append( ("5", "CONSTANT") )
table.append( ("6", "CONSTANT") )
table.append( ("7", "CONSTANT") )
table.append( ("8", "CONSTANT") )
table.append( ("9", "CONSTANT") )
table.append( ("0", "CONSTANT") )

table.append( ("PROGRAM", "RESERVED") )
table.append( ("VAR", "RESERVED") )
table.append( ("BEGIN", "RESERVED") )
table.append( ("END", "RESERVED") )
table.append( ("INPUT", "RESERVED") )
table.append( ("OUTPUT", "RESERVED") )
table.append( ("CHAR", "RESERVED") )
table.append( ("INTEGER", "RESERVED") )

table.append( ("+", "ARITH_OPERATOR") )
table.append( ("-", "ARITH_OPERATOR") )
table.append( ("*", "ARITH_OPERATOR") )
table.append( ("/", "ARITH_OPERATOR") )

table.append( ("=", "LOGICAL_OPERATORS") )
table.append( ("<>", "LOGICAL_OPERATORS") )
table.append( (">=", "LOGICAL_OPERATORS") )
table.append( ("<=", "LOGICAL_OPERATORS") )
table.append( (">", "LOGICAL_OPERATORS") )
table.append( ("<", "LOGICAL_OPERATORS") )

table.append( (":=", "ASSIGNMENT_OP") )
table.append( (";", "SEMICOLON") )
table.append( (",", "COMMA") )
table.append( (":", "COLON") )
table.append( (".", "PERIOD") )
table.append( ("^", "CRAT") )
table.append( ("'", "QUOTE") )
table.append( ("..", "RANGE") )

table.append( ("(", "LParan") )
table.append( (")", "RParan") )
table.append( ("{", "LBrace") )
table.append( ("}", "RBrace") )
table.append( ("[", "LBracket") )
table.append( ("]", "RBracket") )

def get_token(in_token):
	for i in table:
		if i[0] == in_token: return(i[0].ljust(10) + " " +i[1])
	return in_token

with open ("program.txt", "r") as myfile:
    data=myfile.read().split()

for i in data:
	print(get_token(i))