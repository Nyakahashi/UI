class FileManager:
    def __init__(self):
        self.supported_algorithrms = ["none","AES"]
        self.supported_file_type = [".txt",".xlsx",".split"]
        self.directory = "./output/"
        self.export_file_one_name = "example"
        self.export_file_one_path = ""
        self.export_file_two_name = "example.split"
        self.export_file_two_path = ""
        self.selected_file_type = ""
        self.selected_algorithrm = ""
        self.passwd = ""
    def set_file_type(self,index):
        if index > 2 or index < 0:
            return
        self.selected_file_type = self.supported_file_type[index]
    def get_file_suffix(self):
        return self.selected_file_type