#include <bits/stdc++.h>
#include "book.hpp"
#include "novel.hpp"
#include "play.hpp"
#include <dirent.h>
#include <sys/types.h>

using namespace std;

vector <Book*> book_list;

bool match_string(string s1, string s2)
{
	transform(s1.begin(), s1.end(), s1.begin(), ::tolower);
	transform(s2.begin(), s2.end(), s2.begin(), ::tolower);

	size_t found1 = s1.find(s2);
	size_t found2 = s2.find(s1);

    if (found1 != string::npos || found2 != string::npos)
    	return true;

    return false;
}

unordered_map <string, string> case1(string path1)
{
    const char* path = path1.c_str();
    unordered_set <string> names;
    DIR *dr;
    struct dirent *en;
    dr = opendir(path);
    
    if(dr) 
    {
        while ((en = readdir(dr)) != NULL) 
        {
            string file_name = (string)en->d_name;
                        
            names.insert(file_name);
        }
        names.erase(".");
        names.erase("..");
        closedir(dr); 
    }
    else
    {
        cout<<"\n*** File path invalid ***\n";
        exit(1);
    }

    unordered_map <string, string> initial;
    unordered_map <string, string> final;
    ifstream ip ("index.txt");  

    if(!ip.is_open())
    {
        cout<<"index.txt not found in the directory\n";
        exit(1);
    }

    string temp1, temp2;
    
    cout<<"\n*** Processing files in the entered directory ***\n";
    while (!ip.eof())
    {
        ip>>temp1;
        ip>>temp2;
        initial.insert({temp1, temp2});
    }
    
    for (auto itr = names.begin(); itr != names.end(); itr++) 
    {
        if(initial.find((*itr)) == initial.end())
        {
            cout<<"\nIf "<<(*itr)<<" is a novel enter 1 and if it is a play enter 2: ";
            int i;
            cin>>i;
            if(i==1)
            {
                final.insert({(*itr), "Novel"});
            }
            else
            {
                final.insert({(*itr), "Play"});
            }
        }
    }

    for (auto itr = initial.begin(); itr != initial.end(); itr++) 
    {
        if(names.find(itr->first) != names.end())
        {
            final.insert({itr->first, itr->second});
        }
    }

    ofstream op ("index.txt");

    for (auto itr1 = final.begin(); itr1 != final.end(); itr1++) 
    {
        op<<itr1->first<<endl;
        op<<itr1->second<<endl;
    }
    cout<<"\n*** Updated index.txt ***\n";

    return final;
}

void case3(Book*);

void case2()
{
    cout<<"\nEnter 1 if you want to see the list of all books\n";
    cout<<"Enter 2 if you want to search for a book\n";
    cout<<"Enter 3 to quit\n\n";
    cout<<"Enter your choice here : ";

    int in;
    cin>>in;
    map <int, int> index;
    int count = 1;

    if(in == 1)
    {
    	cout<<"\nEnter the index of the book which you want to select from the list below: \n";
        if(book_list.empty())
        {
            cout<<"No available books found\n";
            exit(-1);
        }
        for(int i=0; i<(int)book_list.size(); i++)
        {
            index[count] = i;
            cout<<"\nBook no. "<<i+1;
            book_list[i]->display();
            count++;
        }
    }
    else if(in == 2)
    {
        cout<<"\nEnter 1 if you want to search by title \n";
        cout<<"Enter 2 if you want to search by author\n";
        cout<<"Enter 3 to go back to main menu\n";
        cout<<"\nEnter your choice here : ";
        int j;
        cin>>j;
        string search;

        if(j == 1)
        {
            cout<< "\nEnter the title you want to search for: ";
            cin>>search;
            for(int i=0; i<(int)book_list.size(); i++)
	        {
	        	string name = book_list[i]->getTitle();
	       
	            if(match_string(name, search))
	            {
	            	index[count] = i;
	            	count++;
	            }
	        }
        }
        else if(j==2)
        {
            cout<< "\nEnter the author you want to search for: ";
            cin>>search;
            for(int i=0; i<(int)book_list.size(); i++)
	        {
	        	string name = book_list[i]->getAuthor();
	            if(match_string(name, search))
	            {
	            	index[count] = i;
	            	count++;
	            }
	        }
        }
        else if(j==3)
        {
            case2();
        }
        else
        {
            cout<<"Enter a valid number "<<endl;
            case2();
        }

        if(index.empty())
	    {
	    	cout<<"\nNo matches found"<<endl;
	    	case2();
	    }
	    else
	    {
	    	cout<<"Enter the index of the book which you want to select from the list below: \n";
	    	int count = 1;
	    	for(auto it: index)
	    	{
	    		cout<<"\nBook no. "<<count;
	    		int number = it.second;
	            book_list[number]->display();
	            count++;
	    	}
            cout<<"Enter your choice here : ";
            cin>>count;
            int ll;
            cout<<"\nEnter 1 if you want to read the book or enter 2 if you want to do a query : ";
            cin>>ll;
            if(ll == 1)
                book_list[index[count]]->printBook();
            case3(book_list[index[count]]);
            return;
	    }
    }
    else if(in == 3)
    {
        cout<<"*** THANK YOU ***\n";
        exit(1);
    }
    else 
    {
        cout<<"Invalid input, please try again \n";
        exit(1);
    }
    
    int count1;

    cout<<"Enter your choice here : ";
    cin>>count1;
    while(count1<0 || count1 > count)
    {
        cout<<"\nEnter a valid number, or enter 0 to exit : ";
        cin>>count1;
        if(count1 == 0)
        {
            case2();
        }
    }
    int ll;
    cout<<"\nEnter 1 if you want to read the book or enter 2 if you want to do a query : ";
    cin>>ll;
    if(ll == 1)
        book_list[index[count1]]->printBook();
    case3(book_list[index[count1]]);
}

void case3(Book* book1)
{
    cout<<"\nWhat do you want to do?\n";
    cout<<"Enter 1 if you want to do a query on the book\n";
    cout<<"Enter 2 if you want to go back to the main menu\n";
    cout<<"Enter 3 if you want to quit\n";
    cout<<"\nEnter your choice here : ";
    int choice;
    cin>>choice;

    if(choice == 1)
    {
        if(book1->getType() == "Novel")
        {
            Novel* novel1 = static_cast<Novel*> (book1);
            novel1->parseBook();
            cout<<"\nThe selected book is a Novel, enter a word you want to search : ";
            string q;
            cin>>q;
            novel1->query(q);
        }
        else
        {
            Play* play1 = static_cast<Play*> (book1);
            play1->parseBook();
            cout<<"\nThe selected book is a Play, enter the name of the character : ";
            string q;
            cin>>q;
            play1->query(q);
        }
        case3(book1);
    }
    else if(choice == 2)
    {
        case2();
    }
    else if(choice == 3)
    {
        cout<<"\n*** THANK YOU *** \n";
        exit(1);
    }
    else
    {
        cout<<"Invalid number entered";
        case2();
    }
    return;
}

int main()
{
    string path;
    cout<<"*** WELCOME ***\n\n";
    cout<<"Enter the path of the directory containing the books: ";
    cin>>path;
    unordered_map <string, string> names = case1(path);

    for(auto book: names)
    {
        string new_path = path + "/" + book.first;
        if(book.second == "Novel")
            book_list.push_back(new Novel(new_path, book.first, book.second));
        else
            book_list.push_back(new Play(new_path, book.first, book.second));
    }

    for(auto book: book_list)
    {
        string new_path = book->getPath();
        book->parseHeader(new_path);
    }
    case2();
    return(0);
}
