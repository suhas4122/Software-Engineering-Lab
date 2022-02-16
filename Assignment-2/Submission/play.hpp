#include "book.hpp"
#include <bits/stdc++.h>
using namespace std;

typedef set<string> scene;

#ifndef _PLAY_H
#define _PLAY_H

class Play : public Book
{
private:
	vector<scene> scenes;

public:
	Play(const string &path1, const string &file, const string &bookType);
	void parseBook();
    void query(string q);
};

#endif