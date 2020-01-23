# py-to-crud-php
Python scripts to generate simple CRUD for PHP web pages in Bootstrap style.

The web pages look like this:

![List Page](https://user-images.githubusercontent.com/21377029/72954177-1a2bfd00-3dca-11ea-9978-f88b616fdcfe.png)

![Edit Page](https://user-images.githubusercontent.com/21377029/72954194-29ab4600-3dca-11ea-9da0-9ee463a23703.png)

### **Prerequisite**

Just require basic programs, in my case:
1. XAMPP (v.7.4.1) for PHP, MySQL, Apache web server.
2. Python (v.3.8.0) IDLE.

### **How to use**

1. Download this repository and put it in the web server folder. (htdocs in my case) Create your database with table. (pytocrudphp.sql in my case) 
2. Go to config.php to set your database configuration, save the file.
3. Go to the file generator/TBConfig.py to set table config (i.e. table name, column name, type of input, etc.) that you want ro generate CRUD. (see detail in that file) Then, save the file. For example, I want to create CRUD for table 'person'. 
4. Open Python IDE to run the file generator/TBMain.py This results 5 files including: 
- person_add.php
- person_edit.php
- person_delete.php
- person_view.php
- person_list.php

All task for table 'person' has finished. Enjoy!  


