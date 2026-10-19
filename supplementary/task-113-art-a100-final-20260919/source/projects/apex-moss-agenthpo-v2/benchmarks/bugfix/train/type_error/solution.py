def build_label(name, age):
    """Return a label string like 'Name: Alice, Age: 30'."""
    label = "Name: " + name + ", Age: " + age  # BUG: age is int, needs str(age)
    return label
