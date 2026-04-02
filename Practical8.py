class SemanticNetwork:
    def __init__(self):
        self.facts = []

    def add_fact(self, sub, pred, obj):
        self.facts.append((sub, pred, obj))

    def query(self, sub, pred, obj):
        # Direct match
        if (sub, pred, obj) in self.facts:
            return True

        # Check inheritance (ISA relationship)
        for s, p, o in self.facts:
            if s == sub and p == "ISA":
                if self.query(o, pred, obj):
                    return True

        return False


# Create network
net = SemanticNetwork()

# Add facts
net.add_fact("Sparrow", "ISA", "Bird")
net.add_fact("Bird", "ISA", "Animal")
net.add_fact("Bird", "HAS", "Feathers")
net.add_fact("Animal", "CAN", "Breathe")
net.add_fact("Sparrow", "COLOR", "Brown")

# Test queries
test_queries = [
    ("Sparrow", "ISA", "Bird"),
    ("Sparrow", "ISA", "Animal"),
    ("Sparrow", "HAS", "Feathers"),
    ("Sparrow", "CAN", "Breathe"),
    ("Bird", "CAN", "Breathe")
]

# Execute queries
for sub, pred, obj in test_queries:
    result = net.query(sub, pred, obj)
    print(f"{sub} {pred} {obj} : {result}")