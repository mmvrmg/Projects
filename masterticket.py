#will be used to exit the program after it's done
import sys

#ticket price and service charge are constant so I assign them variables at the start
TICKET_PRICE = 10
SERVICE_CHARGE= 2

#calculates the total price of the tickets
def calculate_price(number_requested):
  pricetotal = (number_requested * TICKET_PRICE) + SERVICE_CHARGE
  return pricetotal

def main():
  #total tickets for sale 
  tickets_remaining = 100 

  #function will keep repeating until condition is met  
  while tickets_remaining:

    name = input('What is your name?\n')
    tickets_requested = input('How many tickets would you like:\n')

    #checks if there are still enough tickets
    try:
      tickets_requested = int(tickets_requested)
      if tickets_requested > tickets_remaining:
        raise ValueError("There are only {} tickets remaining".format(tickets_remaining))

    except ValueError as err:
      print("We ran into an issue. Please try again {}".format(err))

    else: 

      price = calculate_price(tickets_requested)
      
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
  #if there's no more tickets left then the program closes  
  print('sorry sold out')

main()