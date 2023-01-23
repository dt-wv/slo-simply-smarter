#JLL
import json
import requests
import os
import urllib3
import re  

##################################
### Mission Control variables
##################################
#Cookie='full cookie'
#CSRF='abcdefghij-1234-56789-aaaa-bbbbb|45|bbbbb-abc-aaa-000-aaaa'
Cookie=''
CSRF=''

##################################
### Environment Dynatrace
##################################
Tenant="https://"+str(os.getenv('MyTenant'))
Token=os.getenv('MyToken')


##################################
## API
##################################
APIdashboard='/api/config/v1/dashboards'
APIslo='/api/v2/slo'

##################################
## SLO
##################################
SLO_source={'Optimization - CPU Usage':'d432ca69-7cb0-3dcf-a176-6225a6d5ff4c','Optimization - Disk Usage':'f73c599d-87ba-38e8-98ff-1dae02879969','Optimization - Memory Usage':'ef700817-f0c2-33f8-916d-8dfeb0f1ce3a','Smarter - Application Performance':'eb99760c-52f6-303b-94eb-4a67d5bf3b32','Smarter - Browser Monitor Availability':'2d23383a-8124-3799-916a-548d307ffbcd','Smarter - Database Performance':'91f1aaee-8e54-37cd-9771-cacd0bc977dc','Smarter - Database Success Rate':'c3b96795-e1db-3e55-806b-c4dbba302094','Smarter - Http Monitor Availability':'7dffcc5b-a736-32da-bf7e-a981205fc9fb','Smarter - Service Availability':'a0a88884-5d41-3425-8f02-37436794da80','Smarter - Service Performance':'811465a3-5b0b-3096-9279-02a3d499ba25'}
SLO_target={'Optimization - CPU Usage':'','Optimization - Disk Usage':'','Optimization - Memory Usage':'','Smarter - Application Performance':'','Smarter - Browser Monitor Availability':'','Smarter - Database Performance':'','Smarter - Database Success Rate':'','Smarter - Http Monitor Availability':'','Smarter - Service Availability':'','Smarter - Service Performance':''}

##################################
## Dashboard
##################################
Dashboard_source={'🏠 Dynatrace: simply smarter':'bbbbbbbb-a003-a017-0000-000000000133','✔ SLO Simply Smarter':'bbbbbbbb-a003-a017-0008-000000000133','✔ SLO Resource Optimization':'bbbbbbbb-a003-a017-0009-000000000133','✔ User experience (web applications)':'bbbbbbbb-a003-a017-0002-000000000133','✔ User experience (mobile apps)':'bbbbbbbb-a003-a017-0003-000000000133','✔ Synthetic (browser)':'bbbbbbbb-a003-a017-0004-000000000133','✔ Services':'bbbbbbbb-a003-a017-0001-000000000133','✔ Database services':'bbbbbbbb-a003-a017-0005-000000000133','✔ Synthetic (service)':'bbbbbbbb-a003-a017-0006-000000000133','✔ Infrastructure':'bbbbbbbb-a003-a017-0007-000000000133'}
Dashboard_target={'🏠 Dynatrace: simply smarter':'','✔ SLO Simply Smarter':'','✔ SLO Resource Optimization':'','✔ User experience (web applications)':'','✔ User experience (mobile apps)':'','✔ Synthetic (browser)':'','✔ Services':'','✔ Database services':'','✔ Synthetic (service)':'','✔ Infrastructure':''}
Dashboard_mapping_name={'🏠 Dynatrace: simply smarter':'Dynatrace_simply smarter.json','✔ SLO Simply Smarter':'SLO Simply Smarter.json','✔ SLO Resource Optimization':'SLO Resource Optimization.json','✔ User experience (web applications)':'User experience (web applications).json','✔ User experience (mobile apps)':'User experience (mobile apps).json','✔ Synthetic (browser)':'Synthetic (browser).json','✔ Services':'Services.json','✔ Database services':'Database services.json','✔ Synthetic (service)':'Synthetic (service).json','✔ Infrastructure':'Infrastructure.json'}

