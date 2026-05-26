types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_doubles(current_tickets, clear_tickets):
    unique_tickets = []
    for ticket in current_tickets:
        if ticket not in clear_tickets:
            unique_tickets.append(ticket)
            clear_tickets.append(ticket)
    return unique_tickets

def create_severity_tickets_dict(types_dict, tickets_dict):
    result = {}
    clear_tickets = []
    for i in range(1, 6):
        
        if i in tickets_dict:
            unique_list = delete_doubles(tickets_dict[i], clear_tickets)
            severity_name = types_dict[i]
            result[severity_name] = unique_list
        
    return result