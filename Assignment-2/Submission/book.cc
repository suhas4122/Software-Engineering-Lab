#include "book.hpp"
#include <bits/stdc++.h>
using namespace std;

Book::Book(const string &path1, const string &file, const string &bookType){
    this->path = path1;
    this->fileName = file;
    this->type = bookType;
}

string Book:: getTitle()
{
    return title;
}

string Book:: getFilename()
{
    return fileName;
}

string Book:: getAuthor()
{
    return author;
}

string Book:: getPath()
{
    return path;
}

string Book:: getReleaseDate()
{
    return rdate;
}

string Book:: getLanguage()
{
    return language;
}

string Book:: getType()
{
    return type;
}

void Book::printBook()
{
    ifstream myfile(path);
    cout<<"*** Displaying the selected book ***\n\n";
    int count = 1;
    string input;
    string header("*** START OF THIS PROJECT GUTENBERG EBOOK");

    while(getline(myfile, input))
    {
        if(input.find(header) != string::npos)
            break;
    }
    int skip = 0;
    while(getline(myfile, input))
    {
        skip++;
        if(skip == 3)
            break;
    }
    while(getline(myfile, input))
    {
        if(count % 45 == 0)
        {
            cout << "\nDo you want to continue?";
            cout<<"\nEnter 1 for \"No\" and 2 for \"Yes\" : ";
            int num;
            cin>>num;
            if(num == 1){
                cout<<endl;
                return;
            }
            cout<<endl;
        }
        cout<<input<<endl;
        count++;
    }
    cout<<"\n*** Book Completed ***\n";
    myfile.close();
}

void Book::parseHeader(const string &path1)
{
    ifstream file;
    file.open(path1, std::ios::in);
    
    if(file.is_open())
    {
        string line;
        string header("*** START OF THIS PROJECT GUTENBERG EBOOK");
        string title("Title:");
        string author("Author:");
        string rdate("Release Date:");
        string language("Language:");

        while(getline(file,line))
        {
            if(line.find(title) != string::npos)
            {
                this->title.insert(0,line.substr(line.find(" ")+1,line.size()-1));
            }
            else if(line.find(author) != string::npos)
            {
                this->author.insert(0,line.substr(line.find(" ")+1,line.size()-1));
            }
            else if(line.find(language) != string::npos)
            {
                this->language.insert(0,line.substr(line.find(" ")+1,line.size()-1));
            }
            else if(line.find(rdate) != string::npos)
            {
                this->rdate.insert(0,line.substr(line.find(" ")+1,line.size()-1));
            }
            else if(line.find(header) != string::npos)
            {
                break;
            }
        }
    }
    else
    {
        cout<<"Couldn't open file"<<endl;
    }
    
    file.close();
}

void Book::display()
{
	cout<<"\nFile Name : ";
    cout<< this->getFilename();
	cout<<"\nTitle : ";
    cout<< this->getTitle();
    cout<<"\nAuthor : ";
    cout<< this->getAuthor()<<"\n\n";
}