##################################
## Others
##################################
deploy=os.getenv('Deploy')
if deploy == None:
    deploy = 'ALL'
owner=os.getenv('Owner')
if owner == None:
    owner = 'admin'
owner_old=''

#disable warning
urllib3.disable_warnings()

# variable changed if script is run on Windows or Linux. "\\" for Windows, "/" for Linux
if Cookie == '':
    head = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8',
		'Authorization': 'Api-Token {}'.format(Token)
    }
else:
    head = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Api-Token {}'.format(Token),
	'X-CSRFToken': CSRF,
	'Cookie': Cookie
#	'X-CSRFToken': '0f453d68-2b4e-4f5a-b87b-f4c0275c5718|45|fca8afff-feb2-44e0-871d-ca4c9ab9f307',
#	'Cookie': 'p23mn32t=SD3VAX6WR66VXUUAU7LIBE45KE; _ga=GA1.2.744791516.1669713396; _gcl_au=1.1.1483745393.1669713397; _ft_info=%7B%22utm_campaign%22%3A%22none%22%2C%22utm_content%22%3A%22none%22%2C%22utm_medium%22%3A%22website%22%2C%22utm_source%22%3A%22organic%22%2C%22utm_term%22%3A%22none%22%2C%22vehicle_name%22%3A%22none%22%2C%22landingpage%22%3A%22https%3A//university.dynatrace.com/ondemand/course/35813/lab-guide/36056%22%2C%22original_referrer%22%3A%22none%22%7D; _mkto_trk=id:352-NVO-562&token:_mch-dynatrace.com-1669740604052-65143; _fbp=fb.1.1671175210700.1732259401; intercom-id-emeshyeu=c818a06d-de23-47a4-a74d-8c611c3a1b51; intercom-device-id-emeshyeu=10d3f99b-59af-476b-ac0a-13fd66c811ed; _BEAMER_USER_ID_bxOQALFw21023=409d1951-862e-49e9-b982-073e3ada46ee; _BEAMER_FIRST_VISIT_bxOQALFw21023=2023-01-03T16:25:37.997Z; _hp2_props.1080212440=%7B%22account_id%22%3A372179%2C%22screenSize%22%3A%221536x960%22%2C%22screenResolution%22%3A%221920x1200%22%2C%22playGodPrivileges%22%3A%22false%22%2C%22workloadPrivilege%22%3A%22None%22%7D; ajs_group_id=null; ajs_user_id=%2218010603186%22; ajs_anonymous_id=%22248ccbf9-4385-4386-8097-42512d4c865b%22; _BEAMER_LAST_POST_SHOWN_bxOQALFw21023=38399825; _BEAMER_BOOSTED_ANNOUNCEMENT_DATE_bxOQALFw21023=2023-01-03T16:25:39.751Z; _hp2_id.1080212440=%7B%22userId%22%3A%225038743151638933%22%2C%22pageviewId%22%3A%225287055961888428%22%2C%22sessionId%22%3A%228213715816639852%22%2C%22identity%22%3A%2218010603186%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; prexisthb=%7B%22utm_campaign%22%3A%22product-01-05-2023%22%2C%22utm_content%22%3A%22product-news-services-incident-update%22%2C%22utm_medium%22%3A%22email%22%2C%22utm_source%22%3A%22dynatrace%22%2C%22utm_term%22%3A%22none%22%2C%22vehicle_name%22%3A%22none%22%2C%22landingpage%22%3A%22https%3A//www.dynatrace.com/news/blog/services-incident-update/%22%2C%22original_referrer%22%3A%22https%3A//em.dynatrace.ai/%22%7D; BE_CLA3=p_id%3DALPPNPLPARL4RN666L6RNN4P8AAAAAAAAH%26bf%3D4a976c745367233fbec8301d3478aab5%26bn%3D2%26bv%3D3.44%26s_expire%3D1674290500623%26s_id%3DALPPNPLPARL4RLAPPARRNN4P8AAAAAAAAH; _uetvid=134da8207d1211eda46697d52b6a39f1; _gid=GA1.2.1367527116.1674411537; rxVisitor=16745048771923OD78TBLNQ2H1IAMKVDLBE1M98SOUJ2C; b925d32c=NMGSTQJHDCI6CIBA6WKA4Y2M4I; ssoCSRFCookie=eda505492d8124bb1a7cf46b3b4f2a1d2c6a47690eaa0e763c77708cceff25b9; JSESSIONID=node0efed1efptdz1o1ma4d6wi5dk10563252.node0; dtCookie=v_4_srv_7_sn_F680580D76BBB8FA03B9219C6D5843B7_perc_100000_ol_0_mul_1_app-3A9a85821213a24845_1_app-3A98ef57ca1ba5392b_1_app-3Abb68032936bb9776_1_app-3Aea7c4b59f27d43eb_1_app-3Acb22258e570f8ab9_1_app-3Af6b10dd0df01cfe1_1; apmsessionid=node01551fm36clk3enq9kpwpohvcb1739365.node0; dtSa=true%7CKD%7C-1%7CdQl-a%20dQl-o%20dQl-q%7C-%7C1674509514591%7C509475687_877%7Chttps%3A%2F%2Ffca8afff-feb2-44e0-871d-ca4c9ab9f307-45.managed.internal.dynatrace.com%3A8021%2Fe%2F83973fe4-b3e4-4617-8293-0c565e0abb17%2F%7C%7C%7Cdashboard%5Esid%3Dbbbbbbbb-a006-a017-0000-000000000001%5Esgf%3Dall%5Esgtf%3D-2h%7C%7C%23dashboard%7C1674509495227%7C%23dashboard%7Ci2%5Esk1%5Esh0%5Est3; rxvt=1674511317787|1674507323064; dtPC=7$509515156_646h-vUCUKCFOMRIMFURPVQLTCGQNGDPTPLJDJ-0e0; dtLatC=1'	
        }

    

