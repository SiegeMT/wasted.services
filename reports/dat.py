cmd =  {
    'yuma': [
        ['UIC', 'N47198'], 
        'UICTitle': 'NAVMEDREADTRNUNIT YUMA AZ',
    ], 
    'cpen': {
        'UIC': 'N68094', 
        'UICTitle': ' NMRTC CAMP PENDLETON CA',
        }, 
    'cont': {
        'UIC': 'NKTR00',
        'UICTitle': 'CONTRACTOR TRACKING',
        },
    },
} 
    'q1': {
        'cui': {
            'CIN': 'DOD-CUI-001',
            '': 'DOD MANDATORY CONTROLLED UNCLASSIFIED INFORMATION (CUI) TRAINING',
        },
    'q2': {
        'suicide_p': {
            'CIN': 'DHA-US1146',	
            'CSETITLE': 'NAVY SUICIDE PREVENTION TRAINING FOR PROVIDERS (UNCLASSIFIED-FOUO)(2 HRS)',
        },
        'constitution': {
            'CIN': 'DHA-US1159',
            'CSETITLE': 'CONSTITUTION DAY AWARENESS',
        },
        'safety': {
            'CIN': 'DHA-US323',
            'CSETITLE': 'DHA WORKPLACE SAFETY',
        },
        'customer': {
            'CIN': 'DHA-US429',
            'CSETITLE': 'MHS CUSTOMER SERVICE',
        },
    }


CseAddNetcCompletion.aspx

PersOnbdCseGradsForUICReport


CseGrp = [NMRTC, BUMED+FY+TRAINING+REQUIREMENTS]

LECFSELGRP = ['DOD CONTROLLED UNCLASSIFIED INFO TRNG', 'GMT+and+OTHER+TRAINING']
CseCat=BUREAU+OF+MEDICINE+AND+SURGERY
DOD-CUI-001	DOD MANDATORY CONTROLLED UNCLASSIFIED INFORMATION (CUI) TRAINING


DHA-US1146	NAVY SUICIDE PREVENTION TRAINING FOR PROVIDERS (UNCLASSIFIED-FOUO)(2 HRS)
DHA-US1159	CONSTITUTION DAY AWARENESS
DHA-US323	DHA WORKPLACE SAFETY
DHA-US429	MHS CUSTOMER SERVICE




ASPE-1.0	ACTIVE SHOOTER PRACTICAL EXERCISE
CDSE-INSIDER-1.0	INSIDER THREAT AWARENESS
CENSECFOR-AT-010-2.0	ANTI-TERRORISM LEVEL 1 AWARENESS TRAINING
CPPD-GMT-SAP-1.0	SUICIDE AWARENESS AND PREVENTION
CPPD-GMT-SAPRA-1.0	SEXUAL ASSAULT PREVENTION AND RESPONSE AWARENESS
DHA-US001	HIPAA AND PRIVACY ACT TRAINING
DHA-US466	NAVY MEDICINE OFF DUTY EMPLOYMENT (MOONLIGHTING) ANNUAL TRAINING
DHA-US467	NAVY MEDICINE PREVENTION OF UNAUTHORIZED COMMITMENTS (UAC)
DOD-CAC-2022.0	CYBER AWARENESS CHALLENGE 2022
DOD-CTIP-5.0	COMBATING TRAFFICKING IN PERSONS
DON-687121-1.0	DON ACTIVE SHOOTER
DON-CIAR-1.0	NCIS COUNTERINTELLIGENCE AND INSIDER THREAT AWARENESS AND REPORTING TRAINING
DON-PRIV-2.0	DEPARTMENT OF THE NAVY ANNUAL PRIVACY TRAINING
DOR-RM-010-1.2	RECORDS MANAGEMENT IN THE DON: EVERYONE'S RESPONSIBILITY
NOST-USOPSEC-4.0	USOPSEC/IDM

class Report(models.Model):
    
    TYPE = 'D'
    Export = 'CSV'
    GRP = 'UIC'
    PageNum = '0'
    PageSize = '100'
    

    uic = models.CharField(max_length=50)
    uictitle': models.CharField(max_length=50)
    
class Single(models.Model):   
    BEGDT = ''
    ENDDT = ''
    PageNum = '0'
    PageSize = '10'
    ActyGrp = 'UIC'
    ActyGrpText = 'Selected Activity'
    PersFilter = 'ALL'
    Export = 'CSV'
    
    CIN = models.Model.CharField(max_length=50)
    CSETITLE = 

for item in 
json = {
    'BEGDT = ''
    'ENDDT = ''
    'PageNum = '0'
    'PageSize = '10'
    'ActyGrp = 'UIC'
    'ActyGrpText = 'Selected Activity'
    'PersFilter = 'ALL'
    'Export = 'CSV'
    'CIN': f'{cin}',
    'CSETITLE': f'{course_title}',
    'UIC': list(df['UIC']),
    'UICTitle': list(df['UICTitle']),
    'CourseTitle': f'{cin}',
}