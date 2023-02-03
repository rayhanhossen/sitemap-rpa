from process_xml.process_xml import ProcessXML
from config.config import ConfigParser
from database.db_mysql import MySQLDatabase
from xml_to_csv.xml_to_csv_url import xml_to_csv

conf = ConfigParser().get_config()
db_obj = MySQLDatabase(conf)
db_obj.connect()

if __name__ == '__main__':
    # fetch product data from database
    product_select_query = "SELECT * FROM products WHERE isDeleted=0"
    product_db_data = db_obj.select_data_from_table(product_select_query)
    product_list = list()
    if len(product_db_data) > 0:
        for data in product_db_data:
            product_dict = {
                'LOC': data[31],
                'LASTMOD': data[2]
            }
            product_list.append(product_dict)

    # fetch product parent category data from db
    parent_cat_select_query = "SELECT * FROM product_parent_category WHERE isDeleted=0"
    parent_cat_db_data = db_obj.select_data_from_table(parent_cat_select_query)
    parent_cat_list = list()
    if len(parent_cat_db_data) > 0:
        for data in parent_cat_db_data:
            parent_cat_dict = {
                'LOC': data[4],
                'LASTMOD': data[2]
            }
            parent_cat_list.append(parent_cat_dict)

    process_xml = ProcessXML(conf)
    # generate xml file
    file_name = process_xml.create_xml(product_list=product_list, parent_cat_list=parent_cat_list)
    # generate xml to csv file
    xml_to_csv(file_name=file_name)
