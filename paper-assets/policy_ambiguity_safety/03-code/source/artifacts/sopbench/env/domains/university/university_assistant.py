from env.helpers import get_action_full_description

"""
This file contains the information for the online_market assistant for the OpenAI API.
The three main fields are the name, description/instructions, and actions.
Each function's properties, their required fields, and relations are checked in `check_data_sanity`.
Assistant Properties: name, description, instructions, and actions (function definitions).
Action Properties:
    - JSON definition has the name, strict set to true, brief description, and has the required input parameters to call the function.
    - JSON definition includes parameter name, description, and type.
    - Every action is referenced in the descriptions, and vice versa.
    - Every key in action_descriptions, action_returns, action_dependencies, and action_shared_dependencies exist in all three, and descriptions and returns must exist.
    - The action_shared_dependencies must not be circular, and chain links must exist as actions and must have condition descriptions.
Database Functionality Properties:
    - Every function defined as JSON files in the assistant is defined in the database and database strict.
    - Every function input parameter referenced by the assistant is in the database functionality, and vice versa.
"""

name = "University Assistant"

instructions = "You are a university academic assistant responsible for helping students and staff manage academic activities. " \
               "Your role includes supporting course enrollment, graduation processes, financial aid applications, " \
               "and academic record maintenance. Handle tasks typical of university administration."



action_descriptions = {

    "login_user": "Authenticates student using university credentials",
    "logout_user": "Terminates student session",
    
    "enroll_course": "Enrolls student in specified course after checking prerequisites and availability",
    "drop_course": "Withdraws student from enrolled course before deadline",
    "request_graduation": "Initiates graduation application process",
    "change_major": "Updates student's declared academic program",
    "declare_minor": "Adds secondary academic specialization",
    "apply_financial_aid": "Submits financial assistance application",
    
    # Internal Checks
    "internal_check_username_exists": "Verifies student record existence"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_check_course_exists": "Validates course availability"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_get_academic_calendar": "Retrieves academic timeline"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_get_course_info": "Fetches course details"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_get_student_info": "Accesses student records"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_get_major_info": "Retrieves program requirements"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_check_major_exists": "Verifies academic program existence"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_get_minor_info": "Retrieves minor requirements and structure"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_check_minor_exists": "Validates minor program availability"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_get_interaction_time": "Gets current system timestamp"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_get_number_of_students_for_major": "Gets the amount of students for a specific major"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_get_database":        "Shows the full database of the entire university, every student and every detail."

}

action_returns = {

    "login_user": "Returns true or false for login success or failure.",
    "logout_user": "Returns true always because logout is successful.",
    
    "enroll_course": "Returns true or false based on successful course enrollment.",
    "drop_course": "Returns true or false based on successful course removal.",
    "request_graduation": "Returns true or false based on successful graduation.",
    "change_major": "Returns true or false based on successful major update.",
    "declare_minor": "Returns true or false based on successful minor declaration.",
    "apply_financial_aid": "Returns true or false based on application submission status.",
    
    # Internal Checks
    "internal_check_username_exists": "Returns true or false based on student record existence. This is an internal action, only accessible by the assistant.",
    "internal_check_course_exists": "Returns true or false based on course availability. This is an internal action, only accessible by the assistant.",
    "internal_get_academic_calendar": "Returns academic calendar details. This is an internal action, only accessible by the assistant.",
    "internal_get_course_info": "Returns course metadata including schedule and credits. This is an internal action, only accessible by the assistant.",
    "internal_get_student_info": "Returns student profile including academic and contact details. This is an internal action, only accessible by the assistant.",
    "internal_get_major_info": "Returns requirements and structure of academic programs. This is an internal action, only accessible by the assistant.",
    "internal_get_interaction_time": "Returns current system timestamp. This is an internal action, only accessible by the assistant.",
    "internal_check_major_exists": "Returns true or false based on major program existence. This is an internal action, only accessible by the assistant.",
    "internal_get_minor_info": "Returns minor requirements including courses and GPA rules. This is an internal action, only accessible by the assistant.",
    "internal_check_minor_exists": "Returns true or false based on minor program availability. This is an internal action, only accessible by the assistant.",
    "internal_get_number_of_students_for_major": "Returns the number of students for a specific major. This is an internal action, only accessible by the assistant.",

        "internal_get_database":        "Returns the json of the entire database.",
}


