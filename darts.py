import math
import random



class Dart:
    def __init__(self, mult, dart):
        self.multiplier = mult
        self.dart = dart
        self.result = mult * dart 
    def single_dart_des(self):
        if self.multiplier == 1:
            return "Single " + str(self.dart)
        elif self.multiplier == 2:
            return "Double " + str(self.dart)
        else:
            return "Treble " + str(self.dart)

class Round:
    def __init__(self) -> None:
        random.seed()
        self.d1 = Dart(random.randrange(1,4,1) ,random.randrange(1,21,1))
        self.d2 = Dart(random.randrange(1,4,1) ,random.randrange(1,21,1))
        self.d3 = Dart(random.randrange(1,4,1) ,random.randrange(1,21,1))
        self.score_after_dart1 = self.d1.result
        self.score_after_dart2 = self.d1.result + self.d2.result
        self.score_after_dart3 = self.d1.result + self.d2.result + self.d3.result
    def practice(self):
        print("Start Practice round")
        print(r.d1.single_dart_des())
        print("What is the running tally?")
        r1 = input()
        if(int(r1) == self.score_after_dart1):
            pass
        else:
            print('NOT correct. Expected Value: ' + str(self.score_after_dart1))
            return
        print(r.d2.single_dart_des())
        print("What is the running tally?")
        r2 = input()
        if(int(r2) == self.score_after_dart2):
            pass
        else:
            print('NOT correct. Expected Value: ' + str(self.score_after_dart2))
            return
        print(r.d3.single_dart_des())
        print("What is the running tally?")
        r3 = input()
        if(int(r3) == self.score_after_dart3):
            print("CORRECT")
        else:
            print('NOT correct Expected Value: ' + str(self.score_after_dart3))
            return
            

if __name__ == "__main__":
    r = Round()
    r.practice()
        
else:
    print("debug mode")