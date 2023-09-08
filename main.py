class FiniteAutomaton:
    def __init__(self, filename):
        self.transitions = {}  # Словарь для хранения переходов
        self.start_state = None  # Начальное состояние
        self.accept_states = set()  # Множество конечных состояний

        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    source_state, symbol, target_state = parts
                    self.add_transition(source_state, symbol, target_state)
                elif len(parts) == 1:
                    state = parts[0]
                    if self.start_state is None:
                        self.start_state = state
                    self.add_accept_state(state)

    def add_transition(self, source_state, symbol, target_state):
        if source_state not in self.transitions:
            self.transitions[source_state] = {}
        if symbol not in self.transitions[source_state]:
            self.transitions[source_state][symbol] = []
        self.transitions[source_state][symbol].append(target_state)

    def add_accept_state(self, state):
        self.accept_states.add(state)

    def display_transition_table(self):
        print("Transition Table:")
        print("State | Symbol | Next State")
        print("-" * 27)

        for source_state, transitions in self.transitions.items():
            for symbol, target_states in transitions.items():
                for target_state in target_states:
                    print(f"{source_state:^6}|{symbol:^8}|{target_state:^11}")

    def is_accepted(self, string):
        current_state = self.start_state

        for symbol in string:
            if current_state in self.transitions and symbol in self.transitions[current_state]:
                # Переходим в следующее состояние по символу
                current_state = self.transitions[current_state][symbol][0]
            else:
                # Если нет перехода, то строка не принимается
                return False

        # Проверяем, является ли текущее состояние конечным
        return current_state in self.accept_states


# Пример использования:
if __name__ == "__main__":
    filename = "1"  # Путь к файлу с описанием автомата
    automaton = FiniteAutomaton(filename)
    automaton.display_transition_table()
    test_strings = ["abc", "abca", "ab", "a"]

    for string in test_strings:
        if automaton.is_accepted(string):
            print(f"Строка '{string}' принимается автоматом.")
        else:
            print(f"Строка '{string}' не принимается автоматом.")