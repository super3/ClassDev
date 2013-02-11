// Filename: FileOp.h
// Project Github: http://github.com/super3/ClassDev
// Author: Shawn Wilkinson <me@super3.org>
// Author Website: http://super3.org/
// License: GPLv3 <http://gplv3.fsf.org/>

#include <string>
using namespace std;

class FileOp {
	public:
		FileOp(string, string);
		void run(string);
	private:
		string table[50];
		string table_op[50];

		void in_file(string);
		void out_file(string);

		//string print_op(string);
		//string add_op(string);
		//string remove_op(string);
		//string check_op(string);
		//bool check(string);
};