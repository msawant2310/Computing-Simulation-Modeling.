#!/usr/bin/env python
# coding: utf-8
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f17a3f2e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157, 3164, 3171, 3178, 3192, 3199]\n"
     ]
    }
   ],
   "source": [
    "#Q1\n",
    "list1=[]\n",
    "for i in range (2000, 3200):\n",
    "    if i%7==0 and i%5!=0:\n",
    "        list1.append(i)\n",
    "\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "6cbc1f63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type a number:5\n",
      "120\n"
     ]
    }
   ],
   "source": [
    "#Q2\n",
    "num= input(\"Type a number:\")\n",
    "fact=1\n",
    "for i in range(int(num)):\n",
    "    fact=fact*(i+1)\n",
    "print(fact)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f23b63da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type a number:4\n",
      "{1: 1, 2: 4, 3: 9, 4: 16}\n"
     ]
    }
   ],
   "source": [
    "\n",
    "#Q3\n",
    "num= input(\"Type a number:\")\n",
    "dict1=dict()\n",
    "for i in range(1,int(num)+1):\n",
    "    dict1[i]=i*i\n",
    "\n",
    "print(dict1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "577d3098",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type list of numbers:34,67,92\n",
      "34,67,92\n",
      "['34', '67', '92']\n",
      "('34', '67', '92')\n"
     ]
    }
   ],
   "source": [
    "#Q4\n",
    "list2=input(\"Type list of numbers:\")\n",
    "print(list2)\n",
    "list3=list2.split(\",\")\n",
    "tuple1=tuple(list3)\n",
    "print(list3)\n",
    "print(tuple1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "dc815cdc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type your statement here:My name is MOmo\n",
      "MY NAME IS MOMO\n"
     ]
    }
   ],
   "source": [
    "#Q5\n",
    "class uppercase(object):\n",
    "    def __init__(self):\n",
    "        self.statement = \"\"\n",
    "\n",
    "    def getString(self):\n",
    "        self.statement = input(\"Type your statement here:\")\n",
    "    \n",
    "    def printString(self):\n",
    "        print(self.statement.upper())\n",
    "\n",
    "string = uppercase()\n",
    "string.getString()\n",
    "string.printString()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "5b94bb8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type list of numbers:45,89\n",
      "[12.24744871391589, 17.224014243685083]\n"
     ]
    }
   ],
   "source": [
    "#Q6\n",
    "import math\n",
    "\n",
    "Q_value=[]\n",
    "list2=input(\"Type list of numbers:\")\n",
    "D=list2.split(\",\")\n",
    "C=50\n",
    "H=30\n",
    "for i in D:\n",
    "    Q=math.sqrt((2*C*int(i))/H)\n",
    "    Q_value.append(Q)\n",
    "\n",
    "print(Q_value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "da05a5e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type the dimensions of matrix:3,4\n",
      "[[0. 0. 0. 0.]\n",
      " [0. 1. 2. 3.]\n",
      " [0. 2. 4. 6.]]\n"
     ]
    }
   ],
   "source": [
    "#Q7\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "input_x_y = input(\"Type the dimensions of matrix:\")\n",
    "x_y=input_x_y.split(\",\")\n",
    "x=int(x_y[0])\n",
    "y=int(x_y[1])\n",
    "\n",
    "zeros_matrix = np.zeros( (x, y) )\n",
    "for row in range(x):\n",
    "    for col in range(y):\n",
    "        zeros_matrix[row][col]= row*col\n",
    "\n",
    "print(zeros_matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "4c4e8b1b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type list of words:Aditya,Momo,Krunal,pooja\n",
      "['Aditya', 'Krunal', 'Momo', 'pooja']\n"
     ]
    }
   ],
   "source": [
    "#Q8\n",
    "list2=input(\"Type list of words:\")\n",
    "list3=list2.split(\",\")\n",
    "list3.sort()\n",
    "print(list3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "bbb39b4e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type your Sentence:Momo pagal ahe\n",
      "Type your Sentence:\n",
      "MOMO PAGAL AHE\n"
     ]
    }
   ],
   "source": [
    "#Q9\n",
    "output_list = []\n",
    "while True:\n",
    "    sentence = input(\"Type your Sentence:\")\n",
    "    if sentence:\n",
    "        output_list.append(sentence)\n",
    "    else:\n",
    "        break;\n",
    "\n",
    "for i in output_list:\n",
    "    print(i.upper())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "5efb4d31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type list of words:pagan gang momo ahe\n",
      "ahe gang momo pagan\n"
     ]
    }
   ],
   "source": [
    "#Q10\n",
    "list2=input(\"Type list of words:\")\n",
    "list3=list2.split(\" \")\n",
    "list4=sorted(set(list3))\n",
    "print(\" \".join(list4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "cce6bd01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is Mrunali Sawant\n",
      "My name is Aditya Bhanage\n"
     ]
    }
   ],
   "source": [
    "#Q11\n",
    "class Name:\n",
    "    a = \"My\"\n",
    "    \n",
    "    def __init__(self, b=None):\n",
    "        self.a = b\n",
    "\n",
    "momo = Name(\"Mrunali Sawant\")\n",
    "print(\"%s name is %s\" % (Name.a, momo.a))\n",
    "\n",
    "adi = Name()\n",
    "adi.a = \"Aditya Bhanage\"\n",
    "print(\"%s name is %s\" % (Name.a, adi.a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "3bb48f36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "4\n",
      "9\n",
      "16\n",
      "25\n",
      "36\n",
      "49\n",
      "64\n",
      "81\n",
      "100\n",
      "121\n",
      "144\n",
      "169\n",
      "196\n",
      "225\n",
      "256\n",
      "289\n",
      "324\n",
      "361\n",
      "400\n"
     ]
    }
   ],
   "source": [
    "#Q12\n",
    "def numbers():\n",
    "    new_dict=dict()\n",
    "    for i in range(21):\n",
    "        new_dict[i]=i**2\n",
    "        print(new_dict[i])\n",
    "        \n",
    "numbers()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "ecf8f602",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n",
      "16\n",
      "17\n",
      "18\n",
      "19\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "#Q13\n",
    "def numbers():\n",
    "    new_dict=dict()\n",
    "    for i in range(21):\n",
    "        new_dict[i]=i**2\n",
    "        i+1\n",
    "    [print(key) for key,value in new_dict.items()]\n",
    "        \n",
    "numbers()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "96522cc0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]\n"
     ]
    }
   ],
   "source": [
    "#Q14\n",
    "def sqr_num():\n",
    "    list1=[]\n",
    "    for i in range(1,21):\n",
    "        list1.append(i**2)\n",
    "    print(list1)\n",
    "\n",
    "sqr_num()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "3d9420eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 4, 6, 8, 10)\n"
     ]
    }
   ],
   "source": [
    "#Q15\n",
    "tuple1=(1,2,3,4,5,6,7,8,9,10)\n",
    "list1=[]\n",
    "\n",
    "for i in tuple1:\n",
    "    if i%2==0:\n",
    "        list1.append(i)\n",
    "        \n",
    "print(tuple(list1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "84e331ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<__main__.American object at 0x7f82f142a6d0>\n",
      "<__main__.NewYorker object at 0x7f82f142aa60>\n"
     ]
    }
   ],
   "source": [
    "#Q16\n",
    "class American(object):\n",
    "    pass\n",
    "\n",
    "class NewYorker(American):\n",
    "    pass\n",
    "\n",
    "USA = American()\n",
    "NY = NewYorker()\n",
    "print(USA)\n",
    "print(NY)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "3911f54d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "#Q17\n",
    "class Rectangle(object):\n",
    "    \n",
    "    def __init__(self,l,w):\n",
    "        self.length=l\n",
    "        self.width=w\n",
    "        \n",
    "    def compute_area(self):\n",
    "        return self.length*self.width\n",
    "\n",
    "print(Rectangle(5,4).compute_area())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "02363c94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "64\n"
     ]
    }
   ],
   "source": [
    "#Q18\n",
    "class Shape(object):\n",
    "    def __init__(self):\n",
    "        pass\n",
    "\n",
    "    def area(self):\n",
    "        return 0\n",
    "\n",
    "class Square(Shape):\n",
    "    def __init__(self, length):\n",
    "        Shape.__init__(self)\n",
    "        self.length = length\n",
    "\n",
    "    def compute_area(self):\n",
    "        return self.length*self.length\n",
    " \n",
    "print(Square(8).compute_area())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "d3f49733",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "division by zero is not possible!\n"
     ]
    }
   ],
   "source": [
    "#Q19\n",
    "def error_function():\n",
    "    return 5/0\n",
    "\n",
    "try:\n",
    "    error_function()\n",
    "except:\n",
    "    print(\"division by zero is not possible!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "6542d344",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12, 24, 35, 88, 120, 155]\n"
     ]
    }
   ],
   "source": [
    "#Q20\n",
    "list1=[12,24,35,24,88,120,155,88,120,155]\n",
    "list2=set(list1)\n",
    "list3=[]\n",
    "\n",
    "for i in list1:\n",
    "    if i in list2 and i not in list3:\n",
    "        list3.append(i)\n",
    "\n",
    "print(list3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a3caaee",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
# In[ ]:




