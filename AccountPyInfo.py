"""using lists,for loops,and variables in an if-else,concat string statement.( float or int).
Incorporating e-mail and text notification of customers' updated balence."""

import time
import urllib
import re
import smtplib
from datetime import datetime

#set up global variables[]
listCustId = [0,1,2,3,]  
listCustName = ['Amy Smart', 'Bill Dumb','Charles Average','Don Gone',]
listCustBal = [1000,2500,7500,5000,]
now = datetime.now()

#show current accounts on record with balance and payment info

def printData():
    for i in listCustId:
        b = listCustBal[i] * .05
        c = listCustBal[i] * .03
        minPay = listCustBal[i] * .05 if listCustBal[i] < 5000 else listCustBal[i] * .03
    
        print '%s the balance of this loan is %s '%(listCustName[i],listCustBal[i])
        if listCustBal[i] < 5000: 
            print "Customers APR is 5.0%"
        else :
            print "Customers APR is 3.0%"

        print "Your next payment is",minPay,"dollars","\n"
    getData()

#Make a payment, show the new balance, notify account holder of new balance
    
def getData():
    print len(listCustId)
    newId = input('what is the customer id? ')
    if newId == -1:
        print '\n'
        printData()
    for i in listCustId:
        if listCustId[i] == newId :
            newPymnt = input('what is customer payment? ')
            listCustBal[i] = listCustBal[i] - newPymnt
            print'\n'
            print str(listCustName[i]) + "--Your new Balance is: $" + str(listCustBal[i])
            raw_input('Hit Return to Verify')
            print'\n'
            message = 'Thank you for your payment %s.Your new balance is %s '%(listCustName[i],listCustBal[i])
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('gljfb0958@gmail.com','Enter0958Gmail')
            server.sendmail('gljfb0958@gmail.com','gljfb@yahoo.com',message)
            server.sendmail('From Gary','4079732804@messaging.sprintpcs.com',message)
            server.quit()
            now = datetime.now()
            listFileInfo = open('c:/users/gary0958/desktop/accounts/listCustinfo_Row.txt','a')
            listFileInfo.write("ID   " + "" + " NAME" + "    " + "  BAL   " + str(now) +'\n'+'\n')
            listFileInfo.write(str(listCustId[i]) + " , " + str(listCustName[i]) + " , " + str(listCustBal[i]) + " , " + '\n' +'\n')
            listFileInfo.close()
            listFileId = open('c:/users/gary0958/desktop/accounts/listCustInfo_Column.txt','a')
            listFileId.write("ID# " + str(listCustId[i]) + '  ,  ' + str(now) + '\n')
            listFileId.close()
            listFileName = open('c:/users/gary0958/desktop/accounts/listCustInfo_Column.txt','a')
            listFileName.write("NAME " + str(listCustName[i]) + '\n')
            listFileName.close()
            listFileBal = open('c:/users/gary0958/desktop/accounts/listCustInfo_Column.txt','a')
            listFileBal.write("BAL " + str(listCustBal[i]) + '\n' + '\n')
            listFileBal.close()
            printData()                       
                
    newName = raw_input('What is customer name? ')
    newBal = input('what is customer balance? ')
    
    print '\n'
    listCustId.append(newId)
    listCustName.append(newName)
    listCustBal.append(newBal)
        
    print "\n"
    print listCustName
    print '\n'
    print listCustBal
    print '\n'
    print listCustId
    print '\n'
    printData()
    
printData()
