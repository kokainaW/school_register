from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

# Define the layout for the Student Register Form
class RegisterForm(BoxLayout):
    def __init__(self, **kwargs):
        super(RegisterForm, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Image display section
        self.image_display = Image(size_hint=(1, 0.3), allow_stretch=True)
        self.add_widget(self.image_display)

        # Image upload button
        self.upload_btn = Button(text='Select Image', size_hint=(1, 0.1))
        self.upload_btn.bind(on_press=self.open_filechooser)
        self.add_widget(self.upload_btn)

        # Add input fields and labels
        self.add_widget(Label(text="Student ID"))
        self.student_id = TextInput(multiline=False)
        self.add_widget(self.student_id)

        self.add_widget(Label(text="Student Name"))
        self.student_name = TextInput(multiline=False)
        self.add_widget(self.student_name)

        self.add_widget(Label(text="Student Age"))
        self.student_age = TextInput(multiline=False, input_filter='int')
        self.add_widget(self.student_age)

        self.add_widget(Label(text="Date of Birth (YYYY-MM-DD)"))
        self.date_of_birth = TextInput(multiline=False)
        self.add_widget(self.date_of_birth)

        self.add_widget(Label(text="Gender"))
        self.gender_dropdown = DropDown()
        self.gender_options = ['Male', 'Female', 'Other']
        for option in self.gender_options:
            btn = Button(text=option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.gender_dropdown.select(btn.text))
            self.gender_dropdown.add_widget(btn)
        self.gender_button = Button(text='Select Gender', size_hint_y=None, height=44)
        self.gender_button.bind(on_release=self.gender_dropdown.open)
        self.gender_dropdown.bind(on_select=lambda instance, x: setattr(self.gender_button, 'text', x))
        self.add_widget(self.gender_button)

        self.add_widget(Label(text="Student Class"))
        self.student_class = TextInput(multiline=False)
        self.add_widget(self.student_class)

        self.add_widget(Label(text="Address"))
        self.address = TextInput(multiline=False)
        self.add_widget(self.address)

        # Submit button
        self.submit_btn = Button(text="Submit", on_press=self.submit)
        self.add_widget(self.submit_btn)

        # Output Label
        self.output = Label(text="")
        self.add_widget(self.output)

    def open_filechooser(self, instance):
        content = FileChooserIconView()
        content.bind(on_submit=self.load_image)
        self.popup = Popup(title="Select an image", content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    def load_image(self, filechooser, selection, touch):
        if selection:
            self.upload_btn.text = f"Image: {selection[0].split('/')[-1]}"  # Update button text with file name
            self.image_display.source = selection[0]  # Display the selected image
            self.image_display.reload()  # Reload to show the image
        self.popup.dismiss()

    def submit(self, instance):
        # Collect input data
        student_id = self.student_id.text
        name = self.student_name.text
        age = self.student_age.text
        dob = self.date_of_birth.text
        gender = self.gender_button.text
        student_class = self.student_class.text
        address = self.address.text

        # Display confirmation message
        self.output.text = (f"Registered: ID: {student_id}, Name: {name}, Age: {age}, "
                            f"DOB: {dob}, Gender: {gender}, Class: {student_class}, "
                            f"Address: {address}")

class StudentRegisterApp(App):
    def build(self):
        return RegisterForm()

if __name__ == '__main__':
    StudentRegisterApp().run()

