from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

img_list = []

class Message:

    def __init__(self, text, img_path, r_type, r_id, s_id):
        self.text = text
        self.img_path = img_path
        self.receiver_type = r_type
        self.receiver_id = r_id
        self.sender_id = s_id

    def printer(self):
        print("Message was sent from " + str(self.sender_id))
        print("Received by " + self.receiver_type + str(self.receiver_id))
        print(self.text)
        print(self.img_path)

class User:
    def __init__(self, no):
        self.id1 = no
        self.id2 = "User#" + str(no)
        self.contacts = []
        self.groups = []
        self.rec_messages = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def add_group(self, group):
        self.groups.append(group)


class Group:
    def __init__(self, no):
        self.id1 = no
        self.id2 = "Group#" + str(no)
        self.members = []
        self.messages = []

    def add_member(self, member):
        self.members.append(member)

    def add_message(self, message):
        self.messages.append(message)


class LeftFrame(Frame):
    def __init__(self, master, users, rframe):
        Frame.__init__(self, master)
        self.master = master
        self.grid(row=0, column=0)
        master.columnconfigure(0,weight=1)
        master.rowconfigure(0,weight=1)

        self.label = Label(self, text="Select user from the list below\n", font = ("Fixedsys", 13, "bold"), padx=0, pady=0)
        self.label.grid(row=0, column=0, columnspan = 2, sticky = NSEW)

        self.rframe = rframe
        self.users = users

        self.variable = StringVar(self)
        self.variable.set(users[0].id2)  # default value
        self.variable.trace_add("write", self.update)
        member_list = [x.id2 for x in users]
        self.w = OptionMenu(self, self.variable, *member_list)
        self.w.config(width = 20)
        self.w.grid(row=1, column=0, columnspan = 2, sticky = NSEW)

        self.text1 = Text(self, width=40, height=30, font = ("Fixedsys", 12), padx=10, pady=0)
        self.text1.grid(row=3, column=0, sticky = NSEW)

        self.text2 = Text(self, width=40, height=30, font = ("Fixedsys", 12), padx=3, pady=0)
        self.text2.grid(row=3, column=1, sticky = NSEW)

        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)

        self.update1()
        
    def get_user(self):
        return self.variable.get()

    def show_contacts(self):
        user1 = self.get_user()
        self.text1.delete("1.0", "end")
        self.text1.insert(INSERT, "\nThe list of users in contact : \n\n")
        for x in users:
            if x.id2 == user1 :
                for y in x.contacts:
                    self.text1.insert(INSERT, "User#" + str(y) + '\n')
    
    def show_groups(self):
        user1 = self.get_user()
        self.text2.delete("1.0", "end")
        self.text2.insert(INSERT, "\nThe list of groups user is part of : \n\n")
        for x in users:
            if x.id2 == user1 :
                for y in x.groups:
                    self.text2.insert(INSERT, "Group#" + str(y) + '\n')

    def update(self, var, indx, mode):
        g = self.variable.get()
        self.text1.delete(1.0, END)
        self.text2.delete(1.0, END)
        self.rframe.scroll_1(g) 
        self.show_contacts()
        self.show_groups()           
        for x in self.users:
            if x.id2 == g:
                self.rframe.box_1(x.id1)

    def update1(self):
        g = self.variable.get()
        self.text1.delete(1.0, END)
        self.text2.delete(1.0, END)
        self.rframe.scroll_1(g) 
        self.show_contacts()
        self.show_groups()           
        for x in self.users:
            if x.id2 == g:
                self.rframe.box_1(x.id1)


