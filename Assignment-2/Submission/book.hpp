#include <iostream>
#include <string>
using namespace std;

#ifndef _BOOK_H
#define _BOOK_H


class Book
{
protected:
    string fileName;
    string path;
    string title;
    string author;
    string type;
    string rdate;
    string language;

public:
    Book(const string &path, const string &file, const string &bookType);
    string getTitle();
    string getFilename();
    string getAuthor();
    string getPath();
    string getType();
    string getReleaseDate();
    string getLanguage();
    void display();
    void printBook();
    void parseHeader(const string &fileName);
};

#endif