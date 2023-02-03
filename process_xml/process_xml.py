from xml.dom import minidom
from datetime import date, datetime


class ProcessXML:
    def __init__(self, conf):
        self.conf = conf

    def home_page(self, root, xml):
        # home page
        home = root.createElement('url')
        xml.appendChild(home)

        # loc element
        loc = root.createElement('loc')
        loc_value = root.createTextNode(f"{self.conf['site_host']}/")
        loc.appendChild(loc_value)
        home.appendChild(loc)

        # lastmod element
        lastmod = root.createElement('lastmod')
        lastmod_value = root.createTextNode(str(date.today().strftime('%Y-%m-%d')))
        lastmod.appendChild(lastmod_value)
        home.appendChild(lastmod)

        # # xhtml element
        # xhtml = root.createElement('xhtml:link')
        # xhtml.setAttribute('rel', 'alternate')
        # xhtml.setAttribute('hreflang', 'en')
        # xhtml.setAttribute('href', '')
        # home.appendChild(xhtml)

    def product_details(self, root, xml, product_list):
        for data in product_list:
            # url element
            url = root.createElement('url')
            xml.appendChild(url)

            # loc element
            loc = root.createElement('loc')
            loc_value = root.createTextNode(f"{self.conf['site_host']}/product-details/{data.get('LOC')}")
            loc.appendChild(loc_value)
            url.appendChild(loc)

            # lastmod element
            lastmod = root.createElement('lastmod')
            lastmod_value = root.createTextNode(str(data.get('LASTMOD').strftime('%Y-%m-%d')))
            lastmod.appendChild(lastmod_value)
            url.appendChild(lastmod)

            # # xhtml element
            # xhtml = root.createElement('xhtml:link')
            # xhtml.setAttribute('rel', 'alternate')
            # xhtml.setAttribute('hreflang', 'en')
            # xhtml.setAttribute('href', '')
            # url.appendChild(xhtml)

    def product_parent_category(self, root, xml, parent_cat_list):
        for data in parent_cat_list:
            # home page
            home = root.createElement('url')
            xml.appendChild(home)

            # loc element
            loc = root.createElement('loc')
            loc_value = root.createTextNode(f"{self.conf['site_host']}/category/{data.get('LOC')}")
            loc.appendChild(loc_value)
            home.appendChild(loc)

            # lastmod element
            lastmod = root.createElement('lastmod')
            lastmod_value = root.createTextNode(str(data.get('LASTMOD').strftime('%Y-%m-%d')))
            lastmod.appendChild(lastmod_value)
            home.appendChild(lastmod)

            # # xhtml element
            # xhtml = root.createElement('xhtml:link')
            # xhtml.setAttribute('rel', 'alternate')
            # xhtml.setAttribute('hreflang', 'en')
            # xhtml.setAttribute('href', '')
            # home.appendChild(xhtml)

    def product_sub_category(self, root, xml, sub_cat_list):
        for data in sub_cat_list:
            # home page
            home = root.createElement('url')
            xml.appendChild(home)

            # loc element
            loc = root.createElement('loc')
            loc_value = root.createTextNode(f"{self.conf['site_host']}/sub-category/{data.get('LOC')}")
            loc.appendChild(loc_value)
            home.appendChild(loc)

            # lastmod element
            lastmod = root.createElement('lastmod')
            lastmod_value = root.createTextNode(str(data.get('LASTMOD').strftime('%Y-%m-%d')))
            lastmod.appendChild(lastmod_value)
            home.appendChild(lastmod)

            # # xhtml element
            # xhtml = root.createElement('xhtml:link')
            # xhtml.setAttribute('rel', 'alternate')
            # xhtml.setAttribute('hreflang', 'en')
            # xhtml.setAttribute('href', '')
            # home.appendChild(xhtml)

    def static_url(self, root, xml, route_list):
        for route in route_list:
            # home page
            home = root.createElement('url')
            xml.appendChild(home)

            # loc element
            loc = root.createElement('loc')
            loc_value = root.createTextNode(f"{self.conf['site_host']}/{route}")
            loc.appendChild(loc_value)
            home.appendChild(loc)

            # lastmod element
            lastmod = root.createElement('lastmod')
            lastmod_value = root.createTextNode(str(date.today().strftime('%Y-%m-%d')))
            lastmod.appendChild(lastmod_value)
            home.appendChild(lastmod)

            # # xhtml element
            # xhtml = root.createElement('xhtml:link')
            # xhtml.setAttribute('rel', 'alternate')
            # xhtml.setAttribute('hreflang', 'en')
            # xhtml.setAttribute('href', '')
            # home.appendChild(xhtml)

    def create_xml(self, product_list, parent_cat_list, sub_cat_list):
        root = minidom.Document()

        # root element
        xml = root.createElement('urlset')
        xml.setAttribute('xmlns', "http://www.sitemaps.org/schemas/sitemap/0.9")
        xml.setAttribute('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        xml.setAttribute('xsi:schemaLocation',
                         "http://www.sitemaps.org/schemas/sitemap/0.9http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd")
        root.appendChild(xml)

        self.home_page(root=root, xml=xml)
        self.static_url(root=root, xml=xml, route_list=['products'])
        self.product_details(root=root, xml=xml, product_list=product_list)
        self.product_parent_category(root=root, xml=xml, parent_cat_list=parent_cat_list)
        self.product_sub_category(root=root, xml=xml, sub_cat_list=sub_cat_list)
        route_list = [
            'blog',
            'franchise',
            'about-us',
            'career',
            'location'
        ]
        self.static_url(root=root, xml=xml, route_list=route_list)

        xml_str = root.toprettyxml(indent="\t", encoding="UTF-8")

        # working with date
        today = date.today()

        # open file and write the xml
        with open(f"../xml_files/hgs_sitemap_{today.year}{today.month}{today.day}.xml", "wb") as f:
            f.write(xml_str)

        return f"hgs_sitemap_{today.year}{today.month}{today.day}.xml"
