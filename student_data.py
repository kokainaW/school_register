from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class StudentRegisterApp(App):
    def build(self):
        self.students = {}
        layout = BoxLayout(orientation='vertical')
        
        self.name_input = TextInput(hint_text="Enter Student Name")
        self.age_input = TextInput(hint_text="Enter Student Age", input_filter='int')
        self.class_input = TextInput(hint_text="Enter Class")
        self.dob_input = TextInput(hint_text="Enter Date of Birth (YYYY-MM-DD)")
        
        add_button = Button(text="Add Student", on_press=self.add_student)
        self.message_label = Label(text="")
        
        layout.add_widget(self.name_input)
        layout.add_widget(self.age_input)
        layout.add_widget(self.class_input)
        layout.add_widget(self.dob_input)
        layout.add_widget(add_button)
        layout.add_widget(self.message_label)
        
        return layout

    def add_student(self, instance):
        name = self.name_input.text
        age = self.age_input.text
        dob = self.dob_input.text
        student_class = self.class_input.text
        
        if name and age and dob and student_class:
            student_id = len(self.students) + 1
            self.students[student_id] = {
                'name': name,
                'age': int(age),
                'dob': dob,
                'class': student_class
            }
            self.message_label.text = f"Student {name} added successfully!"
        else:
            self.message_label.text = "Please fill out all fields!"

if __name__ == "__main__":
    StudentRegisterApp().run()

