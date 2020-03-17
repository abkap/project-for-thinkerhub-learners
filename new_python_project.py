#python program for trch learners and mentors
class Tech_learners_and_mentors :
    def __init__(self,n,lm,t,i):
        self.name = n
        self.lernerormentor = lm
        self.time = t
        self.interest = i
    def addStack(self):
        print(f'{self.name} has interest in {self.interest}')
    def setMentorOrLearner(self):
        if self.lernerormentor == "learner" :
            print(f'{self.name} is learner')
        else :
            print(f'{self.name} is a mentor')
    def AvailableTime(self):
        if self.lernerormentor == "learner" :
            print(f'{self.name} has no available time as a mentor')
        else :
            print(f'{self.name} has available time at {self.time}')

    def getMentor(self):
        if self.lernerormentor == "learner" :
            print(f'{self.name} is not a mentor ')
        else :
            print(f'{self.name} is  available  mentor')


p1 = Tech_learners_and_mentors(i="python",n="Abhishek",lm="learner",t=10.31)
p1.addStack()
p1.setMentorOrLearner()
p1.AvailableTime()
p1.getMentor()
