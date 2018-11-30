RestEnz  
====  
***  
The RestEnz can treat DNA with restriction enzymes.  
Restriction Enzyme can cut DNA,which change end to blunt end or protruding end.  
Concretely, RestEnz can get specified restriction enzyme(need set up a server) and cut DNA using it.  
further great things, RestEnz created test！but codes to make restriction enzymes json is not created test.  
Thus, it is dangerous to use as it is！  
  
  
  
Setup  
====  
***  
## 1、Write API URL to the config.yml  
  
RestEnz load api url via config.yml.we will prepare the server by yourself.  
If you will use localhost, it can be executed with the following code.  
`php -S localhost:8080`  

### request method  
GETデータ  
  
|JSON Key|型|必須|検索条件|値の説明|
|:---|:---|:---|:---|:---|
|name|string|◯|完全一致|
  
返却データ  
  
|JSON Key|model|need|destription|
|:---|:---|:---|:---|:---| 
|name|string|◯| restriction_enzyme name|
|restriction_site|array|◯recognition sequence|
|  first|string|◯|ahead end when disconnected|
|  last|string|◯|later end when disconnected|
|  whole|string|◯|all of recognition sequence|
|total_site|int|◯|size of restriction_site|
  
## 2、load DNA file via BioPython  
DNA file can get [NCBI](https://www.ncbi.nlm.nih.gov).Details will be checked by yourself！  
  
  
License  
=====  
***  
All codes of this repository except library file are available under the MIT license. See the LICENSE for more information.
