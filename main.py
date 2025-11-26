from storage import load_data, save_data
from gradebook import Gradebook

def menu():
    print("\n===== Student Gradebook CLI =====")
    print("1. Add course")
    print("2. Update course")
    print("3. Delete course")
    print("4. View gradebook")
    print("5. Calculate GPA")
    print("6. GPA by semester")
    print("0. Exit")

def main():
    data = load_data()
    gb = Gradebook(data)

    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            gb.add_course()
        elif choice == "2":
            gb.update_course()
        elif choice == "3":
            gb.delete_course()
        elif choice == "4":
            gb.view_courses()
        elif choice == "5":
            gb.calculate_gpa()
        elif choice == "6":
            gb.calculate_gpa_by_semester()
        elif choice == "0":
            save_data(data)
            print("💾 Data saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
