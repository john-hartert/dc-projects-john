def user_info():
  bill = float(raw_input('What\'s the bill? '))
  return bill
def user_info1():  
  service = raw_input('How\'s service? ')
  return service
def user_info2():
  people = int(raw_input('How many people? '))
  return people
  split = 0


def service_bill_split(service, bill, people):
  if service == "good":
    print "That\'s great!"
    tip = bill * .20
    print "Here\'s the tip: $%.2f" % tip
    total = bill + tip
    print "Total amount: $%.2f" % total
    split = total / people
    print "Here\'s your total: $%.2f" % split
  elif service == "fair":
    print "Too bad..."
    tip = bill * .15
    print "Here\'s the tip: $%.2f" % tip
    total = bill + tip
    print "Total amount: $%.2f" % total
    split = total / people
    print "Here\'s your total: $%.2f" % split
  else:
    print "Get out of my restaurant!"
    tip = bill * .10
    print "Here\'s the tip: $%.2f" % tip
    total = bill + tip
    print "Total amount: $%.2f" % total
    split = total / people
    print "Here\'s your total: $%.2f" % split
  return [service, bill, people]

def main():
    bill = user_info()
    service = user_info1()
    people = user_info2()
    service_bill_split(service, bill, people)

main()