# Code Em  

### Fall 2017  

### Sept 19 - Dec 12  

Initial slides to be used found in [reveal-deck](https://github.com/techemstudios/code_em_fall_2017/tree/master/reveal-deck), in slides-code-em.html --check the latest version. 

*Note:* The content for each section and day below, as well as possible times of each lesson will continuously be populated. The times for each lesson will update with "real" times after each class.    

### Performance Objectives  

By the end of Code Em, students will -  
* Understand computational thinking, or think like a computer scientist  
* Understand how hardware and software communicate  
* Be comfortable interpreting/creating programs to solve problems  
* Learn enough Python to be "dangerous"  
* Explore Python, Java, HTML, Lua programming languages  
* Be comfortable using the Slack messaging app  
* Have all projects from the session on their own GitHub account  

### Day One  

`09/19/2017`  

**Introductions:** Share name, age, grade, and programming experience.  
*5-10 min*

### How to Think  
#### Like a Computer Scientist  
*10 min*  

Take a problem that at first, may seem overwhelming, or not "attackable" with a program, then break the problem into smaller manageable problems where we can use computation to solve. See how the smaller problems together make up the larger one. Think about computational thinking as useful ways to approach and solve problems using these steps: decomposition, generalization, recognize patterns, make plan (or algorithm) and carry it out. Example, Clean the Whole House problem.  

### Python   

| Py Concepts  | Py Projects      |
|--------------|------------------|
| Data Types   | Web Apps         |
| Variables    | Visualizing Data |
| Expressions  | APIs             |
| Statements   | Interface Design |
| Functions    | Art              |
| Loops        | Slackbot         |
| Conditionals | Alexa Skills     |
| Objects      | Pygame           |
| Classes      | Alexa Skills     |

### Get on Same Page  
*5 min*  

We have returning students, as well as new students. We will do a little review first and help eachother to become equally confident with coding.  

### GitHub & Slack  
*10 min*

Each student will create their our own GitHub and Slack accounts. For those who already have both, make sure they can log in and have them help their peers get set up. Students will use their GitHub account to keep track of all their progress. There should be a time set towards the end of each class to have every student push their code to their own repository. Slack will be used to communicate with one another by asking questions, input, etc. Record student emails, to send slack invitations; record GitHub usernames, to invite to slackbot repo.

### What are Computers?  

### Quick Computer History  

*5-10 min*

Early computers were tools (or mechanical devices) people used to help them calculate math problems. A modern computer is a device that can be programmed to perform a task. From Talley Sticks, to the Babbage Machine --end with Ada Lovelace, recognized as the first computer programmer.  

Difference between hardware and software.   

What is a computer program?  

#### Quick Review  
Computers are devices for manipulating information we can put info into a computer, and it can transform the info into new, useful forms. Computer can then output or display the information.  

A program is a set of instructions that causes a computer to perform some kind of action, or a set of commands that tell the hardware in a computer what to do.

### Making Programs for the Computer to Carry Out  

#### Python  

* Interpreter  
* Input Text  
* Output Text  
* Data Types  
* Variables  

### Variables & Strings  

### Day Two  

`09/26/2017`  

### Fetch, Decode, Exectute  

#### How a Program Works  

Software communicating with the hardware. CPU, RAM, and what happens when you fire up your favorite program. Fetch: the computer gets the instructions and puts them in RAM; Decode: instructions are decoded into binary so the CPU can understand them; Execute: CPU carries out those instructions. The computer speedily performs this process continuously from the moment you turn on your computer, to the moment you turn it off.  

### Expressions & Statements  

Expressions: combination of values, variables and operators, a value or variable all by it self.  

Statements: a unit of code that does something, like creating a variable or displaying something --a complete thought.  

We saw this earlier when we typed an expression at the prompt, the interpreter evaluated it, which means it finds the value of the expression and returns the result. When you type in a statement, the interpreter executes it, meaning it does whatever the statement says.  

### Variables & Strings  

Review msg.py

Create a variable called: 'message' and have it hold a value.
```python  
message = "Hello Python world!"
```  
Now, Python knows message to be the string, "Hello Python World!" How can we output the value?  
```python  
print(message)
```  

Let's say we have two variables, each equal to a number.  
```python  
a = 5  
b = 10  
```  
How can we add these two numbers together?  
```python  
answer = a + b  
print(answer)
```  
or  
```python  
print(a+b)  
```  

Look at the whole program. Can you find the statement three statements, expression, and two integers?
```python  
a = 5  
b = 10  
answer = a + b  
print(answer)
```  


Let's combine variables and strings. 

### User Input  
#### I/O  

### Computational Thinking  

Useful ways to approach and solve problems --not just problems involving programming, but every problem! 

### Layers of a Computer System  
#### Abstraction  

When we are working in one layer, we do not need to concern ourselves with the information in the surrounding layers. This way, we can just focus on what needs to be done in the moment. Think of abstraction as a mental model; a way to think about something. Have the unnecessary details hidden, so we can leave only the information we need to complete our goal.  

Abstraction Examples:  

* A Person Driving a Car  
  - The only thing they need to focus on is the road ahead. 
  - It is unnecessary to worry about details of how the engine or electornics of the car work.
  
* Fast Food Restaurant  
  - At many restaurants, the names of meals have corresponding numbers.
  - The food prep has been trained to recognize the meal number, not worry about the full name.


### Functions  
#### Think Abstraction: Encapsualtion  

Test Jupyter Notebook lesson.  

Close look at the parts of a function statement.  

### Day Three    

`10/03/2017`  

### Case Study

#### Interface Design with the Turtle Module  

**Objectives**  

* modules  
* methods  
* for loops  
* Defining Functions  
* arguments & parameters  
* Computational Thinking  
  - Pattern Recognition: Encapsualtion: **DRY**    
  - Generalization  
* Refactoring  

#### The Software Development Process  

Following a process for writing your programs will help you to be more efficient and help you reach your goals. When you need to create a large program, it can be a daunting challenge and almost impossible without a systematic approach.  

#### Computer Hardware History  

Engineers are concerned with building things to be more efficient.  

**Objectives**  

* Pick up from Babbage machine  
* 1st, 2nd, 3rd Gen  
* Components  
* vacuum tubes  
* transistors  
* microchips  
* Desktop computers  

### Control Structures  
#### Conditions: Events: if this, then this  

Temperature warnings program.  

### SlackBot
### Simple Command Response  

command_response.py  
[The Power of Python](http://techemstudios.com/decks/slackpi-to-alexa/#/)

### Data Structures  
#### Python Lists, Tuples, Dictionaries  

Class activity: make a list of dictionaries with student name, github username, slack username.  

### Binary Search Tree  

How computer efficiently search an ordered list.  

Like a sorted list, this is a logical ordering of the nodes.  


### Data Visualization  
#### matplotlib & pygal  


### Object Oriented Programming  

As we talked about decomposing (divide and conquer) and generalization (seeing the big picture) in computational thinking, object oriented in a nutshell is to look at the interaction of simple *objects*, as being part of a complex system. Each object does something, it has its own set of properties and attributes (things it can do) and belongs to a *Class*. Let's look at an example of a dog named, Scrappy. We can say, Scrappy is a specific individual in a larger class, Dogs. In Object Oriented terms, Scrappy is a particular *instance* of the dog class. Since Scrappy is part of the dog class, we can assume certain things about him. Scrappy most likely has four legs, a tail, a wet nose, an age, and can bark. Now take a dog named, Lassy. She will have similar characteristics, but may only differ in behavior, size, or color. So, every object is an instance of some class. The class describes the general characteristics (or properties) an instance will have. The instance of the class will hold more specific properties and attributes.

Objects interact with one another by sending each other messages.  

### Graphics Programming  
#### Objects  

Calling on objects in graphics.py  

Drawing a set of points to a window, shapes, then clickable buttons.  

### Interactive Graphics  

#### Register Mouse Clicks  

Create a program that tracks the coordinates of ten consecutive mouse clicks by the user. Prerequisites: definining functions, for loops, calling object methods.

```python    
# Make sure you have graphics.py

from graphics import *

def main():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at: ", p.getX(), p.getY())

main()

```  

#### Triangle  

Create a program that draws a triangle after the user clicks three points on the window.  

#### Adding GUI to our Temperature Converter Program  

Use the same logic from the temperature converter program and add a graphical user interface, complete with buttons and text input from the user. Once it works, add multi-way condition logic to output temperature warnings.



### Write to Files and Read Files  
#### json.dump() & json.load()

### API  
### Application Programming Interface  

### Pioneers of Computer Science  

### Web Applications  
#### Django Web Framework  
