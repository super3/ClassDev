// Filename: main.cpp
// Project Github: http://github.com/super3/ClassDev
// Author: Shawn Wilkinson <me@super3.org>
// Author Website: http://super3.org/
// License: GPLv3 <http://gplv3.fsf.org/>

#include <iostream>
#include "FileOp.h"
using namespace std;

int main() {
	// Start Object
	FileOp test = FileOp("test", "test");
	test.run("C:\\Users\\super_000\\Code\\ClassDev\\ProgLang\\C++\\Debug\\initial_file.txt");
	
	// Exit Program
	system("PAUSE");
	return 0;
}