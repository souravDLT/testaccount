#beeline

dbName='t_sda01'

#Initializing table list
ManyTables=['party', 'address1', 'address', 'person', 'household', 'FakeTable', 'Organization']
#beelineString=""
status = []

for oneTable in ManyTables:
  tempStr = """select * from  %s.%s limit 1; """%(dbName, oneTable)
  #beelineString = beelineString+tempStr
  beelineCommand='beeline -e '+ '\"' + tempStr + '\"'

  #Storing the output of the beeline command output to retval
  retval = os.popen(beelineCommand).read()
  if (retval==''):
      status.append("Failure")
  else:
        status.append("Success")

logReport = dict(zip(ManyTables, status))
