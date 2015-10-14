# USD/PLN Rate
# Created August 1, 2015 in Sleepy Hollow, NY
# by Aneta Zolkiewicz



import urllib
import re

def get_deta():
    """Reads the currency rates from cinkciarz.pl and prints out, stores the pln/usd
       rate in a variable myRate"""
    
    sock = urllib.urlopen("https://cinkciarz.pl/kantor/kursy-walut-cinkciarz-pl/usd") 
    htmlSource = sock.read()                            
    sock.close()                                        
    #print htmlSource

    currancyRate = re.findall(r'<td class="cur_down">(.*?)</td>',str(htmlSource))

    for eachTd in currancyRate:
        print(eachTd)

    print currancyRate[0]
    myRate = currancyRate[0]
    print myRate
    return myRate


def store_data(myRate):
    """Adds the current currency rate myRateList whete it is stored for the future use"""
    myRateList.append(myRate)
    return myRateList

def compare_data(myRate, myRateList):
    """compares current rate with the previous rate"""
    change =  ( myRate * 100 / myRateList[-1]) - 100
    change = int(change)
    print 'the rate change was:  ', change, '%'
    return change
     
    
def email_data():
    if change >= 5:
        print "there was more than 5% change in your investment, the current rate is:  ", myRate, "the change was: ", change
    
    
# MAIN PROGRAM

myRateList = []

myRateList = store_data(3.3)
myRateList = store_data(3.4)
print myRateList

change = compare_data(3.9, myRateList)
myRate = 3.9
email_data()




   
    


