from prettytable import PrettyTable
from src.ScholarlyInstitution import ScholarlyInstitution
from progress.spinner import Spinner

if __name__ == "__main__":

    print("**************************************************************")
    print("|    Institution Google Scholar Scrapper by Blessing Mashoko |\n".upper())
    print("|    This process my take long, so grab a cup of coffee :-)  |")
    print("**************************************************************")

    scholarlyInstitution = ScholarlyInstitution("Midlands State University")
    link = scholarlyInstitution.get_institution_link()

    affiliates = scholarlyInstitution.get_institution_affiliates(link)
    table = PrettyTable(['Id', 'Name', 'Interests'])
    table.align = "l"
    for affiliate in affiliates:
        affiliate_id = affiliate.id
        author_name = affiliate.name
        author_interests = ','.join(affiliate.interests)
        table.add_row([affiliate_id, author_name, author_interests])
    print(table)
