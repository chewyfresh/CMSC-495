'''
database.py stores fitness data for the cyberfitness application.
'''

import os
import pickle


class database(object):
    '''
    Stores user's fitness data for the cyberfitness application.
    '''
    
    def __init__(self, database_name, version):
        '''
        Initialize a database instance.
        
        :param database_name: Filename for the database.
        :param version: Version of the database.
        '''
        
        self.database_name = database_name
        self.version = version
    
    
    def create_table(self):
        '''
        Creates an empty database if the file does not
        already exist.
        '''
        
        if os.path.isfile(self.database_name + "." + self.version + ".db") == False:
            with open(self.database_name + "." + self.version + ".db", 'wb') as create_db:
                db_header = {'database_name': self.database_name, 'version': self.version}
                database = [db_header]
                pickle.dump(database, create_db)
    
    
    def add_user(self, username, password):
        '''
        Adds an user to the database. If user already exists,
        function return -1.
        
        :param username: Username.
        :param password: User's password.
        '''
        
        with open(self.database_name + "." + self.version + ".db", 'rb') as open_db:
            pickle_file = pickle.load(open_db)
            for i in pickle_file[1:]:
                if i.get('name') == username:
                    return -1   # Username already in use
        with open(self.database_name + "." + self.version + ".db", 'wb') as write_db:
            pickle_file.append({'name': username, 'password': password})
            pickle.dump(pickle_file, write_db)
    
    
    def db_insert(self, username, password, class_name, class_data):
        '''
        Inserts fitness data to user's database. Returns -1 if user does not exists.
        Currently does not handle if class_name already exists.
        
        :param username: Username.
        :param password: User's password.
        :param class_name: User's class name.
        :param class_data: User's class data contained in its own class.
        '''
        
        user_data = None
        with open(self.database_name + "." + self.version + ".db", 'rb') as open_db:
            pickle_file = pickle.load(open_db)
            for i in pickle_file[1:]:
                if i.get('name') == username:
                    if i.get('password') == password:
                        user_data = pickle_file
        if user_data == None:
            return -1
        for index, i in enumerate(pickle_file):
            if i.get('name') == username:
                pickle_file[index].update({class_name : class_data})
        with open(self.database_name + "." + self.version + ".db", 'wb') as write_db:
            pickle.dump(user_data, write_db)
    
    
    #def db_update(self):
    
    
    def db_query(self, username, password):
        '''
        Returns data on user. Returns -1 if user does not exists.
        
        :param username: Username.
        :param password: User's password.
        '''
        
        with open(self.database_name + "." + self.version + ".db", 'rb') as open_db:
            pickle_file = pickle.load(open_db)
            for i in pickle_file[1:]:
                if i.get('name') == username:
                    if i.get('password') == password:
                        return i
            return -1


if __name__ == '__main__':
    '''
    This exists only to test. Will remove after program is finished.
    '''
    
    test = database("cyberfitness", "1.0")
    test.create_table()
    test.add_user("bill", "abc123!!!")
    test.add_user("bob", "password")
    print(test.db_query("bill", "abc123!!!"))
    print(test.db_query("bill", "abc123"))
    print(test.db_query("jason", "abc123!!!"))
    print(test.db_query("bob", "password"))
    test.db_insert("bill", "abc123!!!", "running", "2miles")
    print(test.db_query("bill", "abc123!!!"))
    
    