# Broadworks-OCI-P-Library
Broadworks OCI-P Client 

You must have access to the broadworks documentation to use this library 

## How to Use

```python

import BroadworksOCIP

ocip_connector = BroadworksOCIP.Ocip_lib("broadworks user Id","broadworks password","broadworks oci url")

ocip_connector.send("UserPortalPasscodeModifyRequest",userId="123456@domain.co.uk",newPasscode="123456")

```

If you look at the example above you need to specify the OCI call name and the needed xml tags.

the return data will be a dict containing all the info from OCIResponce 

## Supported Application Server OCI Calls 

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
- UserGetListInGroupRequest
- UserIntegratedIMPGeneratePasswordRequest
- UserPortalPasscodeModifyRequest
- SystemRoutingGetRequest
- SystemSoftwareVersionGetRequest
- SystemSIPGetContentTypeListRequest
- SystemSIPDeviceTypeGetListRequest
- SystemSIPDeviceTypeFileModifyRequest16sp1
- SystemCarrierGetListRequest
- SystemSIPDeviceTypeFileGetListRequest14sp8
- SystemRoutingProfileGetListRequest
- SystemRoutingGetTranslationListRequest
- SystemRoutingGetRouteListRequest
- SystemRoutingGetRouteDeviceListRequest
- SystemRedundancyParametersGetRequest16sp2
- SystemPortalPasscodeRulesGetRequest19
- SystemPortalAPIGetACLListRequest
- SystemPolicyGetDefaultRequest20
- SystemPasswordRulesGetRequest16
- SystemNetworkSynchingServerGetListRequest
- SystemSIPDeviceTypeFileGetRequest20
- UserAuthenticationModifyRequest
- UserCallForwardingNotReachableModifyRequest
- GroupModifyRequest
- GroupDnGetAvailableListRequest
- GroupCallProcessingGetPolicyRequest19sp1
- GroupCallProcessingModifyPolicyRequest15sp2
- UserVoiceMessagingUserModifyVoicePortalRequest20
- UserVoiceMessagingUserModifyAdvancedVoiceManagementRequest
- UserVoiceMessagingUserGetAdvancedVoiceManagementRequest14sp3
