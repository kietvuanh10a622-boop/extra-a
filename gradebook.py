from utils import validate_score, validate_credits

class Gradebook:
    def __init__(self, data):
        self.data = data
    
    def find_course(self, code):
        for c in self.data["courses"]:
            if c["code"].lower() == code.lower():
                return c
        return None
    
    def add_course(self):
        print("\n--- Add Course ---")
        code = input("Course code: ").strip()
        if self.find_course(code):
            print("❌ Course already exists!")
            return
        
        name = input("Course name: ").strip()
        credits = input("Credits: ").strip()
        semester = input("Semester: ").strip()
        score = input("Score (0–10): ").strip()

        if not validate_credits(credits):
            print("❌ Invalid credits!")
            return
        
        if not validate_score(score):
            print("❌ Invalid score!")
            return
        
        new_course = {
            "code": code,
            "name": name,
            "credits": int(credits),
            "semester": semester,
            "score": float(score)
        }
        self.data["courses"].append(new_course)
        print("✅ Course added!")

    def update_course(self):
        print("\n--- Update Course ---")
        code = input("Course code: ").strip()
        course = self.find_course(code)

        if not course:
            print("❌ Course not found!")
            return

        print("Leave blank to keep current value.")

        name = input(f"New name ({course['name']}): ") or course["name"]
        credits = input(f"New credits ({course['credits']}): ") or course["credits"]
        semester = input(f"New semester ({course['semester']}): ") or course["semester"]
        score = input(f"New score ({course['score']}): ") or course["score"]

        if not validate_credits(credits):
            print("❌ Invalid credits!")
            return
        
        if not validate_score(score):
            print("❌ Invalid score!")
            return
        
        course["name"] = name
        course["credits"] = int(credits)
        course["semester"] = semester
        course["score"] = float(score)

        print("✅ Course updated!")

    def delete_course(self):
        print("\n--- Delete Course ---")
        code = input("Course code: ").strip()
        course = self.find_course(code)

        if not course:
            print("❌ Course not found!")
            return
        
        self.data["courses"].remove(course)
        print("🗑️ Course deleted!")

    def view_courses(self):
        if not self.data["courses"]:
            print("No courses yet.")
            return
        
        print("\n--- Gradebook ---")
        print(f"{'Code':10} | {'Name':25} | {'Credits':7} | {'Semester':12} | Score")
        print("-"*70)
        
        for c in self.data["courses"]:
            print(f"{c['code']:10} | {c['name'][:25]:25} | {c['credits']:7} | {c['semester']:12} | {c['score']}")
        print("-"*70)

    def calculate_gpa(self):
        if not self.data["courses"]:
            print("No courses available.")
            return
        
        print("\n--- GPA Calculation ---")
        total_points = 0
        total_credits = 0

        for c in self.data["courses"]:
            total_points += c["score"] * c["credits"]
            total_credits += c["credits"]
        
        gpa = total_points / total_credits if total_credits else 0
        print(f"📌 Overall GPA: {gpa:.2f}")

    def calculate_gpa_by_semester(self):
        print("\n--- GPA by Semester ---")
        
        semester_data = {}
        for c in self.data["courses"]:
            sem = c["semester"]
            semester_data.setdefault(sem, {"points": 0, "credits": 0})
            semester_data[sem]["points"] += c["score"] * c["credits"]
            semester_data[sem]["credits"] += c["credits"]

        for sem, data in semester_data.items():
            gpa = data["points"] / data["credits"]
            print(f"{sem}: GPA = {gpa:.2f}")
