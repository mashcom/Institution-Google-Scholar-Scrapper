from prettytable import PrettyTable
from src.ScholarlyInstitution import ScholarlyInstitution
from progress.spinner import Spinner
from scholarly import scholarly
import csv

if __name__ == "__main__":

    institution_name = "Midlands State University" #input("Type the Institution Name? ")
    print("+----------------------------------------------------------------------------------------------------+")
    print("|    Institution Google Scholar Scrapper by Blessing Mashoko                                         |\n".upper())
    print("|    This process my take long, so grab a cup of coffee :-)                                          |")
    print("|    Institution: " + institution_name.upper() + "                                                   |")
    print("+----------------------------------------------------------------------------------------------------+\n\n")

    scholarlyInstitution = ScholarlyInstitution(institution_name)
    link = scholarlyInstitution.get_institution_link()
    if link is None:
        print("Institution not found")
        exit()
    print("Found: " + link)

    csv_table_header = ['Id', 'Name', 'Interests']
    csv_body = []
    table = PrettyTable(csv_table_header)
    table.align = "l"
    affiliates = scholarlyInstitution.get_institution_affiliates(link)
    for affiliate in affiliates:
        affiliate_id = affiliate.id
        author_name = affiliate.name
        author_interests = ','.join(affiliate.interests)
        processed_affiliate_row = [affiliate_id, author_name, author_interests]
        csv_body.append(processed_affiliate_row)
        table.add_row(processed_affiliate_row)
    print(table)

    filename = "output/"+ institution_name+" Affiliates.csv"

    # writing to csv file  
    with open(filename, 'w', newline="") as csvfile:
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)

        # writing the fields  
        csvwriter.writerow(csv_table_header)

        # writing the data rows  
        csvwriter.writerows(csv_body)
