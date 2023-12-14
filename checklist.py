class ChecklistItem:
    def __init__(self, identifier, description, deduction):
        self.identifier = identifier
        self.description = description
        self.deduction = deduction
        self.is_checked = False

    def toggle_check(self):
        self.is_checked = not self.is_checked

    def get_deduction(self):
        return self.deduction if self.is_checked else 0


def create_checklist():
    return [
        ChecklistItem(
            "1", "-10; Should not be able to access /protected without login.", 10),
        ChecklistItem(
            "2", "-10; Should not be able to access /admin without login.", 10),
        ChecklistItem(
            "3a", "-5; /register page should have no HTML validation errors.", 5),
        ChecklistItem(
            "3b-i", "-2; /register form should have id 'registration-form'.", 2),
        ChecklistItem(
            "3b-ii", "-2; /register should have a first name input with id and name 'firstNameInput', type text.", 2),
        ChecklistItem(
            "3b-iii", "-2; /register should have a last name input with id and name 'lastNameInput', type text.", 2),
        ChecklistItem(
            "3b-iv", "-2; /register should have an email input with id and name 'emailAddressInput', type email.", 2),
        ChecklistItem(
            "3b-v", "-2; /register should have a password input with id and name 'passwordInput', type password.", 2),
        ChecklistItem(
            "3b-vi", "-2; /register should have a confirm password input with id and name 'confirmPasswordInput', type password.", 2),
        ChecklistItem(
            "3b-vii", "-2; /register should have a role input with id and name 'roleInput'.", 2),
        ChecklistItem(
            "3c", "-5; /register should block account creation with invalid credentials.", 5),
        ChecklistItem(
            "3d", "-10; Password must be hashed in the database for account creation on /register.", 10),
        ChecklistItem(
            "3e", "-10; /register should block account creation with the same username in different cases.", 10),
        ChecklistItem(
            "3f", "-0; Create a second account for admin role on /register.", 0),
        ChecklistItem(
            "4a", "-5; /login page should have no HTML validation errors.", 5),
        ChecklistItem(
            "4b-i", "-3; /login form should have id 'login-form'.", 3),
        ChecklistItem(
            "4b-ii", "-3; /login should have an email input with id and name 'emailAddressInput', type email.", 3),
        ChecklistItem(
            "4b-iii", "-3; /login should have a password input with id and name 'passwordInput', type password.", 3),
        ChecklistItem(
            "4c", "-10; Valid login on /login should create a cookie and log the user in.", 10),
        ChecklistItem(
            "5", "-5; After authentication, /login should redirect to /protected.", 5),
        ChecklistItem(
            "6", "-5; After authentication, /register should redirect to /protected.", 5),
        ChecklistItem(
            "7", "-5; After authentication, / should redirect to /protected.", 5),
        ChecklistItem(
            "8a", "-5; /protected page should have no HTML validation errors.", 5),
        ChecklistItem(
            "8b", "-3; /protected page should display the user's first and last name.", 3),
        ChecklistItem(
            "8c", "-3; /protected page should not have a link to the admin page.", 3),
        ChecklistItem(
            "9", "-10; Logout link should expire/delete the cookie, logging the user out.", 10),
        ChecklistItem("10", "-0; Login with admin credentials.", 0),
        ChecklistItem(
            "11", "-5; After admin login, /login should redirect to /admin.", 5),
        ChecklistItem(
            "12", "-5; After admin login, /register should redirect to /admin.", 5),
        ChecklistItem(
            "13", "-5; After admin login, / should redirect to /admin.", 5),
        ChecklistItem(
            "14a", "-5; /admin page should have no HTML validation errors.", 5),
        ChecklistItem(
            "14b", "-3; /admin page should display the user's first and last name.", 3),
        ChecklistItem(
            "14c", "-3; /admin page should have a link to the protected page.", 3),
        ChecklistItem(
            "15a", "-10; Admin should be able to access /protected page.", 10),
        ChecklistItem(
            "15b", "-3; /protected page should have a link to the admin page.", 3),
        ChecklistItem("16", "-0; Logout functionality as admin.", 0),
        ChecklistItem(
            "17a", "-10; /login should block login with bad credentials.", 10),
        ChecklistItem(
            "17b", "-0; Logout if login with bad credentials was successful.", 0),
        ChecklistItem(
            "17c", "-5; Users should be able to login with valid credentials on /login.", 5),
        ChecklistItem("18", "-10; Middleware must log in the terminal.", 10)
    ]


def log_errors(checklist):
    with open("log.txt", "w") as log_file:
        for item in checklist:
            if item.is_checked:
                log_file.write(
                    f"{item.description}\n")


def calculate_final_grade(checklist, total_points=100):
    return total_points - sum(item.get_deduction() for item in checklist)


def display_checklist(checklist):
    print("\nChecklist:")
    for item in checklist:
        status = "[X]" if item.is_checked else "[ ]"
        print(f"{item.identifier}. {status} {item.description}")


def main():
    checklist = create_checklist()
    checklist_dict = {item.identifier: item for item in checklist}

    while True:
        display_checklist(checklist)
        choice = input(
            "\nEnter item identifier to toggle check (or 'done' to finish): ").strip()

        if choice.lower() == 'done':
            break
        elif choice in checklist_dict:
            checklist_dict[choice].toggle_check()
        else:
            print("Invalid input. Please enter a valid identifier or 'done'.")

    log_errors(checklist)
    final_grade = calculate_final_grade(checklist)
    print(f"\nFinal Grade: {final_grade}")


if __name__ == "__main__":
    main()