##################################
## Generic Dynatrace API
##################################

# generic function GET to call API with a given uri
def queryDynatraceAPI(uri):
    jsonContent = None
    #print(head)
    response = requests.get(uri,headers=head)
    #print(response)
    # For successful API call, response code will be 200 (OK)
    if(response.ok):
        if(len(response.text) > 0):
            jsonContent = json.loads(response.text)
    else:
        jsonContent = json.loads(response.text)
        print(jsonContent)
        errorMessage = ""
        if(jsonContent["error"]):
            errorMessage = jsonContent["error"]["message"]
            print("Dynatrace API returned an error: " + errorMessage)
        jsonContent = None
        #raise Exception("Error", "Dynatrace API returned an error: " + errorMessage)

    return(jsonContent)

#generic function POST to call API with a given uri
def postDynatraceAPI(uri, payload):
    jsonContent = None
    response = requests.post(uri,headers=head,verify=False, json=payload)
    # For successful API call, response code will be 200 (OK)
    if(response.ok):
        if(len(response.text) > 0):
            jsonContent = json.loads(response.text)
            jsonContent="success"
    else:
        jsonContent = json.loads(response.text)
        print(jsonContent)
        errorMessage = ""
        if(jsonContent["error"]):
            errorMessage = jsonContent["error"]["message"]
            print("Dynatrace API returned an error: " + errorMessage)
        jsonContent = None
        #raise Exception("Error", "Dynatrace API returned an error: " + errorMessage)

    return(jsonContent)

