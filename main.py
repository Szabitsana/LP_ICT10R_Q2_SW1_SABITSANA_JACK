from pyscript import document, when

club_members = [
    "jack sabitsana",
    "kaizen sy",
    "arturo santos",
    "lucas sarte",
    "marli roxas"
]

@when("submit", "#member-form")
def candidate_checker(e):
    e.preventDefault()

    f_name = document.getElementById("first_name").value.strip()
    l_name = document.getElementById("last_name").value.strip()

    candidate = f"{f_name} {l_name}"
    result = document.getElementById("result")

    if candidate.lower() in club_members:
        result.innerHTML = (
            f"You are a member of Varsity Voys, {candidate}!"
        )
        result.style.backgroundColor = "#d9f5e5"
        result.style.color = "#176b3a"
    else:
        result.innerHTML = (
            f"Sorry, {candidate}. Your name is not on the list."
        )
        result.style.backgroundColor = "#e3f2fd"
        result.style.color = "#1565c0"