<!-- PyON Parser
The theory of context-free languages and stack machines can be profitably applied to the defining and parsing of programming languages. Every programming language has a formally defined (context-free) grammar of what constitutes valid code. One such language is JavaScript Object Notation, or JSON for short.

JSON has become a standard format for serializing, or writing to disk, objects in programs in a portable, human-readable way. These are objects as in object-oriented programming: composite entities in containing multiple data values, and functions for manipulating them. JSON focuses on the data part of objects. Every JSON file is a comma-separated sequence of key-value pairs, much like a dictionary in Python. Though in JSON, keys may only be strings. Values may be:

an integer like 42, or -12,
a floating point like 3.14, 6.022e23, or -1.38e-12
a string like "honey badger"
a Boolean like true or false (all lowercase)
a list containing a mixture of any the other types
another object
For each of these types, you should use the corresponding built-in Python data types to construct the object being represented by the JSON file. This includes the built-in types for set() and complex(), when you extend the JSON standard in Part 3. See below for more information.

Example: wanted_man.json
{
    "name" : "Robin",
    "age" : 29,
    "hobbies" : [
        "larceny",
        "archery",
        "philanthropy"
    ],
    "is_handsome" : true
}
Parsing Process
Typically, making sense of a programming language is done in two stages: tokenizing, and parsing. Tokenizing is the translation of a string into small groups of characters which, taken together, mean something. For example, wanted_man.json is, a first just a string:

'{ "name" : "Robin",\n "age" : 29,\n "hobbies" : [\n "larceny",\n "archery",\n "philanthropy"\n ],\n "is_handsome" : true\n }'

But the meaningful groups here are the strings:

['{', '"name"', ':', '"Robin"', ',', '"age"', ':', '29', ',', '"hobbies"', ':', '[', '"larceny"', ',', '"archery"', ',', '"philanthropy"', ']', ',', '"is_handsome"', ':', 'true', '}']

This removes unnecessary spaces, newlines, and any other characters which should be ignored. Thus, you should strive to break the file into a 1D list of strings first, then proceed to parsing the tokens into dictionaries, lists, etc.

Assignment
Part 1 -- Define the Grammar
Write out the grammar for JSON, as described above. You can use high-level terminal characters like (INT) and (STR) to indicate individual values rather than using terminals like 1 and 'a'. Include this as a documentation string in your code file. (See next part.)

Part 2 -- Implement a Parser
Using the Python programming language, write a program which can parse text files which contain properly formatted JSON, and store them within the program as a dictionary. The values represented in the file should be stored in your dictionary as the corresponding type. To do this, you will probably want to break this task into separate stages for tokenizing and parsing. Within your code, you should indicate in comments which functions are implementing which productions in the JSON grammar you write for Part 1.

Part 3 -- Extend the Standard
There are a useful data types which JSON standard does not allow us to directly represent. Sets, and complex numbers are among them. Once your parser is working files containing only standard JSON, you will:

Add productions into your JSON grammar from Part 1, and
Add support for sets and complex numbers into your parser. Detailed specification for these types is below.
Specifications for set() container
Sets are enclosed in braces { }.
Elements of sets need not all be of the same type.
Elements may only be hashable types. (str, int, float, complex)
Elements of sets are separated by commas.
Elements of sets may be duplicated in the file, but should only appear once in the parsed data.
When constructing the object, use Python's built-in set() type. Documentation: https://docs.python.org/3/tutorial/datastructures.html#sets.

Specifications for complex data type
Complex numbers are composed of a real, and imaginary part.
Valid complex number formats include:
 N+Ni
 N-Ni
-N-Ni
+N+Ni
   Ni
  +Ni
  -Ni
Where N is any valid floating point representation (not including leading + or -, but may include decimals and exponential notation). Note that spaces are not valid within the format, i.e., N + Ni is not valid syntax, and your program should not accept it.

When constructing the object, use Python's built-in complex() type. Documentation: https://docs.python.org/3/library/functions.html#complex

Program Specifications
Your program should be callable with a single command line argument for the name of the file to read. E.g., $ python3 my_parser wanted_man.json
Your program should contain a function parse_file which accepts a string representing the name of a file, and returns the parsed object as a dictionary.
Your parser must support lists which contain more than one type.
Your parser should accept trailing commas in lists, sets, and objects as valid syntax. E.g., all of the following should be valid.
{ 1, 2, 3 }
{ 1, 2, 3, }
[ "arrow", "bow", "mask" ]
[ "arrow", "bow", "mask", ]
{ "are_merry": True, "number_men": 19 }
{ "are_merry": True, "number_men": 19, }
Submission
Upload your code to Moodle before the deadline. You will want to have tested your code on the test files provided before doing so, and ensure that you pass the automatic test cases. If your code passes all the automatic test cases, it is a good indication that you will receive full credit for the "Correctness" category below. If you do not pass all the automatic test cases, it does not necessarily mean that you will receive the grade displayed; it may be higher or lower. -->