#generic function PUT to call API with a given uri
def putDynatraceAPI(uri, payload):
    jsonContent = None
    #print(uri,head,payload)
    response = requests.put(uri,headers=head,verify=False, json=payload)
    # For successful API call, response code will be 200 (OK)
    if(response.ok):
        jsonContent="success"
    else:
        jsonContent = json.loads(response.text)
        print(jsonContent)
        errorMessage = ""
        if (jsonContent["error"]):
            errorMessage = jsonContent["error"]["message"]
            print("Dynatrace API returned an error: " + errorMessage)
        jsonContent = None
        #raise Exception("Error", "Dynatrace API returned an error: " + errorMessage)

    return(jsonContent)
   
##################################
## Get SLO Target
##################################
def getSLO(TENANT, TOKEN):
    for slo_filter in ['smarter', 'optimization']:
        uri=TENANT+APIslo+'?pageSize=100&sloSelector=text("'+slo_filter+'")&sort=name&timeFrame=CURRENT&demo=false&evaluate=false&enabledSlos=true&showGlobalSlos=true'

        #print(uri)
        datastore = queryDynatraceAPI(uri)
        #print(datastore)
        slos = datastore['slo']
        for slo in slos :
            if slo['name'] in SLO_target:
                if SLO_target[slo['name']] == '':
                    #print(slo['name'])
                    SLO_target[slo['name']]=slo['id']
            
    return()

def getDashboard(TENANT, TOKEN):
    global owner
    uri=TENANT+APIdashboard+'?tags=smarter'

    #print(uri+'?Api-Token='+Token)
    datastore = queryDynatraceAPI(uri)
    #print(datastore)
    dashboards = datastore['dashboards']
    for dashboard in dashboards :
        if dashboard['name'] in Dashboard_target:
            if Dashboard_target[dashboard['name']] == '':
                #print(dashboard['name'])
                Dashboard_target[dashboard['name']]=dashboard['id']
        owner_old=dashboard['owner']

    if owner == '' :
        owner == owner_old

    return()


def mappSloDashboard(TENANT, TOKEN):
    print('\nmapping slo')
    uri=TENANT+APIdashboard+'?tags=smarter'

    #print(uri)
    datastore = queryDynatraceAPI(uri)
    #print(datastore)
    dashboards = datastore['dashboards']
    deploy_dash=False
    for dashboard in dashboards :
            if dashboard['name'] in ['✔ SLO Simply Smarter', '✔ SLO Resource Optimization'] :

                uri=TENANT+APIdashboard+'/'+dashboard['id']
                datastore = queryDynatraceAPI(uri)
                #print(datastore)
                data=json.dumps(datastore)
                for i in SLO_source:
                    if SLO_target[i] != '':
                        data=re.sub(SLO_source[i], SLO_target[i], data)

                print(' mapping slo for ', dashboard['name'],dashboard['id'])
                putDynatraceAPI(uri,json.loads(data))
                deploy_dash=True

    if not deploy_dash:
        print(' no dashbaords, import Dynatrace: Simply Smarter or run this script with Deploy=ALL')
    
    return()

def updateSLO(TENANT, TOKEN):
    print('\nupdate slo')
    for slo in SLO_target:
        url='https://raw.githubusercontent.com/dynatrace-ace-services/slo-simply-smarter/main/SLOSimplySmarter/slo/'+slo.replace(' ','')+'.json'
        req = requests.get(url)
        payload=req.json()
        payload['name']=slo
        payload['id']=SLO_target[slo]
        
        print(' update', slo, SLO_target[slo])
        uri=TENANT+APIslo+'/'+SLO_target[slo]
        putDynatraceAPI(uri, payload)


    return()

def generateSLO(TENANT, TOKEN):
    print('\ndeploy slo')
    for slo in SLO_target:
        if SLO_target[slo] == '':
            url='https://raw.githubusercontent.com/dynatrace-ace-services/slo-simply-smarter/main/SLOSimplySmarter/slo/'+slo.replace(' ','')+'.json'
            req = requests.get(url)
            payload=req.json()
            payload['name']=slo
        
            print(' deploy', slo, SLO_target[slo])
            uri=TENANT+APIslo
            result=postDynatraceAPI(uri, payload)

    return()


