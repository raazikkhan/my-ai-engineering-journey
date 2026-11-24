questions  = [
    {
        "question": "Which data type in Python is immutable?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": "Tuple",
        "explanation": "Tuples cannot be modified after creation, unlike lists, dictionaries, and sets.",
    },
    {
        "question": "What is the output of bool([]) in Python?",
        "options": ["True", "False", "None", "Error"],
        "answer": "False",
        "explanation": "Empty sequences and collections like [] are falsy in Python, so bool([]) is False.",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "lambda"],
        "answer": "def",
        "explanation": "The def keyword defines a named function block in Python.",
    },
    {
        "question": "Which method adds a single element to the end of a list?",
        "options": ["append()", "extend()", "insert()", "push()"],
        "answer": "append()",
        "explanation": "append() adds one item to the end; extend() unpacks an iterable and adds its elements.",
    },
    {
        "question": "What does the // operator perform in Python?",
        "options": [
            "Exponentiation",
            "Floor division",
            "Modulo (remainder)",
            "Bitwise shift",
        ],
        "answer": "Floor division",
        "explanation": "// divides and rounds down toward negative infinity to the nearest whole number.",
    },
    {
        "question": "What is the output of type(3.14)?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'double'>", "<class 'str'>"],
        "answer": "<class 'float'>",
        "explanation": "Decimal numbers in Python are floating-point numbers (float), not double.",
    },
    {
        "question": "Which symbol is used for single-line comments in Python?",
        "options": ["//", "/*", "#", "--"],
        "answer": "#",
        "explanation": "Everything after # on a line is ignored by the Python interpreter.",
    },
    {
        "question": "What does len('Python') return?",
        "options": ["5", "6", "7", "Error"],
        "answer": "6",
        "explanation": "'Python' has 6 characters: P-y-t-h-o-n.",
    },
    {
        "question": "Which collection type does not allow duplicate elements?",
        "options": ["List", "Tuple", "Set", "String"],
        "answer": "Set",
        "explanation": "A set automatically enforces uniqueness and removes duplicate values.",
    },
    {
        "question": "What is the output of 2 ** 3 in Python?",
        "options": ["6", "8", "9", "5"],
        "answer": "8",
        "explanation": "** is the exponentiation operator: 2 raised to the power of 3 is 8.",
    },
    {
        "question": "Which keyword is used to exit a loop early?",
        "options": ["stop", "exit", "break", "return"],
        "answer": "break",
        "explanation": "break immediately stops the nearest enclosing for or while loop.",
    },
    {
        "question": "What does 'abc' * 3 evaluate to?",
        "options": ["'abc3'", "'abcabcabc'", "Error", "'aaa'"],
        "answer": "'abcabcabc'",
        "explanation": "Multiplying a string by an integer repeats the string that many times.",
    },
    {
        "question": "How do you access the value for key 'age' in dictionary person?",
        "options": ["person('age')", "person['age']", "person->age", "person.age"],
        "answer": "person['age']",
        "explanation": "Square brackets with the key name look up values in a dictionary.",
    },
    {
        "question": "Which built-in function returns the largest item in an iterable?",
        "options": ["top()", "high()", "max()", "upper()"],
        "answer": "max()",
        "explanation": "max() returns the greatest element in an iterable or among two or more arguments.",
    },
    {
        "question": "What is the index of the first element in a Python list?",
        "options": ["1", "0", "-1", "It depends"],
        "answer": "0",
        "explanation": "Python uses zero-based indexing, so the first element is at index 0 (-1 is the last).",
    },
    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": ["catch", "except", "error", "rescue"],
        "answer": "except",
        "explanation": "Python uses try / except blocks to catch and handle runtime exceptions.",
    },
    {
        "question": "What does 10 % 3 evaluate to?",
        "options": ["3", "1", "0", "3.33"],
        "answer": "1",
        "explanation": "The modulo operator % returns the remainder after division: 10 = (3 * 3) + 1.",
    },
    {
        "question": "Which method removes and returns the last item of a list by default?",
        "options": ["pop()", "remove()", "delete()", "discard()"],
        "answer": "pop()",
        "explanation": "pop() without arguments removes and returns the final element of the list.",
    },
    {
        "question": "What is the output of bool('False') in Python?",
        "options": ["False", "True", "None", "Error"],
        "answer": "True",
        "explanation": "Any non-empty string—even 'False'—evaluates to True when converted with bool().",
    },
    {
        "question": "Which statement sends a value back from a function?",
        "options": ["give", "yield_back", "return", "output"],
        "answer": "return",
        "explanation": "return exits the function and hands a value back to the caller.",
    },
   
    {
        "question": "What does 'hello'[1:4] return?",
        "options": ["'hel'", "'ell'", "'ello'", "'el'"],
        "answer": "'ell'",
        "explanation": "Slicing [start:stop] includes start (index 1 -> 'e') and stops before stop (index 4 -> 'o').",
    },
    {
        "question": "Which keyword skips the rest of the current loop iteration and moves to the next?",
        "options": ["skip", "pass", "continue", "next"],
        "answer": "continue",
        "explanation": "continue jumps straight to the next cycle of the loop, whereas pass is a no-op placeholder.",
    },
    {
        "question": "How do you safely read key 'city' from dict d with a default of 'Unknown'?",
        "options": ["d['city', 'Unknown']", "d.get('city', 'Unknown')", "d.fetch('city', 'Unknown')", "d.value('city', 'Unknown')"],
        "answer": "d.get('city', 'Unknown')",
        "explanation": "dict.get(key, default) returns the default instead of raising a KeyError when the key is missing.",
    },
    {
        "question": "What does [x * 2 for x in [1, 2, 3]] produce?",
        "options": ["[1, 2, 3]", "[2, 4, 6]", "(2, 4, 6)", "[1, 4, 9]"],
        "answer": "[2, 4, 6]",
        "explanation": "This list comprehension doubles each number in [1, 2, 3] and builds a new list.",
    },
    {
        "question": "Which operator checks whether 'py' is inside 'python'?",
        "options": ["in", "has", "contains", "within"],
        "answer": "in",
        "explanation": "The membership operator 'in' checks if a substring is present inside a string (or item in a collection).",
    },
    {
        "question": "What does '  hello world  '.strip() return?",
        "options": ["'hello world'", "'  hello world'", "'hello  world'", "'helloworld'"],
        "answer": "'hello world'",
        "explanation": "strip() removes leading and trailing whitespace while leaving spaces in the middle untouched.",
    },
    {
        "question": "Which keyword is used to check object identity (same object in memory)?",
        "options": ["==", "is", "===", "equals"],
        "answer": "is",
        "explanation": "'is' checks identity (whether two names point to the exact same object), while '==' checks value equality.",
    },
    {
        "question": "What is the idiomatic way to check if a variable x is None?",
        "options": ["x == None", "x is None", "x === None", "is_none(x)"],
        "answer": "x is None",
        "explanation": "Python style (PEP 8) recommends 'x is None' because None is a singleton object.",
    },
    {
        "question": "What does [-1] do when indexing a non-empty list?",
        "options": ["Raises IndexError", "Returns the first item", "Returns the last item", "Reverses the list"],
        "answer": "Returns the last item",
        "explanation": "Negative indices count backward from the end of a sequence, so -1 is always the last element.",
    },
    {
        "question": "What does 'a,b,c'.split(',') return?",
        "options": ["('a', 'b', 'c')", "['a', 'b', 'c']", "{'a', 'b', 'c'}", "'a b c'"],
        "answer": "['a', 'b', 'c']",
        "explanation": "str.split(',') breaks the string at every comma and returns a list of substrings.",
    },
]

# counter
score = 0  

# loop through every questions 
for i, item in enumerate(questions, start=1):
    print(f"\n{i} {item["question"]}")
    # print four option
    for i , option in enumerate(item['options'], start=1):
        print(f"\n{i} {option}")

    # User input
    choice = input("Enter your Option 1,2,3,4: ").strip() # strip remove extra space
    if choice.isdigit() and 1 <= int(choice) <= len(item["options"]):
     selected = item["options"][int(choice) - 1]
     if selected == item['answer']['explanation']:
         print("correct answer ! ")
         score += 1
     else: 
        print(f"Wrong answer ! correct answer is: {item["answer"]}")
        print(f"Explanation:- {item['explanation']}")


    else:     
        print("Invalid Answer, Try Again !!  ")

print(f"\nYour Final Score: {score}/{len(questions)}")
  
