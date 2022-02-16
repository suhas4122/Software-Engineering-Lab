#include "novel.hpp"
#include <bits/stdc++.h>
using namespace std;

Novel::Novel(const string &path1, const string &file, const string &bookType) : Book(path1, file, bookType){}

void Novel::parseBook()
{
    ifstream myfile(path);
    string line;

    if(chapters.empty() == 0)
    {
        chapters.clear();
    }

    int flag = 0;
    int counter = 0;
    int flag2 = 0;
    Chapter ch;
    paragraph currPara;
    while(getline(myfile, line))
    {        
        if(line.substr(0, 7) == "CHAPTER")
        {
            if(flag)
            {
                chapters.push_back(ch);
                ch.blocks.clear();
            }
            flag = 1;
            ch.number = ++counter;
            int ind = line.find('.') + 3;
            ch.name = line.substr(ind - 1, line.length() - ind);
            flag2 = 1;
        }
        else if(!flag) 
        {
            flag2 = 1;
        }
        else if(line == "")
        {
            ch.blocks.push_back(currPara);
            currPara.clear();
            flag2 = 1;
        }
        if(flag2 == 0)
        {
            currPara.push_back(line);
        }
        flag2 = 0;
    }
    chapters.push_back(ch);
}

int countMatchInRegex(string s, string word)
{
    stringstream cs(s);
    string str;
    int c = 0;
    while(getline(cs, str, ' '))
    {
        if (word == str) 
            c++;
        else if(str.back() == ',' ||str.back() == '.' || str.back() == ';' || str.back() == '?' || str.back() == '!')
        {
            if(str.substr(0, str.size() - 1) == word)
                c++;
        }
    }
    return c;
}

void case3(Book*);

void Novel::query(string q)
{
    vector<int>chapter_nos;
    vector<paragraph>paragraph_nos;
    priority_queue<pair<int, int>> top_chaps;
    priority_queue<pair<int, paragraph>> top_paras;
    int count_chap = 0;
    int count_para = 0;

    for(auto a : chapters)
    {
        for(auto b : a.blocks)
        {
            for(auto c : b)
            {
                transform(c.begin(), c.end(), c.begin(), ::tolower);
	            transform(q.begin(), q.end(), q.begin(), ::tolower);
                int counting = countMatchInRegex(c, q);
                count_chap += counting;
                count_para += counting;
            }
            if(count_para != 0) 
            {
                top_paras.push({count_para, b});
            }
            count_para = 0;
        }
        if(count_chap != 0)
        {
            top_chaps.push({count_chap, a.number});
        }
        count_chap = 0;
    }

    if(top_chaps.size() == 0 && top_paras.size() == 0)
    {
        cout<<"\nEntered word could not be found\n";
        Book* b = this;
        case3(b);
    }

    cout<<"\nEnter 1 if you want to see top k paragraphs";
    cout<<"\nEnter 2 if you want to see top k chapters";
    cout<<"\nEnter 3 if you want to end this query";
    cout<<"\n\nEnter your choice here : ";
    int choice;
    cin>>choice;
    int k;
    cout<<"\nEnter k : ";
    cin>>k;
    if(choice == 1)
    {
        cout<<"\nTop paragraphs with most occurances of this word are:\n";
        if(top_paras.size()>=k)
        {    
            for(int i = 1; i<=k; i++)
            {
                cout<<"\nParagrph "<<i<<".\n";
                cout<<"Number of of occurance of the word : "<<top_paras.top().first<<"\n\n";
                paragraph temp = top_paras.top().second;
                top_paras.pop();
                for(auto a : temp)
                {
                    cout<<a<<endl;
                }
            }
        }
        else
        {
            int length = top_paras.size();
            for(int i = 1; i<=length; i++)
            {
                cout<<"\nParagrph "<<i<<".\n";
                cout<<"Number of of occurance of the word : "<<top_paras.top().first<<"\n\n";
                paragraph temp = top_paras.top().second;
                top_paras.pop();
                for(auto a : temp)
                {
                    cout<<a<<endl;
                }
            }
            cout<<"No more paragraphs found with this word\n\n";
        }
    }
    else if(choice == 2)
    {
        cout<<"\nTop chapters with most occurances of this word are:\n\n";
        if(top_chaps.size()>=k)
        {    
            for(int i = 1; i<=k; i++)
            {
                cout<<i<<".  ";
                int temp = top_chaps.top().second;
                top_paras.pop();
                cout<<"CHAPTER "<<temp<<"\n"<<chapters[temp-1].name<<"\n\n";
            }
        }
        else
        {
            int length = top_chaps.size();
            for(int i = 1; i<=length; i++)
            {
                cout<<i<<".  ";
                int temp = top_chaps.top().second;
                top_paras.pop();
                cout<<"CHAPTER "<<temp<<"\n"<<chapters[temp-1].name<<"\n\n";
            }
            cout<<"No more chapter found with this word\n\n";
        }
    }
    else if(choice == 3)
    {
        cout<<"\n";
        return;
    }
    else
    {
        cout<<"\nInvalid choice";
        return;
    }
}