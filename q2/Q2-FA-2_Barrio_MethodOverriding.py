class Patient:
    def __init__(self, patient, bill_amount: float):
        self.patient = patient
        self.__bill_amount = bill_amount


    def get_name(self):
        return  self.patient
    
    def set_name(self):
        print ("Patient:", self.patient)

    def get_bill(self):
        return self.__bill_amount

    def set_bill(self):
        print("Original bill:", self.__bill_amount)
    

    def calculate(self):
        print("Final Bill:", self.__bill_amount)



class Senior_patient(Patient):
    def __init__(self, patient, bill_amount):
        self.patient = patient
        self.__bill_amount = bill_amount



    def set_bill(self):
        print("Original bill:", self.__bill_amount)

    def calculate2(self):
        print("Final Bill:", self.__bill_amount - (15000 * 0.2))

class PhilHealth_patient(Patient):
    def __init__(self, patient, bill_amount):
        self.patient = patient
        self.__bill_amount = bill_amount

    def set_bill(self):
        print("Original bill:", self.__bill_amount)
    
    def calculate3(self):
        print("Final Bill:", self.__bill_amount - (15000 * 0.15))





test = Patient("Juan", 15000)
test2 = Senior_patient("Bron", 15000)
test3 = PhilHealth_patient("Jordan", 15000)


test.set_name()
test.set_bill()
test.calculate()

test2.set_name()
test2.set_bill()
test2.calculate2()

test3.set_name()
test3.set_bill()
test3.calculate3()