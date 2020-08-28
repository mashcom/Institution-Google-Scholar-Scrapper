from prettytable import PrettyTable
from src.ScholarlyInstitution import ScholarlyInstitution
from progress.spinner import Spinner

if __name__ == "__main__":

    institution_name ="Midlands State University"# input("Type the Institution Name? ")
    print("**************************************************************")
    print("|    Institution Google Scholar Scrapper by Blessing Mashoko |\n".upper())
    print("|    This process my take long, so grab a cup of coffee :-)  |")
    print("|    Institution: " + institution_name + "                      |")
    print("**************************************************************")

    scholarlyInstitution = ScholarlyInstitution(institution_name)
    link = scholarlyInstitution.get_institution_link()
    if link is None:
        print("Institution not found")
        exit()
    print(link)
    affiliates = scholarlyInstitution.get_institution_affiliates(link)

    table = PrettyTable(['Id', 'Name', 'Interests'])
    table.align = "l"
    for affiliate in affiliates:
        affiliate_id = affiliate.id
        author_name = affiliate.name
        author_interests = ','.join(affiliate.interests)
        table.add_row([affiliate_id, author_name, author_interests])
    print(table)
