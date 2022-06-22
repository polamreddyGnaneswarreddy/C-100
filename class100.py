class Car:
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.company=company
        self.model=model
        self.speed_limit=speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerate")
        "accelerator functionality here"
        
    def change_gear(self,gear_type):
        print("gear_changed")
        "gear related functionality here"        

                