# Minimal Brython Template for Simple I/O

## Brython?
Typically when writing a web application, you have to write it in javascript.
If we want to use python instead, for this purpose, we need some way to turn our python into javascript.

That's where Brython comes along; It takes your python code, and transpiles it into javascript.

## Layout
In this project there is an index.html file and a main.py file.
The index.html file has our HTML, like the title of our page and our form inputs.

The main.py file has all of our python logic, and some special brython code that let's us talk to the HTML.
By 'talk to the HTML', I mean we can read the input the user entered, and output information to the HTML as well.

## Instructions
1. Clone this repository _or_ copy the index.html and main.py files into a new folder
2. Open this repository/folder open in Visual Studio Code
3. Now, from the extensions (ctrl+shift+x) get the **Live Server** extension
4. Using that extension 'Go Live' and see your index.html file get opened in your browser
5. From here you can enter something, and then click the button, and you'll see the python gets executed!

## What next?
Look in the main.py file and read through the comments to see what the brython specific code is doing.
After that you can figure out how to plug your own functions and logic into the input and output.
That will raise some questions, like, should I have multiple inputs? Or just have the user enter all of their input in the one textbox.

If you want to know [how to do something with HTML and Brython, you can look at their examples here](https://brython.info/demo.html?lang=en#)

And eventually, you can also consider writing CSS to make things look and feel nicer.