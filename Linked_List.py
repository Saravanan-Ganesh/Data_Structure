##Linked List
class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        self.head = None
   
    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr =  self.head
        llstr=''
        while itr:
            llstr +=str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def insert_values(self, data_list):
        self.head=None
        for i in data_list:
            self.insert_at_end(i)
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception ("Invalid index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
            
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception ("Invalid index")
        if index==0:
            self.insert_at_begining(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                
                itr=itr.next
                count+=1
    def insert_after_value(self, data_after,data_to_insert):
        if self.head is None:
            return
        if self.head.data==data_after:
            self.head.data= Node(data_to_insert,self.head.next)
            return
        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break
            itr=itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head= self.head.next
            return
        
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            itr=itr.next
            
if __name__ == '__main__':
    
    a=LinkedList()
    a.insert_at_begining(5)
    a.insert_at_begining(89)
    a.insert_at_begining(10)
    a.insert_at_begining("aa")
    a.insert_at_end(2000)
    a.insert_values(["Dairy milk","Kitkat","Munch","Milkybar","Lollypop","Candy"])
    print("Length:",a.get_length( ))
    a.remove_at(0)
    a.insert_at(1,"Germs")
    a.insert_at(2,"Bar-one")
    a.insert_after_value("Munch","Nestle")
    a.remove_by_value("Lollypop")
    a.print()
    a.remove_by_value("Kitkat")
    a.print()
    a.remove_by_value("Milkybar")
    a.print()

