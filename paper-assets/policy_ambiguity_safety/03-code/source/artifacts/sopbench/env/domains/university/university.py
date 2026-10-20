"""
file for university system functionality implementations
assumes previous steps in dependency chain were called
"""

from env.dep_eval import Dependency_Evaluator
from env.helpers import get_domain_dependency_none
from datetime import datetime
import copy
import re

default_data = {
    "students": {
        "alice": {
            "password": "[REDACTED]",
            "major": "Computer Science",
            "completed_credits": 45,
            "gpa": 3.8,
            "enrolled_courses": ["CS101"],
            "completed_courses": ["MATH100", "ENG101"],
            "current_credits": 4,
            "tuition_balance": 0,
            "academic_status": "Good",
            "financial_aid_quarters": 3,
            "residency": "in-state",
            "income": 45000,
            "minors": [],
            "major_changes": 0,
        }
    },
    "courses": {
        "CS101": {
            "prerequisites": [],
            "capacity": 30,
            "enrolled": 28,
            "schedule": {"days": ["Mon", "Wed"], "time": "10:00-11:30"},
            "credits": 4,
            "division": "lower",
            "exam_schedule": "2023-12-15T09:00",
            "restricted_to_majors": ["Computer Science"]
        },
        "CS201": {
            "prerequisites": ["CS101"],
            "capacity": 25,
            "enrolled": 24,
            "schedule": {"days": ["Tue", "Thu"], "time": "14:00-15:30"},
            "credits": 4,
            "division": "upper",
            "exam_schedule": "2023-12-16T14:00",
            "restricted_to_majors": ["Computer Science"]
        }
    },
    "academic_calendar": {
        "registration_period": ["2023-11-01", "2023-11-30"],
        "graduation_deadline": "2024-03-01",
        "withdrawal_deadline": "2023-12-01",
        "major_change_deadline": "2023-11-15",
        "minor_declaration_deadline": "2023-11-20"
    },
    "majors": {
        "Computer Science": {
            "required_courses": ["CS101", "CS201", "MATH200"],
            "min_gpa": 2.5,
            "capacity": 20
        },
        "Music": {
            "required_courses": ["MUS101"],
            "min_gpa": 3.0,
            "capacity": 50,
        }
    },
    "minors": {
        "Physics": {
            "required_courses": ["PHYS101"],
            "min_credits": 30,
            "min_gpa": 2.8,
            "prerequisites": ["MATH100"],
            "max_overlap": 1,
            "incompatible_majors": ["Music"]
        },
        "Digital Arts": {
            "required_courses": ["ART120"],
            "min_credits": 45,
            "min_gpa": 3.0,
            "prerequisites": ["ART100"],
            "max_overlap": 2,
            "incompatible_majors": []
        }
    },
    "interaction_time": "2023-11-15T10:00:00"
}

default_data_descriptions = {
    "students": "Student academic records including major, credits, GPA, and enrollment status",
    "courses": "Course catalog with scheduling, capacity, and requirements",
    "academic_calendar": "Important dates for university operations",
    "major": "Student's declared academic major",
    "completed_credits": "Total credits successfully completed",
    "current_credits": "Credits currently enrolled in for this term",
    "academic_status": "Current academic standing (Good, Probation, etc.)",
    "financial_aid_quarters": "Number of quarters financial aid has been used",
    "residency": "Student's residency status for tuition purposes",
    "exam_schedule": "Date and time of final exam for course in ISO format",
    "major_restrictions": "List of majors allowed to enroll in course",
    "health_compliance": "Whether student meets vaccination requirements",
    "incompatible_majors": "List of majors that can't declare this minor (empty means no restrictions)",
    "restricted_to_majors": "List of majors that can take this class (empty means no restrictions)."
}

ddp = default_dependency_parameters = {
    "max_credits_per_quarter": 18,
    "min_credits_drop": 12,
    "graduation_credit_requirement": 180,
    "min_gpa_graduation": 2.0,
    "max_financial_aid_quarters": 12,
    "max_minors": 3,
    "max_major_changes": 3,
    "min_credits_major_change": 45,
    "max_minors": 2,
    "min_credits_minor": 30,
    "max_overlap_minor_major": 2,
    "min_gpa_financial_aid": 2.0,
    "max_income_financial_aid": 50000,
    "min_credits_financial_aid": 6,
}

