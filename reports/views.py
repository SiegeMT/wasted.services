from django.shortcuts import render
import urllib.request


def reports(request):
    #script = server_document(request.build_absolute_uri())
    req_url = urllib.request.urlopen("https://ntmpsweb.dc3n.navy.mil/FLTMPS/Personnel/Course%20Grads/PersOnbdCseGradsForUICReport.aspx?BEGDT=&ENDDT=&PageNum=0&PageSize=250&CIN=DHA-US1159&CSETITLE=%20CONSTITUTION%20DAY%20AWARENESS&ActyGrp=UIC&ActyGrpText=Selected%20Activity&UIC=N68094&UICTitle=%20NMRTC%20CAMP%20PENDLETON%20CA&PersFilter=ALL&CourseTitle=%20CONSTITUTION%20DAY%20AWARENESS&Export=CSV")
    return render(request, 'reports/reports.html', {})

