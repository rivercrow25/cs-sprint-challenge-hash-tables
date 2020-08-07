#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    dct = {}
    route = []
    for ticket in tickets:
        dct[ticket.source] = ticket.destination

    i = 0
    start = "NONE"
    while i < length:
        route.append(dct[start])
        start = dct[start]
        i += 1

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, len(tickets)))
