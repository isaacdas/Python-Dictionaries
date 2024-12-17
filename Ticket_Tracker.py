

def add_ticket(tickets, ticket):
    if ticket not in tickets:
        tickets[ticket] = {}
        print(f"{ticket} added")
    else:
        print(f"{ticket} already there")

def update_status(tickets, ticket, status):
    try:
        tickets[ticket]["Status"] = status
        print(f"{ticket} status: {status}")
    except KeyError:
        print("Ticket not found")

def display_tickets(tickets):
    for ticket, items in tickets.items():
        print(ticket,"-")
        for key, value in items.items():
            print(f"    {key}: {value}")


service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

add_ticket(service_tickets, "Ticket003")
update_status(service_tickets, "Ticket001", "closed" )
display_tickets(service_tickets)
