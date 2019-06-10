![alt text]( https://www.captivateonhold.com/wp-content/uploads/2016/03/BroadWorks.jpg "Broadsoft")

[![PyPI pyversions](https://img.shields.io/pypi/status/BroadworksOCIP.svg)](https://pypi.org/project/BroadworksOCIP/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/BroadworksOCIP.svg)](https://pypi.python.org/pypi/BroadworksOCIP/)
[![PyPI license](https://img.shields.io/pypi/l/BroadworksOCIP.svg)](https://pypi.python.org/pypi/BroadworksOCIP/)
#  Broadworks OCI-P (Open Client Interface Provisioning) Client


## Broadworks Release Testing

Anyone is welcome to test the client against any untested releases and confirm the results

| Release        | Tested          |
| ------------- |:-------------:| 
|Release 20    | Yes |
|Release 21     | No  (Soon!)    |
|Release 22 | No      |
|Release 23|No|



## Usable OCI Calls

### System Level Calls

- SystemRoutingGetRequest
- SystemSoftwareVersionGetRequest
- SystemCodecGetListRequest

### Service Prvider Level Calls

- ServiceProviderGetListRequest
- ServiceProviderGetRequest17sp1

### Group Level Calls

Not Yet !

### User Level Calls

Not Yet !

## Login Level Calls

- AuthenticationRequest
- LoginRequest14sp4

## Installing

```bash

pip install BroadworksOCIP

```
## How to Use

```python
from BroadworksOCIP import Client
from BroadworksOCIP.broadworks.schema.request.system import SystemRoutingGetRequest

client = Client(username="user@broadsoft.com", password="supersecret", address="https://api.broadsoft.com/webservice/services/ProvisioningService")

client.login() 

response = client.send(SystemRoutingGetRequest())

response.is_route_round_robin()

```


 



