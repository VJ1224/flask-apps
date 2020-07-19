# -*- coding: UTF-8 -*-
import sqlite3


def main():
    sql_connect = sqlite3.connect('business.db')
    cursor = sql_connect.cursor()

    try:
        create_query = "DROP TABLE 'employees'"
        cursor.execute(create_query)
        sql_connect.commit()
        print("Deleted table employees")
    except Exception as e:
        print(e)

    try:
        create_query = "CREATE TABLE 'employees' (`id` INTEGER PRIMARY KEY NOT NULL,`name` varchar(255) default NULL,`city` varchar(255),`country` varchar(100) default NULL)"  # noqa
        cursor.execute(create_query)
        sql_connect.commit()
        print("Created table employees")
    except Exception as e:
        print(e)

    try:
        insert_query = 'INSERT INTO "employees" (`name`,`city`,`country`) VALUES ("Cecilia Merritt","PiŽtrebais","Venezuela"),("Nyssa Sweeney","Warangal","Jersey"),("Jameson Daniel","Erpe","Cambodia"),("Hasad Cunningham","San José del Guaviare","Curaçao"),("Flynn Wood","Cunco","Guadeloupe"),("Garrett Walter","Kanchipuram","Slovakia"),("Kennedy Noble","Mundare","Albania"),("Stephen Horn","Rionero in Vulture","Dominican Republic"),("Gabriel Stout","Haverfordwest","Pitcairn Islands"),("Clark Whitney","Meißen","Belize"),("Cassady Herrera","Perchtoldsdorf","Uganda"),("Elijah Hahn","Tula","Maldives"),("Hermione Mcdowell","Montauban","Solomon Islands"),("Quentin Harris","General Escobedo","Belgium"),("Vaughan Barrera","Baisy-Thy","Morocco"),("Bertha Bowen","Lawton","Paraguay"),("Helen Golden","Marchihue","Cape Verde"),("Gil Dickson","New Sarepta","Latvia"),("Genevieve Mclaughlin","Cajazeiras","Haiti"),("Erasmus Holt","Jonesboro","Anguilla"),("Breanna Christian","Kawartha Lakes","Virgin Islands, British"),("Gary Mcknight","Halifax","Paraguay"),("Lewis Frederick","Bras","Cape Verde"),("Juliet Craig","Vidnoye","Bosnia and Herzegovina"),("Isaac George","Itagüí","Anguilla"),("Beatrice Hart","Contulmo","Equatorial Guinea"),("Kareem Alford","Jaboatão dos Guararapes","Papua New Guinea"),("Steven White","Serpukhov","Nicaragua"),("Lucian Mckenzie","Sart-Dames-Avelines","Bouvet Island"),("Cherokee Melendez","Tourinne","Bulgaria"),("Sylvia Burgess","Omaha","Guernsey"),("Cullen Albert","Regina","Iran"),("Ella Velez","Bellary","Bonaire, Sint Eustatius and Saba"),("Kendall Cross","Huelva","New Zealand"),("Brenna Camacho","Vitrival","Iran"),("Jessica Jarvis","Terme","Western Sahara"),("Kadeem Shields","Milmort","Madagascar"),("Adrian Rose","Athens","Svalbard and Jan Mayen Islands"),("Andrew Camacho","Tarvisio","Côte D\'Ivoire (Ivory Coast)"),("Fletcher Phelps","El Tabo","Qatar"),("Kitra Nunez","Cockburn","Brunei"),("Jael Page","Canmore","Estonia"),("Shafira Fulton","Arequipa","Cook Islands"),("Anthony Jacobson","Dietzenbach","Botswana"),("Bert Medina","Bosa","Belarus"),("Cruz Perkins","Jalna","Gibraltar"),("Kaden Rocha","Palayankottai","Belize"),("Josiah Pate","Rostock","Korea, North"),("Benedict Guerra","Annapolis Royal","Lithuania"),("Sloane Holland","Nelson","Sint Maarten"),("Driscoll Mendez","Abolens","Yemen"),("Myra Puckett","Ciudad Victoria","Malta"),("Rooney Craig","Buzenol","Mongolia"),("Tyler Atkins","Motta Visconti","Maldives"),("Jolie Holden","Orangeville","Mexico"),("Cheryl Morrison","Augsburg","Maldives"),("Teegan Madden","Bay Roberts","Mauritius"),("Amir Nelson","Walhain","Belize"),("Nelle Rasmussen","Jammu","Puerto Rico"),("Blaine Olson","Portofino","Turkmenistan"),("Adena May","Chekhov","Benin"),("Raymond Sweet","Canterano","Bhutan"),("Colton Ramsey","Rio Marina","Iran"),("Nadine Mullen","Iquitos","Ethiopia"),("Wade Everett","San Antonio","Greenland"),("Zeus Bush","Mombaruzzo","Grenada"),("Kenneth Craft","Chemnitz","Ethiopia"),("Mohammad Chambers","Sart-Dames-Avelines","Guatemala"),("Mira Edwards","San Carlos","United States Minor Outlying Islands"),("Donovan Benson","Lo Espejo","Monaco"),("Valentine Velasquez","Penna in Teverina","Saint Vincent and The Grenadines"),("Herman Massey","Yakhroma","Guatemala"),("Quintessa Randall","Bolton","Russian Federation"),("Clio Frazier","Alloa","Indonesia"),("Rahim Floyd","Shawville","Wallis and Futuna"),("Alice Castro","Somma Lombardo","Gambia"),("Emi Higgins","Sotteville-lès-Rouen","Thailand"),("Lance Hughes","Santarém","Armenia"),("Dennis Chen","Montoggio","American Samoa"),("Jade Whitaker","Leersum","United States"),("Madeline Hubbard","Kursk","Mexico"),("Oleg Graves","Saguenay","Mongolia"),("Dara Johnston","Sylvan Lake","Turkey"),("Doris Baker","Crehen","Luxembourg"),("Zephania Petty","Harelbeke","United States Minor Outlying Islands"),("Myra Johnson","Quillón","Bosnia and Herzegovina"),("Ayanna Dale","Portico e San Benedetto","Bangladesh"),("Kaden Foley","Voskresensk","Mauritania"),("Lane Odonnell","Lens-Saint-Remy","Senegal"),("Dante Beard","Montenero Val Cocchiara","Somalia"),("Maisie Head","Abaetetuba","Latvia"),("Amal Rivas","Asigliano Veneto","Wallis and Futuna"),("Brandon Erickson","Altamura","Bulgaria"),("Amos Ramsey","Aklavik","Argentina"),("Uriah Thompson","Móstoles","Israel"),("Ivan Blanchard","Kirkwall","Falkland Islands"),("Gannon Saunders","Walhain-Saint-Paul","Cayman Islands"),("Clementine Burton","Onoz","Lebanon"),("Xyla Finch","St. Albert","Liberia"),("Ulric Cline","Henderson","Jordan");'  # noqa
        cursor.execute(insert_query)
        sql_connect.commit()
        print("Inserted dummy data to table employees")
    except Exception as e:
        print(e)

    sql_connect.close()


if __name__ == '__main__':
    main()