class University:
    def __init__(self, data=default_data, dep_innate_full=get_domain_dependency_none("University"), 
                 dep_params:dict=default_dependency_parameters, data_descriptions=default_data_descriptions):
        self.data = data
        self.students = self.data["students"]
        self.courses = self.data["courses"]
        self.academic_calendar = self.data["academic_calendar"]
        self.majors = self.data.get("majors", {})
        self.innate_state_tracker = University_State_Tracker(self, **dep_params)
        self.domain_dep = Dependency_Evaluator(self, self.innate_state_tracker, dep_innate_full)
        self.data_descriptions = data_descriptions

    def login_user(self, username: str, password: [REDACTED] -> bool:
        if not self.domain_dep.process(method_str="login_user", username=username, password=[REDACTED] 
            return False
        return self.students[username]["password"] == password

    def logout_user(self, username: str) -> bool:
        if not self.domain_dep.process(method_str="logout_user", username=username): 
            return False
        return True

    def enroll_course(self, username: str, course_code: str) -> bool:
        if not self.domain_dep.process(method_str="enroll_course", username=username, course_code=course_code): 
            return False
        
        course = self.courses[course_code]
        student = self.students[username]
        
        student["enrolled_courses"].append(course_code)
        student["current_credits"] += course["credits"]
        course["enrolled"] += 1
        return True

    def drop_course(self, username: str, course_code: str) -> bool:
        if not self.domain_dep.process(method_str="drop_course", username=username, course_code=course_code): 
            return False
        
        course = self.courses[course_code]
        student = self.students[username]
        
        student["enrolled_courses"].remove(course_code)
        student["current_credits"] -= course["credits"]
        course["enrolled"] -= 1
        return True

    def request_graduation(self, username: str) -> bool:
        if not self.domain_dep.process(method_str="request_graduation", username=username): 
            return False
        # grad apps
        return True

    def apply_financial_aid(self, username: str) -> bool:
        if not self.domain_dep.process(method_str="apply_financial_aid", username=username): 
            return False
        
        self.students[username]["financial_aid_quarters"] += 1
        return True


    def change_major(self, username: str, new_major: str) -> bool:
        if not self.domain_dep.process(method_str="change_major", username=username, new_major=new_major): 
            return False
        
        self.students[username]["major"] = new_major
        self.students[username]["major_changes"] += 1
        return True

    def declare_minor(self, username: str, minor: str) -> bool:
        if not self.domain_dep.process(method_str="declare_minor", username=username, minor=minor): 
            return False
        
        self.students[username]["minors"].append(minor)
        return True

    def internal_check_username_exists(self, username: str) -> tuple[bool, bool]:
        if not self.domain_dep.process(method_str="internal_check_username_exists", username = username): return False
        return True, username in self.students

    def internal_check_course_exists(self, course_code: str) -> tuple[bool, bool]:
        if not self.domain_dep.process(method_str="internal_check_course_exists", course_code = course_code): return False
        return True, course_code in self.courses

    def internal_get_student_info(self, username: str) -> tuple[bool, dict]:
        if not self.domain_dep.process(method_str="internal_get_student_info", username = username): return False, {}
        return True, self.students[username]

    def internal_get_course_info(self, course_code: str) -> tuple[bool, dict]:
        if not self.domain_dep.process(method_str="internal_get_course_info", course_code = course_code): return False, {}
        return True, self.courses[course_code]

    def internal_get_academic_calendar(self) -> tuple[bool, dict]:
        if not self.domain_dep.process(method_str="internal_get_academic_calendar"): return False
        return True, self.academic_calendar


    def internal_get_major_info(self, major: str) -> tuple[bool, dict]:
        if not self.domain_dep.process(method_str="internal_get_major_info", major = major): return False, {}
        return True, self.majors.get(major, {})
    
    def internal_get_minor_info(self, minor: str) -> tuple[bool, dict]:
        if not self.domain_dep.process(method_str="internal_get_minor_info", minor=minor): 
            return False, None
        return True, self.data["minors"].get(minor, {})

    def internal_check_minor_exists(self, minor: str) -> tuple[bool, bool]:
        if not self.domain_dep.process(method_str="internal_check_minor_exists", minor=minor): 
            return False, False
        return True, minor in self.data["minors"]

    def internal_check_major_exists(self, major: str) -> tuple[bool, bool]:
        if not self.domain_dep.process(method_str="internal_check_major_exists", major=major): 
            return False, False
        return True, major in self.data["majors"]

    def internal_get_interaction_time(self) -> tuple[bool, str]:
        if not self.domain_dep.process(method_str="internal_get_interaction_time"): return False
        return True, self.data["interaction_time"]
    
    def internal_get_database(self)->bool|tuple[bool,dict]:
        if not self.domain_dep.process(method_str="internal_get_database"): return False
        return True, self.data
    
    def internal_get_number_of_students_for_major(self, major: str) -> tuple[bool, int]:
        if not self.domain_dep.process(method_str="internal_get_number_of_students_for_major", major=major): 
            return False
        student_count = sum(1 for s in self.data['students'].values() 
                          if s['major'] == major)
        return True, student_count

    def evaluation_get_database(self)->dict:
        return self.data
    
    def evaluation_get_database_descriptions(self)->dict:
        return self.data_descriptions





class University_State_Tracker:
    def __init__(self, domain_system: University,
                max_credits_per_quarter: int,
                min_credits_drop: int,
                graduation_credit_requirement: int,
                min_gpa_graduation: float,
                max_financial_aid_quarters: int,
                max_minors: int,
                max_major_changes: int,
                min_credits_major_change: int,
                min_credits_minor: int,
                max_overlap_minor_major: int,
                min_gpa_financial_aid: float,
                max_income_financial_aid: float,
                min_credits_financial_aid: int):
        self.domain_system = domain_system
        self.previously_logged_in_username: str = None
        self.max_credits_per_quarter = max_credits_per_quarter
        self.min_credits_drop = min_credits_drop
        self.graduation_credit_requirement = graduation_credit_requirement
        self.min_gpa_graduation = min_gpa_graduation
        self.max_financial_aid_quarters = max_financial_aid_quarters
        self.max_minors = max_minors
        self.max_major_changes = max_major_changes
        self.min_credits_major_change = min_credits_major_change
        self.min_credits_minor = min_credits_minor
        self.max_overlap_minor_major = max_overlap_minor_major
        self.min_gpa_financial_aid = min_gpa_financial_aid
        self.max_income_financial_aid = max_income_financial_aid
        self.min_credits_financial_aid = min_credits_financial_aid

    def logged_in_user(self, username: str) -> bool:
        return self.previously_logged_in_username == username
    def set_login_user(self, username: str):
        self.previously_logged_in_username = username
    def set_logout_user(self):
        self.previously_logged_in_username = None

    def has_completed_prerequisites(self, username: str, course_code: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        _, course = self.domain_system.internal_get_course_info(course_code)
        return all(p in student["completed_courses"] for p in course["prerequisites"])

    def within_registration_period(self) -> bool:
        _, calendar = self.domain_system.internal_get_academic_calendar()
        _, now = self.domain_system.internal_get_interaction_time()
        start = datetime.fromisoformat(calendar["registration_period"][0])
        now = datetime.fromisoformat(now)
        end = datetime.fromisoformat(calendar["registration_period"][1])
        return start <= now <= end

    def course_has_capacity(self, course_code: str) -> bool:
        _,course = self.domain_system.internal_get_course_info(course_code)
        return course["enrolled"] < course["capacity"]

    def credits_within_limit(self, username: str, course_code: str) -> bool:
        _,student = self.domain_system.internal_get_student_info(username)
        _,course = self.domain_system.internal_get_course_info(course_code)
        return student["current_credits"] + course["credits"] <= self.max_credits_per_quarter
    
    def _schedules_overlap(self, schedule1: dict, schedule2: dict) -> bool:
        days_overlap = any(day in schedule2["days"] for day in schedule1["days"])
        if not days_overlap:
            return False
            
        time1_start, time1_end = [datetime.strptime(t, "%H:%M") for t in schedule1["time"].split("-")]
        time2_start, time2_end = [datetime.strptime(t, "%H:%M") for t in schedule2["time"].split("-")]
        
        return (time1_start < time2_end) and (time2_start < time1_end)

    def no_schedule_conflict(self, username: str, course_code: str) -> bool:
        _,new_course = self.domain_system.internal_get_course_info(course_code)
        _,student = self.domain_system.internal_get_student_info(username)
        
        for enrolled_code in student["enrolled_courses"]:
            _,existing_course = self.domain_system.internal_get_course_info(enrolled_code)
            if self._schedules_overlap(existing_course["schedule"], new_course["schedule"]):
                return False
        return True

    def meets_division_requirements(self, username: str, course_code: str) -> bool:
        _,course = self.domain_system.internal_get_course_info(course_code)
        _,student = self.domain_system.internal_get_student_info(username)
        return course["division"] != "upper" or student["completed_credits"] >= 90

    def course_not_completed(self, username: str, course_code: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        return course_code not in student["completed_courses"]

    def no_exam_conflict(self, username: str, course_code: str) -> bool:
        _,new_course = self.domain_system.internal_get_course_info(course_code)
        _,student = self.domain_system.internal_get_student_info(username)
        new_exam = datetime.fromisoformat(new_course["exam_schedule"])
        
        for enrolled_code in student["enrolled_courses"]:
            _,existing_course = self.domain_system.internal_get_course_info(enrolled_code)
            existing_exam = datetime.fromisoformat(existing_course["exam_schedule"])
            if existing_exam == new_exam:
                return False
        return True

    def major_requirements_met(self, username: str) -> bool:
        _,student = self.domain_system.internal_get_student_info(username)
        _, major_info = self.domain_system.internal_get_major_info(student["major"]);
        return all(c in student["completed_courses"] for c in major_info.get("required_courses", []))

    def gen_ed_requirements_met(self, username: str) -> bool:
        _,student = self.domain_system.internal_get_student_info(username)
        return len([c for c in student["completed_courses"] if c.startswith("GEN")]) >= 10

    def credit_requirement_met(self, username: str) -> bool:
        _,student = self.domain_system.internal_get_student_info(username)
        return student["completed_credits"] >= self.graduation_credit_requirement

    def gpa_requirement_met(self, username: str) -> bool:
        _,student = self.domain_system.internal_get_student_info(username)
        return student["gpa"] >= self.min_gpa_graduation

    def tuition_balance_zero(self, username: str) -> bool:
        _,student = self.domain_system.internal_get_student_info(username)
        return student["tuition_balance"] <= 0

    def before_graduation_deadline(self) -> bool:
        _,calendar = self.domain_system.internal_get_academic_calendar()
        deadline = datetime.fromisoformat(calendar["graduation_deadline"])
        _, now = self.domain_system.internal_get_interaction_time()
        current = datetime.fromisoformat(now)
        return current <= deadline

    def not_on_probation(self, username: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        return student["academic_status"].lower() != "probation"

    def meets_half_time_enrollment(self, username: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        return student["current_credits"] >= 6

    def financial_aid_quota_available(self, username: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        return student["financial_aid_quarters"] < self.max_financial_aid_quarters

    def meets_major_gpa_requirement(self, username: str, new_major: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        _, major_info = self.domain_system.internal_get_major_info(new_major)
        return student["gpa"] >= major_info.get("min_gpa", 0)

    def within_major_change_period(self) -> bool:
        _, calendar = self.domain_system.internal_get_academic_calendar()
        deadline = datetime.fromisoformat(calendar["major_change_deadline"]).date()
        _, now = self.domain_system.internal_get_interaction_time()
        now = datetime.fromisoformat(now).date()
        return now <= deadline

    def under_max_major_changes(self, username: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        return student["major_changes"] < self.max_major_changes

    def minor_compatible_with_major(self, username: str, minor: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)        
        _, minor_info = self.domain_system.internal_get_minor_info(minor)        
        incompatible_majors = minor_info.get("incompatible_majors", [])
        return student["major"] not in incompatible_majors

    def under_max_minors(self, username: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        return len(student["minors"]) < self.max_minors
    
    def minor_course_overlap_check(self, username: str, minor: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)        
        _, minor_info = self.domain_system.internal_get_minor_info(minor)        
        _, major_info = self.domain_system.internal_get_major_info(major=student["major"])

        minor_courses = minor_info.get("required_courses", [])
        major_courses = major_info.get("required_courses", [])
        overlap = len(set(minor_courses) & set(major_courses))
        return overlap <= self.max_overlap_minor_major
    
    def meets_minor_gpa_requirement(self, username: str, minor: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        _, minor_info = self.domain_system.internal_get_minor_info(minor)
        return student["gpa"] >= minor_info.get("min_gpa", 2.0)
    
    def meets_minor_prerequisites(self, username: str, minor: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        _, minor_info = self.domain_system.internal_get_minor_info(minor)        
        return all(p in student["completed_courses"] for p in minor_info.get("prerequisites", []))
    
    def within_minor_declaration_period(self) -> bool:
        _, calendar = self.domain_system.internal_get_academic_calendar()
        deadline = datetime.fromisoformat(calendar["minor_declaration_deadline"])
        _, now = self.domain_system.internal_get_interaction_time()
        now = datetime.fromisoformat(now)
        return now <= deadline
    
    def has_min_credits_for_major_change(self, username: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        return student["completed_credits"] >= self.min_credits_major_change

    def major_has_capacity(self, new_major: str) -> bool:
        _, major_info = self.domain_system.internal_get_major_info(new_major)
        _, student_count = self.domain_system.internal_get_number_of_students_for_major(new_major)
        return student_count < major_info['capacity']
    
    def meets_min_gpa_for_aid(self, username: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        return student["gpa"] >= self.min_gpa_financial_aid

    def meets_income_requirements(self, username: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        return student["income"] <= self.max_income_financial_aid

    def valid_residency_status(self, username: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        return student["residency"] in ["in-state", "public"]
    
    def meets_major_restriction(self, username: str, course_code: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        _, course = self.domain_system.internal_get_course_info(course_code)
        return student["major"] in course.get("restricted_to_majors", [])
    
    def maintains_min_credits(self, username: str, course_code: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        _, course = self.domain_system.internal_get_course_info(course_code)
        return (student["current_credits"] - course["credits"]) >= self.min_credits_drop
    
    def within_withdrawal_period(self) -> bool:
        _, calendar = self.domain_system.internal_get_academic_calendar()
        deadline = datetime.fromisoformat(calendar["withdrawal_deadline"])
        _, now = self.domain_system.internal_get_interaction_time()
        return datetime.fromisoformat(now) <= deadline
    
    def course_enrolled_by_user(self, username: str, course_code: str) -> bool:
        _, student = self.domain_system.internal_get_student_info(username)
        return course_code in student["enrolled_courses"]

    
    

class University_Strict:
    def __init__(self, data=default_data, dep_innate_full=get_domain_dependency_none("University"),
                 dep_full=get_domain_dependency_none("University_Strict"),
                dep_params:dict=default_dependency_parameters, data_descriptions=default_data_descriptions):
        self.domain_system = University(data, dep_innate_full, dep_params, data_descriptions)
        self.state_tracker = University_State_Tracker(self.domain_system, **dep_params)
        self.domain_dep = Dependency_Evaluator(self.domain_system, self.state_tracker, dep_full)
        self.dep_params = dep_params

    def login_user(self, username: str, password: [REDACTED] -> bool:
        if not self.domain_dep.process(method_str="login_user", username=username, password=[REDACTED]
            return False
        self.state_tracker.set_login_user(username)
        return self.domain_system.login_user(username, password)
    
    def logout_user(self, username: str) -> bool:
        dep_res = self.domain_dep.process(method_str="logout_user", username=username)
        if not dep_res:
            return False
        self.state_tracker.set_logout_user()
        return self.domain_system.logout_user(username)

    def enroll_course(self, username: str, course_code: str) -> bool:
        return self._check_dep_and_do("enroll_course", username=username, course_code=course_code)

    def drop_course(self, username: str, course_code: str) -> bool:
        return self._check_dep_and_do("drop_course", username=username, course_code=course_code)

    def request_graduation(self, username: str) -> bool:
        return self._check_dep_and_do("request_graduation", username=username)

    def apply_financial_aid(self, username: str) -> bool:
        return self._check_dep_and_do("apply_financial_aid", username=username)

    
    def change_major(self,  username: str, new_major: str) -> bool:
        return self._check_dep_and_do("change_major", username = username, new_major = new_major)
    
    def declare_minor(self, username: str, minor: str) -> bool:
        return self._check_dep_and_do("declare_minor", username = username, minor = minor)

    
    #add the internals
    def evaluation_get_database(self)->dict:
        return self.domain_system.evaluation_get_database()
    def evaluation_get_dependency_parameters(self)->dict:
        return self.dep_params
    def evaluation_get_domain_system(self)->University:
        return self.domain_system
    def evaluation_get_database_descriptions(self)->dict:
        return self.domain_system.evaluation_get_database_descriptions()
    def evaluation_get_dependency_evaluator(self)->Dependency_Evaluator:
        return self.domain_dep
    def evaluation_get_state_tracker(self)->University_State_Tracker:
        return self.state_tracker
    def _check_dep_and_do(self, method_str, **kwargs):
      if not self.domain_dep.process(method_str=method_str, **kwargs): return False
      return getattr(self.domain_system, method_str)(**kwargs)
    