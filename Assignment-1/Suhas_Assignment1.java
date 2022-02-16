/*
Suhas Jain
19CS30048
Group - 6
Software Engineering lab
Assignment - 0
*/

import java.util.*;

public class Suhas_Assignment1
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in); //to scan for inputs 
		String  x;  // to take input from main menu
		int identity = 0; //to keep track of unique id of each node 
		Map<Integer, Node> nodes = new HashMap<Integer, Node>(); //a set storing all the nodes 
		ArrayList<String> names = new ArrayList<String>(Arrays.asList(" ", "Individual", "Business", "Organisation", "Group")); //storing names for each type of node

		x = "0";

		System.out.println("\n*** For a better experience, please use terminal in enlarged mode ***\n");

		while(x != "11")// this is the while loop which takes input about the action user want to do and calls the required function
		{
			System.out.println("*** MAIN MENU ***") ;
			System.out.println("Enter the number in front to action you want to do.") ;
			System.out.println("1  : Create new node") ;
		    System.out.println("2  : Delete a node") ;
		    System.out.println("3  : Print all nodes") ;
		    System.out.println("4  : Search for a node") ;
		    System.out.println("5  : Add a new link") ;
		    System.out.println("6  : Print all nodes linked to a given node") ;
			System.out.println("7  : Create a post ") ;
			System.out.println("8  : Reposting an old post ") ;
		    System.out.println("9  : Searching content by a node ") ;
		    System.out.println("10 : Display contents of nodes linked to a given node ") ;
		    System.out.println("11 : Quit") ;

			x = input.nextLine();

			if(x.equals("1")) 
		    {
				Node n = createNode(input, identity);
				nodes.put(identity, n);
				System.out.println("\nNode created successfully!!");
				System.out.println("Id of the created node : "+ identity + "\n");
				identity++;
			}
			else if(x.equals("2"))
			{
				deleteNodes(input, nodes);
			}
			else if(x.equals("3"))
			{
				printAllNodes(nodes, names);
			}
			else if(x.equals("4"))
			{
				searchNode(input, nodes, names);
			}
			else if(x.equals("5"))
			{
				createLinks(input, nodes, identity);
			}
			else if(x.equals("6"))
			{
				allNodes(input, nodes, names);
			}
			else if(x.equals("7"))
			{
				createPost(input, nodes);
			}
			else if(x.equals("8"))
			{
				createRepost(input, nodes);
			}
			else if(x.equals("9"))
			{
				searchContent(input, nodes);
			}
			else if(x.equals("10"))
			{
				allContentLinked(input, nodes);
			}
			else if(x.equals("11"))
			{
				break;
			}
			else
			{
				System.out.println("Invalid input, please try again");
			}
		}
	}
	
	static Node createNode(Scanner input, int identity){
	    /* 
	    Function to create a new node and return it 
	    It takes input the type of node user wants to make
	    and then calls the constructor of that type of node 
	    */
	    System.out.println("Individuals  : 1") ;
		System.out.println("Business     : 2") ;
		System.out.println("Organisation : 3") ;
	    System.out.println("Groups       : 4") ;
	    System.out.print("Enter the option : ") ;
	    String x = input.nextLine() ; 
	    
	    if(x.equals("1")){ 
			return new Individual(input, identity); 
		}
		else if(x.equals("2")){ 
			return new Business(input, identity); 
		}
		else if(x.equals("3")){ 
			return new Organisation(input, identity); 
		}
		else if(x.equals("4")){ 
			return new Group(input, identity); 
		}
		else{ 
			System.out.println("Enter a number between 1-4");
		}

		return createNode(input, identity); 
	}

	static void deleteNodes(Scanner input, Map<Integer, Node> nodes)
	{
		/*
		Function to delete a node, it does 2 tasks:
		1) Deletes node from main nodes set defined in main
		2) Deletes node fron all the sets storing the link to that node in all the nodes
		*/
		System.out.print("Enter Id of the element you want to delete  : ");
		int in = Integer.parseInt(input.nextLine());

		if(nodes.containsKey(in)) 
		{
			Node rem = nodes.get(in);
			nodes.remove(in);  //removing from nodes set
			for(Map.Entry element : nodes.entrySet())
            {
				Node temp = (Node) element.getValue();
				if(temp.link.containsKey(rem))
				{
					temp.link.remove(rem); //cheching if the link to the node is present and deleting it if found
				}
			}
			System.out.println("Node deleted successfully!! \n");
		}
		else
		{
			System.out.println("No such key exists \n"); //in case node of that id does not exist 
		}
	}

	static void printAllNodes(Map<Integer, Node> nodes, ArrayList<String> names)
	{
		/*
		This function just checks if the set containing nodes is non-empty and 
		prints all the nodes calling the printing functions of Node class if found so
		*/
		if(nodes.isEmpty())
		{
			System.out.println("No nodes found");
			return;
		}
		for(Map.Entry element : nodes.entrySet())
		{
			Node temp = (Node) element.getValue();
			temp.printobj(names);
		}
	}

	static void searchNode(Scanner input, Map<Integer, Node> nodes, ArrayList<String> names) 
	{
		/*
		This function searhes for a particular node in 3 ways 
		1) By name
		2) By type
		3) By birthday
		*/
		if(nodes.isEmpty())
		{
			System.out.println("No nodes found.\n");
			return;	
		}

        System.out.println("Enter Keytype (N or name, T for type and B for birthday)");
        String keyType = input.nextLine();

        ArrayList<Integer> ans = new ArrayList<Integer>(); //to store all the nodes which satisfy input conditions 

        if (keyType.equalsIgnoreCase("N"))  //in case user wants to search from name
        {
        	System.out.println("Enter Key");
        	String key = input.nextLine();

            for(Map.Entry element : nodes.entrySet())
            {
				Node temp = (Node) element.getValue();
				if(temp.name.equalsIgnoreCase(key))  //Matching the name of all the nodes with input and additing to ans if found
				{
					ans.add(temp.id);
				}
			}
		} 
		else if (keyType.equalsIgnoreCase("T"))  //in case user wants to search from type
		{
			System.out.println("Enter Key");
        	String key = input.nextLine();

			for(Map.Entry element : nodes.entrySet())
			{
				Node temp = (Node) element.getValue();
				if(names.get(temp.type).equalsIgnoreCase(key)) //Matching the type of all the nodes with input and adding to ans if found
				{
					ans.add(temp.id);
				}
			}
		} 
		else if (keyType.equalsIgnoreCase("B"))   //in case user wants to search from type
		{
			System.out.println("Enter Key");
        	String key = input.nextLine();
        	
			for(Map.Entry element : nodes.entrySet())
			{
				Node temp = (Node) element.getValue();
				if(temp.type == 1)                    //in this case we also need to check if the node is of type indivisual or not
				{				
					Individual temp1 = (Individual) temp;	
					if(temp1.birthday.equals(key)) //Matching the type of all the indivisuals with input and adding to ans if found
					{
						ans.add(temp1.id);
					}
				}
			}
        }
        else
        {
        	System.out.println("Invalid key entered \n");
        	return;
        }
		if(ans.isEmpty())
		{
			System.out.println("No nodes found by that keyword \n");
			return;
		}
        for (int i : ans)
        {
			Node temp = nodes.get(i);
			temp.printobj(names);
		}
	}
	
	static void createLinks(Scanner input, Map<Integer, Node> nodes, int i)
	{
		/*
		This function creates links between 2 nodes 
		It checks the type of link user wants to create and 
		checks if it is among the 4 types permitted
		And then adds the link accordingly
		It has all the exception handling taken care of
		*/
		System.out.println("Enter ID of 1st node");
        int x = Integer.parseInt(input.nextLine());
        if(!nodes.containsKey(x)){    // checking if the index exists
			System.out.println("Invalid index entered\n");
			return;
		}
        System.out.println("Enter ID of 2nd node");
		int y = Integer.parseInt(input.nextLine());
		if(!nodes.containsKey(y)){     // checking if the index exists
			System.out.println("Invalid index entered\n");
			return;
		}
		
		Node node1 = nodes.get(x);
		Node node2 = nodes.get(y);
		int type1 = node1.type;
		int type2 = node2.type;
		int flag = 0;  //used to track if the link was created, to notify the error message 

		if((type1 == 1 && type2 == 3) || (type1 == 3 && type2 == 1))  //link between indivisual and organisation 
		{
			node1.link.put(node2, "Member of Organisation");
			node2.link.put(node1, "Member of Organisation");
			flag = 1;
		}
		else if((type1 == 1 && type2 == 4) || (type1 == 4 && type2 == 1)) //link between indivisual and group
		{
			node1.link.put(node2, "Member of Group");
			node2.link.put(node1, "Member of Group");
			flag = 1;
		}
		else if((type1 == 4 && type2 == 2) || (type1 == 2 && type2 == 4)) //link between business and group
		{
			node1.link.put(node2, "Business member of Organisation");
			node2.link.put(node1, "Business member of Organisation");
			flag = 1;
		}
		else if((type1 == 1 && type2 == 2) || (type1 == 2 && type2 == 1))//link between indivisual and business
		{
			System.out.println("Enter 1 if Individual is a customer and 2 if owner");
			int type = Integer.parseInt(input.nextLine());// in this case link can be of 2 types, indivisual can be owner or customer
			if(type == 1)
			{
				node1.link.put(node2, "Customer of Business");
				node2.link.put(node1, "Customer of Business");
				flag = 1;
			}
			else if(type == 2)
			{
				node1.link.put(node2, "Owner of Business");
				node2.link.put(node1, "Owner of Business");
				flag = 1;
			}
		}
		if(flag == 1)
		{
			System.out.println("Link created successfully!!\n");
		}
		else
		{
			System.out.println("This type of link is not permitted, try again\n");
		}
	}	

	static void allNodes(Scanner input, Map<Integer, Node> nodes, ArrayList<String> names)
	{
		/*
		This function prints all nodes that are linked to a given node
		it does this in 2 steps 
		1) Checks if the set storing links of that node is non-empty
		2) Traversal over the links set of that node and calling print function of all nodes present
		*/
		System.out.println("Enter ID of the node");
		int id1 = Integer.parseInt(input.nextLine());
		Node n1 = nodes.get(id1);

		if(n1.link.isEmpty())
		{
			System.out.println("No links found\n");
			return;
		}

		for(Map.Entry element : n1.link.entrySet())
		{
			Node temp = (Node) element.getKey();
			String relation = (String) element.getValue();
			System.out.println(relation);
			temp.printobj(names);
		}	
	}

	static void createPost(Scanner input, Map<Integer, Node> nodes)
	{
		/*
		This function creates a post for a node
		All the unique posts of a node are stored within array of strings within the node
		This function does the following
		1) Takes input the id of node and the post (as string) from the user
		2) Checks within the previous posts if it is already present (uniqueness)
		3) Appends the post at the end of the posts array if it is unique, otherwise throws an error message
		*/
		System.out.println("Enter the ID of node for which you will like to post");
		int id1 = Integer.parseInt(input.nextLine());

		if(!nodes.containsKey(id1))
		{
			System.out.println("No such ID exists" + "\n");
			return;
		}

		System.out.println("Enter the message that you want to post");
		String message = input.nextLine();
		
		Node given = nodes.get(id1);

		if(given.contents.isEmpty())
		{
			given.contents.add(message);
			System.out.println("Message posted successfully!!" + "\n");
		}
		else
		{
			for(String s : given.contents)
			{
				if(s.equals(message))
				{
					System.out.println("Message already exists" + "\n");
					return;
				}
			}
			given.contents.add(message);
			System.out.println("Message posted successfully!!" + "\n");
		}
	}

	static void createRepost(Scanner input, Map<Integer, Node> nodes)
	{
		/*
		This function just prints all the previously posted messages of a given user and 
		asks which message you wants to repost.
		It reposts if the input is valid otherwise throws an error message 
		*/
		System.out.println("Enter the ID of node for which you will like to re-post");
		int id1 = Integer.parseInt(input.nextLine());
		Node given = nodes.get(id1);

		System.out.println("Enter the index of post which you want to re-post");
		int i = 1;
		if(given.contents.isEmpty())
		{
			System.out.println("No previous message found.\n");
			return;
		}
		else
		{
			for(String s : given.contents)
			{
				System.out.println("Index : " + i);
				i++;
				System.out.println(s + "\n");
			}
		}
		int index = Integer.parseInt(input.nextLine());
		if(index>0 && index<=given.contents.size())
		{
			System.out.println("Message reposted successfully\n");
		}
		else
		{
			System.out.println("Invalid index entered\n");
		}
	}

	static void searchContent(Scanner input, Map<Integer, Node> nodes)
	{
		/*
		This function bascically prints all the previous posts by a node
		whose id is input by the user with proper indexing
		*/
		System.out.println("Enter the ID of node for which you want to search content");
		int id1 = Integer.parseInt(input.nextLine());
		Node given = nodes.get(id1);

		int count = 1;

		if(given.contents.isEmpty())
		{
			System.out.println("No message found.\n");
		}
		else
		{
			for(String s : given.contents)
			{
				System.out.println("Post no. " + count);
				count++;
				System.out.println(s + "\n");
			}
		}
	}

	static void allContentLinked(Scanner input, Map<Integer, Node> nodes)
	{
		/*
		This function goes to all the linked nodes of a particular node
		and then accesses all their posts and indexes them and prints 
		*/
		System.out.println("Enter the ID of node");
		int id1 = Integer.parseInt(input.nextLine());
		Node given = nodes.get(id1);
		int i = 1;

		if(given.link.isEmpty())
		{
			System.out.println("No links found\n");
			return;
		}
		for(Map.Entry element : given.link.entrySet())
		{
			Node temp = (Node) element.getKey();
			System.out.println("Node no. "+ i);
			System.out.println("Name : " + temp.name + "\n");
			int j = 1;
			if(temp.contents.isEmpty())
			{
				System.out.println("No message found.\n");
			}
			else
			{
				for(String s : temp.contents)
				{
					System.out.println("Post no. " + j);
					j++;
					System.out.println(s + "\n");
				}
			}
			i++;
		}
	}
}

