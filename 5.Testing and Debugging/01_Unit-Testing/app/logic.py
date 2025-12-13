def is_eligible_for_loan(income: float, age: int, employement_status: str) -> bool:
    """
    Determines if a person is eligible for a loan based on their income, age, and employment status.

    Args:
        income (float): The annual income of the person.
        age (int): The age of the person.
        employement_status (str): The employment status of the person. 
                                  Expected values are 'employed', 'unemployed'.

    Returns:
        bool: True if the person is eligible for a loan, False otherwise.
    """
    return (income >= 50000) and (age >= 21) and (employement_status == 'employed')