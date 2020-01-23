#--------- Site Name and Table -----------------------------------------------------

# Define your web site name 
siteName = "Py to CRUD PHP"

# Define a table name
tbName = 'person'



#--------- Field Name and Input ----------------------------------------------------

# Define field names (columns in the table)
names = [
    'pid',
    'name',
    'description',
    'mjid',
    'blood',
    'mnid',
    'sex',
    'sjid',
	'color',
    'biography',
]

# Define input elements according to the filed name list (same ordering) 
# including: text, textarea, editor, selectTb, selectCt, radioTb, radioCt, checkboxTb, checkboxCt
# For Tb or Ct, you need to define the datasource in the next variable
fieldInput = [
    'text',
    'text',
    'textarea',
    'selectTb',
    'selectCt',
    'radioTb',
    'radioCt',
    'checkboxTb',
    'checkboxCt',
    'editor',
]



#--------- Select Input -------------------------------------------------------------

# Define table, key, and value for select input that retrieve data from a table
# ['tableName', 'id', 'name']
selInputByTb = [
    ['major','mjid','mjname'],
]

# Define table, key, and value for select input based on your customized data
# [['key1','value1'],['key2','value2'],...],
selInputByCt = [
    [['a','A'],['b','B'],['ab','AB'],['o','O']],
]



#--------- Radio Input ---------------------------------------------------------------

# Define table, key, and value for radio input that retrieve data from a table
# ['tableName', 'id', 'name']
radInputByTb = [
    ['minor','mnid','mnname'],
]

# Define table, key, and value for radio input based on your customized data
# [['key1','value1'],['key2','value2'],...],
radInputByCt = [
    [[1,'Male'],[2,'Female']],
]



#--------- Checkbox Input ------------------------------------------------------------

# Define table, key, and value for checkbox input that retrieve data from a table
# ['tableName', 'id', 'name']
chkInputByTb = [
    ['subject','sjid','sjname'],
]

#Define table, key, and value for checkbox input based on your customized data
# [['key1','value1'],['key2','value2'],...],
chkInputByCt = [
    [['red','Red'],['green','Green'],['blue','Blue']],
]