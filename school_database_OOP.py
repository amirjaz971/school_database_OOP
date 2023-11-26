import sqlite3

    
class School:
        __city='Tehran'
        def __init__(self,table):
            self.table=table

        def connect(self):
            db=sqlite3.connect('school.db')
            cr=db.cursor()
            cr.execute(f'create table if not exists {self.table}(code int,name varchar(30),family varchar(30),city varchar(30))')
            
            db.commit()
            db.close()
            
            print(f'Table {self.table} has been created')
        def insert(self,num):
            db=sqlite3.connect('school.db')
            cr=db.cursor()            
            
            
                
            while num>0:
                    code=int(input('Enter the code:'))
                    
                    cr.execute(f'select * from {self.table}')
                    rows=cr.fetchall()
                    for i in rows:
                        if code in i:
                            print(f'{code} has been already entered!')
                            break
                    
           
                    
                    else: 
                        
                        name=input('Enter the name:')
                        family=input('Enter the family:')
                        cr.execute(f'insert into {self.table} values(?,?,?,?)',(code,name.lower(),family.lower(),School.__city))
                        db.commit()
                        num-=1
            print(f'values have been inserted in table {self.table}')   
                            
            
                       
        def show(self):
            db=sqlite3.connect('school.db')
            cr=db.cursor()
            cr.execute(f'select * from {self.table}')
            
            rows=cr.fetchall()
            if len(rows) != 0:
             n=1   
             for i in rows:
                print(f'Row{n}={i}')
                n+=1
            else:
                print('Table is empty!')
                                    
        def delete(self):
            db=sqlite3.connect('school.db')
            cr=db.cursor()
            cr.execute(f'select * from {self.table}')
                        
            rows=cr.fetchall()
            if len(rows) != 0:
                num=int(input('Enter the number of the records that you want to delete:'))
                if num>0:
                    
                
                
                    if num<=len(rows):
                        
                     while num>0 :
                        cr.execute(f'select * from {self.table}')
                        
                        rows=cr.fetchall()                         
                        code=int(input(f'Enter the code that you want to delete from table student:'))
                        
                        for i in rows:
                            
                            if code  in i:
                             cr.execute(f'delete from {self.table} where code={code}')
                             db.commit()
                             num-=1                                
                                
                             break
                        else:
                            print(f'{code} not found!')

                     print('Fields have been deleted')
                    else:
                        print('The number of records that you want to delete are more than the actual records!')
                else:
                    print('The number must be bigger than zero!')        
                                 
                            
                
                    
                
                

            else:
                print('Table is empty!')            
        def update(self):
            db=sqlite3.connect('school.db')
            cr=db.cursor()
            cr.execute(f'select * from {self.table}')
            rows=cr.fetchall()
            if len(rows)!=0:
                num=int(input('Enter the number of the records which you want to update:'))
                if num>0:
                    
                 if num<=len(rows):
                     while num>0 :
                         code=int(input(f'Enter the code that you want to update in table {self.table}:'))
                         for i in rows:
                             if code  in i:
                                 name=input('Enter the new value for name:')
                                 family=input('Enter the new value for family:')
                                 if name=='' and family!='':
                                     
                                     
                                     cr.execute(f'update {self.table} set  family="{family}"   where code={code}')
                                     db.commit()
                                     num-=1   
                                 elif family=='' and name!='':
                                     
                                     cr.execute(f'update {self.table} set  name="{name}"   where code={code}')
                                     db.commit()
                                     num-=1                                       
                                 elif name!='' and family!='':
                                     
                                     cr.execute(f'update {self.table} set  name="{name}" , family="{family}"   where code={code}')
                                     db.commit()
                                     num-=1 
                                 else:
                                     print('Enter value for at least name or family!')                                            
                                 break
                         else:
                             print(f'{code} not found!')
                     print(f'Values have been updated in table {self.table}')         
                             
                                 
                        
                 else:
                    print('The number of records that you want to update are more than the lenght of records!')
                else:
                    print('The number must be bigger than zero!')    
            else:
                print('Table is empty')            
 
        def search(self,field,value):
            db=sqlite3.connect('school.db')
            cr=db.cursor()
            cr.execute(f'select * from {self.table}')
            rows=cr.fetchall()
            if len(rows)==0:
                print('Table is empty')
            else:
                    ok=0
                    for i in rows:
                        if value in i:
                            ok+=1
                            
                            search=cr.execute(f'select * from {self.table} where {field}="{value}"')
                            
                           
                                    
                    if ok==0:
                        print(f'{value} not found!')
                    else:
                        for i in search:
                            print(i)    
                    print('Searching has been done')               
            
 
        def order(self,model,field):
            db=sqlite3.connect('school.db')
            cr=db.cursor()
            cr.execute(f'select * from {self.table}')
            rows=cr.fetchall()
            if len(rows)==0:
                print('Table is empty!')
            else:
                c=cr.execute(f'select * from {self.table} order by {field} {model}')
                for i in c:
                    print(i)
                print(f'Table {self.table} ordered by {field} {model}')
                    

        def union(self,table):
            db=sqlite3.connect('school.db')
            cr=db.cursor()
            cr.execute(f'select * from {self.table} ')
            rows1=cr.fetchall()
            cr.execute(f'select * from {table}')
            rows2=cr.fetchall()
            if len(rows1)==0 and len(rows2)==0:
                print(f'{self.table} and {table} are empty!')
            elif len(rows1)==0:
                print(f'{self.table} is empty!')
            elif len(rows2)==0:
                print(f'{table} is empty!')
            else:
                print('The union of two tables are:')
                u=cr.execute(f'select code as codes,name as names,family as families from {self.table} union select code,name,family from {table}') 
                for i in u:
                    print(i)   
 
 
 
 
 
 
 
        
        
            
