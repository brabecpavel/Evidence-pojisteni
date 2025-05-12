class InsuredPerson:
    def __init__(self, first_name, last_name, age, phone):
        """Initialize an insured person with basic information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone

    def __str__(self):
        """String representation of the insured person"""
        return f"Jméno: {self.first_name}, Příjmení: {self.last_name}, Věk: {self.age}, Telefon: {self.phone}"

    def match_input_keywords(self, input_keywords):
        """Checks if all keywords match the person's data (name, surname or phone)

        Args:
            input_keywords: List of search terms (lowercase)

        Returns:
            boolean: True if all keywords are found in person's data
        """
        searchable_text = f"{self.first_name} {self.last_name} {self.phone}".lower()
        return all(keyword in searchable_text for keyword in input_keywords)
