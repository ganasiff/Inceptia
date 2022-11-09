from modules.state_machine import ChatBot

NO_OF_TRYOUTS = 3
try_outs_or=0
try_outs_dr=0
bot = ChatBot("Snowy")
#Initial bot status
status = bot.init_check()

while bot.state != 'final':

    if bot.state == "wheater check":
        bot.check_weather()
    
    if bot.state == 'welcome':
        status = bot.welcome_message()
    
    if bot.state == 'order request':
        status = bot.request_order()
    
    if bot.state == 'order process':
        status = bot.process_order()
        if bot.state == 'order process':
            if try_outs_or >= NO_OF_TRYOUTS:
                bot.end()
            else:
                #No. of retries exit condition
                try_outs_or=try_outs_or+1
                #Backs 1 State in order to list available prods
                bot.request_order()

    if bot.state == 'discount request':
        bot.request_discount()
        if bot.state == 'discount request':
            if try_outs_dr >= NO_OF_TRYOUTS:
                bot.end()
            else:
                #No. of retries exit condition
                try_outs_dr=try_outs_dr+1

    if bot.state == 'discount validation':
        bot.end()
