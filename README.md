# SLO Simply Smarter & SLO Resource Optimization

## 1) Prerequisite : `Host Group` and `Management Zone` best practices

- [quickstart-ace-configurator](https://github.com/dynatrace-ace-services/quickstart-ace-configurator)

## 2) Import Dashboard `Dynatrace: Simply Smarter`
 - For Saas and Managed, use the [bizops configurator](https://dynatrace.github.io/BizOpsConfigurator/index.html#begin)  
 Prerequisite : create your [token](https://dynatrace.github.io/BizOpsConfigurator/index.html#prerequisites)
 
       https://dynatrace.github.io/BizOpsConfigurator/index.html#begin
       use your *tenant** and **token** (don't care with Source)
       connect
       deploy 
       .../ALL
       Dynatrace_Simply Smarter
       next
       advanced (you can define the owenr = admin)
       done
       
 
 ![image](https://user-images.githubusercontent.com/40337213/210232428-7de19b44-579a-4979-9e4e-6b9ef61bcc7a.png)  
 - For OffLine environment, follow the process [here](/Import_Dynatrace_Simply_Smarter_for_OffLine_environment.pdf)
 
## 3) Import `SLO template`
 - Use [monaco](https://dynatrace-oss.github.io/dynatrace-monitoring-as-code/)
 
 `installation`
 
       git clone https://github.com/dynatrace-ace-services/slo-simply-smarter
       cd slo-simply-smarter
       wget https://github.com/dynatrace-oss/dynatrace-monitoring-as-code/releases/latest/download/monaco-linux-amd64
       mv monaco-linux-amd64 monaco
       chmod +x monaco
       
`varaiables`

       export NEW_CLI=1
       export MyTenant=abcd123.live.dynatrace.com (without https://...)
       export MyToken=xxxx1234yyyy1234
       
`deploy`

       ./monaco deploy -e=environments.yaml SLOSimplySmarter
       
 ## 4) Mapp `SLO Simply Smarter` Dashboard with SLO
 
 For each SLO tile, mapp SLO Smarter and period
 
 `Application`
 
    Smarter - Application Performance => 1w, 1M and 1y
    Smarter - Browser Monitor Availability => 1w, 1M and 1y
    Smarter - HTTP Monitor Availability => 1w, 1M and 1y
    
`Webservice and Webrequest`
 
    Smarter - Service Performance => 1w, 1M and 1y
    Smarter - Service Availability => 1w, 1M and 1y
 
`Database`
 
    Smarter - Database Performance => 1w, 1M and 1y
    Smarter - Database Success Rate => 1w, 1M and 1y
       
![image](https://user-images.githubusercontent.com/40337213/210246167-71c63329-11f5-4f0b-9ba9-98c4485be86b.png)

## 5) Mapp `SLO Resource Optimization` Dashboard with SLO

`Memory`

    Optimization - Memory Usage => 1w, 1M and 1y
    
`CPU`

    Optimization - CPU Usage => 1w, 1M and 1y
    
`Disk`

    Optimization - Disk Usage => 1w, 1M and 1y    

![image](https://user-images.githubusercontent.com/40337213/210247317-06d3a1dd-331c-44ca-9c41-cc3d08249a2c.png)
     
  

    
    
 
 
 

  
