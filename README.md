# Dashboarding Dynatrace Simply Smarter

Fundamentals for deployment & configuration :  [fundamentals](https://github.com/dynatrace-ace-services/fundamentals/#readme) & [monaco example](https://github.com/dynatrace-ace-services/dynatrace-lab/tree/main/project)      
ITSM integration & SLO Quality of Service : [itsm-integration-with-slo](https://github.com/dynatrace-ace-services/itsm-integration-with-slo#readme) & [monaco-template](https://github.com/dynatrace-ace-services/itsm-integration-with-slo/tree/main/monaco-template#readme)    
✅ Dashboarding Dynatrace Simply Smarter : [slo-simply-smarter with monaco template](https://github.com/dynatrace-ace-services/slo-simply-smarter#readme)  

Demo (internal only): [https://demo.live.dynatrace.com](https://demo.live.dynatrace.com/#dashboard;gtf=-2h;gf=all;id=bbbbbbbb-a003-a017-0000-000000000133)

![image](https://user-images.githubusercontent.com/40337213/217482105-8ad929a7-ce7a-4a7e-b0c4-026886851441.png)

---
---

# Installation with `Monaco v2` (recommanded)

## 1) Prerequisites installation

- `Host Group` and `Management Zone` best practices with [Deployment best practices](https://github.com/dynatrace-ace-services/quickstart-ace-configurator)
- `ITSM integration` best practices with [ITSM integration & SLO Quality of Service](https://github.com/dynatrace-ace-services/easy-itsm-integration/blob/main/Readme.md)


## 2) Create an `APi-Token` with this scope :

 - Read configuration 
 - Write configuration
 - Read SLO
 - Write SLO
 - Access problem and event feed, metrics, and topology


## 3) Deploy with Monaco :

Documentation v2 [here](https://www.dynatrace.com/support/help/manage/configuration-as-code)  
Example for linux 

`installation`  
 
    git clone https://github.com/dynatrace-ace-services/slo-simply-smarter
    cd slo-simply-smarter
    curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-amd64 -o monaco
    chmod +x monaco
       
`variables`

    export DT_TENANT_URL=https://abcd123.live.dynatrace.com for saas or export MyTenant=https://domaine.com/e/abcd12234 for managed 
    export DT_API_TOKEN=dt0c01.1234ABCD.XXXX
       
`deploy`

    ./monaco deploy manifest.yaml
    
`result`

![image](https://user-images.githubusercontent.com/40337213/230628299-ace2a7f6-1555-4f18-b67d-3f184c83d9d0.png)
