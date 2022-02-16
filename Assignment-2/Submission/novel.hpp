#include "book.hpp"
#include <bits/stdc++.h>
using namespace std;

typedef vector<string> paragraph;

#ifndef _CHAPTER_H
#define _CHAPTER_H

struct Chapter 
{
    int number;
    string name;
    vector<paragraph> blocks;
};

#endif

#ifndef _NOVEL_H
#define _NOVEL_H

class Novel : public Book
{
protected:
    vector<Chapter> chapters;

public:
    Novel(const string &path1, const string &file, const string &bookType);
    void parseBook();
    void query(string q);
};


#endif