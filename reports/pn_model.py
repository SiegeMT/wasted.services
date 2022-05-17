import pandas as pd
import panel as pn
from param import Parameterized, Selector

class Pull(Parameterized):
    
    dom = 'https://ntmpsweb.dc3n.navy.mil/FLTMPS/Personnel/Course%20Grads/'
    form_single = 'PersOnbdCseGradsForUICReport.aspx'
    form_fy = 'PersAddFYTrngRqmtsReport.aspx'

    indiv = "BEGDT=&ENDDT=&PageNum=0&PageSize=250&ActyGrp=UIC&ActyGrpText=Selected%20Activity&PersFilter=ALL&Export=CSV"
    uic = [
      'N68094',
      'N47198',
      'NKTR00',
    ]
    cin = [DHA-US1159, DHA-US429, DHA-US1146, DHA-US323]
    csetitle = [
      "%20CONSTITUTION%20DAY%20AWARENESS",
      "%20MHS%20CUSTOMER%20SERVICE",
      "NAVY+SUICIDE+PREVENTION+TRAINING+FOR+PROVIDERS+(UNCLASSIFIED-FOUO)(2+HRS)",
      " DHA EMPLOYEE SAFETY"]
    CONSTITUTION = [%20CONSTITUTION%20DAY%20AWARENESS
        "CSETITLE=%20CONSTITUTION%20DAY%20AWARENESS&UIC=N68094&UICTitle=%20NMRTC%20CAMP%20PENDLETON%20CACourseTitle=%20CONSTITUTION%20DAY%20AWARENESS",
        "CSETITLE=%20CONSTITUTION%20DAY%20AWARENESS&UIC=N47198&UICTitle=NAVMEDREADTRNUNIT%20YUMA%20AZ&CourseTitle=%20CONSTITUTION%20DAY%20AWARENESS"] 
    CUSTOMER_SERVICE = [
        "CSETITLE=%20MHS%20CUSTOMER SERVICE&UIC=N68094&UICTitle=%20NMRTC%20CAMP%20PENDLETON%20CA&CourseTitle= MHS CUSTOMER SERVICE",
        "CSETITLE=%20MHS%20CUSTOMER SERVICE&UIC=N47198&UICTitle=NAVMEDREADTRNUNIT%20YUMA%20AZ&CourseTitle= MHS CUSTOMER SERVICE"]
    SUICIDE= [
        "CSETITLE=NAVY+SUICIDE+PREVENTION+TRAINING+FOR+PROVIDERS+(UNCLASSIFIED-FOUO)(2+HRS)&UIC=N47198&UICTitle=NAVMEDREADTRNUNIT%20YUMA%20AZ&CourseTitle=NAVY+SUICIDE+PREVENTION+TRAINING+FOR+PROVIDERS+(UNCLASSIFIED-FOUO)(2+HRS)",
        "CSETITLE=NAVY+SUICIDE+PREVENTION+TRAINING+FOR+PROVIDERS+(UNCLASSIFIED-FOUO)(2+HRS)&UIC=N68094&UICTitle=%20NMRTC%20CAMP%20PENDLETON%20CA&CourseTitle=NAVY+SUICIDE+PREVENTION+TRAINING+FOR+PROVIDERS+(UNCLASSIFIED-FOUO)(2+HRS)"]

    SAFETY = [
        UIC=N68094&UICTitle=%20NMRTC%20CAMP%20PENDLETON%20CA&CourseTitle= MHS CUSTOMER SERVICE",
        UIC=N47198&UICTitle=NAVMEDREADTRNUNIT%20YUMA%20AZ&CourseTitle= MHS CUSTOMER SERVICE"]
    
        BEGDT = ''
        ENDDT = ''
    PageNum = '0'
    PageSize = '10'
    ActyGrp = 'UIC'
    ActyGrpText = 'Selected Activity'
    PersFilter = 'ALL'
    Export = 'CSV'


TYPE=D&UIC=N47198&UICTitle=NAVMEDREADTRNUNIT%20YUMA%20AZ&GRP=UIC&PageNum=0&PageSize=250&Export=CSV
    dom_yuma = 'PersAddFYTrngRqmtsReport.aspx'
    yuma = {
        'TYPE': 'D',
        'UIC': 'N47198',
        'UICTitle': 'NAVMEDREADTRNUNIT YUMA AZ',
        'GRP': 'UIC',
        'PageNum': '0',
        'PageSize': '250',
        'Export': 'CSV',
    }

    cpen = {
        'TYPE': 'D',
        'UIC': 'N68094',
        'UICTitle': ' NMRTC CAMP PENDLETON CA',
        'GRP': 'UIC',
        'PageNum': '0',
        'PageSize': '250',
        'Export': 'CSV',
    }

    cont = {
        'TYPE': 'D',
        'UIC': 'NKRT00',
        'UICTitle': 'CONTRACTOR TRACKING',
        'GRP': 'UIC',
        'PageNum': '0',
        'PageSize': '250',
        'Export': 'CSV',
    }

    BEGDT = ''
    ENDDT = ''
    PageNum = '0'
    PageSize = '10'
    ActyGrp = 'UIC'
    ActyGrpText = 'Selected Activity'
    PersFilter = 'ALL'
    Export = 'CSV'