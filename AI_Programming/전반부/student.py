import abc #abstract base class (추상클래스를 만들기 위한 library)
class Student:
    def __init__(self, name="", midterm=0, final=0):
        self._name = name
        self._midterm = midterm
        self._final = final
      
    def setName(self, name):
        self._name = name

    def setMidterm(self, midterm):
        self._midterm = midterm

    def setFinal(self, final):
        self._final = final

    def getName(self):
        return self._name    
    
    # @ -> 데코레이터(자바에 어노테이션 같은 느낌인가)
    # cf @staticmethod ; 정적메소드 -> 불필요한 인스턴스 생성없이 불러오고 싶을때 사용(대신 함수 parameter에 self는 쓰지 않음, 관련 없기 때문)
    @abc.abstractmethod # 추상메서드나 클래스는 객체로 받을 수 없음
    def calcSemGrade(self):
        pass 
        
    def __str__(self):
        return self._name + "\t" + self.calcSemGrade()
     
class LGstudent(Student):
    SECRETNUMBER = 486
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

class PFstudent(Student):
        
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 60:
            return "Pass"
        else:
            return "Fail"