def generateDashboard(TENANT, TOKEN):
    print('\ndeploy dashboards')
    global owner
    if owner == '' :
        owner = 'admin'

    for dashboard in Dashboard_target:
        if Dashboard_target[dashboard] == '':
            url='https://raw.githubusercontent.com/JLLormeau/dynatrace_template_fr/master/'+Dashboard_mapping_name[dashboard]
            req = requests.get(url)
            payload=req.json()
            payload['dashboardMetadata']['owner']=owner
            del payload['id']
    
            print(' deploy', dashboard, Dashboard_target[dashboard])
            uri=TENANT+APIdashboard
            result=postDynatraceAPI(uri, payload)
        else:
            url='https://raw.githubusercontent.com/JLLormeau/dynatrace_template_fr/master/'+Dashboard_mapping_name[dashboard]
            req = requests.get(url)
            payload=req.json()
            payload['dashboardMetadata']['owner']=owner
            payload['id']=Dashboard_target[dashboard]
    
            print(' deploy', dashboard, Dashboard_target[dashboard])
            uri=TENANT+APIdashboard+'/'+Dashboard_target[dashboard]
            result=putDynatraceAPI(uri, payload)
            
    return()

def mappDashboard(TENANT, TOKEN):
    global owner
    print('\nupdate dashboards')
    for dashboard in Dashboard_target: 
            uri=TENANT+APIdashboard+'/'+Dashboard_target[dashboard]
            datastore = queryDynatraceAPI(uri)
            #print(datastore)
            datastore['dashboardMetadata']['owner']=owner
            data=json.dumps(datastore)
            for i in Dashboard_source:
                if Dashboard_target[i] != '':
                        data=re.sub(Dashboard_source[i], Dashboard_target[i], data)
                        
            print(' update', dashboard, Dashboard_target[dashboard])
            uri=TENANT+APIdashboard+'/'+Dashboard_target[dashboard]
            putDynatraceAPI(uri, json.loads(data))
    print(' => with owner', owner)
            
    return()

##################################
## Main program
##################################
print("######## SLO Simply Smarter automatic deployment ")
print('\nvariables') 
print(' MyTenant', Tenant)
print(' MyToken', 'dt0c01.'+Token.split('.')[1]+'.*****')
print(' Deploy', deploy)
if Cookie != '' or CSRF != '' :
    print(' Temporary Cookie and CSRFToken from Mission Control')
    print('  Cookie', Cookie)
    print('  X-CSRFToken', CSRF)
if deploy != 'SLO' and deploy != 'slo' :
    print(' Owner', owner)
if Tenant == None :
    print('ERROR : MyTenant is empty')
    exit()
if Token == None :
    print('ERROR : MyToken is empty')
    exit()
if Cookie != '' :
    if CSRF == '' :
        print('ERROR : CSRFToken is empty')
        exit()
if CSRF != '' :
    if Cookie == '' :
        print('ERROR : Cookie is empty')
        exit()

#info dashboard
getDashboard(Tenant, Token)

#update dashboards
if deploy != 'SLO' and deploy != 'slo' :
    generateDashboard(Tenant, Token)
    getDashboard(Tenant, Token)
    mappDashboard(Tenant, Token)

#validate slo
getSLO(Tenant, Token)
generateSLO(Tenant, Token)
getSLO(Tenant, Token)

#mapping slo dashboards
mappSloDashboard(Tenant, Token)

#update slo and owner
if deploy != 'SLO' and deploy != 'slo' :
    updateSLO(Tenant, Token)
    

print('\nsimply smarter')
Home=Tenant+"/#dashboard;id="+Dashboard_target['🏠 Dynatrace: simply smarter']
print(' ',Home)
#################################