class Node {  //This the node class which stores the data of all nodes
	int id ; //unique id of all nodes
	String name; //name of the node
	Date doc ;  //Date of creation of each node 
	int type;  //type of each node among the 4 given types
	ArrayList<String> contents; // array of strings storing all the posts (unique posts)
    Map<Node, String> link; //Storing all the nodes which are linked 

    public Node(Scanner input, int identity) //constructor 
    {
        this.id = identity;  //assigning unique id
        System.out.print("Enter the name : ") ; 
        this.name = input.nextLine() ;  //Taking name as input
        contents = new ArrayList<String>();
        link = new HashMap<Node, String>();
        doc = new Date(); //storing date of creation 
    }

    void printobj(ArrayList<String> names) //function to print the arrtributes of the node 
    {
		System.out.println("Id : "+id);
		System.out.println("Type : "+ names.get(this.type));
        System.out.println("Name : "+name);
        System.out.println("Date of Creation : "+doc);
    }
}

class Individual extends Node  //indivisual class
{
    String birthday ;  //Storing special attribute birthday 

    public Individual(Scanner input, int identity) //constructor
    {
        super(input, identity) ; 
        System.out.print("Enter the date of Birth in DD/MM/YYYY : ");
		this.birthday = input.nextLine() ; 
		this.type = 1;
    }
    void printobj(ArrayList<String> names) //printing function
    {
		super.printobj(names);
        System.out.println("Date of Birth : "+birthday+ "\n") ; 
    }
}

