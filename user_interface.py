from insured_person import InsuredPerson
from registry import InsuredPersonsRegistry

class UserInterface:
    def __init__(self):
        """Initialize the UserInterface with a new InsuredPersonsRegistry instance"""
        self.registry = InsuredPersonsRegistry()

    # Pauza pro uživatele, pokračuje po stisku klávesy Enter
    def pause(self):
        """
        Pause program until user presses Enter key
        Clear the console after pause
        """
        input("\nPokračujte stisknutím klávesy Enter...")
        self.clear_console()

    # Vyčištění konzole výpisem prázdných řádků
    def clear_console(self):
        """Clear the console by printing 100 new lines"""
        print("\n" * 100)

    # Metoda pro načtení řetězce od uživatele
    def get_string_input(self, prompt):
        """
        Get validated string input from user
        Args:
            prompt (str): The prompt message to display
        Returns:
            str: The validated input string or None if validation fails
        Validation rules:
            - Input cannot be empty
            - Maximum length is 50 characters
        """
        text = input(prompt).strip()

        # Pokud je řetězec prázdný, ukončí se funkce a vrátí None
        if not text:
            self.clear_console()
            print("Vstupní pole nesmí být prázdné.")
            return None

        # Pokud je délka řetězce větší než 50, ukončí se funkce a vrátí None
        if len(text) > 50:
            self.clear_console()
            print("Maximální délka vstupu je 50 znaků.")
            return None

        return text

    # Metoda pro načtení číselné hodnoty
    def get_number_input(self, prompt):
        """
        Get validated integer input from user
        Args:
            prompt (str): The prompt message to display
        Returns:
            int: The validated number or None if input is not numeric
        """
        number = input(prompt).strip()

        if not number.isdigit():
            print("Zadejte prosím platné číslo.")
            return None

        return int(number)

    # Metoda pro načtení telefonního čísla
    def get_phone_input(self, prompt):
        """
        Get validated phone number input from user
        Args:
            prompt (str): The prompt message to display
        Returns:
            str: The validated phone number (digits only) or None if invalid
        Validation rules:
            - Can contain only digits
        """
        phone = self.get_string_input(prompt)

        # Pokud telefon neobsahuje pouze číslice, vrátí None
        if phone is None or not phone.isdigit():
            print("Zadejte platné telefonní číslo (pouze číslice).")
            return None

        return phone

    # Metoda pro načtení věku
    def get_age_input(self, prompt):
        """
        Get validated age input from user
        Args:
            prompt (str): The prompt message to display
        Returns:
            int: The validated age (1-150) or None if invalid
        """
        age = self.get_number_input(prompt)

        # Pokud je věk mimo rozmezí 1 až 150, vrátí None
        if age is None or not (1 <= age <= 150):
            print("Zadejte prosím věk v rozmezí 1 až 150 let.")
            return None

        return age

    # Přidání nového pojištěnce
    def add_insured_person(self):
        """
        Add a new insured person to the registry
        Guides user through input process for:
        - First name
        - Last name
        - Age
        - Phone number
        Validates all inputs before creating new InsuredPerson
        """
        first_name = self.get_string_input("Zadejte jméno: ")
        if first_name is None: return

        last_name = self.get_string_input("Zadejte příjmení: ")
        if last_name is None: return

        age = self.get_age_input("Zadejte věk: ")
        if age is None: return

        phone = self.get_phone_input("Zadejte telefonní číslo: ")
        if phone is None: return

        # Vytvoření a přidání pojištěnce do evidence
        insured = InsuredPerson(first_name, last_name, age, phone)
        self.registry.add_insured_person(insured)
        print(f"Pojištěnec {first_name} {last_name} byl úspěšně přidán.")
        self.pause()

    # Výpis všech pojištěnců
    def list_insured_persons(self):
        """
        Display all insured persons in the registry
        Handles case when registry is empty
        Shows formatted list of all insured persons
        """
        try:
            insured_list = self.registry.display_insured_persons()
            print("\n--- Seznam pojištěnců ---")
            for insured in insured_list:
                print(insured)
        except ValueError as e:
            self.clear_console()
            print(f"{e}")
        self.pause()

    # Vyhledávání pojištěnců podle jména, příjmení, nebo telefonu v libovolném pořadí
    def search_insured_persons(self):
        """
        Search for insured persons by name, surname or phone number
        Supports partial matches and case-insensitive search
        Displays search results or "not found" message
        """
        # Zkontrolujeme, zda existují nějací pojištěnci
        try:
            self.registry.display_insured_persons()
        except ValueError:
            self.clear_console()
            print("\nNení evidován žádný pojištěnec.")
            self.pause()
            return

        print("\n--- Vyhledat pojištěnce ---")
        search_text = self.get_string_input("Zadejte jméno, příjmení nebo telefon: ")
        if not search_text:
            print("Nebyl zadán žádný hledaný výraz.")
            self.pause()
            return

        results = self.registry.search_by_text(search_text)

        print("\n--- Výsledek vyhledávání ---")
        if not results:
            print("Nenalezen žádný pojištěnec.")
        else:
            for insured in results:
                print(insured)

        self.pause()

    # Hlavní smyčka programu – zobrazuje menu a zpracovává volbu uživatele
    def run(self):
        """
        Display menu options and handle user choices:
        1. Add new insured person
        2. List all insured persons
        3. Search insured persons
        4. Exit program
        Validate menu choices
        """
        choice = ""
        while choice != "4":
            print("\n--- Evidence pojištěnců ---")
            print("1. Přidat nového pojištěnce")
            print("2. Vypsat všechny pojištěnce")
            print("3. Vyhledat pojištěnce")
            print("4. Konec\n")
            choice = input("Zadejte možnost (1–4): ").strip()

            if choice == "1":
                print("\n--- Přidat nového pojištěnce ---")
                self.add_insured_person()
            elif choice == "2":
                print("\n--- Vypsat všechny pojištěnce ---")
                self.list_insured_persons()
            elif choice == "3":
                print("\n--- Vyhledat pojištěnce ---")
                self.search_insured_persons()
            elif choice == "4":
                self.clear_console()
                print("\nUkončuji program...")
            else:
                self.clear_console()
                print("Neplatná volba. Zkuste to znovu.\n")