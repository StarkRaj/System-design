from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional


# ==============================================================================
# EXAMPLE 1: SUPPORT TICKET ESCALATION SYSTEM
# ==============================================================================

class Severity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Ticket:
    """
    Represents a customer support request with a specific severity level.
    """

    def __init__(self, title: str, severity: Severity):
        self.title = title
        self.severity = severity
        self.is_resolved = False


class SupportHandler(ABC):
    """
    Abstract Base Handler for the support chain.
    """

    def __init__(self):
        self._next_handler: Optional[SupportHandler] = None

    def set_next(self, handler: "SupportHandler") -> "SupportHandler":
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle_ticket(self, ticket: Ticket) -> None:
        pass

    def pass_to_next(self, ticket: Ticket) -> None:
        if self._next_handler:
            self._next_handler.handle_ticket(ticket)
        else:
            print(f"[-] No support tier could handle ticket '{ticket.title}' (Severity: {ticket.severity.name}). Escalated to Executive Operations.")


class Level1Support(SupportHandler):
    def handle_ticket(self, ticket: Ticket) -> None:
        if ticket.severity == Severity.LOW:
            print(f"[+] Level 1 Support resolved ticket: '{ticket.title}' (Simple inquiry/password reset).")
            ticket.is_resolved = True
        else:
            print(f"[>] Level 1 Support cannot handle '{ticket.title}' (Severity: {ticket.severity.name}). Escalating...")
            self.pass_to_next(ticket)


class Level2Support(SupportHandler):
    def handle_ticket(self, ticket: Ticket) -> None:
        if ticket.severity == Severity.MEDIUM:
            print(f"[+] Level 2 Support resolved ticket: '{ticket.title}' (Software configuration/troubleshooting).")
            ticket.is_resolved = True
        else:
            print(f"[>] Level 2 Support cannot handle '{ticket.title}' (Severity: {ticket.severity.name}). Escalating...")
            self.pass_to_next(ticket)


class Level3Support(SupportHandler):
    def handle_ticket(self, ticket: Ticket) -> None:
        if ticket.severity == Severity.HIGH:
            print(f"[+] Level 3 Support (Engineers) resolved ticket: '{ticket.title}' (Database optimization/bug fix).")
            ticket.is_resolved = True
        else:
            print(f"[>] Level 3 Support cannot handle '{ticket.title}' (Severity: {ticket.severity.name}). Escalating...")
            self.pass_to_next(ticket)


if __name__ == "__main__":
    print("=================================================================")
    print("RUNNING EXAMPLE 1: SUPPORT TICKET ESCALATION")
    print("=================================================================")
    # Constructing chain: Level 1 -> Level 2 -> Level 3
    l1 = Level1Support()
    l2 = Level2Support()
    l3 = Level3Support()
    l1.set_next(l2).set_next(l3)

    tickets = [
        Ticket("Reset my email password", Severity.LOW),
        Ticket("Unable to access internal portal", Severity.MEDIUM),
        Ticket("Production database queries are timing out", Severity.HIGH),
        Ticket("Cybersecurity breach detected / Ransomware", Severity.CRITICAL),
    ]

    for t in tickets:
        print(f"\nProcessing ticket: '{t.title}'")
        l1.handle_ticket(t)

    print("\n" + "=" * 65 + "\n")