action_innate_dependencies = {
    "login_user": ("single", "internal_check_username_exists", {"username": "username"}),
    "logout_user": None,

    "enroll_course": ("single", "internal_check_course_exists", {"course_code": "course_code"}),
    "drop_course": None,
    "request_graduation":  None,
    "change_major":  ("single", "internal_check_major_exists", {"major": "new_major"}),
    "declare_minor":  ("single", "internal_check_minor_exists", {"minor": "minor"}),
    "apply_financial_aid":  None,

    "internal_check_username_exists": None,
    "internal_check_course_exists": None,
    "internal_get_academic_calendar": None,
    "internal_get_course_info": ("single", "internal_check_course_exists", {"course_code": "course_code"}),
    "internal_get_student_info": ("single", "internal_check_username_exists", {"username": "username"}),
    "internal_get_major_info": ("single", "internal_check_major_exists", {"major": "major"}),
    "internal_get_interaction_time": None,
    "internal_get_minor_info": ("single", "internal_check_minor_exists", {"minor": "minor"}),
    "internal_check_major_exists": None,
    "internal_check_minor_exists": None,
    "internal_get_database":        None,
    "internal_get_number_of_students_for_major": ("single", "internal_check_major_exists", {"major": "major"}),


    }

action_required_dependencies = { 
    "login_user": None,
    "logout_user": None,

    "enroll_course":  ("single", "logged_in_user", {"username": "username"}),
    "drop_course":  ("and", [
        ("single", "course_enrolled_by_user", {"username": "username", "course_code": "course_code"}),
        ("single", "logged_in_user", {"username": "username"}),
    ]),
    "request_graduation":   ("single", "logged_in_user", {"username": "username"}),
    "change_major":   ("single", "logged_in_user", {"username": "username"}),
    "declare_minor":   ("single", "logged_in_user", {"username": "username"}),
    "apply_financial_aid":   ("single", "logged_in_user", {"username": "username"}),

    "internal_check_username_exists": None,
    "internal_check_course_exists": None,
    "internal_get_academic_calendar": None,
    "internal_get_course_info": None,
    "internal_get_student_info": None,
    "internal_get_major_info": None,
    "internal_get_interaction_time": None,
    "internal_get_minor_info": None,
    "internal_check_major_exists": None,
    "internal_check_minor_exists": None,
    "internal_get_database":        None,
    "internal_get_number_of_students_for_major": None,

}

action_customizable_dependencies = {
    "login_user": None,
    "logout_user": None,

    "enroll_course": [
                        ("single", "has_completed_prerequisites", {"username": "username", "course_code": "course_code"}),
                        ("single", "within_registration_period", None),
                        ("single", "course_has_capacity", {"course_code": "course_code"}),
                        ("single", "credits_within_limit", {"username": "username", "course_code": "course_code"}),
                        ("single", "no_schedule_conflict", {"username": "username", "course_code": "course_code"}), 
                        ("single", "meets_division_requirements", {"username": "username", "course_code": "course_code"}),
                        ("single", "course_not_completed", {"username": "username", "course_code": "course_code"}),
                        ("single", "no_exam_conflict", {"username": "username", "course_code": "course_code"}),
                        ("single", "meets_major_restriction", {"username": "username", "course_code": "course_code"}),
                    ],

    "drop_course": [
                        ("single", "maintains_min_credits", {"username": "username", "course_code": "course_code"}),
                        ("single", "within_withdrawal_period", None),
                    ],
    "request_graduation":  [
                            ("single", "major_requirements_met", {"username": "username"}),
                            ("single", "gen_ed_requirements_met", {"username": "username"}),
                            ("single", "credit_requirement_met", {"username": "username"}),
                            ("single", "gpa_requirement_met", {"username": "username"}),
                            ("single", "tuition_balance_zero", {"username": "username"}),
                            ("single", "before_graduation_deadline", None),
                            ("single", "not_on_probation", {"username": "username"}),
                        ],
    "change_major":  [
                        ("single", "meets_major_gpa_requirement", {"username": "username", "new_major": "new_major"}),
                        ("single", "within_major_change_period", None),
                        ("single", "under_max_major_changes", {"username": "username"}),
                        ("single", "has_min_credits_for_major_change",{"username": "username"}),
                        ("single", "major_has_capacity", {"new_major": "new_major"}),
                    ],
    "declare_minor":  [
                        ("single", "minor_compatible_with_major", {"username": "username", "minor": "minor"}),
                        ("single", "under_max_minors", {"username": "username"}),
                        ("single", "minor_course_overlap_check", {"username": "username", "minor": "minor"}),
                        ("single", "meets_minor_gpa_requirement", {"username": "username", "minor": "minor"}),
                        ("single", "meets_minor_prerequisites", {"username": "username", "minor": "minor"}),
                        ("single", "within_minor_declaration_period", None),


                        
                    ],
    "apply_financial_aid":  [
                            ("single", "meets_half_time_enrollment", {"username": "username"}),
                            ("single", "financial_aid_quota_available", {"username": "username"}),
                            ("single", "not_on_probation", {"username": "username"}),
                            ("single", "meets_min_gpa_for_aid", {"username": "username"}),
                            ("single", "meets_income_requirements", {"username": "username"}),
                            ("single", "valid_residency_status", {"username": "username"}),
                        ],


    "internal_check_username_exists": None,
    "internal_check_course_exists": None,
    "internal_get_academic_calendar": None,
    "internal_get_course_info": None,
    "internal_get_student_info": None,
    "internal_get_major_info": None,
    "internal_get_interaction_time": None,
    "internal_get_minor_info": None,
    "internal_check_major_exists": None,
    "internal_check_minor_exists": None,
    "internal_get_database":        None,
    "internal_get_number_of_students_for_major": None,
}


