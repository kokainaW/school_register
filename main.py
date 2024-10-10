from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Define the layout for the Student Register Form
class RegisterForm(BoxLayout):
    def __init__(self, **kwargs):
        super(RegisterForm, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Add input fields and labels
        self.add_widget(Label(text="Student Name"))
        self.student_name = TextInput(multiline=False)
        self.add_widget(self.student_name)

        self.add_widget(Label(text="Student Age"))
        self.student_age = TextInput(multiline=False, input_filter='int')
        self.add_widget(self.student_age)

        self.add_widget(Label(text="Student Class"))
        self.student_class = TextInput(multiline=False)
        self.add_widget(self.student_class)

        # Submit button
        self.submit_btn = Button(text="Submit", on_press=self.submit)
        self.add_widget(self.submit_btn)

        # Output Label
        self.output = Label(text="")
        self.add_widget(self.output)

    def submit(self, instance):
        # Collect input data
        name = self.student_name.text.strip()
        age = self.student_age.text.strip()
        student_class = self.student_class.text.strip()

        # Validate input data
        if not name or not age or not student_class:
            self.output.text = "Please fill in all fields."
            return

        if not age.isdigit():
            self.output.text = "Please enter a valid age."
            return

        # Display confirmation message
        self.output.text = f"Registered: {name}, Age: {age}, Class: {student_class}"

class StudentRegisterApp(App):
    def build(self):
        return RegisterForm()

if __name__ == '__main__':
    StudentRegisterApp().run()

