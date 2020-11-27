import sys

TICKET_PRICE = 10

def main():

  tickets_remaining = 100 

  while tickets_remaining:

    name = input('What is your name?  ')
    tickets_requested = input('How many tickets would you like  ')

    try:
      tickets_requested = int(tickets_requested)
      if tickets_requested > tickets_remaining:
        raise ValueError("There are only {} tickets remaining".format(tickets_remaining))

    except ValueError as err:
      print("We ran into an issue. Please try again {}".format(err))

    else: 

      price = tickets_requested * TICKET_PRICE
      
      total = ('The total price of the ticket you requested is £{} \n'.format(price))
      print(total)
      choice = input('Would you like to continue? [yes/no]  ')

      if choice == 'yes':
        print('SOLD!')
        tickets_remaining -= tickets_requested
        thanks = print('Thank you for your purchase')
        print('There are {} tickets left'.format(tickets_remaining))
      else:
        exit_quote = print('Thank you anyway, {}!'.format(name))
        sys.exit()

  print('sorry sold out')

main()