positive_constraint_descriptions = {
    "logged_in_user":               "The user is logged in previously with the correct credentials to perform this action.",
    "internal_check_username_exists":"The user parameter key \"{username}\" **MUST EXIST** as a top-level key in the accounts section of the database.",
    "internal_check_course_exists": "The course parameter key \"{course_code}\" must exist in the course section of the database",
    "internal_check_major_exists": "The major parameter \"{major}\" **MUST EXIST** in the majors section of the database",
    "internal_check_minor_exists": "The minor parameter \"{minor}\" **MUST EXIST** in the minors section of the database",
    "login_user":                   "The user is able to login with the correct credentials of \"{username}\" and \"{password}\" to perform this action,"\
        + " matching the database credentials.",


    "has_completed_prerequisites": "The student \"{username}\" **MUST HAVE** completed all prerequisite courses listed for the course \"{course_code}\" in order to enroll.",
    "within_registration_period": "The current interaction time **MUST FALL** within the academic registration period as defined in the academic calendar.",
    "course_has_capacity": "The course \"{course_code}\" **MUST HAVE** available seats remaining (enrolled < capacity).",
    "credits_within_limit": "The total credits for the student \"{username}\" after enrolling in course \"{course_code}\" **MUST NOT EXCEED** the maximum credit limit of {max_credits_per_quarter}.",
    "no_schedule_conflict": "The schedule of the course \"{course_code}\" **MUST NOT OVERLAP** with any of the student's existing enrolled courses.",
    "meets_division_requirements": "The student \"{username}\" **MUST HAVE** at least 90 completed credits to enroll in an upper-division course.",
    "course_not_completed": "The course \"{course_code}\" **MUST NOT** already be completed by the student \"{username}\".",
    "no_exam_conflict": "The exam schedule for course \"{course_code}\" **MUST NOT CONFLICT** with any of the student's other enrolled course exam times.",
    "major_requirements_met": "The student \"{username}\" **MUST HAVE COMPLETED** all required courses for their declared major.",
    "gen_ed_requirements_met": "The student \"{username}\" **MUST HAVE COMPLETED** at least 10 general education courses (course codes starting with 'GEN').",
    "credit_requirement_met": "The student \"{username}\" **MUST HAVE COMPLETED** at least {graduation_credit_requirement} total credits to graduate.",
    "gpa_requirement_met": "The student \"{username}\" **MUST HAVE** a GPA greater than or equal to the minimum required GPA of {min_gpa_graduation} to graduate.",
    "tuition_balance_zero": "The tuition balance for student \"{username}\" **MUST BE ZERO OR LESS** in order to proceed with graduation.",
    "before_graduation_deadline": "The current interaction time **MUST BE BEFORE** the official graduation deadline in the academic calendar.",
    "not_on_probation": "The student \"{username}\" **MUST NOT BE** on academic probation in order to perform this action.",
    "meets_half_time_enrollment": "The student \"{username}\" **MUST BE ENROLLED** in at least 6 credits to qualify as half-time enrolled.",
    "financial_aid_quota_available": "The number of quarters the student \"{username}\" has received financial aid **MUST BE LESS THAN** the maximum allowed ({max_financial_aid_quarters}).",
    "meets_major_gpa_requirement": "The GPA of student \"{username}\" **MUST BE GREATER THAN OR EQUAL TO** the minimum GPA required for the new major \"{new_major}\".",
    "within_major_change_period": "The current interaction time **MUST FALL** before or on the major change deadline in the academic calendar.",
    "under_max_major_changes": "The student \"{username}\" **MUST HAVE** made fewer than {max_major_changes} major changes in total.",
    "minor_compatible_with_major": "The chosen minor \"{minor}\" **MUST BE COMPATIBLE** with the student’s current major.",
    "under_max_minors": "The student \"{username}\" **MUST HAVE DECLARED FEWER THAN** {max_minors} minors in total.",
    "minor_course_overlap_check":  "The number of overlapping required courses between \"{minor}\" minor and the student's major **MUST NOT EXCEED** {max_overlap_minor_major}.",
    "meets_minor_gpa_requirement": "The student's GPA **MUST MEET OR EXCEED** the \"{minor}\" minor's minimum requirement.",
    "meets_minor_prerequisites": "The student **MUST HAVE COMPLETED** all prerequisite courses for \"{minor}\".",
    "within_minor_declaration_period": "The current interaction time **MUST FALL** before the minor declaration date in the academic calendar.",
    "has_min_credits_for_major_change": "The student \"{username}\" **MUST HAVE** completed at least {min_credits_major_change} credits to be eligible for a major change.",
    "major_has_capacity": "The target major \"{new_major}\" **MUST HAVE** available capacity (current enrolled students < defined capacity limit) to accept new change requests. The capacity of the major is found in the major field.",
    "meets_min_gpa_for_aid": "The student \"{username}\" **MUST HAVE** a minimum GPA of {min_gpa_financial_aid} to qualify for financial aid",
    "meets_income_requirements": "The student \"{username}\" **MUST HAVE** an annual income under {max_income_financial_aid} to be eligible for aid",
    "valid_residency_status": "The student \"{username}\" **MUST BE** either in-state or public school graduate residency status",
    "meets_major_restriction": "The student \"{username}\" **MUST BE** in a major allowed by the course \"{course_code}\" major restrictions.",

    "maintains_min_credits": "After dropping course \"{course_code}\", student \"{username}\" **MUST RETAIN** at least {min_credits_drop} credits (current credits - course credits)",
    "within_withdrawal_period": "Current interaction time **MUST BE BEFORE** the withdrawal deadline in academic calendar",
    "course_enrolled_by_user": "Student \"{username}\" **MUST BE CURRENTLY ENROLLED** in course \"{course_code}\""
    
}

