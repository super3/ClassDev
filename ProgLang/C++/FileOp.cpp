// Filename: FileOp.cpp
// Project Github: http://github.com/super3/ClassDev
// Author: Shawn Wilkinson <me@super3.org>
// Author Website: http://super3.org/
// License: GPLv3 <http://gplv3.fsf.org/>

#include <iostream>
#include <fstream>
#include "FileOp.h"
using namespace std;

FileOp::FileOp(string ini_file, string op_file)
{

}

void FileOp::in_file(string path)
{
	// Open File
	ifstream myfile(path);
	// Get Number of Lines
	int numLines = 0;
	while ( getline(myfile, string()) )
	   ++numLines;
	cout << numLines << endl;
}

void FileOp::out_file(string path)
{
	ofstream myfile(path);
}

void FileOp::run(string path)
{
	FileOp::in_file(path);
}