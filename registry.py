from insured_person import InsuredPerson

class InsuredPersonsRegistry:
    def __init__(self):
        # Inicializace prázdného seznamu pro uložení pojištěných osob
        self.insured_persons = []

    def add_insured_person(self, insured_person):
        """Add a new insured person to the registry"""
        self.insured_persons.append(insured_person)

    def display_insured_persons(self):
        """Return all insured persons in the registry
        Raises ValueError if the registry is empty"""
        if not self.insured_persons:
            raise ValueError("Seznam pojištěnců je prázdný.")
        return self.insured_persons

    def search_by_text(self, search_text):
        """Search for insured persons matching the given text
        The search is case-insensitive and splits the input by commas/spaces"""
        input_keywords = search_text.lower().replace(",", " ").split()
        return [insured_person for insured_person in self.insured_persons
                if insured_person.match_input_keywords(input_keywords)]
