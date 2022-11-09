from transitions import Machine
from .geo_api import GeoAPI
from .product_stock import list_products, is_product_available
from .validate_discount_code import validate_discount_code

class ChatBot(object):

    #States that define the behaviour of the bot
    states = ['initial',
        'wheater check',
        'welcome',
        'order request',
        'order process',
        'discount request',
        'discount validation',
        'order confirmation',
        'final']

    def __init__(self, name):

        # Descriptive name for the chatbot
        self.name = name

        # Initialize the state machine
        #self.machine = Machine(model=self, states=ChatBot.states, initial='initial',after_state_change='show_state') #For logic debug
        self.machine = Machine(model=self, states=ChatBot.states, initial='initial')

        #Initial Transition
        self.machine.add_transition(trigger='init_check', source='initial',
                        dest='wheater check')
        
        #Wheater Check
        self.machine.add_transition('check_weather', 'wheater check', 'welcome',
                        before=['get_weather_n_welcome'])

        #Welcome message
        self.machine.add_transition('welcome_message', 'welcome', 'order request')

        #Ask to user prod n quantity
        self.machine.add_transition('request_order', ['order request','order process'],'order process',
                        before=['list_product'])

        #Process of user's order request
        self.machine.add_transition('process_order', 'order process', 'discount request',
                        conditions=['product_request'])


        #Prompt for discount
        self.machine.add_transition('request_discount','discount request','discount validation',
                        conditions=['val_disc'],after=['msg_order_process_ok'])#Space for discoount validation
        
        #Discount Validate
        self.machine.add_transition('end',['discount validation','order process','discount request'],'final',
                        after=['msg_goodbye'])

        # What have we accomplished today?
        #self.consumers_attended = 0        

        # Reset Transition - for daily use
        # self.machine.add_transition(trigger='restart', source='*', dest='initial',
        #                 after='reset')

    def product_request(self):
        """
            Requests Input from user and checks if there is product available 
        """
        print("Por favor seleccione el sabor")
        user_input_flavor = input("Quiero el sabor $: ")
        print("Por favor seleccione la cantidad")
        user_input_quantity = input("Numero de bochas? $: ")

        return is_product_available(user_input_flavor,user_input_quantity)

    def get_weather_n_welcome(self):
        """
            Checks for weather in Specific Location to make welcome message
        """
        try:
            if GeoAPI.is_hot_in_pehuajo():
                print("----Bienvenid@ a Heladería Frozen!----\nCon este calor merece un helado!")
            else:
                print("----Bienvenid@ a Heladería Frozen!----\nQue tenga un muy bien dia.")
        except:
            pass
    
    def list_product(self):
        print(list_products())
    
    def msg_order_process_ok(self):
        print("\nSu pedido fue realizado con exito!")

    def msg_goodbye(self):
        print("\nGracias por visitarnos, vuelva pronto!")

    def val_disc(self):
        """
            Requests Input from user and checks if discount code is ok
        """
        print("Por favor ingrese código de descuento")
        return validate_discount_code(input("$: "))

    def msg_prod_req_error(self):
        print ("-------Por favor revisa tu pedido----------")

    def show_state(self):
        """
            Shows the bot current state change
        """
        print (f"El estado del bot paso a: {self.state}")
    
    # def reset(self):
    #     print(f"Consumers attended so far: {self.consumers_attended}")
    #     self.consumers_attended=0
    #     print("Reset Done")