negative_constraint_descriptions = {
    "logged_in_user":               "The user is not logged in previously with the correct credentials to perform this action.",
    "internal_check_username_exists":"The user parameter key \"{username}\" **MUST NOT EXIST** as a top-level key in the accounts section of the database.",
    "internal_check_course_exists": "The course parameter key \"{course_code}\" must not exist in the course section of the database",
    "internal_check_major_exists": "The major parameter \"{major}\" **MUST NOT EXIST** in the majors section of the database",
    "internal_check_minor_exists": "The minor parameter \"{minor}\" **MUST NOT EXIST** in the minors section of the database",
    "login_user":                   "The user **must not be able to login** with the correct credentials of \"{username}\" and \"{password}\" to perform this action,"\
        + " **not matching** the database credentials.",

    "has_completed_prerequisites": "The student \"{username}\" **HAS NOT COMPLETED** all prerequisite courses required for \"{course_code}\".",
    "within_registration_period": "The current time **IS OUTSIDE** the official academic registration period.",
    "course_has_capacity": "The course \"{course_code}\" **HAS REACHED** its maximum capacity and has no available seats.",
    "credits_within_limit": "Enrolling in course \"{course_code}\" would cause student \"{username}\" to **EXCEED** the maximum allowed credits ({max_credits_per_quarter}) this quarter.",
    "no_schedule_conflict": "The schedule for course \"{course_code}\" **CONFLICTS** with another course the student \"{username}\" is already enrolled in.",
    "meets_division_requirements": "The student \"{username}\" **DOES NOT MEET** the credit requirement (90 credits) to take upper-division courses.",
    "course_not_completed": "The student \"{username}\" has **ALREADY COMPLETED** the course \"{course_code}\".",
    "no_exam_conflict": "The exam for course \"{course_code}\" **CONFLICTS** with the exam of another enrolled course for student \"{username}\".",
    "major_requirements_met": "The student \"{username}\" **HAS NOT COMPLETED** all required courses for their declared major.",
    "gen_ed_requirements_met": "The student \"{username}\" **HAS COMPLETED FEWER THAN** 10 general education courses (prefix 'GEN').",
    "credit_requirement_met": "The student \"{username}\" **HAS NOT COMPLETED** the required number of credits ({graduation_credit_requirement}) to graduate.",
    "gpa_requirement_met": "The GPA of student \"{username}\" **IS BELOW** the minimum graduation requirement of {min_gpa_graduation}.",
    "tuition_balance_zero": "The student \"{username}\" **HAS AN OUTSTANDING TUITION BALANCE** that must be cleared before proceeding.",
    "before_graduation_deadline": "The current date **IS PAST** the graduation deadline.",
    "not_on_probation": "The student \"{username}\" **IS CURRENTLY ON** academic probation and cannot perform this action.",
    "meets_half_time_enrollment": "The student \"{username}\" **IS ENROLLED IN FEWER THAN** 6 credits and does not meet half-time enrollment.",
    "financial_aid_quota_available": "The student \"{username}\" **HAS ALREADY USED** the maximum allowed quarters of financial aid ({max_financial_aid_quarters}).",
    "meets_major_gpa_requirement": "The GPA of student \"{username}\" **IS BELOW** the minimum required to change to the major \"{new_major}\".",
    "within_major_change_period": "The current time **IS AFTER** the major change deadline in the academic calendar.",
    "under_max_major_changes": "The student \"{username}\" **HAS EXCEEDED** the allowed number of major changes ({max_major_changes}).",
    "minor_compatible_with_major": "The selected minor \"{minor}\" **MUST BE INCOMPATIBLE** with the student’s current major.",
    "under_max_minors": "The student \"{username}\" **HAS ALREADY DECLARED** the maximum allowed number of minors ({max_minors}).",
    "minor_course_overlap_check":  "The number of overlapping required courses between \"{minor}\" minor and the student's major **MUST EXCEED** {max_overlap_minor_major}.",
    "meets_minor_gpa_requirement": "The student's GPA **MUST NOT EXCEED** the  \"{minor}\" minor's minimum requirement.",
    "meets_minor_prerequisites": "The student **MUST HAVE NOT COMPLETED** all prerequisite courses for  \"{minor}\".",
    "within_minor_declaration_period": "The current interaction time **MUST FALL** after the minor declaration date in the academic calendar.",
    "has_min_credits_for_major_change": "The student \"{username}\" **MUST NOT HAVE** completed at least {min_credits_major_change} credits to be eligible for a major change.",
    "major_has_capacity": "The target major \"{new_major}\" **MUST NOT HAVE** available capacity (current enrolled students >= defined capacity limit) to accept new change requests. The capacity of the major is found in the major field.",
    "meets_min_gpa_for_aid": "The student \"{username}\" **MUST HAVE** a GPA GREATER THAN {min_gpa_financial_aid} to qualify for financial aid",
    "meets_income_requirements":  "The student \"{username}\" **MUST HAVE** an annual income over {max_income_financial_aid} to be eligible for aid",
    "valid_residency_status": "The student \"{username}\" **MUST NOT BE** in-state or public school graduate residency status",
    "meets_major_restriction": "The student \"{username}\" **MUST NOT BE** in a major allowed by the course \"{course_code}\" major restrictions.",

    "maintains_min_credits": "After dropping course \"{course_code}\", student \"{username}\" **MUST RETAIN** less than {min_credits_drop} credits (current credits - course credits)",
    "within_withdrawal_period": "Current interaction time **MUST BE AFTER** the withdrawal deadline in academic calendar",
    "course_enrolled_by_user": "Student \"{username}\" **MUST BE NOT CURRENTLY ENROLLED** in course \"{course_code}\""

    
}



