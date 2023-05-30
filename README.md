# Todo-App
This is a simple todo app using Python and HTML

![Screenshot](https://github.com/Efendo/Todo-App/blob/master/todo-app-screenshot.png)

Link 👇

[Todo App](https://efendo.github.io/Todo-App)

## what is the code behind this?
It uses Pyscript and TailwindCSS.

### Python Backend source code:
````
class Application:

    def __init__(self):
        self.content = [] # This is the Todo list
        self.todo_out = Element('todo_out') # This is a div element which displays the Todo list
        self.text_input = Element('text_input') # This is the text field for adding todo to the list
        self.del_index = Element('del_index') # This is the number field to get the ID of the item to Delete
        self.error_log = Element('error_log') # This is the div which displays custom errors

    def addTodo(self): # This function adds a new item to the Todo list and displays it using the CycleTodo function
        self.error_log.element.innerHTML = ""
        self.content.append(self.text_input.value)
        self.todo_out.element.innerHTML = self.CycleTodos() # Updates the content on the page

    def CycleTodos(self): # This function returns a variable containing properly formatted Todo's
        self.error_log.element.innerHTML = ""
        fs = ""
        for i in range(0, len(self.content)):
            fs += f"<p class='font-bold text-xl'>• {self.content[i]}</p>"
        return fs

    def delTodo(self): # This function deletes a specific item from the Todo List
        self.error_log.element.innerHTML = ""
        try:
            index = int(self.del_index.value)
            del self.content[index - 1]
            self.todo_out.element.innerHTML = self.CycleTodos() # Updates the content on the page
        except IndexError: # This displays a custom error message: Element {index} does not exist
            self.error_log.element.innerHTML = f"<pre class='py-error'> Element {index} does not exist </pre>"
        except ValueError: # This displays a custom error message: Please enter a valid number
            self.error_log.element.innerHTML = f"<pre class='py-error'> Please enter a valid number </pre>"
````

### HTML Frontend source code:
````
<!DOCTYPE html>
<html lang="en" style="overflow: hidden;touch-action: manipulation;user-scalable: none;-ms-content-zooming: none;-ms-touch-action: manipulation;">
    <head>
        <style>html { width: 100%; height: 100%; } </style>
        <title>Todo App</title>
        <meta charset="UTF-8">
        <link rel="icon" type="image/x-icon" href="favicon.ico">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
        <script defer src="https://pyscript.net/latest/pyscript.js"></script>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-white text-black dark:text-white dark:bg-slate-800">
        <py-script src="app.py"> </py-script>
        <py-script>App = Application()</py-script>
        <header class="text-black bg-slate-300 h-28 dark:text-white dark:bg-slate-700">
            <h1 class="text-center font-bold text-4xl mb-4">Todo App</h1>
            <p class="text-center">
                <input type="text" id="text_input" class="text-black rounded-l-md h-8 w-24"><button type="button" id="add_Todo" class="bg-sky-500 text-white rounded-r-md h-8" py-onClick="App.addTodo()">Add todo</button>
                <button type="button" py-onClick="App.delTodo()" class="bg-red-500 text-white rounded-l-md ml-7 h-8">Delete Todo</button><input class="w-10 rounded-r-md text-black h-8" id="del_index" type="number">
            </p>
        </header>
        <div id="todo_out"></div>
        <div id="error_log"></div>
    </body>
</html>

````