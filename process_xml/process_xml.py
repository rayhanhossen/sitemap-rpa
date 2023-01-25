from xml.dom import minidom
from datetime import date


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
        lastmod_value = root.createTextNode("2023-01-20T10:51:49")
        lastmod.appendChild(lastmod_value)
        home.appendChild(lastmod)

        # xhtml element
        xhtml = root.createElement('xhtml:link')
        xhtml.setAttribute('rel', 'alternate')
        xhtml.setAttribute('hreflang', 'en')
        xhtml.setAttribute('href', '')
        home.appendChild(xhtml)

    def blog_page(self, root, xml):
        # home page
        home = root.createElement('url')
        xml.appendChild(home)

        # loc element
        loc = root.createElement('loc')
        loc_value = root.createTextNode(f"{self.conf['site_host']}/blog")
        loc.appendChild(loc_value)
        home.appendChild(loc)

        # lastmod element
        lastmod = root.createElement('lastmod')
        lastmod_value = root.createTextNode("2023-01-20T10:51:49")
        lastmod.appendChild(lastmod_value)
        home.appendChild(lastmod)

        # xhtml element
        xhtml = root.createElement('xhtml:link')
        xhtml.setAttribute('rel', 'alternate')
        xhtml.setAttribute('hreflang', 'en')
        xhtml.setAttribute('href', '')
        home.appendChild(xhtml)

    def franchise_page(self, root, xml):
        # home page
        home = root.createElement('url')
        xml.appendChild(home)

        # loc element
        loc = root.createElement('loc')
        loc_value = root.createTextNode(f"{self.conf['site_host']}/franchise")
        loc.appendChild(loc_value)
        home.appendChild(loc)

        # lastmod element
        lastmod = root.createElement('lastmod')
        lastmod_value = root.createTextNode("2023-01-20T10:51:49")
        lastmod.appendChild(lastmod_value)
        home.appendChild(lastmod)

        # xhtml element
        xhtml = root.createElement('xhtml:link')
        xhtml.setAttribute('rel', 'alternate')
        xhtml.setAttribute('hreflang', 'en')
        xhtml.setAttribute('href', '')
        home.appendChild(xhtml)

    def about_us_page(self, root, xml):
        # home page
        home = root.createElement('url')
        xml.appendChild(home)

        # loc element
        loc = root.createElement('loc')
        loc_value = root.createTextNode(f"{self.conf['site_host']}/about-us")
        loc.appendChild(loc_value)
        home.appendChild(loc)

        # lastmod element
        lastmod = root.createElement('lastmod')
        lastmod_value = root.createTextNode("2023-01-20T10:51:49")
        lastmod.appendChild(lastmod_value)
        home.appendChild(lastmod)

        # xhtml element
        xhtml = root.createElement('xhtml:link')
        xhtml.setAttribute('rel', 'alternate')
        xhtml.setAttribute('hreflang', 'en')
        xhtml.setAttribute('href', '')
        home.appendChild(xhtml)

    def career_page(self, root, xml):
        # home page
        home = root.createElement('url')
        xml.appendChild(home)

        # loc element
        loc = root.createElement('loc')
        loc_value = root.createTextNode(f"{self.conf['site_host']}/career")
        loc.appendChild(loc_value)
        home.appendChild(loc)

        # lastmod element
        lastmod = root.createElement('lastmod')
        lastmod_value = root.createTextNode("2023-01-20T10:51:49")
        lastmod.appendChild(lastmod_value)
        home.appendChild(lastmod)

        # xhtml element
        xhtml = root.createElement('xhtml:link')
        xhtml.setAttribute('rel', 'alternate')
        xhtml.setAttribute('hreflang', 'en')
        xhtml.setAttribute('href', '')
        home.appendChild(xhtml)

    def location_page(self, root, xml):
        # home page
        home = root.createElement('url')
        xml.appendChild(home)

        # loc element
        loc = root.createElement('loc')
        loc_value = root.createTextNode(f"{self.conf['site_host']}/location")
        loc.appendChild(loc_value)
        home.appendChild(loc)

        # lastmod element
        lastmod = root.createElement('lastmod')
        lastmod_value = root.createTextNode("2023-01-20T10:51:49")
        lastmod.appendChild(lastmod_value)
        home.appendChild(lastmod)

        # xhtml element
        xhtml = root.createElement('xhtml:link')
        xhtml.setAttribute('rel', 'alternate')
        xhtml.setAttribute('hreflang', 'en')
        xhtml.setAttribute('href', '')
        home.appendChild(xhtml)

    def product_page(self, root, xml):
        # home page
        home = root.createElement('url')
        xml.appendChild(home)

        # loc element
        loc = root.createElement('loc')
        loc_value = root.createTextNode(f"{self.conf['site_host']}/products")
        loc.appendChild(loc_value)
        home.appendChild(loc)

        # lastmod element
        lastmod = root.createElement('lastmod')
        lastmod_value = root.createTextNode("2023-01-20T10:51:49")
        lastmod.appendChild(lastmod_value)
        home.appendChild(lastmod)

        # xhtml element
        xhtml = root.createElement('xhtml:link')
        xhtml.setAttribute('rel', 'alternate')
        xhtml.setAttribute('hreflang', 'en')
        xhtml.setAttribute('href', '')
        home.appendChild(xhtml)

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
            lastmod_value = root.createTextNode(str(data.get('LASTMOD').isoformat()))
            lastmod.appendChild(lastmod_value)
            home.appendChild(lastmod)

            # xhtml element
            xhtml = root.createElement('xhtml:link')
            xhtml.setAttribute('rel', 'alternate')
            xhtml.setAttribute('hreflang', 'en')
            xhtml.setAttribute('href', '')
            home.appendChild(xhtml)

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
            lastmod_value = root.createTextNode(str(data.get('LASTMOD').isoformat()))
            lastmod.appendChild(lastmod_value)
            home.appendChild(lastmod)

            # xhtml element
            xhtml = root.createElement('xhtml:link')
            xhtml.setAttribute('rel', 'alternate')
            xhtml.setAttribute('hreflang', 'en')
            xhtml.setAttribute('href', '')
            home.appendChild(xhtml)

    def create_xml(self, product_list, parent_cat_list, sub_cat_list):
        root = minidom.Document()

        # root element
        xml = root.createElement('urlset')
        xml.setAttribute('xmlns', "http://www.sitemaps.org/schemas/sitemap/0.9")
        xml.setAttribute('xmlns:xhtml', "http://www.w3.org/1999/xhtml")
        root.appendChild(xml)

        self.home_page(root, xml)
        self.product_page(root, xml)

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
            lastmod_value = root.createTextNode(str(data.get('LASTMOD').isoformat()))
            lastmod.appendChild(lastmod_value)
            url.appendChild(lastmod)

            # xhtml element
            xhtml = root.createElement('xhtml:link')
            xhtml.setAttribute('rel', 'alternate')
            xhtml.setAttribute('hreflang', 'en')
            xhtml.setAttribute('href', '')
            url.appendChild(xhtml)

        self.product_parent_category(root, xml, parent_cat_list)
        self.product_sub_category(root, xml, sub_cat_list)
        self.blog_page(root, xml)
        self.franchise_page(root, xml)
        self.about_us_page(root, xml)
        self.career_page(root, xml)
        self.location_page(root, xml)

        xml_str = root.toprettyxml(indent="\t", encoding="UTF-8")

        # working with date
        today = date.today()

        # open file and write the xml
        with open(f"../xml_files/sitemap_{today.year}{today.month}{today.day}.xml", "wb") as f:
            f.write(xml_str)
