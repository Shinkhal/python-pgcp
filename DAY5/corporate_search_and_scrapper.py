import re


def scrape_directory_phones(directory_text):

    pattern = re.compile(
        r"(?<!\d)"
        r"(?:"
        r"\((\d{3})\)\s+(\d{3})-(\d{4})"
        r"|"
        r"(\d{3})-(\d{3})-(\d{4})"
        r"|"
        r"(\d{3})(\d{3})(\d{4})"
        r")"
        r"(?!\d)"
    )

    results = []

    for match in pattern.finditer(directory_text):
        groups = match.groups()

        if groups[0] is not None:
            area_code = groups[0]
            prefix = groups[1]
            line_number = groups[2]

        elif groups[3] is not None:
            area_code = groups[3]
            prefix = groups[4]
            line_number = groups[5]

        else:
            area_code = groups[6]
            prefix = groups[7]
            line_number = groups[8]

        results.append({
            "area_code": area_code,
            "prefix": prefix,
            "line_number": line_number,
            "formatted": f"({area_code}) {prefix}-{line_number}"
        })

    return results

directory = (
    "Contact HR at 123-456-7890 or the helpdesk at "
    "(987) 654-3210. Direct line is 5558881234."
)

print(scrape_directory_phones(directory))
