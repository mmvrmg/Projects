TICKET_PRICE = 10

tickets_remaining = 100 

print('there are {} tickets remaing'.format(tickets_remaining))

name = input('What is your name?  ')
tickets_requested = input('How many tickets would you like  ')

def calculate_total(amount_requested):
  return int(amount_requested) * TICKET_PRICE

price = ('The total price of the ticket you requested is {} \n'
         'Would you like to continue? [yes/no]  '.format(calculate_total(tickets_requested)))

print(price)


