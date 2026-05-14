#Attempt to create a suitable file picker on mobile environment.

import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class FileChooserUI(App):
    def build(self):
        self.current_path = "/storage/emulated/0/"  # start in phone storage

        layout = BoxLayout(orientation='vertical')
        self.path_label = Label(text=f"📂 {self.current_path}", size_hint_y=None, height=40)
        layout.add_widget(self.path_label)

        # Scrollable file list
        self.scroll = ScrollView()
        self.file_grid = GridLayout(cols=1, size_hint_y=None)
        self.file_grid.bind(minimum_height=self.file_grid.setter('height'))
        self.scroll.add_widget(self.file_grid)
        layout.add_widget(self.scroll)

        self.output_label = Label(text="Select a file", size_hint_y=None, height=40)
        layout.add_widget(self.output_label)

        self.load_files(self.current_path)
        return layout

    def load_files(self, path):
        self.file_grid.clear_widgets()
        try:
            files = os.listdir(path)
        except PermissionError:
            self.output_label.text = "Permission denied"
            return

        for f in files:
            full_path = os.path.join(path, f)
            btn = Button(text=f, size_hint_y=None, height=40)
            btn.bind(on_press=lambda instance, p=full_path: self.select_file(p))
            self.file_grid.add_widget(btn)

    def select_file(self, path):
        if os.path.isdir(path):
            self.current_path = path
            self.path_label.text = f"📂 {self.current_path}"
            self.load_files(path)
        else:
            self.output_label.text = f"Selected file:\n{path}"

FileChooserUI().run()