class RightFrame(Frame):

    def __init__(self, master, users, groups):
        Frame.__init__(self, master)
        self.master = master
        self.users = users
        self.groups = groups

        self.grid(row=0, column=1, sticky = NSEW)
        master.columnconfigure(1,weight=1)

        self.i_path = ""

        self.label1 = Label(self, text="\nReceived Messages", font = ("Fixedsys", 13, "bold"))
        self.label1.grid(row=1, column=0, sticky = NSEW)

        self.label2 = Label(self, text="\nPost Messages", font = ("Fixedsys", 13, "bold"))
        self.label2.grid(row=0, column=1, columnspan = 2, sticky = NSEW)

        self.t1 = Text(self, width=40, height=29, font = ("Fixedsys", 12), padx=15, pady=0)
        self.t2 = Text(self, width=40, height=29, font = ("Fixedsys", 12), padx=15, pady=0)
        self.t1.grid(row=2, column=0, sticky = NSEW)               
        self.t2.grid(row=2, column=1, columnspan = 2, sticky = NSEW)

        self.b1 = Button(self, text="Post", font = ("Fixedsys", 11, "bold"), command = self.post_message)
        self.b1.grid(row=3, column=1, columnspan = 1, sticky = NSEW)

        self.b2 = Button(self, text="Select Image", font = ("Fixedsys", 11, "bold"), command = self.insert_image)
        self.b2.grid(row=3, column=2, columnspan = 1, sticky = NSEW)

        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)


    def scroll_1(self, user1):
        self.g_user = user1
        self.cons = []
        for x in self.users:
            if x.id2 == user1 :
                for y in x.contacts:
                    self.cons.append("User#" + str(y))
        for x in self.users:
            if x.id2 == user1 :
                for y in x.groups:
                    self.cons.append("Group#" + str(y))
        self.v1 = StringVar(self)
        self.v1.set(self.cons[0])
        self.w1 = OptionMenu(self, self.v1, *self.cons)
        self.w1.config(width = 13)
        self.w1.grid(row=1, column=1, columnspan = 2, sticky = S+E+W)    

    def box_1(self, user1):
        global img 
        self.t1.delete("1.0", "end")
        for i in self.users[user1-1].rec_messages:
            if i.receiver_type == "u":
                s1 = " (Personal)";
            else:
                s1 = " (through Group#" + str(i.receiver_id) +")"
            s = "From User#" + str(i.sender_id) + s1 + "\n" + i.text
            self.t1.insert(END, s)
            if i.img_path != "":
                img = Image.open(i.img_path)
                img = img.resize((350, 250), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                img_list.append(img)
                self.t1.image_create(END, image = img_list[-1])
            self.t1.insert(END, "\n\n")

    def insert_image(self):
        global img
        self.i_path = filedialog.askopenfilename(initialdir="/home", title="Select a file")
    

    def post_message(self):
        receiver = self.v1.get()
        text = self.t2.get(1.0, END)

        if receiver[0] == "U":
            s_id = int(self.g_user[5:])
            r_id = int(self.v1.get()[5:])
            m = Message(text, self.i_path, "u", r_id, s_id)
            messages.append(m)
            self.users[r_id-1].rec_messages.append(m)
            self.t2.delete(1.0, END)

        else:
            s_id = int(self.g_user[5:])
            r_id = int(self.v1.get()[6:])
            m = Message(text, self.i_path, "g", r_id, s_id)
            messages.append(m)
            for x in self.groups:
                if x.id1 == r_id:
                    x.add_message(m)
                    for y in x.members:
                        self.users[y-1].rec_messages.append(m)
            self.t2.delete(1.0, END)

        self.i_path = ""
        m1 = messages[-1]
        f1 = open("messages.txt", "r")
        s1 = f1.read()
        f1.close()
        f1 = open("messages.txt", "w")
        s2 = "\n" + m1.receiver_type + "\n" + str(m1.receiver_id) + "\n" + str(m1.sender_id) + "\n" + m1.img_path + "\n" + m1.text
        s1 = s1 + s2
        s1 = f1.write(s1)
        f1.close()

users = []
groups = []
contacts = {}
grpmem = {}

class update():
    def __init__(self):
        file = open("social_network.txt")
        flag = 0
        users.clear()
        groups.clear()
        contacts.clear()
        grpmem.clear()

        for line in file:

            if line.find('users') != -1:
                flag = 1

            elif line.find('groups') != -1:
                flag = 2

            elif flag==1:
                line = line[1:-2]
                pos = line.find(':')
                no = int(line[0:pos])
                m = User(no)
                line = line[pos+2:]
                identity = m.id1
                contacts[identity] = set(map(str, line.split(', ')))
                for x in contacts[identity]:
                    y = int(x)
                    m.add_contact(y)
                users.append(m)

            elif flag == 2:
                line = line[1:-2]
                pos = line.find(':')
                no = int(line[0:pos])
                g = Group(no)
                line = line[pos+2:]
                identity = g.id1
                grpmem[identity] = set(map(str, line.split(', ')))
                for x in grpmem[identity]:
                    y = int(x)
                    g.add_member(y)
                    users[y-1].add_group(int(identity))
                groups.append(g)

        file.close()

messages = [] 

class updatemsgs:

    def __init__(self):
        f = open("messages.txt", "r")
        lines = f.readlines()
        i = 1
        while i<len(lines):
            lines[i] = lines[i].strip()
            if(lines[i] == "u"):
                i = i+1
                r_id = int(lines[i])
                i = i+1
                s_id = int(lines[i])
                i = i+1
                i_t = lines[i]
                i = i + 1
                t = lines[i]
                if i_t == "\n":
                    i_t = ""
                i_t = i_t.strip()
                m = Message(t, i_t, "u", r_id, s_id)

                users[r_id-1].rec_messages.append(m)
                messages.append(m)
                i = i+2

            elif (lines[i] == "g"):
                i = i+1
                r_id = int(lines[i])
                i = i+1
                s_id = int(lines[i])
                i = i+1
                i_t = lines[i]
                i = i + 1
                t = lines[i]
                if i_t == "\n":
                    i_t = ""
                i_t = i_t.strip()
                m = Message(t, i_t, "g", r_id, s_id)

                for x in groups:
                    if x.id1 == r_id:
                        x.add_message(m)
                        for y in x.members:
                                users[y-1].rec_messages.append(m)

                messages.append(m)
                i = i+2
            else:
                break

        f.close()


class Window(Frame):
    def __init__(self, master, users, groups):
        Frame.__init__(self, master)
        self.master = master
        master.geometry("")
        self.rightframe = RightFrame(master, users, groups)
        self.leftframe = LeftFrame(master, users, self.rightframe)
        master.wm_title("Social Media")
        self.grid(row=0, column=0, sticky= NSEW)
    
    def update_val(self, user1):
        self.rightframe.scroll_1(user1)

update()
updatemsgs()
root = Tk()
app = Window(root, users, groups)
root.mainloop()