# Broadworks-OCI-P-Library
Broadworks OCI-P Client 

You must have access to the broadworks documentation to use this library 

## How to Use

```python

import ocip_lib

ocip_connector = ocip_lib.Ocip_lib("broadworks user Id","broadworks password","broadworks oci url")

ocip_connector.send("UserPortalPasscodeModifyRequest",userId="123456@domain.co.uk",newPasscode="123456")

```

If you look at the example above you need to specify the OCI call name and the needed xml tags.

the return data will be a dict containing all the info from OCIResponce 

## Supported OCI Calls 

- ServiceProviderServicePackGetListRequest
- AuthenticationRequest
- LoginRequest14sp4
- ServiceProviderGetListRequest
- GroupGetListInServiceProviderRequest
- GroupServiceGetAuthorizationListRequest
- GroupAutoAttendantGetInstanceListRequest
- GroupHuntGroupGetInstanceListRequest
- GroupCallCenterGetInstanceListRequest
- GroupRoutePointGetInstanceListRequest
- GroupTrunkGroupGetInstanceListRequest14
- GroupFlexibleSeatingHostGetInstanceListRequest
- GroupVoiceXmlGetInstanceListRequest
- GroupGroupPagingGetInstanceListRequest
- GroupMeetMeConferencingGetInstanceListRequest
- GroupCallPickupGetInstanceListRequest
- GroupBroadWorksAnywhereGetInstanceListRequest
- GroupDnGetListRequest
- UserGetRequest20
- LogoutRequest
- UserVoiceMessagingUserModifyVoicePortalRequest20
- UserModifyRequest17sp4
- UserCallRecordingModifyRequest
- UserHotelingGuestModifyRequest
- UserHotelingHostModifyRequest
- UserIntegratedIMPModifyRequest
- UserIntegratedIMPGeneratePasswordRequest
- UserPortalPasscodeModifyRequest