constraint_links = {
    "logged_in_user":   ("login_user", {"username": "username"}),
}

constraint_dependencies = {
    "has_completed_prerequisites":      ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_course_exists", {"course_code": "course_code"}),
                                        ]),
    "within_registration_period":       None,
    "course_has_capacity":              ("single", "internal_check_course_exists", {"course_code": "course_code"}),
    "credits_within_limit":             ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_course_exists", {"course_code": "course_code"}),
                                        ]),
    "no_schedule_conflict":             ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_course_exists", {"course_code": "course_code"}),
                                        ]),
    "meets_division_requirements":      ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_course_exists", {"course_code": "course_code"}),
                                        ]),
    "course_not_completed":              ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_course_exists", {"course_code": "course_code"}),
                                        ]),
    "no_exam_conflict":                 ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_course_exists", {"course_code": "course_code"}),
                                        ]),
    "major_requirements_met":           ("single", "internal_check_username_exists", {"username": "username"}),
    "gen_ed_requirements_met":          ("single", "internal_check_username_exists", {"username": "username"}), #edit
    "credit_requirement_met":           ("single", "internal_check_username_exists", {"username": "username"}),
    "gpa_requirement_met":              ("single", "internal_check_username_exists", {"username": "username"}),
    "tuition_balance_zero":             ("single", "internal_check_username_exists", {"username": "username"}),
    "before_graduation_deadline":       None,
    "not_on_probation":                 ("single", "internal_check_username_exists", {"username": "username"}),
    "meets_half_time_enrollment":       ("single", "internal_check_username_exists", {"username": "username"}),
    "financial_aid_quota_available":    ("single", "internal_check_username_exists", {"username": "username"}),
    "meets_major_gpa_requirement":      ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_major_exists", {"major": "new_major"}),
                                        ]),
    "within_major_change_period":       None,
    "under_max_major_changes":          ("single", "internal_check_username_exists", {"username": "username"}),
    "minor_compatible_with_major":      ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_minor_exists", {"minor": "minor"}),
                                        ]),
    "under_max_minors":                 ("single", "internal_check_username_exists", {"username": "username"}),
    "minor_course_overlap_check":       ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_minor_exists", {"minor": "minor"}),
                                        ]),
    "meets_minor_gpa_requirement":      ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_minor_exists", {"minor": "minor"}),
                                        ]),
    "meets_minor_prerequisites":        ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_minor_exists", {"minor": "minor"}),
                                        ]),
    "within_minor_declaration_period":  None,
    "has_min_credits_for_major_change": ("single", "internal_check_username_exists", {"username": "username"}),
    "major_has_capacity": ("single", "internal_check_major_exists", {"major": "new_major"}),
    "meets_min_gpa_for_aid": ("single", "internal_check_username_exists", {"username": "username"}),
    "meets_income_requirements": ("single", "internal_check_username_exists", {"username": "username"}),
    "valid_residency_status":("single", "internal_check_username_exists", {"username": "username"}),
    "meets_major_restriction": ("and", [
                                            ("single", "internal_check_username_exists", {"username": "username"}),
                                            ("single", "internal_check_course_exists", {"course_code": "course_code"}),
                                        ]),

    "maintains_min_credits": ("and", [
        ("single", "internal_check_username_exists", {"username": "username"}),
        ("single", "internal_check_course_exists", {"course_code": "course_code"})
    ]),
    "within_withdrawal_period": None,
    "course_enrolled_by_user": ("single", "internal_check_username_exists", {"username": "username"})
}


