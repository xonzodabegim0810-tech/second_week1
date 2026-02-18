
class LibraryMember:
    library_name = "City Library"
    total_members = 0
    def __init__(self, name, member_id, borrowed=None):
        self.name = name 
        self.member_id = member_id
        #if borrowed is None:
        #    self.borrowed = []
        #else:
        #    self.borrowed = borrowed
        self.borrowed = borrowed if borrowed is not None else [] 
        LibraryMember.total_members += 1
    def borrowed_book(self, title):
        if title != "":
            self.borrowed.append(title)
            print(f"Borrowed: {title}")
    def return_book(self, title):
        if title in self.borrowed:
            self.borrowed.remove(title)
            print(f"Return: {title}")
        else:
            print("Book not found")
    def display_member(self):
        print(f"Member: {self.name} ({self.member_id}) at {self.library_name}")


member1 = LibraryMember("Aziza", "L-101")
member1.display_member()
member1.borrowed_book("1984")
member1.borrowed_book("Dune")
member1.return_book("Dune")
member2 = LibraryMember("Bekzod", "L-102")
member2.display_member()
member2.return_book("Foundation")
print(f"Total members: {LibraryMember.total_members}")

print()

#variant 2 Fitness class enrollment


class FitnessClass:
    gym_name = "Power Gym"
    max_capacity = 3
    total_classes = 0
    def __init__(self, class_name, instructor):
        self.class_name = class_name 
        self.instructor = instructor
        self.participants = []
        FitnessClass.total_classes += 1
    def add_participant(self, name):
        if len(self.participants) < FitnessClass.max_capacity:
            self.participants.append(name)
            print(f"Added {name} to {self.class_name}")
        else:
            print("Class is full")
    def remove_participant(self, name):
        if name in self.participants:
            self.participants.remove(name)
            print(f"Removed {name} from {self.class_name}")
        else:
            print("Participant not found")
    def display_class(self):
        print(f"Class: {self.class_name}, Instructor: {self.instructor}, Gym: {self.gym_name}")


class1 = FitnessClass("Yoga", "Malika")
class1.display_class()
class1.add_participant("Ali")
class1.add_participant("Vali")
class1.add_participant("Gulnora")
class1.add_participant("Rustam")
class1.remove_participant("Vali")
class1.remove_participant("Sarvar")
print(f"Total classes: {FitnessClass.total_classes}")