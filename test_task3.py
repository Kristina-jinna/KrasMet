import task3

### Test connection
con = task3.Connection('https','reqres.in')

### getListOfUser
con.getListOfUser(['api','users'])

### get solo user
con.getCurrentUser(['api','users'],1)