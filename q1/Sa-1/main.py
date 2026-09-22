class AssignmentSubmissions:

    def __init__(self, name, id, assignment, due, is_submitted, grade:float, submitted_files):
        self.student_name = name
        self.student_id = id
        self._assignment_title = assignment
        self._due_date = due
        self.__is_submitted = True
        self.__grade = grade:float
        self.__submitted_files = []

    def __validate_grade(self, score:float):
        if self.__grade >= 0:
            return True
        else:
            return False
        

    def __check_submission_status():
        self.__is_submitted != True
            self.__is_submitted = False
            return self.__is_submitted
        return self.__is_submitted
    
    def __is_duplacate(self, filename:str):
        filename = []
        while True:
            return True
        if self.__submitted_files in filename:
            return False

    def add_file(self, filename:str):
        self.__submitted_files.append(filename)

    def remove_file(self, filename:str):
        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)

    def __assign_grade(self, score:float):
        self.__grade = score

    def get_grade():
        def.__grade = get_grade
        return str(self.__grade)
    
    def view_files():
        return str(self.__submitted_files)

    def get_status_report():
        if len(self.__submitted_files) == 0:
            return "missing"
        else:
            return "submitted"
    



        