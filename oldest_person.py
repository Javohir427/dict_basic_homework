def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    s = 0
    for i in people.values():
        if i>s:
            s=i
    return (s)
        
    

print(oldest({"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}))