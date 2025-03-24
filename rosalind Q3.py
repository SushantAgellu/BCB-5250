Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "0KNAlm9xUncozrde8Pbn0BGU6blN86GUs6lhJDXUcWWRP74RWcChelusvIHT9geeCAwrx7DA5y3plvzBoGeX1dKzlYbep1CvnXVqNZYo3Z3ONxvmcFxboschasoLtnWHvxBRKZs9F3p2iD238kQ32gISkDxWvfcVgVcuGD1oJgewnv3PZYGrJ1YUoJaR6CwqwA."
>>> a,b,c,d = 50,55,115,121
>>> print(s[a:b=1] + " " +s[c:d+1])
SyntaxError: invalid syntax
>>> print(s[a:b+1] + " " +s[c:d+1])
Chelus boschas
