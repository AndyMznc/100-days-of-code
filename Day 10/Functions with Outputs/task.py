def format_name(first_name, last_name):
    """Take a first and last name and format it to return the title case version of the name.

    Args:
        first_name (string): The first name
        last_name (string): The last name

    Returns:
        string: Return de first and last name formatted.
    """
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()

    return f"{formatted_first_name} {formatted_last_name}"


formatted_string = format_name("aNgElA", "yU")
print(formatted_string)
