class CallCenter:
    def __init__(self):
        self.queue = []

    def menu(self):
        print("===============")
        print("1) Add Call")
        print("2) Answer call")
        print("3) View Queue")
        print("4) Check if the Queue is empty")
        print("0) Exit")
        print("===============")

    def add_call(self):
        customer_id = input("Enter Customer ID: ")
        call_time = int(input("Enter call time: "))
        self.queue.append([customer_id, call_time])

    def answer_call(self):
        if not self.queue:
            print("No Calls Left to answer")
        else:
            call = self.queue.pop(0)
            print(f"Answered call with customer ID: {call[0]} for {call[1]} mins")

    def view_queue(self):
        print("Customer ID : Call Time")
        for call in self.queue:
            print(f"{call[0]} : {call[1]}")

    def check(self):
        if not self.queue:
            print("The Queue is Empty")
        else:
            print("The Queue is NOT Empty")

if __name__ == "__main__":
    cc = CallCenter()
    while True:
        cc.menu()
        choice = int(input("Enter Your choice: "))
        match choice:
            case 1:
                cc.add_call()
            case 2:
                cc.answer_call()
            case 3:
                cc.view_queue()
            case 4:
                cc.check()
            case 0:
                break
            case _:
                print("Error! Wrong Input")