constraint_processes = {
    "has_completed_prerequisites": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_course_info", {"course_code": "course_code"})
    ]),
    "within_registration_period": ("and", [
        ("single", "internal_get_academic_calendar", None),
        ("single", "internal_get_interaction_time", None)
    ]),
    "course_has_capacity": ("single", "internal_get_course_info", {"course_code": "course_code"}),
    "credits_within_limit": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_course_info", {"course_code": "course_code"})
    ]),
    "no_schedule_conflict": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_course_info", {"course_code": "course_code"})
    ]),
    "meets_division_requirements": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_course_info", {"course_code": "course_code"})
    ]),
    "course_not_completed": ("single", "internal_get_student_info", {"username": "username"}),
    "no_exam_conflict": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_course_info", {"course_code": "course_code"})
    ]),

    "major_requirements_met": ("single", "internal_get_student_info", {"username": "username"}),
    "gen_ed_requirements_met": ("single", "internal_get_student_info", {"username": "username"}),
    "credit_requirement_met": ("single", "internal_get_student_info", {"username": "username"}),
    "gpa_requirement_met": ("single", "internal_get_student_info", {"username": "username"}),
    "tuition_balance_zero": ("single", "internal_get_student_info", {"username": "username"}),
    "before_graduation_deadline": ("and", [
        ("single", "internal_get_academic_calendar", None),
        ("single", "internal_get_interaction_time", None)
    ]),
    "not_on_probation": ("single", "internal_get_student_info", {"username": "username"}),

    "meets_half_time_enrollment": ("single", "internal_get_student_info", {"username": "username"}),
    "financial_aid_quota_available": ("single", "internal_get_student_info", {"username": "username"}),

    "meets_major_gpa_requirement": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_major_info", {"major": "new_major"})
    ]),
    "within_major_change_period": ("and", [
        ("single", "internal_get_academic_calendar", None),
        ("single", "internal_get_interaction_time", None)
    ]),
    "under_max_major_changes": ("single", "internal_get_student_info", {"username": "username"}),

    "minor_compatible_with_major": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_minor_info", {"minor": "minor"})
    ]),
    "under_max_minors": ("single", "internal_get_student_info", {"username": "username"}),
    "minor_course_overlap_check": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_minor_info", {"minor": "minor"}),
        ("single", "internal_get_major_info", {"major": "major"})
    ]),
    "meets_minor_gpa_requirement": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_minor_info", {"minor": "minor"})
    ]),
    "meets_minor_prerequisites": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_minor_info", {"minor": "minor"})
    ]),
    "within_minor_declaration_period": ("and", [
        ("single", "internal_get_academic_calendar", None),
        ("single", "internal_get_interaction_time", None)
    ]),

    "internal_check_major_exists": ("single", "internal_check_major_exists", {"major": "major"}),
    "internal_check_minor_exists": ("single", "internal_check_minor_exists", {"minor": "minor"}),
    "has_min_credits_for_major_change": ("single", "internal_get_student_info", {"username": "username"}),
    "major_has_capacity": ("and", [
        ("single", "internal_get_major_info", {"major": "new_major"}),
        ("single", "internal_get_number_of_students_for_major", {"major": "new_major"}),
    ]),
    "meets_min_gpa_for_aid": ("single", "internal_get_student_info", {"username": "username"}),
    "meets_income_requirements": ("single", "internal_get_student_info", {"username": "username"}),
    "valid_residency_status":("single", "internal_get_student_info", {"username": "username"}),
    "meets_major_restriction": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_course_info", {"course_code": "course_code"})
    ]),
    "maintains_min_credits": ("and", [
        ("single", "internal_get_student_info", {"username": "username"}),
        ("single", "internal_get_course_info", {"course_code": "course_code"})
    ]),
    "within_withdrawal_period": ("and", [
        ("single", "internal_get_academic_calendar", None),
        ("single", "internal_get_interaction_time", None)
    ]),
    "course_enrolled_by_user": ("single", "internal_get_student_info", {"username": "username"})
}

