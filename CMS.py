
#All Global Variables
class Customer:
    list_cus=[]#Static Member it has only one memory blocks.
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mobile_no=""
        self.age=0
    def __str__(self):
        return "Id:{0},Name:{1},'Address:{2},Mobile No:{3},Age:{4}".format(self.id,self.name,self.address,self.mobile_no,self.age)

    def add_customer(self):
        Customer.list_cus.append(self)
    def search_customer(self,cus_id):
        for e in Customer.list_cus:
            if e.id==cus_id:
                self.id=e.id
                self.name=e.name
                self.address=e.address
                self.mobile_no=e.mobile_no
                self.age=e.age
                return True
        return False




# BLL Code Start from Here

   
def delete_customer(self,cus_id):
     for i in range(len(Customer.list_cus)):
        if Customer.list_cus[i].id==cus_id:
            Customer.list_cus.pop(i)
            return True
     return False
def update_customer(self,cus_id):
    for e in Customer.list_cus:
            if e.id==cus_id:
                e.id=self.id
                e.name=self.name
                e.address=self.address
                e.mobile_no=self.mobile_no
                e.age=self.age
                return True
    return False



# BLL Code Ends  Here
# PL Code Start from Here
def show_all_customer():
    for cus in Customer.list_cus:
        details="Id:{0},Name:{1},address:{2},mobile no:{3},age:{4}".format(cus.id,cus.name,cus.address,cus.mobile_no,cus.age)
        print(details)
# def show_all_customer():
#     for i in range(len(Customer.list_cus)):
#         details="Id:{0},Name:{1},address:{2},mobile no:{3},age:{4}".format(list_cus[i].id,list_cus[i].name,list_cus[i].address,list_cus[i].mobile_no,list_cus[i].age)
#         print(details)
while(True):
    print('1.Add Customer.\n2.Search Customer.\n3.Modify Customer.\n4.Delete Customer.\n5.Show All Customer.\n0.Exit')
    ch=input('Enter Your Choice')
    match ch:
    case '1':
        cus=Customer()
        cus.id=int(input('Enter id'))
        cus.name=input('Enter Name')
        cus.address=input('Enter Address')
        cus.mobile_no=input('Enter Mobile No')
        cus.age=int(input('Enter Age'))
        
        cus.add_customer()
        print('Customer Added Sucessfully')
        #Write code to add a customer
    case '2':
        cus=Customer()
        cus_id=int(input('Enter ID'))
        check=cus.search_customer(cus_id)
        if(check==False):
            print("Id Not Found")
        else:
            print("Id",cus.id,"Name",cus.name,"Address",cus.address,"Mobile No",cus.mobile_no,"Age",cus.age)

        
        #Write code to Search a customer
    case '3':
        cus=Customer()
        cus.id=int(input('Enter ID for update'))
        cus.name=input('Enter Name for Update')
        cus.address=input('Enter Address for Update')
        cus.mobile_no=input('Enter Mobile No for Update')
        cus.age=input('Enter Age for Update')
        check=cus.update_customer(cus.id)
        if(check==False):
            print("Id Not Found")
        else:
            print('Customer Updated Successfully')

        
        
        #Write code to Modify a customer
    case '4':
      
        id=int(input('Enter ID'))
        cus=Customer()
        check=cus.delete_customer(id)
        if(check==False):
            print("Id Not Found")
        else:
            print('Customer Deeted Sucessfully')

        
        #Write code to Delete a customer
    case '5':
        
        show_all_customer()
        #Write code to Show All a customer
    elif ch=='0':
        break
    case _:
        exit()
#Write code to Exit
# PL Code Ends  Here
