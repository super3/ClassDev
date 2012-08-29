// Filename: main.cpp
// Project Github: http://github.com/super3/ClassDev
// Author: Shawn Wilkinson <me@super3.org>
// Author Website: http://super3.org/
// License: GPLv3 <http://gplv3.fsf.org/>

// Includes
#include <iostream>
#include <string>
// Namespace
using namespace std;

// Global Varibles
char board[3][3] =
{
	{'_','_','_',},
	{'_','_','_',},
	{'_','_','_',}
};
string tmpBoard;
string winsX[9] = { "XXX??????", "???XXX???", "??????XXX", "X??X??X??", "?X??X??X?", "??X??X??X", "X???X???X", "??X?X?X??" };
string winsO[9] = { "OOO??????", "???OOO???", "??????OOO", "O??O??O??", "?O??O??O?", "??O??O??O", "O???O???O", "??O?O?O??" };
int scoreX = 0, scoreO = 0, ties = 0;
short int x, y; // "Disposable" varibles for positions on the game board 
bool trade = true; // Switches between true, and false for each players turn
bool startTrade = true;

// http://www.codeproject.com/KB/string/wildcmp.aspx
// Wildcard functions
int wildcmp(const char *wild, const char *string) {
  // Written by Jack Handy - jakkhandy@hotmail.com

  const char *cp = NULL, *mp = NULL;

  while ((*string) && (*wild != '*')) {
    if ((*wild != *string) && (*wild != '?')) {
      return 0;
    }
    wild++;
    string++;
  }

  while (*string) {
    if (*wild == '*') {
      if (!*++wild) {
        return 1;
      }
      mp = wild;
      cp = string+1;
    } else if ((*wild == *string) || (*wild == '?')) {
      wild++;
      string++;
    } else {
      wild = mp;
      string = cp++;
    }
  }

  while (*wild == '*') {
    wild++;
  }
  return !*wild;
}

// Prints out the game board
bool isNotFull() {
	for(int i = 0; i < 3; i++) {
		for(int j = 0; j < 3; j++)
			if(board[i][j] == '_') { return true; } 
	}
	return false; 
}

// Replaces an empty spot on the grid board
bool move(short int x, short int y, char spot) {
	// This is a way to use an if statment without specifying an else statement. The if statment contains a 
	// return so the function will exit. All other values, i.e. else, will return false. 
	if(board[(y-1)][(x-1)] == '_') {
		board[(y-1)][(x-1)] = spot;
		return true;
	}
	return false; 
}

// Reduces the board to a 9 letter string so it can be tested for a win
string boardString() {
	tmpBoard = ""; 
	for(int i = 0; i < 3; i++) {
		for(int j = 0; j < 3; j++)
			tmpBoard += board[i][j];
	}
	return tmpBoard;
}

void score() {
	cout << "Score X: " << scoreX << endl;
	cout << "Score O: " << scoreO << endl;
	cout << "Ties: " << ties << endl;
}

// Checks the board's state using all known win states. 
bool isWin() {
	for(int i = 0; i < 9; i++) {
		if( wildcmp(winsX[i].c_str(), boardString().c_str()) )
			{
				cout << "\nPlayer 1 Wins!" << endl;
				cout << "Player 2 will be sacrificed." << endl;
				scoreX++;
				score();
				return true; 
			}
		else if ( wildcmp(winsO[i].c_str(), boardString().c_str()) ) 
			{
				cout << "\nPlayer 2 Wins!" << endl;
				cout << "Player 1 will be sacrificed." << endl;
				scoreO++;
				score();
				return true;
			}	
		else if  ( !isNotFull() ) 
			{
				cout << "\nThe game is a tie." << endl;
				ties++;
				score();
				return true; 
			}
		}
	return false;
}

const int ROW=3;
const int COL=3;

void printBoard()
{
	int col;				//column counter
	int row;				//row counter

	//indent column markers
	cout<<"             ";

	//set column markers
	for(int i=1; i<=COL; i++)
		cout<<i<<"   ";

	//indent row 1
	cout<<"\n\n         ";

	//print ROW-1xCOL grid populated by the present values in the mark array
	for(row=0; row<ROW-1; row++)
	{
		cout<<row+1<<"  ";		//set row marker

		//print each column
		for(col=0; col<COL; col++)
		{
			cout<<"_"<<board[row][col]<<(col==(COL-1)? "_" : "_|");
		}
		cout<<"\n         ";
	}

	//print the final row
	row=ROW-1;
	cout<<row+1<<"  ";
	for(col=0; col<COL; col++)
		cout<<"_"<<board[row][col]<<(col==COL-1? "_" : "_|");
}

int main()
{
	//Welcome Message
	cout << "Welcome to Tic Tac Toe." << endl;
	cout << "Please pick your spots in grid format from the top-left corner." << endl;

	//Print Array
	printBoard();

	//Choose Spot
	while (1) {
		if(trade) {
			cout << "\nPlayer 1, please choose a spot: ";
			cin >> x >> y;
			move(x, y, 'X');
			trade = false;
		}
		else {
			cout << "\nPlayer 2, please choose a spot: ";
			cin >> x >> y;
			move(x, y, 'O');
			trade = true;
		}
		//Print Array
		printBoard();
		//Check Win
		if(isWin()) { 
			// Print 
			cout << "Starting next game." << endl;

			// Clear Board 
			for(int x=0; x<3; x++) {
				for( int y=0; y<3; y++) {
					board[x][y] = '_';
				}
			}

			// Opposite Start Turns
			startTrade = !startTrade;
			trade = startTrade;
		}
	}

	//Exit Program
	cout << endl;
	system("PAUSE");
	return 0;
}