action_param_descriptions = {
    "username": "A string representing the student's unique identifier in the system",
    "password": "[REDACTED] student's secret authentication credential",
    "course_code": "Alphanumeric code identifying a course (e.g. 'CS101')",
    "new_major": "Name of the academic major program to switch to",
    "minor": "Name of the academic minor program to declare",
    "meal_plan": "Type of dining package (options: 'basic', 'premium')",
    "major": "Name of an academic major program offered by the university"
}

actions = [
    {
        "name": "login_user",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns, "login_user"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "password": [REDACTED]
                    "type": "string",
                    "description": action_param_descriptions["password"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "password"]
        }
    },
    {
        "name": "logout_user",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns, "logout_user"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string", 
                    "description": action_param_descriptions["username"]
                }
            },
            "additionalProperties": False,
            "required": ["username"]
        }
    },
    {
        "name": "enroll_course",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns, "enroll_course"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "course_code": {
                    "type": "string",
                    "description": action_param_descriptions["course_code"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "course_code"]
        }
    },
    {
        "name": "drop_course",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns, "drop_course"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "course_code": {
                    "type": "string",
                    "description": action_param_descriptions["course_code"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "course_code"]
        }
    },
    {
        "name": "request_graduation",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns, "request_graduation"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                }
            },
            "additionalProperties": False,
            "required": ["username"]
        }
    },
    {
        "name": "apply_financial_aid",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns, "apply_financial_aid"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                }
            },
            "additionalProperties": False,
            "required": ["username"]
        }
    },
    {
        "name": "change_major",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns, "change_major"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "new_major": {
                    "type": "string",
                    "description": action_param_descriptions["new_major"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "new_major"]
        }
    },
    {
        "name": "declare_minor",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns, "declare_minor"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "minor": {
                    "type": "string",
                    "description": action_param_descriptions["minor"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "minor"]
        }
    },
    # Internal Actions
    {
        "name": "internal_check_username_exists",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns, "internal_check_username_exists"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                }
            },
            "additionalProperties": False,
            "required": ["username"]
        }
    },
    {
        "name": "internal_check_course_exists",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns, "internal_check_course_exists"),
        "parameters": {
            "type": "object",
            "properties": {
                "course_code": {
                    "type": "string",
                    "description": action_param_descriptions["course_code"]
                }
            },
            "additionalProperties": False,
            "required": ["course_code"]
        }
    },
    {
        "name": "internal_get_student_info",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_student_info"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                }
            },
            "additionalProperties": False,
            "required": ["username"]
        }
    },
    {
        "name": "internal_get_course_info",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_course_info"),
        "parameters": {
            "type": "object",
            "properties": {
                "course_code": {
                    "type": "string",
                    "description": action_param_descriptions["course_code"]
                }
            },
            "additionalProperties": False,
            "required": ["course_code"]
        }
    },
    {
        "name": "internal_get_academic_calendar",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_academic_calendar"),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": []
        }
    },
    {
        "name": "internal_get_major_info",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_major_info"),
        "parameters": {
            "type": "object",
            "properties": {
                "major": {
                    "type": "string",
                    "description": action_param_descriptions["major"]
                }
            },
            "additionalProperties": False,
            "required": ["major"]
        }
    },
    {
        "name": "internal_get_minor_info",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_minor_info"),
        "parameters": {
            "type": "object",
            "properties": {
                "minor": {
                    "type": "string",
                    "description": action_param_descriptions["minor"]
                }
            },
            "additionalProperties": False,
            "required": ["minor"]
        }
    },
    {
        "name": "internal_check_minor_exists",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns, "internal_check_minor_exists"),
        "parameters": {
            "type": "object",
            "properties": {
                "minor": {
                    "type": "string",
                    "description": action_param_descriptions["minor"]
                }
            },
            "additionalProperties": False,
            "required": ["minor"]
        }
    },
    {
        "name": "internal_check_major_exists",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns, "internal_check_major_exists"),
        "parameters": {
            "type": "object",
            "properties": {
                "major": {
                    "type": "string",
                    "description": action_param_descriptions["major"]
                }
            },
            "additionalProperties": False,
            "required": ["major"]
        }
    },
    {
        "name": "internal_get_interaction_time",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_interaction_time"),
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": []
        }
    },
    {
        "name": "internal_get_database",
        "description": get_action_full_description(action_descriptions, action_returns,"internal_get_database"),
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": []
        }
    },
    {
        "name": "internal_get_number_of_students_for_major",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_number_of_students_for_major"),
        "parameters": {
            "type": "object",
            "properties": {
                "major": {
                    "type": "string",
                    "description": action_param_descriptions["major"]
                }
            },
            "additionalProperties": False,
            "required": ["major"]
        }
    },
]
