import pickle as cPickle

_first_qtr = {
    'anti_terror': {
        'CIN': "ANTI-TERRORISM LEVEL 1 AWARENESS TRAINING",
        'CseTitle': "CENSECFOR-AT-010-2.0",
    },
    'cyber_aware': {
        'CIN': "CYBER AWARENESS CHALLENGE 2022",
        'CseTitle': "DOD-CAC-2022.0",
    },
    'active_shooter': {
        'CIN': "DON ACTIVE SHOOTER",
        'CseTitle': "DON-687121-1.0",
    },
    'opsec': {
        'CIN': "USOPSEC/IDM",
        'CseTitle': "NOST-USOPSEC-4.0",
    },
}
_second_qtr = {
    'uac': {
        'CIN': "NAVY MEDICINE PREVENTION OF UNAUTHORIZE COMMITMENTS(UAC)",
        'CseTitle': "DHA-US467",
    },
    'insider_threat': {
        'CIN': "INSIDER THREAT AWARENESS",
        'CseTitle': "CDSE-INSIDER-1.0",
    },
    'records_mgmt': {
        'CIN': "RECORDS MANAGEMENT IN THE DON: EVERYONE'S RESPONSIBILITY",
        'CseTitle': "DOR-RM-010-1.2",
    },
    'ctip': {
        'CIN': "COMBATING TRAFFICKING IN PERSONS",
        'CseTitle': "DOD-CTIP-5.0",
    },
    'wrk_safety': {
        'CIN': "DHA WORKPLACE SAFETY",
        'CseTitle': "DHA-US429",
    },
    'cust_service': {
        'CIN': "MHS CUSTOMER SERVICE",
        'CseTitle': "DHA-US323",
    },
    'ciar': {
        'CIN': "NCIS COUNTERINTELLIGENCE AND INSIDER THREA  AWARENESSAND REPORTING TRAINING",
        'CseTitle': "DON-CIAR-1.0",
    },
    'prov_suicide': {
        'CIN': "NAVY SUICIDE PREVENTION TRAINING FOR PROVIDER  (UNCLASSIFIED-FOUO)(2 HRS)",
        'CseTitle': "DHA-US1159",
    },
}
_third_qtr = {
    'hipaa': {
        'CIN': "HIPAA AND PRIVACY ACT TRAINING",
        'CseTitle': "DHA-US001",
    },
    'privacy': {
        'CIN': "DEPARTMENT OF THE NAVY ANNUAL PRIVACY TRAINING",
        'CseTitle': "DON-PRIV-2.0",
    },
    'constitution': {
        'CIN': "CONSTITUTION DAY AWARENESS",
        'CseTitle': "DHA-US1146",
    },
    'moonlight': {
        'CIN': "NAVY MEDICINE OFF DUTY EMPLOYMENT (MOONLIGHTING) ANNUAL TRAINING",
        'CseTitle': "DHA-US466",
    },
}

sites = {
    'base': {
        'fltmps': 'https://ntmpsweb.dc3n.navy.mil/FLTMPS/',
        'jko': 'https://jkodirect.jten.mil/Atlas2/',
        'twms': 'https://mytwms.dc3n.navy.mil/',
        },
    'login': {},
    'endpt': {},
}

domains = {
    'fltmps': {
        'base': 'https://ntmpsweb.dc3n.navy.mil/FLTMPS/',
        'login': ('DoDBanner.aspx', 'Home.aspx'),
        'rpt': '/Personnel/Course Grads/' ['PersOnbdCseGradsForUICReport.aspx',]
    },
    'jko': {
        'base': 'https://jkodirect.jten.mil/Atlas2/',
    },
    'twms': {
        'base': 'https://mytwms.dc3n.navy.mil/',
    }
}


mylist = [_first_qtr, _second_qtr, _third_qtr, domains]



with open('dat.txt', 'wb') as fh:
    cPickle.dump(mylist, fh)