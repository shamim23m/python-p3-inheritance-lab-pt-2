class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")  # Correct capitalization

class ChattyStudent(Student):
    def hello(self):
        super().hello()  # Call the parent class's hello method
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! "
              "What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        for _ in range(10):  # Raise hand 10 times
            super().raise_hand()  # Correct capitalization here as well
