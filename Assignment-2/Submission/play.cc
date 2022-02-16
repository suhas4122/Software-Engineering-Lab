#include "play.hpp"
#include <bits/stdc++.h>
using namespace std;

Play::Play(const string &path1, const string &file, const string &bookType) : Book(path1, file, bookType){}

void Play::parseBook()
{
    ifstream myfile(path);
    string line;
    scene s;
    
    if(scenes.empty() == 0)
    {
        scenes.clear();
    }

    regex r("^[A-Z]+\\s{0,1}[A-Z]*\\.");

    while(getline(myfile, line))
    {
        if(line.substr(0, 6) == "CHORUS")
            continue;

        if(line.substr(0, 5) == "SCENE")
        {
            if(!s.empty())
            {
                scenes.push_back(s);
                s.clear();
            }
            continue;
        }

        smatch m;
        regex_search(line, m, r);
        if(m.size())
        {
            for(auto x : m)
                s.insert(x);
        }
    }
    if(!s.empty())
    {
        scenes.push_back(s);
        s.clear();
    }
}

void Play::query(string q)
{
    transform(q.begin(), q.end(), q.begin(), ::toupper);
    q = q + ".";

    set<string> answer;
    int count = 0;
    for(auto s : scenes)
    {
        if(s.find(q) != s.end())
        {
            for(auto s1 : s)
            {
                if(s1.compare(q))
                    answer.insert(s1);
            }
            count++;
        }
    }

    if(count == 0)
    {
        cout<<"\nNo matches found\n";
        return;
    }

    cout<<"\nList of all characters that come in atleast one scene with "<<q<<" is : \n";
    for(auto s1 : answer)
    {
        cout<<s1<<endl;
    }
    return;
}
