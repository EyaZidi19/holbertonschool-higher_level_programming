#!/usr/bin/python3
'''reclangle Module'''


from models.base import Base


class Rectangle(Base):
    '''class of Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initilaze'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    '''property of width '''

    @property
    def width(self):
        ''' the  width'''
        return self.__width

    ''' setter of width'''

    @width.setter
    def width(self, value):
        '''width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    '''property of height'''

    @property
    def height(self):
        '''the height '''
        return self.__height

    ''' setter of  height '''

    @height.setter
    def height(self, value):
        '''the height '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    ''' property x '''

    @property
    def x(self):
        ''' x '''
        return self.__x

    ''' setter of x '''

    @x.setter
    def x(self, value):
        ''' x '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    ''' property of y '''

    @property
    def y(self):
        ''' y self '''
        return self.__y

    ''' setter of y '''

    @y.setter
    def y(self, value):
        '''y self value'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
            Returns the area
        '''
        return (self.height * self.width)

    def display(self):
        '''
            Prints to stdout the representation
        '''
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")
