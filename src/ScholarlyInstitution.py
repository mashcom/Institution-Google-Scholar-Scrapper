from scholarly import scholarly
from bs4 import BeautifulSoup
import requests


class ScholarlyInstitution:
    INSTITUTION_BASE_URL = "https://scholar.google.com/scholar?q="
    institution_name = None

    def __init__(self, institution_name):
        if institution_name is not None:
            self.institution_name = institution_name
        else:
            exit('Please provide the instition name')

    def get_institution_link(self):

        url = self.INSTITUTION_BASE_URL + self.institution_name
        page = requests.get(url)
        institution_link = None
        if page.status_code >= 200 or page.status_code <= 299:
            soup = BeautifulSoup(page.text, 'html.parser')
            institution = soup.find_all("div", class_="gs_ob_inst_r")

            for div in institution:
                institution_link = div.find('a')['href']
        return institution_link

    def get_url_param(self, url, parameter_name):

        query = requests.utils.urlparse(url).query
        params = dict(x.split('=') for x in query.split('&'))
        parameter_found = params[parameter_name]
        return parameter_found

    def get_institution_affiliates(self, link):

        url = "https://scholar.google.com" + link
        organisation_id = self.get_url_param(url, 'org')
        affiliates = []
        can_progress = True
        i = 0
        while can_progress:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            profiles = soup.find_all("h3", class_="gs_ai_name")
            try:
                next_page = soup.find("button", class_="gsc_pgn_pnx")['onclick']
            except:
                can_progress = False
                print("The are no more records to get")

            if next_page is not None:
                split_next_page_link = next_page.split('\\')
                target_start_author_raw = split_next_page_link[len(split_next_page_link) - 3]
                after_author_param = target_start_author_raw.replace('x3d', '')
                astart = i * 10
                next_url = "https://scholar.google.com/citations?view_op=view_org&hl=en&org=" + organisation_id + "&after_author=" + after_author_param + "&astart=" + astart.__str__()
                url = next_url
                print("Following Link => "+next_url)
                for div in profiles:
                    profile_link = div.find('a')['href']
                    profile_name = div.find('a').contents[0]
                    extracted_author_id = self.get_url_param(profile_link, 'user')
                    author_details = scholarly.search_author_id(extracted_author_id)
                    affiliates.append(author_details)
                i += 1

        return affiliates
