class Application:
    # This class is for PyScript Websites #

    def __init__(self):
        self.content = []
        self.todo_out = Element('todo_out')
        self.text_input = Element('text_input')
        self.del_index = Element('del_index')
        self.error_log = Element('error_log')

    def addTodo(self):
        self.error_log.element.innerHTML = ""
        self.content.append(self.text_input.value)
        self.todo_out.element.innerHTML = self.CycleTodos()

    def CycleTodos(self):
        self.error_log.element.innerHTML = ""
        fs = ""
        for i in range(0, len(self.content)):
            fs += f"<p class='font-bold text-xl'>• {self.content[i]}</p>"
        
        return fs

    def delTodo(self):
        self.error_log.element.innerHTML = ""
        try:
            index = int(self.del_index.value)
            del self.content[index - 1]
            self.todo_out.element.innerHTML = self.CycleTodos()
        except IndexError:
            self.error_log.element.innerHTML = f"<pre class='py-error'> Element {index} does not exist </pre>"
        except ValueError:
            self.error_log.element.innerHTML = f"<pre class='py-error'> Please enter a valid number </pre>"

        