class Business extends Node //business class
{
	String x, y ;  //Storing special attributes, coordinates

    public Business(Scanner input, int identity) //Constructor 
    {
        super(input, identity) ; 
        System.out.print("Enter the X coordinate : ") ; 
        this.x = input.nextLine() ; 
        System.out.print("Enter the Y coordinate : ") ; 
		this.y = input.nextLine() ;
		this.type = 2;
    }

    void printobj(ArrayList<String> names) //printing function
    {
        super.printobj(names);
        System.out.println("Location of Business is : ("+ x +","+ y+")\n");
    }
}

class Organisation extends Node //organisation class
{
    String x, y ;  //Storing special attributes, coordinates

    public Organisation(Scanner input, int identity)//Constructor 
    {
        super(input, identity) ; 
        System.out.print("Enter the X coordinate : ") ; 
        this.x = input.nextLine() ; 
        System.out.print("Enter the Y coordinate : ") ; 
		this.y = input.nextLine() ;
		this.type = 3;
    }

    void printobj(ArrayList<String> names) //printing function
    {
        super.printobj(names);
        System.out.println("Location of Organisation is : ("+ x +","+ y+ ")\n");
    }
}

class Group extends Node //group class
{
    public Group(Scanner myObj, int identity) //Constructor 
    {
		super(myObj, identity) ; 
		this.type = 4;
    }

    void printobj(ArrayList<String> names)  //printing function
    { 
		super.printobj(names);
		System.out.println("");
    }
}
