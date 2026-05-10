# Simple Customer Support Chatbot

print("===== Welcome to Customer Support Chatbot =====")

print("Type 'bye' to exit\n")

while True:

    # Take user input
    user = input("You: ").lower()

    # Greeting
    if user in ["hello", "hi", "hey"]:

        print("Bot: Hello! How can I help you?")

    # Product inquiry
    elif "product" in user:

        print("Bot: We provide laptops, mobiles, and accessories.")

    # Price inquiry
    elif "price" in user:

        print("Bot: Prices depend on the product model.")

    # Working hours
    elif "hours" in user or "time" in user:

        print("Bot: Our shop is open from 9 AM to 9 PM.")

    # Contact information
    elif "contact" in user:

        print("Bot: You can contact us at support@gmail.com")

    # Thank you message
    elif "thank" in user:

        print("Bot: You're welcome!")

    # Exit condition
    elif user == "bye":

        print("Bot: Thank you for visiting!")
        break

    # Unknown query
    else:

        print("Bot: Sorry, I didn't understand that.")
        """
        What Actually Are We Doing In This Code?
This program creates a simple text-based Customer Support Chatbot using Python.
The chatbot:


Greets the user


Takes input from the user


Checks what the user typed


Gives different replies based on the message


Keeps running again and again until the user types "bye"


This is an example of:


Conditional statements (if, elif, else)


Infinite loops (while True)


User input handling


String operations


Basic chatbot logic


The chatbot works using keyword matching.
Example:


If the user types "hello" → chatbot gives greeting


If the user types "price" → chatbot gives price-related response


If the user types "bye" → chatbot stops



CODE BLOCK 1
# Simple Customer Support Chatbotprint("===== Welcome to Customer Support Chatbot =====")print("Type 'bye' to exit\n")
EXPLANATION :
# Simple Customer Support Chatbot


# is called a comment symbol in Python.


Anything written after # on the same line is ignored by Python.


Comments are written for humans to understand the code better.


This line simply describes the program.


It tells us that this program is a simple customer support chatbot.


Internally:


Python sees #


Python ignores the entire line


It is not executed


Purpose:


Makes code readable


Helps beginners understand the code


Used for documentation



print("===== Welcome to Customer Support Chatbot =====")
print()


print is a built-in Python function.


A function is a reusable block of code that performs a task.


print() displays output on the screen.


( and )


Parentheses are used to pass data into the function.


The data inside parentheses is called an argument.


"===== Welcome to Customer Support Chatbot ====="


Double quotes " represent a string.


A string is text data in programming.


This text is displayed exactly as written.
Internally what happens:


Python reads the print() function


Python takes the string inside it


Python sends the string to the console/output screen


User sees the message


Output:
===== Welcome to Customer Support Chatbot =====
Purpose:


Displays welcome message


Makes chatbot user-friendly



print("Type 'bye' to exit\n")
Again:


print() displays text on screen.


"Type 'bye' to exit\n"
This is a string.
'bye'


Single quotes are used inside double quotes.


This is allowed in Python.


It highlights the word bye.


\n


\n is called a newline character.


It moves the cursor to the next line.


Internally:


Python prints:
Type 'bye' to exit


\n creates an empty line after it


Output:
Type 'bye' to exit
Purpose:


Tells user how to stop the chatbot


Creates cleaner formatting



CODE BLOCK 2
while True:
EXPLANATION :
while


while is a loop statement in Python.


A loop repeats code again and again.


True


True is a Boolean value.


Boolean values are:


True


False




while True
This means:
Keep running forever
Because:


Condition is always True


So loop never stops automatically


:


Colon : tells Python that a block of code starts below it.


Internally what happens:


Python checks condition


Condition is True


Loop starts


Code inside loop executes


Python goes back again


Checks condition again


Still True


Repeats forever


The loop only stops when:


break statement is executed


Purpose:


Keeps chatbot active continuously


Allows multiple conversations



CODE BLOCK 3
    # Take user input    user = input("You: ").lower()
EXPLANATION :
# Take user input


Comment explaining purpose of code below it.



user = input("You: ").lower()
This is one of the most important lines.

user


user is a variable.


Variable stores data in memory.


Purpose:


Stores user message



=


Assignment operator


Stores right-side value into left-side variable


Meaning:
Store input value inside variable user

input()


input() is a built-in Python function.


It takes input from keyboard.


Internally:


Program pauses


Waits for user to type something


User presses Enter


Input becomes a string



"You: "


Prompt message shown before input


Output example:
You:

.lower()


lower() is a string method.


Converts all letters into lowercase.


Example:
"HELLO".lower()
Becomes:
"hello"
Purpose:


Makes chatbot case-insensitive


Without this:


"HELLO" and "hello" would be treated differently


Internally what happens:


User types message


input() stores it as string


.lower() converts string to lowercase


Final lowercase string stored in user


Example:
User types:
HELLO
Stored value:
user = "hello"

CODE BLOCK 4
    # Greeting    if user in ["hello", "hi", "hey"]:
EXPLANATION :
# Greeting


Comment explaining greeting condition.



if user in ["hello", "hi", "hey"]:
if


Conditional statement


Used to make decisions


Meaning:
If condition is true, execute code

user


Variable storing user message



in


Membership operator


Checks whether value exists inside collection



["hello", "hi", "hey"]
This is a list.
A list:


Stores multiple values


This list contains greeting words.

:


Starts block of code



Internally what happens:


Python takes value of user


Checks whether it exists in list


If found:
condition becomes True


Greeting response executes


Example:
user = "hi"
Python checks:
"hi" in ["hello", "hi", "hey"]
Result:
True
Purpose:


Detect greeting messages



CODE BLOCK 5
        print("Bot: Hello! How can I help you?")
EXPLANATION :
print()
Displays chatbot response.

"Bot: Hello! How can I help you?"
String displayed to user.
Output:
Bot: Hello! How can I help you?
Purpose:


Responds to greeting


Internally:


Condition becomes true


Python enters if block


Executes print()


Message displayed



CODE BLOCK 6
    # Product inquiry    elif "product" in user:
EXPLANATION :
elif


Means:
"else if"


Used when:


Previous condition is false


New condition needs checking



"product" in user
Checks whether word "product" exists inside user message.
Example:
user = "tell me about product"
Python checks:
"product" in user
Result:
True
Purpose:


Detects product-related questions



CODE BLOCK 7
        print("Bot: We provide laptops, mobiles, and accessories.")
EXPLANATION :
Displays product-related response.
Output:
Bot: We provide laptops, mobiles, and accessories.
Purpose:


Gives product information



CODE BLOCK 8
    # Price inquiry    elif "price" in user:
EXPLANATION :
Checks whether user message contains word "price".
Example:
user = "what is the price"
Condition becomes true.
Purpose:


Detect price-related questions



CODE BLOCK 9
        print("Bot: Prices depend on the product model.")
EXPLANATION :
Displays pricing response.
Output:
Bot: Prices depend on the product model.
Purpose:


Answers price inquiries



CODE BLOCK 10
    # Working hours    elif "hours" in user or "time" in user:
EXPLANATION :
or
Logical operator.
Meaning:


If ANY condition is true


Condition becomes true if:


"hours" exists
OR


"time" exists


Example:
user = "shop time"
Condition:
"time" in user
Result:
True
Purpose:


Detect working-hours questions



CODE BLOCK 11
        print("Bot: Our shop is open from 9 AM to 9 PM.")
EXPLANATION :
Displays shop timing.
Output:
Bot: Our shop is open from 9 AM to 9 PM.

CODE BLOCK 12
    # Contact information    elif "contact" in user:
EXPLANATION :
Checks whether user asked for contact details.
Example:
user = "contact number"
Condition becomes true.
Purpose:


Detect contact-related questions



CODE BLOCK 13
        print("Bot: You can contact us at support@gmail.com")
EXPLANATION :
Displays contact information.
Output:
Bot: You can contact us at support@gmail.com

CODE BLOCK 14
    # Thank you message    elif "thank" in user:
EXPLANATION :
Checks whether user thanked the chatbot.
Example:
user = "thank you"
Condition becomes true.
Purpose:


Detect gratitude messages



CODE BLOCK 15
        print("Bot: You're welcome!")
EXPLANATION :
Displays polite reply.
Output:
Bot: You're welcome!

CODE BLOCK 16
    # Exit condition    elif user == "bye":
EXPLANATION :
==
Comparison operator.
Checks whether two values are equal.
Difference between:


= → assignment


== → comparison


Condition checks:
Is user exactly equal to "bye"?
If yes:


chatbot exits


Purpose:


Stops infinite loop safely



CODE BLOCK 17
        print("Bot: Thank you for visiting!")        break
EXPLANATION :
print("Bot: Thank you for visiting!")
Displays goodbye message.
Output:
Bot: Thank you for visiting!

break
break


Special loop control statement


Immediately exits loop


Internally:


Python encounters break


Loop stops instantly


Program moves outside loop


Program ends


Without break:


Infinite loop would continue forever


Purpose:


Properly terminates chatbot



CODE BLOCK 18
    # Unknown query    else:
EXPLANATION :
else
Runs when:


All previous conditions are false


Meaning:
If nothing matches, execute this block
Purpose:


Handles unknown questions



CODE BLOCK 19
        print("Bot: Sorry, I didn't understand that.")
EXPLANATION :
Displays fallback response.
Output:
Bot: Sorry, I didn't understand that.
Purpose:


Prevents chatbot from staying silent


Handles unexpected input



COMPLETE FLOW OF PROGRAM
Step-by-step internally:


Program starts


Welcome message displayed


Infinite loop starts


User types message


Message converted to lowercase


Python checks conditions one-by-one


Matching response displayed


Loop repeats


If user types "bye"


break stops loop


Program ends



SAMPLE INPUT AND OUTPUT
Example 1
Input
You: hello
Output
Bot: Hello! How can I help you?

Example 2
Input
You: what products do you have
Output
Bot: We provide laptops, mobiles, and accessories.

Example 3
Input
You: what are your hours
Output
Bot: Our shop is open from 9 AM to 9 PM.

Example 4
Input
You: thanks
Output
Bot: You're welcome!

Example 5
Input
You: bye
Output
Bot: Thank you for visiting!
        """