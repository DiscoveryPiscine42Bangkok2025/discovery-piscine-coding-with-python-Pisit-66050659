def array_of_names(names_dict):
    return [
        f"{first.capitalize()} {last.capitalize()}"
        for first, last in names_dict.items()
    ]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))