if __name__=='__main__':
    s=School('student')
    t=School('teacher')
    print('Data Base connected')
    s.connect()
    t.connect()
    while True:
        try:
            
            print('1.Insert')     
            print('2.Show')     
            print('3.Delete')     
            print('4.Update')     
            print('5.Search')     
            print('6.Order')
            print('7.Union')     
            print('8.Exit')     
            choose=input('Enter the option number:')
            if choose=='1':
                while True:
                    print('1.Student')
                    print('2.Teacher')
                    print('3.Back')
                    choose=input('Enter the number of the table which you want to insert its fields values:')
                    if choose=='1':
                        num=int(input('Enter the number of records that you want to insert their values:'))
                        if num>0:
                            
                            s.insert(num)
                        else:
                            print('The number must be bigger than zero!') 
                            
                    elif choose=='2':
                        num=int(input('Enter the number of records that you want to insert their values:'))
                        if num>0:
                            
                             t.insert(num)
                        else:
                            print('The number must be bigger than zero!') 
                                 
                    elif choose=='3':
                        break
                    else:
                        print('Wrong command!')
            elif choose=='2':
                while True:
                    print('1.Student')
                    print('2.Teacher')
                    print('3.Back')
                    choose=input('Enter the number of the table which you want to see its fields:')
                    
                    if choose=='1':
                        s.show()
                    elif choose=='2':
                        t.show()
                    elif choose=='3':
                        break
                    else:
                        print('Wrong command!')                    
            elif choose=='3':
                while True:
                    print('1.Student')
                    print('2.Teacher')
                    print('3.Back')
                    choose=input('Enter the number of the table which you want to delete its fields:')
                    
                    if choose=='1':
                        
                        
                        
                            s.delete()
                        
                              
                    elif choose=='2':
                        
                        
                        
                            t.delete()
                        
                                                   
                        
                    elif choose=='3':
                        break
                    else:
                        print('Wrong command!')  
            elif choose=='4':
                 while True:
                    print('1.Student')
                    print('2.Teacher')
                    print('3.Back')
                    choose=input('Enter the number of the table which you want to update its fields:')
                    
                    if choose=='1':
                        s.update()
                    elif choose=='2':
                        t.update()
                    elif choose=='3':
                        break
                    else:
                        print('Wrong command!')  
            elif choose=='5':
                while True:
                    print('1.Student')
                    print('2.Teacher')
                    print('3.Back')
                    choose=input('Enter the number of the table which you want to search in its fields:')
                    
                    if choose=='1':
                        print('1.Code')
                        print('2.Name')
                        print('3.Family')
                        choose=input('Search by which field:')
                        if choose=='1':
                            code=int(input('Enter the code:'))
                            s.search('code',code)
                        elif choose=='2':
                            name=input('Enter the name:')
                            s.search('name',name.lower())
                        elif choose=='3':
                            family=input('Enter the family:')
                            s.search('family',family.lower())
                        else:
                            print('Wrong command!')
                    elif choose=='2':
                        print('1.Code')
                        print('2.Name')
                        print('3.Family')
                        choose=input('Search by which field:')
                        if choose=='1':
                            code=int(input('Enter the code:'))
                            t.search('code',code)
                        elif choose=='2':
                            name=input('Enter the name:')
                            t.search('name',name.lower())
                        elif choose=='3':
                            family=input('Enter the family:')
                            print(family)
                            t.search('family',family.lower())
                        else:
                            print('Wrong command!')                        
                    elif choose=='3':
                        break
                    else:
                        print('Wrong command!')  
            elif choose=='6':
                while True:
                    print('1.Student')
                    print('2.Teacher')
                    print('3.Back')
                    choose=input('Enter the number of the table which you want to see it by order:')
                    
                    if choose=='1':
                        print('1.Ascending')
                        print('2.Descending')
                        choose=input('Which Order model:')
                        if choose=='1':
                            print('1.Code')
                            print('2.Name')
                            print('3.Family')
                            
                            choose=input('Order by which field:')
                            if choose=='1':
                                s.order('ASC','code')
                            elif choose=='2':
                                s.order('ASC','name')
                                
                            elif choose=='3':
                                s.order('ASC','family')
                                
                            else:
                                print('Wrong command!')
                        elif choose=='2':
                            print('1.Code')
                            print('2.Name')
                            print('3.Family')
                            choose=input('Order by which field:')   
                            if choose=='1':
                                s.order('DESC','code')
                            elif choose=='2':
                                s.order('DESC','name')
                                
                            elif choose=='3':
                                s.order('DESC','family')
                                
                            else:
                                print('Wrong command!')                                                     
                        else:
                            print('Wrong command!')
                    elif choose=='2':
                        print('1.Ascending')
                        print('2.Descending')
                        choose=input('Which Order model:')
                        if choose=='1':
                            print('1.Code')
                            print('2.Name')
                            print('3.Family')
                            
                            choose=input('Order by which field:')
                            if choose=='1':
                                t.order('ASC','code')
                            elif choose=='2':
                                t.order('ASC','name')
                                
                            elif choose=='3':
                                t.order('ASC','family')
                                
                            else:
                                print('Wrong command!')
                        elif choose=='2':
                            print('1.Code')
                            print('2.Name')
                            print('3.Family')
                            choose=input('Order by which field:')   
                            if choose=='1':
                                t.order('DESC','code')
                            elif choose=='2':
                                t.order('DESC','name')
                                
                            elif choose=='3':
                                t.order('DESC','family')
                                
                            else:
                                print('Wrong command!')                                                     
                        else:
                            print('Wrong command!')                     
                    elif choose=='3':
                        break
                    else:
                        print('Wrong command!')  
            elif choose=='7':
                while True:
                    
                    print('1.Student')
                    print('2.Teacher')
                    print('3.Back')
                    choose=input('Choose one of these tables as the first table for union:')
                    if choose=='1':
                        s.union('teacher')
                    elif choose=='2':
                        t.union('student')
                    elif choose=='3':
                        break
                    else:
                        print('Wrong command!')
                    

                    

            elif choose=='8':
                print('Exiting...')
                break
            else:
                print('Wrong command!')   
        except ValueError:
            print('Invalid value/RESET')     