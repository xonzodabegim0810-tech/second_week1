class StudentTranscript:
    university = "Al-Khwarizmi University"
    max_courses = 6
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    def __init__(self, student_name, student_id, major, courses = None):
        self.student_name = student_name
        self.student_id = student_id
        self.major = major
        self.courses= []
    def add_course(self, course_name, credits, grade):
        if grade not in StudentTranscript.grade_points:
            print("It should be A, B, C, D, F")
        if credits < 1 or credits > 4:
            print("Invalid credits")
        if len(self.courses) > StudentTranscript.max_courses:
            print("Max courses range is out of range")
        self.courses.append({f"Name: {course_name},"
                           f"Grade: {grade}", 
                           f"credits: {credits}"})
    def calculate_gpa(self):
        total_points = 0
        total_credits = 0
        for course in self.courses:
            total_points += self.courses["Grade"] * StudentTranscript.grade_points[self.courses["Grade"]]
            total_credits += course["credits"]
        gpa = total_points / total_credits
        return gpa
    def get_standing(self, gpa=None):
        if gpa == None:
            gpa = self.calculate_gpa()
        if gpa >= 3.5:
            return "Excellent"
        elif gpa >= 3.0:
            return "Good"
        elif gpa >= 2.0:
            return "Satisfactiory"
        elif gpa >= 1.0:
            return "Failing"
    def get_honors_status(self):
        gpa = self.calculate_gpa()
        if len(self.courses) <= 4:
            return "no honors"
        if gpa >= 3.8:
            return "highest honor"
        elif gpa >= 3.5:
            return"high honor"
        elif gpa >= 3.0:
            return"high honor"
        else:
            return"no honor"
    def generate_transcript(self):
        print(f"OFFICIAL TRANSCRIPT - Al-Khwarizmi University,"
        print(f"Student: {self.student_name} | ID: {self.student_id} | Major: {self.major}")
        
        print(f"--------------------------------------------------")
        for course in self.courses:
            print(f"{course:["name"]:<21}")
        f"Total Credits: 16,"
        f"GPA: 3.56/4.00,"
        f"Standing: Excellent,"
        f","
        f"Honors: High Honors")
                