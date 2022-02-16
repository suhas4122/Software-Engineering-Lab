# In this python file, only the definations for the magic functions and the basic operations
# for the question segments are provided. There may be the need to add new functions or overload 
# existing ones as per the question requirements.

class Vector:
        
    def __init__(self, *args): 
        # if arg is an int(dimension)
        if isinstance(args[0], int): 
            self._coords = [0]*args[0]
        if isinstance(args[0], list):
            self._coords = args[0]

    def __len__(self):
        # return the dimension of the vector
        return len(self._coords)

    def __getitem__(self, j):
        # return the jth coordinate of the vector
        if j >= len(self):
            print("Index out of bounds")
            return
        return self._coords[j-1]

    def __setitem__(self, j, val):
        # set the jth coordinate of vector to val
        if j >= len(self):
            print("Index out of bounds")
            return
        self._coords[j-1] = val

    def __add__(self, other):
        # u + v
        if(len(self) != len(other)):
            print("Size of both the vectors isn't same")
        else:
            new = [0] * len(self)
            for i in range(len(self)):
                new [i] = self._coords[i] + other._coords[i]
        return Vector(new)
            
    def __eq__(self, other):
        # return True if vector has same coordinates as other
        if(len(self) != len(other)):
            return False
        else:
            for i in range(len(self)):
                if self._coords[i] != other._coords[i]:
                    return False
            return True
    
    def __ne__(self, other):
        # return True if vector differs from other
        if(len(self) != len(other)):
            return True
        else:
            for i in range(len(self)):
                if self._coords[i] != other._coords[i]:
                    return True 
            return False

    def __str__(self):
        # return the string representation of a vector within <>
        s = "<"
        for x in self._coords:
            s = s + str(x) + ", "
        s = s[0:len(s)-2] + ">"
        return s 

    def __sub__(self, other):
        # Soln for Qs. 2
        if(len(self) != len(other)):
            print("Size of both the vectors isn't same")
        else:
            new = [0] * len(self)
            for i in range(len(self)):
                new [i] = self._coords[i] - other._coords[i]
            return Vector(new)

    def __neg__(self):
        # Soln for Qs. 3
        new = [element * -1 for element in self._coords]
        return Vector(new)

    def __rmul__(self, value):
        return (self * value) 

    def __mul__(self, other):
        if type(self) == type(other):
            if(len(self) != len(other)):
                print("Size of both the vectors isn't same")
            else:
                new = 0
                for i in range(len(self)):
                    new = new + self._coords[i] * other._coords[i]
                return new
        elif isinstance(other, int):
            new = [element * other for element in self._coords]
            return Vector(new)
    
def main():
    v1 = Vector([2,3,4,5])
    v2 = Vector(7)
    v3 = Vector([1,2,3,4])
    # Add suitable print statements to display the results   
    print(v1)
    print(v2)
    print(v3)
    print(len(v1))
    print(v1[1])
    v1[1] = 5 
    print(v1)
    print(v1 + v3)
    print(v1 == v3)
    print(v1 != v3)
    print(v1 - v3)
    print(-v1)
    print(v1 * 3)
    print(3 * v1)
    print(v1 * v3)
    # of the different question segments

if __name__ == '__main__':
    main()