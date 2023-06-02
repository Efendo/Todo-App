from js import window
import ast

class Application:

    def __init__(self):
        if window.localStorage.getItem('content') == None:                           ########################
            self.content = []                                                        ########################
        else:                                                                        ##  Error prevention  ##
            self.content =  ast.literal_eval(window.localStorage.getItem('content')) ########################
                                                                                     ########################
        
        self.todo_out = Element('todo_out') # This is a div element which displays the Todo list
        self.text_input = Element('text_input') # This is the text field for adding todo to the list
        self.del_index = Element('del_index') # This is the number field to get the ID of the item to Delete
        self.error_log = Element('error_log') # This is the div which displays custom errors
        self.todo_out.element.innerHTML = self.CycleTodos() # Updates the content on the page

    def addTodo(self): # This function adds a new item to the Todo list and displays it using the CycleTodo function
        self.error_log.element.innerHTML = ""
        self.content.append(self.text_input.value)
        self.todo_out.element.innerHTML = self.CycleTodos() # Updates the content on the page
        window.localStorage.setItem('content', self.content)

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
            window.localStorage.setItem('content', self.content)
        except IndexError: # This displays a custom error message: Element {index} does not exist
            self.error_log.element.innerHTML = f"<pre class='py-error'> Element {index} does not exist </pre>"
        except ValueError: # This displays a custom error message: Please enter a valid number
            self.error_log.element.innerHTML = f"<pre class='py-error'> Please enter a valid number </pre>"
