"""
Class Rectangle
Created: June 06/2020
By: Carlos Murcia
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor.
        atributes:
        width: width of rectangle
        height: height of rectangle
        x: private value
        y: private value
        id: private value inherits from base
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        property method for width
        Return: value of width
        """
        return self.__width

    @width.setter
    def width_setter(self, value):
        """
        setter method for width
        Return: new value of width
        """
        self.__width = value
        return self.__width

    @property
    def height(self):
        """
        property method for height
        Return: value of height
        """
        return self.__width

    @height.setter
    def height_setter(self, value):
        """
        setter method for height
        Return: value of height
        """
        self.__height = value
        return self.__height

    @property
    def x(self):
        """
        property method for x
        Return: value of x
        """
        return self.__x

    @x.setter
    def x_setter(self, value):
        """
        setter method for x
        Return: value of x
        """
        self.__x = value
        return self.__x

    @property
    def y(self):
        """
        property method for y
        Return: value of y
        """
        return self.__y

    @height.setter
    def y_setter(self, value):
        """
        setter method for y
        Return: value of y
        """
        self.__y = value
        return self.__y
