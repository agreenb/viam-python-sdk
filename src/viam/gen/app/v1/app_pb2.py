"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...tagger.v1 import tagger_pb2 as tagger_dot_v1_dot_tagger__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10app/v1/app.proto\x12\x0bviam.app.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16tagger/v1/tagger.proto"\xec\x02\n\x05Robot\x123\n\x02id\x18\x01 \x01(\tB#\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"R\x02id\x120\n\x04name\x18\x02 \x01(\tB\x1c\x9a\x84\x9e\x03\x17bson:"name" json:"name"R\x04name\x12@\n\x08location\x18\x03 \x01(\tB$\x9a\x84\x9e\x03\x1fbson:"location" json:"location"R\x08location\x12g\n\x0blast_access\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB*\x9a\x84\x9e\x03%bson:"last_access" json:"last_access"R\nlastAccess\x12Q\n\ncreated_on\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x16\x9a\x84\x9e\x03\x11bson:"created_on"R\tcreatedOn"\xd3\x07\n\tRobotPart\x123\n\x02id\x18\x01 \x01(\tB#\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"R\x02id\x120\n\x04name\x18\x02 \x01(\tB\x1c\x9a\x84\x9e\x03\x17bson:"name" json:"name"R\x04name\x12?\n\x08dns_name\x18\n \x01(\tB$\x9a\x84\x9e\x03\x1fbson:"dns_name" json:"dns_name"R\x07dnsName\x12B\n\x06secret\x18\x03 \x01(\tB*\x9a\x84\x9e\x03%bson:"secret" json:"secret,omitempty"R\x06secret\x124\n\x05robot\x18\x04 \x01(\tB\x1e\x9a\x84\x9e\x03\x19bson:"robot" json:"robot"R\x05robot\x12A\n\x0blocation_id\x18\x0c \x01(\tB \x9a\x84\x9e\x03\x1bbson:"location_id" json:"-"R\nlocationId\x12b\n\x0crobot_config\x18\x05 \x01(\x0b2\x17.google.protobuf.StructB&\x9a\x84\x9e\x03!bson:"config" json:"robot_config"R\x0brobotConfig\x12g\n\x0blast_access\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB*\x9a\x84\x9e\x03%bson:"last_access" json:"last_access"R\nlastAccess\x12\x7f\n\x12user_supplied_info\x18\x07 \x01(\x0b2\x17.google.protobuf.StructB8\x9a\x84\x9e\x033bson:"user_supplied_info" json:"user_supplied_info"R\x10userSuppliedInfo\x12C\n\tmain_part\x18\x08 \x01(\x08B&\x9a\x84\x9e\x03!bson:"main_part" json:"main_part"R\x08mainPart\x12\x12\n\x04fqdn\x18\t \x01(\tR\x04fqdn\x12\x1d\n\nlocal_fqdn\x18\x0b \x01(\tR\tlocalFqdn\x12Q\n\ncreated_on\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x16\x9a\x84\x9e\x03\x11bson:"created_on"R\tcreatedOn\x12H\n\x07secrets\x18\x0e \x03(\x0b2\x19.viam.app.v1.SharedSecretB\x13\x9a\x84\x9e\x03\x0ebson:"secrets"R\x07secrets"\x93\x02\n\x15RobotPartHistoryEntry\x120\n\x04part\x18\x01 \x01(\tB\x1c\x9a\x84\x9e\x03\x17bson:"part" json:"part"R\x04part\x124\n\x05robot\x18\x02 \x01(\tB\x1e\x9a\x84\x9e\x03\x19bson:"robot" json:"robot"R\x05robot\x12L\n\x04when\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\x9a\x84\x9e\x03\x17bson:"when" json:"when"R\x04when\x12D\n\x03old\x18\x04 \x01(\x0b2\x16.viam.app.v1.RobotPartB\x1a\x9a\x84\x9e\x03\x15bson:"old" json:"old"R\x03old"\x1a\n\x18ListOrganizationsRequest"\xde\x01\n\x0cOrganization\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x129\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedOn\x12)\n\x10public_namespace\x18\x04 \x01(\tR\x0fpublicNamespace\x12%\n\x0edefault_region\x18\x05 \x01(\tR\rdefaultRegion\x12\x15\n\x03cid\x18\x06 \x01(\tH\x00R\x03cid\x88\x01\x01B\x06\n\x04_cid"\xcf\x01\n\x12OrganizationMember\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x16\n\x06emails\x18\x02 \x03(\tR\x06emails\x129\n\ndate_added\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tdateAdded\x12>\n\nlast_login\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\tlastLogin\x88\x01\x01B\r\n\x0b_last_login"\\\n\x19ListOrganizationsResponse\x12?\n\rorganizations\x18\x01 \x03(\x0b2\x19.viam.app.v1.OrganizationR\rorganizations"\xaf\x01\n\x12OrganizationInvite\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x14\n\x05email\x18\x02 \x01(\tR\x05email\x129\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedOn\x12\x1f\n\x0brobot_count\x18\x04 \x01(\x03R\nrobotCount"/\n\x19CreateOrganizationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"[\n\x1aCreateOrganizationResponse\x12=\n\x0corganization\x18\x01 \x01(\x0b2\x19.viam.app.v1.OrganizationR\x0corganization"A\n\x16GetOrganizationRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId"X\n\x17GetOrganizationResponse\x12=\n\x0corganization\x18\x01 \x01(\x0b2\x19.viam.app.v1.OrganizationR\x0corganization"X\n+GetOrganizationNamespaceAvailabilityRequest\x12)\n\x10public_namespace\x18\x01 \x01(\tR\x0fpublicNamespace"L\n,GetOrganizationNamespaceAvailabilityResponse\x12\x1c\n\tavailable\x18\x01 \x01(\x08R\tavailable"\xf2\x01\n\x19UpdateOrganizationRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01\x12.\n\x10public_namespace\x18\x03 \x01(\tH\x01R\x0fpublicNamespace\x88\x01\x01\x12\x1b\n\x06region\x18\x04 \x01(\tH\x02R\x06region\x88\x01\x01\x12\x15\n\x03cid\x18\x05 \x01(\tH\x03R\x03cid\x88\x01\x01B\x07\n\x05_nameB\x13\n\x11_public_namespaceB\t\n\x07_regionB\x06\n\x04_cid"[\n\x1aUpdateOrganizationResponse\x12=\n\x0corganization\x18\x01 \x01(\x0b2\x19.viam.app.v1.OrganizationR\x0corganization"D\n\x19DeleteOrganizationRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId"\x1c\n\x1aDeleteOrganizationResponse"I\n\x1eListOrganizationMembersRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId"\xc0\x01\n\x1fListOrganizationMembersResponse\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x129\n\x07members\x18\x02 \x03(\x0b2\x1f.viam.app.v1.OrganizationMemberR\x07members\x129\n\x07invites\x18\x03 \x03(\x0b2\x1f.viam.app.v1.OrganizationInviteR\x07invites"\xa4\x01\n\x1fCreateOrganizationInviteRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x14\n\x05email\x18\x02 \x01(\tR\x05email\x12B\n\x0eauthorizations\x18\x03 \x03(\x0b2\x1a.viam.app.v1.AuthorizationR\x0eauthorizations"[\n CreateOrganizationInviteResponse\x127\n\x06invite\x18\x01 \x01(\x0b2\x1f.viam.app.v1.OrganizationInviteR\x06invite"\x8a\x02\n-UpdateOrganizationInviteAuthorizationsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x14\n\x05email\x18\x02 \x01(\tR\x05email\x12I\n\x12add_authorizations\x18\x03 \x03(\x0b2\x1a.viam.app.v1.AuthorizationR\x11addAuthorizations\x12O\n\x15remove_authorizations\x18\x04 \x03(\x0b2\x1a.viam.app.v1.AuthorizationR\x14removeAuthorizations"i\n.UpdateOrganizationInviteAuthorizationsResponse\x127\n\x06invite\x18\x01 \x01(\x0b2\x1f.viam.app.v1.OrganizationInviteR\x06invite"`\n\x1fDeleteOrganizationInviteRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x14\n\x05email\x18\x02 \x01(\tR\x05email""\n DeleteOrganizationInviteResponse"`\n\x1fResendOrganizationInviteRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x14\n\x05email\x18\x02 \x01(\tR\x05email"[\n ResendOrganizationInviteResponse\x127\n\x06invite\x18\x01 \x01(\x0b2\x1f.viam.app.v1.OrganizationInviteR\x06invite"c\n\x1fDeleteOrganizationMemberRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId""\n DeleteOrganizationMemberResponse"Y\n\x14LocationOrganization\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x18\n\x07primary\x18\x02 \x01(\x08R\x07primary"\x80\x01\n\x0cLocationAuth\x12\x1a\n\x06secret\x18\x01 \x01(\tB\x02\x18\x01R\x06secret\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId\x123\n\x07secrets\x18\x03 \x03(\x0b2\x19.viam.app.v1.SharedSecretR\x07secrets"\'\n\rStorageConfig\x12\x16\n\x06region\x18\x01 \x01(\tR\x06region"\xe4\x02\n\x08Location\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12,\n\x12parent_location_id\x18\x04 \x01(\tR\x10parentLocationId\x12-\n\x04auth\x18\x05 \x01(\x0b2\x19.viam.app.v1.LocationAuthR\x04auth\x12G\n\rorganizations\x18\x06 \x03(\x0b2!.viam.app.v1.LocationOrganizationR\rorganizations\x129\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedOn\x12\x1f\n\x0brobot_count\x18\x07 \x01(\x05R\nrobotCount\x122\n\x06config\x18\x08 \x01(\x0b2\x1a.viam.app.v1.StorageConfigR\x06config"\xd0\x02\n\x0cSharedSecret\x12\x1e\n\x02id\x18\x01 \x01(\tB\x0e\x9a\x84\x9e\x03\tbson:"id"R\x02id\x12*\n\x06secret\x18\x02 \x01(\tB\x12\x9a\x84\x9e\x03\rbson:"secret"R\x06secret\x12c\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB(\x9a\x84\x9e\x03#bson:"created_on" json:"created_on"R\tcreatedOn\x12H\n\x05state\x18\x04 \x01(\x0e2\x1f.viam.app.v1.SharedSecret.StateB\x11\x9a\x84\x9e\x03\x0cbson:"state"R\x05state"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x11\n\rSTATE_ENABLED\x10\x01\x12\x12\n\x0eSTATE_DISABLED\x10\x02"\x9e\x01\n\x15CreateLocationRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x121\n\x12parent_location_id\x18\x03 \x01(\tH\x00R\x10parentLocationId\x88\x01\x01B\x15\n\x13_parent_location_id"K\n\x16CreateLocationResponse\x121\n\x08location\x18\x01 \x01(\x0b2\x15.viam.app.v1.LocationR\x08location"5\n\x12GetLocationRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId"H\n\x13GetLocationResponse\x121\n\x08location\x18\x01 \x01(\x0b2\x15.viam.app.v1.LocationR\x08location"\xcc\x01\n\x15UpdateLocationRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01\x121\n\x12parent_location_id\x18\x03 \x01(\tH\x01R\x10parentLocationId\x88\x01\x01\x12\x1b\n\x06region\x18\x04 \x01(\tH\x02R\x06region\x88\x01\x01B\x07\n\x05_nameB\x15\n\x13_parent_location_idB\t\n\x07_region"K\n\x16UpdateLocationResponse\x121\n\x08location\x18\x01 \x01(\x0b2\x15.viam.app.v1.LocationR\x08location"8\n\x15DeleteLocationRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId"\x18\n\x16DeleteLocationResponse"?\n\x14ListLocationsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId"`\n\x14ShareLocationRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId\x12\'\n\x0forganization_id\x18\x02 \x01(\tR\x0eorganizationId"\x17\n\x15ShareLocationResponse"b\n\x16UnshareLocationRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId\x12\'\n\x0forganization_id\x18\x02 \x01(\tR\x0eorganizationId"\x19\n\x17UnshareLocationResponse"L\n\x15ListLocationsResponse\x123\n\tlocations\x18\x01 \x03(\x0b2\x15.viam.app.v1.LocationR\tlocations">\n\x1bCreateLocationSecretRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId"M\n\x1cCreateLocationSecretResponse\x12-\n\x04auth\x18\x01 \x01(\x0b2\x19.viam.app.v1.LocationAuthR\x04auth"[\n\x1bDeleteLocationSecretRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId\x12\x1b\n\tsecret_id\x18\x02 \x01(\tR\x08secretId"\x1e\n\x1cDeleteLocationSecretResponse"6\n\x13LocationAuthRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId"E\n\x14LocationAuthResponse\x12-\n\x04auth\x18\x01 \x01(\x0b2\x19.viam.app.v1.LocationAuthR\x04auth"!\n\x0fGetRobotRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"4\n\x1bGetRoverRentalRobotsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\x9a\x01\n\x10RoverRentalRobot\x12\x19\n\x08robot_id\x18\x01 \x01(\tR\x07robotId\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId\x12\x1d\n\nrobot_name\x18\x03 \x01(\tR\trobotName\x12+\n\x12robot_main_part_id\x18\x04 \x01(\tR\x0frobotMainPartId"U\n\x1cGetRoverRentalRobotsResponse\x125\n\x06robots\x18\x01 \x03(\x0b2\x1d.viam.app.v1.RoverRentalRobotR\x06robots"<\n\x10GetRobotResponse\x12(\n\x05robot\x18\x01 \x01(\x0b2\x12.viam.app.v1.RobotR\x05robot"1\n\x14GetRobotPartsRequest\x12\x19\n\x08robot_id\x18\x01 \x01(\tR\x07robotId"E\n\x15GetRobotPartsResponse\x12,\n\x05parts\x18\x01 \x03(\x0b2\x16.viam.app.v1.RobotPartR\x05parts"%\n\x13GetRobotPartRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"c\n\x14GetRobotPartResponse\x12*\n\x04part\x18\x01 \x01(\x0b2\x16.viam.app.v1.RobotPartR\x04part\x12\x1f\n\x0bconfig_json\x18\x02 \x01(\tR\nconfigJson"\xa5\x01\n\x17GetRobotPartLogsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1f\n\x0berrors_only\x18\x02 \x01(\x08R\nerrorsOnly\x12\x1b\n\x06filter\x18\x03 \x01(\tH\x00R\x06filter\x88\x01\x01\x12"\n\npage_token\x18\x04 \x01(\tH\x01R\tpageToken\x88\x01\x01B\t\n\x07_filterB\r\n\x0b_page_token"\x97\x02\n\x08LogEntry\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x14\n\x05level\x18\x02 \x01(\tR\x05level\x12.\n\x04time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\x04time\x12\x1f\n\x0blogger_name\x18\x04 \x01(\tR\nloggerName\x12\x18\n\x07message\x18\x05 \x01(\tR\x07message\x12/\n\x06caller\x18\x06 \x01(\x0b2\x17.google.protobuf.StructR\x06caller\x12\x14\n\x05stack\x18\x07 \x01(\tR\x05stack\x12/\n\x06fields\x18\x08 \x03(\x0b2\x17.google.protobuf.StructR\x06fields"m\n\x18GetRobotPartLogsResponse\x12)\n\x04logs\x18\x01 \x03(\x0b2\x15.viam.app.v1.LogEntryR\x04logs\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken"s\n\x18TailRobotPartLogsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1f\n\x0berrors_only\x18\x02 \x01(\x08R\nerrorsOnly\x12\x1b\n\x06filter\x18\x03 \x01(\tH\x00R\x06filter\x88\x01\x01B\t\n\x07_filter"F\n\x19TailRobotPartLogsResponse\x12)\n\x04logs\x18\x01 \x03(\x0b2\x15.viam.app.v1.LogEntryR\x04logs",\n\x1aGetRobotPartHistoryRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"[\n\x1bGetRobotPartHistoryResponse\x12<\n\x07history\x18\x01 \x03(\x0b2".viam.app.v1.RobotPartHistoryEntryR\x07history"x\n\x16UpdateRobotPartRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12:\n\x0crobot_config\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x0brobotConfig"E\n\x17UpdateRobotPartResponse\x12*\n\x04part\x18\x01 \x01(\x0b2\x16.viam.app.v1.RobotPartR\x04part"M\n\x13NewRobotPartRequest\x12\x19\n\x08robot_id\x18\x01 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x02 \x01(\tR\x08partName"/\n\x14NewRobotPartResponse\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId"1\n\x16DeleteRobotPartRequest\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId"\x19\n\x17DeleteRobotPartResponse"\xe8\x04\n\x08Fragment\x123\n\x02id\x18\x01 \x01(\tB#\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"R\x02id\x120\n\x04name\x18\x02 \x01(\tB\x1c\x9a\x84\x9e\x03\x17bson:"name" json:"name"R\x04name\x12Y\n\x08fragment\x18\x03 \x01(\x0b2\x17.google.protobuf.StructB$\x9a\x84\x9e\x03\x1fbson:"fragment" json:"fragment"R\x08fragment\x12Z\n\x12organization_owner\x18\x04 \x01(\tB+\x9a\x84\x9e\x03&bson:"organization_owner" json:"owner"R\x11organizationOwner\x128\n\x06public\x18\x05 \x01(\x08B \x9a\x84\x9e\x03\x1bbson:"public" json:"public"R\x06public\x12Q\n\ncreated_on\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x16\x9a\x84\x9e\x03\x11bson:"created_on"R\tcreatedOn\x12+\n\x11organization_name\x18\x07 \x01(\tR\x10organizationName\x12(\n\x10robot_part_count\x18\t \x01(\x05R\x0erobotPartCount\x12-\n\x12organization_count\x18\n \x01(\x05R\x11organizationCount\x12+\n\x12only_used_by_owner\x18\x0b \x01(\x08R\x0fonlyUsedByOwner"`\n\x14ListFragmentsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x1f\n\x0bshow_public\x18\x02 \x01(\x08R\nshowPublic"L\n\x15ListFragmentsResponse\x123\n\tfragments\x18\x01 \x03(\x0b2\x15.viam.app.v1.FragmentR\tfragments"$\n\x12GetFragmentRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"H\n\x13GetFragmentResponse\x121\n\x08fragment\x18\x01 \x01(\x0b2\x15.viam.app.v1.FragmentR\x08fragment"\x85\x01\n\x15CreateFragmentRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12/\n\x06config\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x06config\x12\'\n\x0forganization_id\x18\x03 \x01(\tR\x0eorganizationId"K\n\x16CreateFragmentResponse\x121\n\x08fragment\x18\x01 \x01(\x0b2\x15.viam.app.v1.FragmentR\x08fragment"\x94\x01\n\x15UpdateFragmentRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12/\n\x06config\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x06config\x12\x1b\n\x06public\x18\x04 \x01(\x08H\x00R\x06public\x88\x01\x01B\t\n\x07_public"K\n\x16UpdateFragmentResponse\x121\n\x08fragment\x18\x01 \x01(\x0b2\x15.viam.app.v1.FragmentR\x08fragment"\'\n\x15DeleteFragmentRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x18\n\x16DeleteFragmentResponse"4\n\x11ListRobotsRequest\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId"@\n\x12ListRobotsResponse\x12*\n\x06robots\x18\x01 \x03(\x0b2\x12.viam.app.v1.RobotR\x06robots"A\n\x0fNewRobotRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1a\n\x08location\x18\x02 \x01(\tR\x08location""\n\x10NewRobotResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"T\n\x12UpdateRobotRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1a\n\x08location\x18\x03 \x01(\tR\x08location"?\n\x13UpdateRobotResponse\x12(\n\x05robot\x18\x01 \x01(\x0b2\x12.viam.app.v1.RobotR\x05robot"$\n\x12DeleteRobotRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x15\n\x13DeleteRobotResponse"0\n\x15MarkPartAsMainRequest\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId"\x18\n\x16MarkPartAsMainResponse"4\n\x19MarkPartForRestartRequest\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId"\x1c\n\x1aMarkPartForRestartResponse"7\n\x1cCreateRobotPartSecretRequest\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId"K\n\x1dCreateRobotPartSecretResponse\x12*\n\x04part\x18\x01 \x01(\x0b2\x16.viam.app.v1.RobotPartR\x04part"T\n\x1cDeleteRobotPartSecretRequest\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId\x12\x1b\n\tsecret_id\x18\x02 \x01(\tR\x08secretId"\x1f\n\x1dDeleteRobotPartSecretResponse"\x9e\x02\n\rAuthorization\x12-\n\x12authorization_type\x18\x01 \x01(\tR\x11authorizationType\x12)\n\x10authorization_id\x18\x02 \x01(\tR\x0fauthorizationId\x12#\n\rresource_type\x18\x03 \x01(\tR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x04 \x01(\tR\nresourceId\x12\x1f\n\x0bidentity_id\x18\x05 \x01(\tR\nidentityId\x12\'\n\x0forganization_id\x18\x06 \x01(\tR\x0eorganizationId\x12#\n\ridentity_type\x18\x07 \x01(\tR\x0cidentityType"R\n\x0eAddRoleRequest\x12@\n\rauthorization\x18\x01 \x01(\x0b2\x1a.viam.app.v1.AuthorizationR\rauthorization"\x11\n\x0fAddRoleResponse"U\n\x11RemoveRoleRequest\x12@\n\rauthorization\x18\x01 \x01(\x0b2\x1a.viam.app.v1.AuthorizationR\rauthorization"\x14\n\x12RemoveRoleResponse"\xa5\x01\n\x11ChangeRoleRequest\x12G\n\x11old_authorization\x18\x01 \x01(\x0b2\x1a.viam.app.v1.AuthorizationR\x10oldAuthorization\x12G\n\x11new_authorization\x18\x02 \x01(\x0b2\x1a.viam.app.v1.AuthorizationR\x10newAuthorization"\x14\n\x12ChangeRoleResponse"g\n\x19ListAuthorizationsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12!\n\x0cresource_ids\x18\x02 \x03(\tR\x0bresourceIds"`\n\x1aListAuthorizationsResponse\x12B\n\x0eauthorizations\x18\x01 \x03(\x0b2\x1a.viam.app.v1.AuthorizationR\x0eauthorizations"_\n\x17CheckPermissionsRequest\x12D\n\x0bpermissions\x18\x01 \x03(\x0b2".viam.app.v1.AuthorizedPermissionsR\x0bpermissions"\x7f\n\x15AuthorizedPermissions\x12#\n\rresource_type\x18\x01 \x01(\tR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\x12 \n\x0bpermissions\x18\x03 \x03(\tR\x0bpermissions"u\n\x18CheckPermissionsResponse\x12Y\n\x16authorized_permissions\x18\x01 \x03(\x0b2".viam.app.v1.AuthorizedPermissionsR\x15authorizedPermissions"R\n\x13CreateModuleRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name"E\n\x14CreateModuleResponse\x12\x1b\n\tmodule_id\x18\x01 \x01(\tR\x08moduleId\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url"\xad\x02\n\x13UpdateModuleRequest\x12\x1b\n\tmodule_id\x18\x01 \x01(\tR\x08moduleId\x12,\n\x0forganization_id\x18\x07 \x01(\tH\x00R\x0eorganizationId\x88\x01\x01\x127\n\nvisibility\x18\x02 \x01(\x0e2\x17.viam.app.v1.VisibilityR\nvisibility\x12\x10\n\x03url\x18\x03 \x01(\tR\x03url\x12 \n\x0bdescription\x18\x04 \x01(\tR\x0bdescription\x12*\n\x06models\x18\x05 \x03(\x0b2\x12.viam.app.v1.ModelR\x06models\x12\x1e\n\nentrypoint\x18\x06 \x01(\tR\nentrypointB\x12\n\x10_organization_id"(\n\x14UpdateModuleResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url"/\n\x05Model\x12\x10\n\x03api\x18\x01 \x01(\tR\x03api\x12\x14\n\x05model\x18\x02 \x01(\tR\x05model"\xa5\x01\n\x0eModuleFileInfo\x12\x1b\n\tmodule_id\x18\x01 \x01(\tR\x08moduleId\x12,\n\x0forganization_id\x18\x04 \x01(\tH\x00R\x0eorganizationId\x88\x01\x01\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12\x1a\n\x08platform\x18\x03 \x01(\tR\x08platformB\x12\n\x10_organization_id"\x87\x01\n\x17UploadModuleFileRequest\x12G\n\x10module_file_info\x18\x01 \x01(\x0b2\x1b.viam.app.v1.ModuleFileInfoH\x00R\x0emoduleFileInfo\x12\x14\n\x04file\x18\x02 \x01(\x0cH\x00R\x04fileB\r\n\x0bmodule_file",\n\x18UploadModuleFileResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url"q\n\x10GetModuleRequest\x12\x1b\n\tmodule_id\x18\x01 \x01(\tR\x08moduleId\x12,\n\x0forganization_id\x18\x02 \x01(\tH\x00R\x0eorganizationId\x88\x01\x01B\x12\n\x10_organization_id"@\n\x11GetModuleResponse\x12+\n\x06module\x18\x01 \x01(\x0b2\x13.viam.app.v1.ModuleR\x06module"\xe5\x03\n\x06Module\x12\x1b\n\tmodule_id\x18\x01 \x01(\tR\x08moduleId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x127\n\nvisibility\x18\x03 \x01(\x0e2\x17.viam.app.v1.VisibilityR\nvisibility\x127\n\x08versions\x18\x04 \x03(\x0b2\x1b.viam.app.v1.VersionHistoryR\x08versions\x12\x10\n\x03url\x18\x05 \x01(\tR\x03url\x12 \n\x0bdescription\x18\x06 \x01(\tR\x0bdescription\x12*\n\x06models\x18\x07 \x03(\x0b2\x12.viam.app.v1.ModelR\x06models\x12*\n\x11total_robot_usage\x18\x08 \x01(\x03R\x0ftotalRobotUsage\x128\n\x18total_organization_usage\x18\t \x01(\x03R\x16totalOrganizationUsage\x12\'\n\x0forganization_id\x18\n \x01(\tR\x0eorganizationId\x12\x1e\n\nentrypoint\x18\x0b \x01(\tR\nentrypoint\x12)\n\x10public_namespace\x18\x0c \x01(\tR\x0fpublicNamespace"\xa2\x01\n\x0eVersionHistory\x12\x18\n\x07version\x18\x01 \x01(\tR\x07version\x12*\n\x05files\x18\x02 \x03(\x0b2\x14.viam.app.v1.UploadsR\x05files\x12*\n\x06models\x18\x03 \x03(\x0b2\x12.viam.app.v1.ModelR\x06models\x12\x1e\n\nentrypoint\x18\x04 \x01(\tR\nentrypoint"b\n\x07Uploads\x12\x1a\n\x08platform\x18\x01 \x01(\tR\x08platform\x12;\n\x0buploaded_at\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\nuploadedAt"V\n\x12ListModulesRequest\x12,\n\x0forganization_id\x18\x01 \x01(\tH\x00R\x0eorganizationId\x88\x01\x01B\x12\n\x10_organization_id"D\n\x13ListModulesResponse\x12-\n\x07modules\x18\x01 \x03(\x0b2\x13.viam.app.v1.ModuleR\x07modules"/\n\x17GetUserIDByEmailRequest\x12\x14\n\x05email\x18\x01 \x01(\tR\x05email"3\n\x18GetUserIDByEmailResponse\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId"9\n\x1eListOrganizationsByUserRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId">\n\nOrgDetails\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x19\n\x08org_name\x18\x02 \x01(\tR\x07orgName"N\n\x1fListOrganizationsByUserResponse\x12+\n\x04orgs\x18\x01 \x03(\x0b2\x17.viam.app.v1.OrgDetailsR\x04orgs"j\n\x10CreateKeyRequest\x12B\n\x0eauthorizations\x18\x01 \x03(\x0b2\x1a.viam.app.v1.AuthorizationR\x0eauthorizations\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name"5\n\x11CreateKeyResponse\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id*W\n\nVisibility\x12\x1a\n\x16VISIBILITY_UNSPECIFIED\x10\x00\x12\x16\n\x12VISIBILITY_PRIVATE\x10\x01\x12\x15\n\x11VISIBILITY_PUBLIC\x10\x022\xf7+\n\nAppService\x12_\n\x10GetUserIDByEmail\x12$.viam.app.v1.GetUserIDByEmailRequest\x1a%.viam.app.v1.GetUserIDByEmailResponse\x12e\n\x12CreateOrganization\x12&.viam.app.v1.CreateOrganizationRequest\x1a\'.viam.app.v1.CreateOrganizationResponse\x12b\n\x11ListOrganizations\x12%.viam.app.v1.ListOrganizationsRequest\x1a&.viam.app.v1.ListOrganizationsResponse\x12t\n\x17ListOrganizationsByUser\x12+.viam.app.v1.ListOrganizationsByUserRequest\x1a,.viam.app.v1.ListOrganizationsByUserResponse\x12\\\n\x0fGetOrganization\x12#.viam.app.v1.GetOrganizationRequest\x1a$.viam.app.v1.GetOrganizationResponse\x12\x9b\x01\n$GetOrganizationNamespaceAvailability\x128.viam.app.v1.GetOrganizationNamespaceAvailabilityRequest\x1a9.viam.app.v1.GetOrganizationNamespaceAvailabilityResponse\x12e\n\x12UpdateOrganization\x12&.viam.app.v1.UpdateOrganizationRequest\x1a\'.viam.app.v1.UpdateOrganizationResponse\x12e\n\x12DeleteOrganization\x12&.viam.app.v1.DeleteOrganizationRequest\x1a\'.viam.app.v1.DeleteOrganizationResponse\x12t\n\x17ListOrganizationMembers\x12+.viam.app.v1.ListOrganizationMembersRequest\x1a,.viam.app.v1.ListOrganizationMembersResponse\x12w\n\x18CreateOrganizationInvite\x12,.viam.app.v1.CreateOrganizationInviteRequest\x1a-.viam.app.v1.CreateOrganizationInviteResponse\x12\xa1\x01\n&UpdateOrganizationInviteAuthorizations\x12:.viam.app.v1.UpdateOrganizationInviteAuthorizationsRequest\x1a;.viam.app.v1.UpdateOrganizationInviteAuthorizationsResponse\x12w\n\x18DeleteOrganizationMember\x12,.viam.app.v1.DeleteOrganizationMemberRequest\x1a-.viam.app.v1.DeleteOrganizationMemberResponse\x12w\n\x18DeleteOrganizationInvite\x12,.viam.app.v1.DeleteOrganizationInviteRequest\x1a-.viam.app.v1.DeleteOrganizationInviteResponse\x12w\n\x18ResendOrganizationInvite\x12,.viam.app.v1.ResendOrganizationInviteRequest\x1a-.viam.app.v1.ResendOrganizationInviteResponse\x12Y\n\x0eCreateLocation\x12".viam.app.v1.CreateLocationRequest\x1a#.viam.app.v1.CreateLocationResponse\x12P\n\x0bGetLocation\x12\x1f.viam.app.v1.GetLocationRequest\x1a .viam.app.v1.GetLocationResponse\x12Y\n\x0eUpdateLocation\x12".viam.app.v1.UpdateLocationRequest\x1a#.viam.app.v1.UpdateLocationResponse\x12Y\n\x0eDeleteLocation\x12".viam.app.v1.DeleteLocationRequest\x1a#.viam.app.v1.DeleteLocationResponse\x12V\n\rListLocations\x12!.viam.app.v1.ListLocationsRequest\x1a".viam.app.v1.ListLocationsResponse\x12V\n\rShareLocation\x12!.viam.app.v1.ShareLocationRequest\x1a".viam.app.v1.ShareLocationResponse\x12\\\n\x0fUnshareLocation\x12#.viam.app.v1.UnshareLocationRequest\x1a$.viam.app.v1.UnshareLocationResponse\x12S\n\x0cLocationAuth\x12 .viam.app.v1.LocationAuthRequest\x1a!.viam.app.v1.LocationAuthResponse\x12k\n\x14CreateLocationSecret\x12(.viam.app.v1.CreateLocationSecretRequest\x1a).viam.app.v1.CreateLocationSecretResponse\x12k\n\x14DeleteLocationSecret\x12(.viam.app.v1.DeleteLocationSecretRequest\x1a).viam.app.v1.DeleteLocationSecretResponse\x12G\n\x08GetRobot\x12\x1c.viam.app.v1.GetRobotRequest\x1a\x1d.viam.app.v1.GetRobotResponse\x12k\n\x14GetRoverRentalRobots\x12(.viam.app.v1.GetRoverRentalRobotsRequest\x1a).viam.app.v1.GetRoverRentalRobotsResponse\x12V\n\rGetRobotParts\x12!.viam.app.v1.GetRobotPartsRequest\x1a".viam.app.v1.GetRobotPartsResponse\x12S\n\x0cGetRobotPart\x12 .viam.app.v1.GetRobotPartRequest\x1a!.viam.app.v1.GetRobotPartResponse\x12_\n\x10GetRobotPartLogs\x12$.viam.app.v1.GetRobotPartLogsRequest\x1a%.viam.app.v1.GetRobotPartLogsResponse\x12d\n\x11TailRobotPartLogs\x12%.viam.app.v1.TailRobotPartLogsRequest\x1a&.viam.app.v1.TailRobotPartLogsResponse0\x01\x12h\n\x13GetRobotPartHistory\x12\'.viam.app.v1.GetRobotPartHistoryRequest\x1a(.viam.app.v1.GetRobotPartHistoryResponse\x12\\\n\x0fUpdateRobotPart\x12#.viam.app.v1.UpdateRobotPartRequest\x1a$.viam.app.v1.UpdateRobotPartResponse\x12S\n\x0cNewRobotPart\x12 .viam.app.v1.NewRobotPartRequest\x1a!.viam.app.v1.NewRobotPartResponse\x12\\\n\x0fDeleteRobotPart\x12#.viam.app.v1.DeleteRobotPartRequest\x1a$.viam.app.v1.DeleteRobotPartResponse\x12Y\n\x0eMarkPartAsMain\x12".viam.app.v1.MarkPartAsMainRequest\x1a#.viam.app.v1.MarkPartAsMainResponse\x12e\n\x12MarkPartForRestart\x12&.viam.app.v1.MarkPartForRestartRequest\x1a\'.viam.app.v1.MarkPartForRestartResponse\x12n\n\x15CreateRobotPartSecret\x12).viam.app.v1.CreateRobotPartSecretRequest\x1a*.viam.app.v1.CreateRobotPartSecretResponse\x12n\n\x15DeleteRobotPartSecret\x12).viam.app.v1.DeleteRobotPartSecretRequest\x1a*.viam.app.v1.DeleteRobotPartSecretResponse\x12M\n\nListRobots\x12\x1e.viam.app.v1.ListRobotsRequest\x1a\x1f.viam.app.v1.ListRobotsResponse\x12G\n\x08NewRobot\x12\x1c.viam.app.v1.NewRobotRequest\x1a\x1d.viam.app.v1.NewRobotResponse\x12P\n\x0bUpdateRobot\x12\x1f.viam.app.v1.UpdateRobotRequest\x1a .viam.app.v1.UpdateRobotResponse\x12P\n\x0bDeleteRobot\x12\x1f.viam.app.v1.DeleteRobotRequest\x1a .viam.app.v1.DeleteRobotResponse\x12V\n\rListFragments\x12!.viam.app.v1.ListFragmentsRequest\x1a".viam.app.v1.ListFragmentsResponse\x12P\n\x0bGetFragment\x12\x1f.viam.app.v1.GetFragmentRequest\x1a .viam.app.v1.GetFragmentResponse\x12Y\n\x0eCreateFragment\x12".viam.app.v1.CreateFragmentRequest\x1a#.viam.app.v1.CreateFragmentResponse\x12Y\n\x0eUpdateFragment\x12".viam.app.v1.UpdateFragmentRequest\x1a#.viam.app.v1.UpdateFragmentResponse\x12Y\n\x0eDeleteFragment\x12".viam.app.v1.DeleteFragmentRequest\x1a#.viam.app.v1.DeleteFragmentResponse\x12D\n\x07AddRole\x12\x1b.viam.app.v1.AddRoleRequest\x1a\x1c.viam.app.v1.AddRoleResponse\x12M\n\nRemoveRole\x12\x1e.viam.app.v1.RemoveRoleRequest\x1a\x1f.viam.app.v1.RemoveRoleResponse\x12M\n\nChangeRole\x12\x1e.viam.app.v1.ChangeRoleRequest\x1a\x1f.viam.app.v1.ChangeRoleResponse\x12e\n\x12ListAuthorizations\x12&.viam.app.v1.ListAuthorizationsRequest\x1a\'.viam.app.v1.ListAuthorizationsResponse\x12_\n\x10CheckPermissions\x12$.viam.app.v1.CheckPermissionsRequest\x1a%.viam.app.v1.CheckPermissionsResponse\x12S\n\x0cCreateModule\x12 .viam.app.v1.CreateModuleRequest\x1a!.viam.app.v1.CreateModuleResponse\x12S\n\x0cUpdateModule\x12 .viam.app.v1.UpdateModuleRequest\x1a!.viam.app.v1.UpdateModuleResponse\x12a\n\x10UploadModuleFile\x12$.viam.app.v1.UploadModuleFileRequest\x1a%.viam.app.v1.UploadModuleFileResponse(\x01\x12J\n\tGetModule\x12\x1d.viam.app.v1.GetModuleRequest\x1a\x1e.viam.app.v1.GetModuleResponse\x12P\n\x0bListModules\x12\x1f.viam.app.v1.ListModulesRequest\x1a .viam.app.v1.ListModulesResponse\x12J\n\tCreateKey\x12\x1d.viam.app.v1.CreateKeyRequest\x1a\x1e.viam.app.v1.CreateKeyResponseB\x18Z\x16go.viam.com/api/app/v1b\x06proto3')
_VISIBILITY = DESCRIPTOR.enum_types_by_name['Visibility']
Visibility = enum_type_wrapper.EnumTypeWrapper(_VISIBILITY)
VISIBILITY_UNSPECIFIED = 0
VISIBILITY_PRIVATE = 1
VISIBILITY_PUBLIC = 2
_ROBOT = DESCRIPTOR.message_types_by_name['Robot']
_ROBOTPART = DESCRIPTOR.message_types_by_name['RobotPart']
_ROBOTPARTHISTORYENTRY = DESCRIPTOR.message_types_by_name['RobotPartHistoryEntry']
_LISTORGANIZATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListOrganizationsRequest']
_ORGANIZATION = DESCRIPTOR.message_types_by_name['Organization']
_ORGANIZATIONMEMBER = DESCRIPTOR.message_types_by_name['OrganizationMember']
_LISTORGANIZATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListOrganizationsResponse']
_ORGANIZATIONINVITE = DESCRIPTOR.message_types_by_name['OrganizationInvite']
_CREATEORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['CreateOrganizationRequest']
_CREATEORGANIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['CreateOrganizationResponse']
_GETORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['GetOrganizationRequest']
_GETORGANIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['GetOrganizationResponse']
_GETORGANIZATIONNAMESPACEAVAILABILITYREQUEST = DESCRIPTOR.message_types_by_name['GetOrganizationNamespaceAvailabilityRequest']
_GETORGANIZATIONNAMESPACEAVAILABILITYRESPONSE = DESCRIPTOR.message_types_by_name['GetOrganizationNamespaceAvailabilityResponse']
_UPDATEORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['UpdateOrganizationRequest']
_UPDATEORGANIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['UpdateOrganizationResponse']
_DELETEORGANIZATIONREQUEST = DESCRIPTOR.message_types_by_name['DeleteOrganizationRequest']
_DELETEORGANIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['DeleteOrganizationResponse']
_LISTORGANIZATIONMEMBERSREQUEST = DESCRIPTOR.message_types_by_name['ListOrganizationMembersRequest']
_LISTORGANIZATIONMEMBERSRESPONSE = DESCRIPTOR.message_types_by_name['ListOrganizationMembersResponse']
_CREATEORGANIZATIONINVITEREQUEST = DESCRIPTOR.message_types_by_name['CreateOrganizationInviteRequest']
_CREATEORGANIZATIONINVITERESPONSE = DESCRIPTOR.message_types_by_name['CreateOrganizationInviteResponse']
_UPDATEORGANIZATIONINVITEAUTHORIZATIONSREQUEST = DESCRIPTOR.message_types_by_name['UpdateOrganizationInviteAuthorizationsRequest']
_UPDATEORGANIZATIONINVITEAUTHORIZATIONSRESPONSE = DESCRIPTOR.message_types_by_name['UpdateOrganizationInviteAuthorizationsResponse']
_DELETEORGANIZATIONINVITEREQUEST = DESCRIPTOR.message_types_by_name['DeleteOrganizationInviteRequest']
_DELETEORGANIZATIONINVITERESPONSE = DESCRIPTOR.message_types_by_name['DeleteOrganizationInviteResponse']
_RESENDORGANIZATIONINVITEREQUEST = DESCRIPTOR.message_types_by_name['ResendOrganizationInviteRequest']
_RESENDORGANIZATIONINVITERESPONSE = DESCRIPTOR.message_types_by_name['ResendOrganizationInviteResponse']
_DELETEORGANIZATIONMEMBERREQUEST = DESCRIPTOR.message_types_by_name['DeleteOrganizationMemberRequest']
_DELETEORGANIZATIONMEMBERRESPONSE = DESCRIPTOR.message_types_by_name['DeleteOrganizationMemberResponse']
_LOCATIONORGANIZATION = DESCRIPTOR.message_types_by_name['LocationOrganization']
_LOCATIONAUTH = DESCRIPTOR.message_types_by_name['LocationAuth']
_STORAGECONFIG = DESCRIPTOR.message_types_by_name['StorageConfig']
_LOCATION = DESCRIPTOR.message_types_by_name['Location']
_SHAREDSECRET = DESCRIPTOR.message_types_by_name['SharedSecret']
_CREATELOCATIONREQUEST = DESCRIPTOR.message_types_by_name['CreateLocationRequest']
_CREATELOCATIONRESPONSE = DESCRIPTOR.message_types_by_name['CreateLocationResponse']
_GETLOCATIONREQUEST = DESCRIPTOR.message_types_by_name['GetLocationRequest']
_GETLOCATIONRESPONSE = DESCRIPTOR.message_types_by_name['GetLocationResponse']
_UPDATELOCATIONREQUEST = DESCRIPTOR.message_types_by_name['UpdateLocationRequest']
_UPDATELOCATIONRESPONSE = DESCRIPTOR.message_types_by_name['UpdateLocationResponse']
_DELETELOCATIONREQUEST = DESCRIPTOR.message_types_by_name['DeleteLocationRequest']
_DELETELOCATIONRESPONSE = DESCRIPTOR.message_types_by_name['DeleteLocationResponse']
_LISTLOCATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListLocationsRequest']
_SHARELOCATIONREQUEST = DESCRIPTOR.message_types_by_name['ShareLocationRequest']
_SHARELOCATIONRESPONSE = DESCRIPTOR.message_types_by_name['ShareLocationResponse']
_UNSHARELOCATIONREQUEST = DESCRIPTOR.message_types_by_name['UnshareLocationRequest']
_UNSHARELOCATIONRESPONSE = DESCRIPTOR.message_types_by_name['UnshareLocationResponse']
_LISTLOCATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListLocationsResponse']
_CREATELOCATIONSECRETREQUEST = DESCRIPTOR.message_types_by_name['CreateLocationSecretRequest']
_CREATELOCATIONSECRETRESPONSE = DESCRIPTOR.message_types_by_name['CreateLocationSecretResponse']
_DELETELOCATIONSECRETREQUEST = DESCRIPTOR.message_types_by_name['DeleteLocationSecretRequest']
_DELETELOCATIONSECRETRESPONSE = DESCRIPTOR.message_types_by_name['DeleteLocationSecretResponse']
_LOCATIONAUTHREQUEST = DESCRIPTOR.message_types_by_name['LocationAuthRequest']
_LOCATIONAUTHRESPONSE = DESCRIPTOR.message_types_by_name['LocationAuthResponse']
_GETROBOTREQUEST = DESCRIPTOR.message_types_by_name['GetRobotRequest']
_GETROVERRENTALROBOTSREQUEST = DESCRIPTOR.message_types_by_name['GetRoverRentalRobotsRequest']
_ROVERRENTALROBOT = DESCRIPTOR.message_types_by_name['RoverRentalRobot']
_GETROVERRENTALROBOTSRESPONSE = DESCRIPTOR.message_types_by_name['GetRoverRentalRobotsResponse']
_GETROBOTRESPONSE = DESCRIPTOR.message_types_by_name['GetRobotResponse']
_GETROBOTPARTSREQUEST = DESCRIPTOR.message_types_by_name['GetRobotPartsRequest']
_GETROBOTPARTSRESPONSE = DESCRIPTOR.message_types_by_name['GetRobotPartsResponse']
_GETROBOTPARTREQUEST = DESCRIPTOR.message_types_by_name['GetRobotPartRequest']
_GETROBOTPARTRESPONSE = DESCRIPTOR.message_types_by_name['GetRobotPartResponse']
_GETROBOTPARTLOGSREQUEST = DESCRIPTOR.message_types_by_name['GetRobotPartLogsRequest']
_LOGENTRY = DESCRIPTOR.message_types_by_name['LogEntry']
_GETROBOTPARTLOGSRESPONSE = DESCRIPTOR.message_types_by_name['GetRobotPartLogsResponse']
_TAILROBOTPARTLOGSREQUEST = DESCRIPTOR.message_types_by_name['TailRobotPartLogsRequest']
_TAILROBOTPARTLOGSRESPONSE = DESCRIPTOR.message_types_by_name['TailRobotPartLogsResponse']
_GETROBOTPARTHISTORYREQUEST = DESCRIPTOR.message_types_by_name['GetRobotPartHistoryRequest']
_GETROBOTPARTHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['GetRobotPartHistoryResponse']
_UPDATEROBOTPARTREQUEST = DESCRIPTOR.message_types_by_name['UpdateRobotPartRequest']
_UPDATEROBOTPARTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateRobotPartResponse']
_NEWROBOTPARTREQUEST = DESCRIPTOR.message_types_by_name['NewRobotPartRequest']
_NEWROBOTPARTRESPONSE = DESCRIPTOR.message_types_by_name['NewRobotPartResponse']
_DELETEROBOTPARTREQUEST = DESCRIPTOR.message_types_by_name['DeleteRobotPartRequest']
_DELETEROBOTPARTRESPONSE = DESCRIPTOR.message_types_by_name['DeleteRobotPartResponse']
_FRAGMENT = DESCRIPTOR.message_types_by_name['Fragment']
_LISTFRAGMENTSREQUEST = DESCRIPTOR.message_types_by_name['ListFragmentsRequest']
_LISTFRAGMENTSRESPONSE = DESCRIPTOR.message_types_by_name['ListFragmentsResponse']
_GETFRAGMENTREQUEST = DESCRIPTOR.message_types_by_name['GetFragmentRequest']
_GETFRAGMENTRESPONSE = DESCRIPTOR.message_types_by_name['GetFragmentResponse']
_CREATEFRAGMENTREQUEST = DESCRIPTOR.message_types_by_name['CreateFragmentRequest']
_CREATEFRAGMENTRESPONSE = DESCRIPTOR.message_types_by_name['CreateFragmentResponse']
_UPDATEFRAGMENTREQUEST = DESCRIPTOR.message_types_by_name['UpdateFragmentRequest']
_UPDATEFRAGMENTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateFragmentResponse']
_DELETEFRAGMENTREQUEST = DESCRIPTOR.message_types_by_name['DeleteFragmentRequest']
_DELETEFRAGMENTRESPONSE = DESCRIPTOR.message_types_by_name['DeleteFragmentResponse']
_LISTROBOTSREQUEST = DESCRIPTOR.message_types_by_name['ListRobotsRequest']
_LISTROBOTSRESPONSE = DESCRIPTOR.message_types_by_name['ListRobotsResponse']
_NEWROBOTREQUEST = DESCRIPTOR.message_types_by_name['NewRobotRequest']
_NEWROBOTRESPONSE = DESCRIPTOR.message_types_by_name['NewRobotResponse']
_UPDATEROBOTREQUEST = DESCRIPTOR.message_types_by_name['UpdateRobotRequest']
_UPDATEROBOTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateRobotResponse']
_DELETEROBOTREQUEST = DESCRIPTOR.message_types_by_name['DeleteRobotRequest']
_DELETEROBOTRESPONSE = DESCRIPTOR.message_types_by_name['DeleteRobotResponse']
_MARKPARTASMAINREQUEST = DESCRIPTOR.message_types_by_name['MarkPartAsMainRequest']
_MARKPARTASMAINRESPONSE = DESCRIPTOR.message_types_by_name['MarkPartAsMainResponse']
_MARKPARTFORRESTARTREQUEST = DESCRIPTOR.message_types_by_name['MarkPartForRestartRequest']
_MARKPARTFORRESTARTRESPONSE = DESCRIPTOR.message_types_by_name['MarkPartForRestartResponse']
_CREATEROBOTPARTSECRETREQUEST = DESCRIPTOR.message_types_by_name['CreateRobotPartSecretRequest']
_CREATEROBOTPARTSECRETRESPONSE = DESCRIPTOR.message_types_by_name['CreateRobotPartSecretResponse']
_DELETEROBOTPARTSECRETREQUEST = DESCRIPTOR.message_types_by_name['DeleteRobotPartSecretRequest']
_DELETEROBOTPARTSECRETRESPONSE = DESCRIPTOR.message_types_by_name['DeleteRobotPartSecretResponse']
_AUTHORIZATION = DESCRIPTOR.message_types_by_name['Authorization']
_ADDROLEREQUEST = DESCRIPTOR.message_types_by_name['AddRoleRequest']
_ADDROLERESPONSE = DESCRIPTOR.message_types_by_name['AddRoleResponse']
_REMOVEROLEREQUEST = DESCRIPTOR.message_types_by_name['RemoveRoleRequest']
_REMOVEROLERESPONSE = DESCRIPTOR.message_types_by_name['RemoveRoleResponse']
_CHANGEROLEREQUEST = DESCRIPTOR.message_types_by_name['ChangeRoleRequest']
_CHANGEROLERESPONSE = DESCRIPTOR.message_types_by_name['ChangeRoleResponse']
_LISTAUTHORIZATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListAuthorizationsRequest']
_LISTAUTHORIZATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListAuthorizationsResponse']
_CHECKPERMISSIONSREQUEST = DESCRIPTOR.message_types_by_name['CheckPermissionsRequest']
_AUTHORIZEDPERMISSIONS = DESCRIPTOR.message_types_by_name['AuthorizedPermissions']
_CHECKPERMISSIONSRESPONSE = DESCRIPTOR.message_types_by_name['CheckPermissionsResponse']
_CREATEMODULEREQUEST = DESCRIPTOR.message_types_by_name['CreateModuleRequest']
_CREATEMODULERESPONSE = DESCRIPTOR.message_types_by_name['CreateModuleResponse']
_UPDATEMODULEREQUEST = DESCRIPTOR.message_types_by_name['UpdateModuleRequest']
_UPDATEMODULERESPONSE = DESCRIPTOR.message_types_by_name['UpdateModuleResponse']
_MODEL = DESCRIPTOR.message_types_by_name['Model']
_MODULEFILEINFO = DESCRIPTOR.message_types_by_name['ModuleFileInfo']
_UPLOADMODULEFILEREQUEST = DESCRIPTOR.message_types_by_name['UploadModuleFileRequest']
_UPLOADMODULEFILERESPONSE = DESCRIPTOR.message_types_by_name['UploadModuleFileResponse']
_GETMODULEREQUEST = DESCRIPTOR.message_types_by_name['GetModuleRequest']
_GETMODULERESPONSE = DESCRIPTOR.message_types_by_name['GetModuleResponse']
_MODULE = DESCRIPTOR.message_types_by_name['Module']
_VERSIONHISTORY = DESCRIPTOR.message_types_by_name['VersionHistory']
_UPLOADS = DESCRIPTOR.message_types_by_name['Uploads']
_LISTMODULESREQUEST = DESCRIPTOR.message_types_by_name['ListModulesRequest']
_LISTMODULESRESPONSE = DESCRIPTOR.message_types_by_name['ListModulesResponse']
_GETUSERIDBYEMAILREQUEST = DESCRIPTOR.message_types_by_name['GetUserIDByEmailRequest']
_GETUSERIDBYEMAILRESPONSE = DESCRIPTOR.message_types_by_name['GetUserIDByEmailResponse']
_LISTORGANIZATIONSBYUSERREQUEST = DESCRIPTOR.message_types_by_name['ListOrganizationsByUserRequest']
_ORGDETAILS = DESCRIPTOR.message_types_by_name['OrgDetails']
_LISTORGANIZATIONSBYUSERRESPONSE = DESCRIPTOR.message_types_by_name['ListOrganizationsByUserResponse']
_CREATEKEYREQUEST = DESCRIPTOR.message_types_by_name['CreateKeyRequest']
_CREATEKEYRESPONSE = DESCRIPTOR.message_types_by_name['CreateKeyResponse']
_SHAREDSECRET_STATE = _SHAREDSECRET.enum_types_by_name['State']
Robot = _reflection.GeneratedProtocolMessageType('Robot', (_message.Message,), {'DESCRIPTOR': _ROBOT, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(Robot)
RobotPart = _reflection.GeneratedProtocolMessageType('RobotPart', (_message.Message,), {'DESCRIPTOR': _ROBOTPART, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(RobotPart)
RobotPartHistoryEntry = _reflection.GeneratedProtocolMessageType('RobotPartHistoryEntry', (_message.Message,), {'DESCRIPTOR': _ROBOTPARTHISTORYENTRY, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(RobotPartHistoryEntry)
ListOrganizationsRequest = _reflection.GeneratedProtocolMessageType('ListOrganizationsRequest', (_message.Message,), {'DESCRIPTOR': _LISTORGANIZATIONSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListOrganizationsRequest)
Organization = _reflection.GeneratedProtocolMessageType('Organization', (_message.Message,), {'DESCRIPTOR': _ORGANIZATION, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(Organization)
OrganizationMember = _reflection.GeneratedProtocolMessageType('OrganizationMember', (_message.Message,), {'DESCRIPTOR': _ORGANIZATIONMEMBER, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(OrganizationMember)
ListOrganizationsResponse = _reflection.GeneratedProtocolMessageType('ListOrganizationsResponse', (_message.Message,), {'DESCRIPTOR': _LISTORGANIZATIONSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListOrganizationsResponse)
OrganizationInvite = _reflection.GeneratedProtocolMessageType('OrganizationInvite', (_message.Message,), {'DESCRIPTOR': _ORGANIZATIONINVITE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(OrganizationInvite)
CreateOrganizationRequest = _reflection.GeneratedProtocolMessageType('CreateOrganizationRequest', (_message.Message,), {'DESCRIPTOR': _CREATEORGANIZATIONREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateOrganizationRequest)
CreateOrganizationResponse = _reflection.GeneratedProtocolMessageType('CreateOrganizationResponse', (_message.Message,), {'DESCRIPTOR': _CREATEORGANIZATIONRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateOrganizationResponse)
GetOrganizationRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationRequest', (_message.Message,), {'DESCRIPTOR': _GETORGANIZATIONREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetOrganizationRequest)
GetOrganizationResponse = _reflection.GeneratedProtocolMessageType('GetOrganizationResponse', (_message.Message,), {'DESCRIPTOR': _GETORGANIZATIONRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetOrganizationResponse)
GetOrganizationNamespaceAvailabilityRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationNamespaceAvailabilityRequest', (_message.Message,), {'DESCRIPTOR': _GETORGANIZATIONNAMESPACEAVAILABILITYREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetOrganizationNamespaceAvailabilityRequest)
GetOrganizationNamespaceAvailabilityResponse = _reflection.GeneratedProtocolMessageType('GetOrganizationNamespaceAvailabilityResponse', (_message.Message,), {'DESCRIPTOR': _GETORGANIZATIONNAMESPACEAVAILABILITYRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetOrganizationNamespaceAvailabilityResponse)
UpdateOrganizationRequest = _reflection.GeneratedProtocolMessageType('UpdateOrganizationRequest', (_message.Message,), {'DESCRIPTOR': _UPDATEORGANIZATIONREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateOrganizationRequest)
UpdateOrganizationResponse = _reflection.GeneratedProtocolMessageType('UpdateOrganizationResponse', (_message.Message,), {'DESCRIPTOR': _UPDATEORGANIZATIONRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateOrganizationResponse)
DeleteOrganizationRequest = _reflection.GeneratedProtocolMessageType('DeleteOrganizationRequest', (_message.Message,), {'DESCRIPTOR': _DELETEORGANIZATIONREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteOrganizationRequest)
DeleteOrganizationResponse = _reflection.GeneratedProtocolMessageType('DeleteOrganizationResponse', (_message.Message,), {'DESCRIPTOR': _DELETEORGANIZATIONRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteOrganizationResponse)
ListOrganizationMembersRequest = _reflection.GeneratedProtocolMessageType('ListOrganizationMembersRequest', (_message.Message,), {'DESCRIPTOR': _LISTORGANIZATIONMEMBERSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListOrganizationMembersRequest)
ListOrganizationMembersResponse = _reflection.GeneratedProtocolMessageType('ListOrganizationMembersResponse', (_message.Message,), {'DESCRIPTOR': _LISTORGANIZATIONMEMBERSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListOrganizationMembersResponse)
CreateOrganizationInviteRequest = _reflection.GeneratedProtocolMessageType('CreateOrganizationInviteRequest', (_message.Message,), {'DESCRIPTOR': _CREATEORGANIZATIONINVITEREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateOrganizationInviteRequest)
CreateOrganizationInviteResponse = _reflection.GeneratedProtocolMessageType('CreateOrganizationInviteResponse', (_message.Message,), {'DESCRIPTOR': _CREATEORGANIZATIONINVITERESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateOrganizationInviteResponse)
UpdateOrganizationInviteAuthorizationsRequest = _reflection.GeneratedProtocolMessageType('UpdateOrganizationInviteAuthorizationsRequest', (_message.Message,), {'DESCRIPTOR': _UPDATEORGANIZATIONINVITEAUTHORIZATIONSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateOrganizationInviteAuthorizationsRequest)
UpdateOrganizationInviteAuthorizationsResponse = _reflection.GeneratedProtocolMessageType('UpdateOrganizationInviteAuthorizationsResponse', (_message.Message,), {'DESCRIPTOR': _UPDATEORGANIZATIONINVITEAUTHORIZATIONSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateOrganizationInviteAuthorizationsResponse)
DeleteOrganizationInviteRequest = _reflection.GeneratedProtocolMessageType('DeleteOrganizationInviteRequest', (_message.Message,), {'DESCRIPTOR': _DELETEORGANIZATIONINVITEREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteOrganizationInviteRequest)
DeleteOrganizationInviteResponse = _reflection.GeneratedProtocolMessageType('DeleteOrganizationInviteResponse', (_message.Message,), {'DESCRIPTOR': _DELETEORGANIZATIONINVITERESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteOrganizationInviteResponse)
ResendOrganizationInviteRequest = _reflection.GeneratedProtocolMessageType('ResendOrganizationInviteRequest', (_message.Message,), {'DESCRIPTOR': _RESENDORGANIZATIONINVITEREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ResendOrganizationInviteRequest)
ResendOrganizationInviteResponse = _reflection.GeneratedProtocolMessageType('ResendOrganizationInviteResponse', (_message.Message,), {'DESCRIPTOR': _RESENDORGANIZATIONINVITERESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ResendOrganizationInviteResponse)
DeleteOrganizationMemberRequest = _reflection.GeneratedProtocolMessageType('DeleteOrganizationMemberRequest', (_message.Message,), {'DESCRIPTOR': _DELETEORGANIZATIONMEMBERREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteOrganizationMemberRequest)
DeleteOrganizationMemberResponse = _reflection.GeneratedProtocolMessageType('DeleteOrganizationMemberResponse', (_message.Message,), {'DESCRIPTOR': _DELETEORGANIZATIONMEMBERRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteOrganizationMemberResponse)
LocationOrganization = _reflection.GeneratedProtocolMessageType('LocationOrganization', (_message.Message,), {'DESCRIPTOR': _LOCATIONORGANIZATION, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(LocationOrganization)
LocationAuth = _reflection.GeneratedProtocolMessageType('LocationAuth', (_message.Message,), {'DESCRIPTOR': _LOCATIONAUTH, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(LocationAuth)
StorageConfig = _reflection.GeneratedProtocolMessageType('StorageConfig', (_message.Message,), {'DESCRIPTOR': _STORAGECONFIG, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(StorageConfig)
Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {'DESCRIPTOR': _LOCATION, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(Location)
SharedSecret = _reflection.GeneratedProtocolMessageType('SharedSecret', (_message.Message,), {'DESCRIPTOR': _SHAREDSECRET, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(SharedSecret)
CreateLocationRequest = _reflection.GeneratedProtocolMessageType('CreateLocationRequest', (_message.Message,), {'DESCRIPTOR': _CREATELOCATIONREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateLocationRequest)
CreateLocationResponse = _reflection.GeneratedProtocolMessageType('CreateLocationResponse', (_message.Message,), {'DESCRIPTOR': _CREATELOCATIONRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateLocationResponse)
GetLocationRequest = _reflection.GeneratedProtocolMessageType('GetLocationRequest', (_message.Message,), {'DESCRIPTOR': _GETLOCATIONREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetLocationRequest)
GetLocationResponse = _reflection.GeneratedProtocolMessageType('GetLocationResponse', (_message.Message,), {'DESCRIPTOR': _GETLOCATIONRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetLocationResponse)
UpdateLocationRequest = _reflection.GeneratedProtocolMessageType('UpdateLocationRequest', (_message.Message,), {'DESCRIPTOR': _UPDATELOCATIONREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateLocationRequest)
UpdateLocationResponse = _reflection.GeneratedProtocolMessageType('UpdateLocationResponse', (_message.Message,), {'DESCRIPTOR': _UPDATELOCATIONRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateLocationResponse)
DeleteLocationRequest = _reflection.GeneratedProtocolMessageType('DeleteLocationRequest', (_message.Message,), {'DESCRIPTOR': _DELETELOCATIONREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteLocationRequest)
DeleteLocationResponse = _reflection.GeneratedProtocolMessageType('DeleteLocationResponse', (_message.Message,), {'DESCRIPTOR': _DELETELOCATIONRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteLocationResponse)
ListLocationsRequest = _reflection.GeneratedProtocolMessageType('ListLocationsRequest', (_message.Message,), {'DESCRIPTOR': _LISTLOCATIONSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListLocationsRequest)
ShareLocationRequest = _reflection.GeneratedProtocolMessageType('ShareLocationRequest', (_message.Message,), {'DESCRIPTOR': _SHARELOCATIONREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ShareLocationRequest)
ShareLocationResponse = _reflection.GeneratedProtocolMessageType('ShareLocationResponse', (_message.Message,), {'DESCRIPTOR': _SHARELOCATIONRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ShareLocationResponse)
UnshareLocationRequest = _reflection.GeneratedProtocolMessageType('UnshareLocationRequest', (_message.Message,), {'DESCRIPTOR': _UNSHARELOCATIONREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UnshareLocationRequest)
UnshareLocationResponse = _reflection.GeneratedProtocolMessageType('UnshareLocationResponse', (_message.Message,), {'DESCRIPTOR': _UNSHARELOCATIONRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UnshareLocationResponse)
ListLocationsResponse = _reflection.GeneratedProtocolMessageType('ListLocationsResponse', (_message.Message,), {'DESCRIPTOR': _LISTLOCATIONSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListLocationsResponse)
CreateLocationSecretRequest = _reflection.GeneratedProtocolMessageType('CreateLocationSecretRequest', (_message.Message,), {'DESCRIPTOR': _CREATELOCATIONSECRETREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateLocationSecretRequest)
CreateLocationSecretResponse = _reflection.GeneratedProtocolMessageType('CreateLocationSecretResponse', (_message.Message,), {'DESCRIPTOR': _CREATELOCATIONSECRETRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateLocationSecretResponse)
DeleteLocationSecretRequest = _reflection.GeneratedProtocolMessageType('DeleteLocationSecretRequest', (_message.Message,), {'DESCRIPTOR': _DELETELOCATIONSECRETREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteLocationSecretRequest)
DeleteLocationSecretResponse = _reflection.GeneratedProtocolMessageType('DeleteLocationSecretResponse', (_message.Message,), {'DESCRIPTOR': _DELETELOCATIONSECRETRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteLocationSecretResponse)
LocationAuthRequest = _reflection.GeneratedProtocolMessageType('LocationAuthRequest', (_message.Message,), {'DESCRIPTOR': _LOCATIONAUTHREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(LocationAuthRequest)
LocationAuthResponse = _reflection.GeneratedProtocolMessageType('LocationAuthResponse', (_message.Message,), {'DESCRIPTOR': _LOCATIONAUTHRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(LocationAuthResponse)
GetRobotRequest = _reflection.GeneratedProtocolMessageType('GetRobotRequest', (_message.Message,), {'DESCRIPTOR': _GETROBOTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRobotRequest)
GetRoverRentalRobotsRequest = _reflection.GeneratedProtocolMessageType('GetRoverRentalRobotsRequest', (_message.Message,), {'DESCRIPTOR': _GETROVERRENTALROBOTSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRoverRentalRobotsRequest)
RoverRentalRobot = _reflection.GeneratedProtocolMessageType('RoverRentalRobot', (_message.Message,), {'DESCRIPTOR': _ROVERRENTALROBOT, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(RoverRentalRobot)
GetRoverRentalRobotsResponse = _reflection.GeneratedProtocolMessageType('GetRoverRentalRobotsResponse', (_message.Message,), {'DESCRIPTOR': _GETROVERRENTALROBOTSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRoverRentalRobotsResponse)
GetRobotResponse = _reflection.GeneratedProtocolMessageType('GetRobotResponse', (_message.Message,), {'DESCRIPTOR': _GETROBOTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRobotResponse)
GetRobotPartsRequest = _reflection.GeneratedProtocolMessageType('GetRobotPartsRequest', (_message.Message,), {'DESCRIPTOR': _GETROBOTPARTSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRobotPartsRequest)
GetRobotPartsResponse = _reflection.GeneratedProtocolMessageType('GetRobotPartsResponse', (_message.Message,), {'DESCRIPTOR': _GETROBOTPARTSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRobotPartsResponse)
GetRobotPartRequest = _reflection.GeneratedProtocolMessageType('GetRobotPartRequest', (_message.Message,), {'DESCRIPTOR': _GETROBOTPARTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRobotPartRequest)
GetRobotPartResponse = _reflection.GeneratedProtocolMessageType('GetRobotPartResponse', (_message.Message,), {'DESCRIPTOR': _GETROBOTPARTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRobotPartResponse)
GetRobotPartLogsRequest = _reflection.GeneratedProtocolMessageType('GetRobotPartLogsRequest', (_message.Message,), {'DESCRIPTOR': _GETROBOTPARTLOGSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRobotPartLogsRequest)
LogEntry = _reflection.GeneratedProtocolMessageType('LogEntry', (_message.Message,), {'DESCRIPTOR': _LOGENTRY, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(LogEntry)
GetRobotPartLogsResponse = _reflection.GeneratedProtocolMessageType('GetRobotPartLogsResponse', (_message.Message,), {'DESCRIPTOR': _GETROBOTPARTLOGSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRobotPartLogsResponse)
TailRobotPartLogsRequest = _reflection.GeneratedProtocolMessageType('TailRobotPartLogsRequest', (_message.Message,), {'DESCRIPTOR': _TAILROBOTPARTLOGSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(TailRobotPartLogsRequest)
TailRobotPartLogsResponse = _reflection.GeneratedProtocolMessageType('TailRobotPartLogsResponse', (_message.Message,), {'DESCRIPTOR': _TAILROBOTPARTLOGSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(TailRobotPartLogsResponse)
GetRobotPartHistoryRequest = _reflection.GeneratedProtocolMessageType('GetRobotPartHistoryRequest', (_message.Message,), {'DESCRIPTOR': _GETROBOTPARTHISTORYREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRobotPartHistoryRequest)
GetRobotPartHistoryResponse = _reflection.GeneratedProtocolMessageType('GetRobotPartHistoryResponse', (_message.Message,), {'DESCRIPTOR': _GETROBOTPARTHISTORYRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetRobotPartHistoryResponse)
UpdateRobotPartRequest = _reflection.GeneratedProtocolMessageType('UpdateRobotPartRequest', (_message.Message,), {'DESCRIPTOR': _UPDATEROBOTPARTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateRobotPartRequest)
UpdateRobotPartResponse = _reflection.GeneratedProtocolMessageType('UpdateRobotPartResponse', (_message.Message,), {'DESCRIPTOR': _UPDATEROBOTPARTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateRobotPartResponse)
NewRobotPartRequest = _reflection.GeneratedProtocolMessageType('NewRobotPartRequest', (_message.Message,), {'DESCRIPTOR': _NEWROBOTPARTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(NewRobotPartRequest)
NewRobotPartResponse = _reflection.GeneratedProtocolMessageType('NewRobotPartResponse', (_message.Message,), {'DESCRIPTOR': _NEWROBOTPARTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(NewRobotPartResponse)
DeleteRobotPartRequest = _reflection.GeneratedProtocolMessageType('DeleteRobotPartRequest', (_message.Message,), {'DESCRIPTOR': _DELETEROBOTPARTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteRobotPartRequest)
DeleteRobotPartResponse = _reflection.GeneratedProtocolMessageType('DeleteRobotPartResponse', (_message.Message,), {'DESCRIPTOR': _DELETEROBOTPARTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteRobotPartResponse)
Fragment = _reflection.GeneratedProtocolMessageType('Fragment', (_message.Message,), {'DESCRIPTOR': _FRAGMENT, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(Fragment)
ListFragmentsRequest = _reflection.GeneratedProtocolMessageType('ListFragmentsRequest', (_message.Message,), {'DESCRIPTOR': _LISTFRAGMENTSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListFragmentsRequest)
ListFragmentsResponse = _reflection.GeneratedProtocolMessageType('ListFragmentsResponse', (_message.Message,), {'DESCRIPTOR': _LISTFRAGMENTSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListFragmentsResponse)
GetFragmentRequest = _reflection.GeneratedProtocolMessageType('GetFragmentRequest', (_message.Message,), {'DESCRIPTOR': _GETFRAGMENTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetFragmentRequest)
GetFragmentResponse = _reflection.GeneratedProtocolMessageType('GetFragmentResponse', (_message.Message,), {'DESCRIPTOR': _GETFRAGMENTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetFragmentResponse)
CreateFragmentRequest = _reflection.GeneratedProtocolMessageType('CreateFragmentRequest', (_message.Message,), {'DESCRIPTOR': _CREATEFRAGMENTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateFragmentRequest)
CreateFragmentResponse = _reflection.GeneratedProtocolMessageType('CreateFragmentResponse', (_message.Message,), {'DESCRIPTOR': _CREATEFRAGMENTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateFragmentResponse)
UpdateFragmentRequest = _reflection.GeneratedProtocolMessageType('UpdateFragmentRequest', (_message.Message,), {'DESCRIPTOR': _UPDATEFRAGMENTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateFragmentRequest)
UpdateFragmentResponse = _reflection.GeneratedProtocolMessageType('UpdateFragmentResponse', (_message.Message,), {'DESCRIPTOR': _UPDATEFRAGMENTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateFragmentResponse)
DeleteFragmentRequest = _reflection.GeneratedProtocolMessageType('DeleteFragmentRequest', (_message.Message,), {'DESCRIPTOR': _DELETEFRAGMENTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteFragmentRequest)
DeleteFragmentResponse = _reflection.GeneratedProtocolMessageType('DeleteFragmentResponse', (_message.Message,), {'DESCRIPTOR': _DELETEFRAGMENTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteFragmentResponse)
ListRobotsRequest = _reflection.GeneratedProtocolMessageType('ListRobotsRequest', (_message.Message,), {'DESCRIPTOR': _LISTROBOTSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListRobotsRequest)
ListRobotsResponse = _reflection.GeneratedProtocolMessageType('ListRobotsResponse', (_message.Message,), {'DESCRIPTOR': _LISTROBOTSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListRobotsResponse)
NewRobotRequest = _reflection.GeneratedProtocolMessageType('NewRobotRequest', (_message.Message,), {'DESCRIPTOR': _NEWROBOTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(NewRobotRequest)
NewRobotResponse = _reflection.GeneratedProtocolMessageType('NewRobotResponse', (_message.Message,), {'DESCRIPTOR': _NEWROBOTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(NewRobotResponse)
UpdateRobotRequest = _reflection.GeneratedProtocolMessageType('UpdateRobotRequest', (_message.Message,), {'DESCRIPTOR': _UPDATEROBOTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateRobotRequest)
UpdateRobotResponse = _reflection.GeneratedProtocolMessageType('UpdateRobotResponse', (_message.Message,), {'DESCRIPTOR': _UPDATEROBOTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateRobotResponse)
DeleteRobotRequest = _reflection.GeneratedProtocolMessageType('DeleteRobotRequest', (_message.Message,), {'DESCRIPTOR': _DELETEROBOTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteRobotRequest)
DeleteRobotResponse = _reflection.GeneratedProtocolMessageType('DeleteRobotResponse', (_message.Message,), {'DESCRIPTOR': _DELETEROBOTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteRobotResponse)
MarkPartAsMainRequest = _reflection.GeneratedProtocolMessageType('MarkPartAsMainRequest', (_message.Message,), {'DESCRIPTOR': _MARKPARTASMAINREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(MarkPartAsMainRequest)
MarkPartAsMainResponse = _reflection.GeneratedProtocolMessageType('MarkPartAsMainResponse', (_message.Message,), {'DESCRIPTOR': _MARKPARTASMAINRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(MarkPartAsMainResponse)
MarkPartForRestartRequest = _reflection.GeneratedProtocolMessageType('MarkPartForRestartRequest', (_message.Message,), {'DESCRIPTOR': _MARKPARTFORRESTARTREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(MarkPartForRestartRequest)
MarkPartForRestartResponse = _reflection.GeneratedProtocolMessageType('MarkPartForRestartResponse', (_message.Message,), {'DESCRIPTOR': _MARKPARTFORRESTARTRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(MarkPartForRestartResponse)
CreateRobotPartSecretRequest = _reflection.GeneratedProtocolMessageType('CreateRobotPartSecretRequest', (_message.Message,), {'DESCRIPTOR': _CREATEROBOTPARTSECRETREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateRobotPartSecretRequest)
CreateRobotPartSecretResponse = _reflection.GeneratedProtocolMessageType('CreateRobotPartSecretResponse', (_message.Message,), {'DESCRIPTOR': _CREATEROBOTPARTSECRETRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateRobotPartSecretResponse)
DeleteRobotPartSecretRequest = _reflection.GeneratedProtocolMessageType('DeleteRobotPartSecretRequest', (_message.Message,), {'DESCRIPTOR': _DELETEROBOTPARTSECRETREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteRobotPartSecretRequest)
DeleteRobotPartSecretResponse = _reflection.GeneratedProtocolMessageType('DeleteRobotPartSecretResponse', (_message.Message,), {'DESCRIPTOR': _DELETEROBOTPARTSECRETRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(DeleteRobotPartSecretResponse)
Authorization = _reflection.GeneratedProtocolMessageType('Authorization', (_message.Message,), {'DESCRIPTOR': _AUTHORIZATION, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(Authorization)
AddRoleRequest = _reflection.GeneratedProtocolMessageType('AddRoleRequest', (_message.Message,), {'DESCRIPTOR': _ADDROLEREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(AddRoleRequest)
AddRoleResponse = _reflection.GeneratedProtocolMessageType('AddRoleResponse', (_message.Message,), {'DESCRIPTOR': _ADDROLERESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(AddRoleResponse)
RemoveRoleRequest = _reflection.GeneratedProtocolMessageType('RemoveRoleRequest', (_message.Message,), {'DESCRIPTOR': _REMOVEROLEREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(RemoveRoleRequest)
RemoveRoleResponse = _reflection.GeneratedProtocolMessageType('RemoveRoleResponse', (_message.Message,), {'DESCRIPTOR': _REMOVEROLERESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(RemoveRoleResponse)
ChangeRoleRequest = _reflection.GeneratedProtocolMessageType('ChangeRoleRequest', (_message.Message,), {'DESCRIPTOR': _CHANGEROLEREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ChangeRoleRequest)
ChangeRoleResponse = _reflection.GeneratedProtocolMessageType('ChangeRoleResponse', (_message.Message,), {'DESCRIPTOR': _CHANGEROLERESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ChangeRoleResponse)
ListAuthorizationsRequest = _reflection.GeneratedProtocolMessageType('ListAuthorizationsRequest', (_message.Message,), {'DESCRIPTOR': _LISTAUTHORIZATIONSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListAuthorizationsRequest)
ListAuthorizationsResponse = _reflection.GeneratedProtocolMessageType('ListAuthorizationsResponse', (_message.Message,), {'DESCRIPTOR': _LISTAUTHORIZATIONSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListAuthorizationsResponse)
CheckPermissionsRequest = _reflection.GeneratedProtocolMessageType('CheckPermissionsRequest', (_message.Message,), {'DESCRIPTOR': _CHECKPERMISSIONSREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CheckPermissionsRequest)
AuthorizedPermissions = _reflection.GeneratedProtocolMessageType('AuthorizedPermissions', (_message.Message,), {'DESCRIPTOR': _AUTHORIZEDPERMISSIONS, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(AuthorizedPermissions)
CheckPermissionsResponse = _reflection.GeneratedProtocolMessageType('CheckPermissionsResponse', (_message.Message,), {'DESCRIPTOR': _CHECKPERMISSIONSRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CheckPermissionsResponse)
CreateModuleRequest = _reflection.GeneratedProtocolMessageType('CreateModuleRequest', (_message.Message,), {'DESCRIPTOR': _CREATEMODULEREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateModuleRequest)
CreateModuleResponse = _reflection.GeneratedProtocolMessageType('CreateModuleResponse', (_message.Message,), {'DESCRIPTOR': _CREATEMODULERESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateModuleResponse)
UpdateModuleRequest = _reflection.GeneratedProtocolMessageType('UpdateModuleRequest', (_message.Message,), {'DESCRIPTOR': _UPDATEMODULEREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateModuleRequest)
UpdateModuleResponse = _reflection.GeneratedProtocolMessageType('UpdateModuleResponse', (_message.Message,), {'DESCRIPTOR': _UPDATEMODULERESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UpdateModuleResponse)
Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {'DESCRIPTOR': _MODEL, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(Model)
ModuleFileInfo = _reflection.GeneratedProtocolMessageType('ModuleFileInfo', (_message.Message,), {'DESCRIPTOR': _MODULEFILEINFO, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ModuleFileInfo)
UploadModuleFileRequest = _reflection.GeneratedProtocolMessageType('UploadModuleFileRequest', (_message.Message,), {'DESCRIPTOR': _UPLOADMODULEFILEREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UploadModuleFileRequest)
UploadModuleFileResponse = _reflection.GeneratedProtocolMessageType('UploadModuleFileResponse', (_message.Message,), {'DESCRIPTOR': _UPLOADMODULEFILERESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(UploadModuleFileResponse)
GetModuleRequest = _reflection.GeneratedProtocolMessageType('GetModuleRequest', (_message.Message,), {'DESCRIPTOR': _GETMODULEREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetModuleRequest)
GetModuleResponse = _reflection.GeneratedProtocolMessageType('GetModuleResponse', (_message.Message,), {'DESCRIPTOR': _GETMODULERESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetModuleResponse)
Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), {'DESCRIPTOR': _MODULE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(Module)
VersionHistory = _reflection.GeneratedProtocolMessageType('VersionHistory', (_message.Message,), {'DESCRIPTOR': _VERSIONHISTORY, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(VersionHistory)
Uploads = _reflection.GeneratedProtocolMessageType('Uploads', (_message.Message,), {'DESCRIPTOR': _UPLOADS, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(Uploads)
ListModulesRequest = _reflection.GeneratedProtocolMessageType('ListModulesRequest', (_message.Message,), {'DESCRIPTOR': _LISTMODULESREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListModulesRequest)
ListModulesResponse = _reflection.GeneratedProtocolMessageType('ListModulesResponse', (_message.Message,), {'DESCRIPTOR': _LISTMODULESRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListModulesResponse)
GetUserIDByEmailRequest = _reflection.GeneratedProtocolMessageType('GetUserIDByEmailRequest', (_message.Message,), {'DESCRIPTOR': _GETUSERIDBYEMAILREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetUserIDByEmailRequest)
GetUserIDByEmailResponse = _reflection.GeneratedProtocolMessageType('GetUserIDByEmailResponse', (_message.Message,), {'DESCRIPTOR': _GETUSERIDBYEMAILRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(GetUserIDByEmailResponse)
ListOrganizationsByUserRequest = _reflection.GeneratedProtocolMessageType('ListOrganizationsByUserRequest', (_message.Message,), {'DESCRIPTOR': _LISTORGANIZATIONSBYUSERREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListOrganizationsByUserRequest)
OrgDetails = _reflection.GeneratedProtocolMessageType('OrgDetails', (_message.Message,), {'DESCRIPTOR': _ORGDETAILS, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(OrgDetails)
ListOrganizationsByUserResponse = _reflection.GeneratedProtocolMessageType('ListOrganizationsByUserResponse', (_message.Message,), {'DESCRIPTOR': _LISTORGANIZATIONSBYUSERRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(ListOrganizationsByUserResponse)
CreateKeyRequest = _reflection.GeneratedProtocolMessageType('CreateKeyRequest', (_message.Message,), {'DESCRIPTOR': _CREATEKEYREQUEST, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateKeyRequest)
CreateKeyResponse = _reflection.GeneratedProtocolMessageType('CreateKeyResponse', (_message.Message,), {'DESCRIPTOR': _CREATEKEYRESPONSE, '__module__': 'app.v1.app_pb2'})
_sym_db.RegisterMessage(CreateKeyResponse)
_APPSERVICE = DESCRIPTOR.services_by_name['AppService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x16go.viam.com/api/app/v1'
    _ROBOT.fields_by_name['id']._options = None
    _ROBOT.fields_by_name['id']._serialized_options = b'\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"'
    _ROBOT.fields_by_name['name']._options = None
    _ROBOT.fields_by_name['name']._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"name" json:"name"'
    _ROBOT.fields_by_name['location']._options = None
    _ROBOT.fields_by_name['location']._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"location" json:"location"'
    _ROBOT.fields_by_name['last_access']._options = None
    _ROBOT.fields_by_name['last_access']._serialized_options = b'\x9a\x84\x9e\x03%bson:"last_access" json:"last_access"'
    _ROBOT.fields_by_name['created_on']._options = None
    _ROBOT.fields_by_name['created_on']._serialized_options = b'\x9a\x84\x9e\x03\x11bson:"created_on"'
    _ROBOTPART.fields_by_name['id']._options = None
    _ROBOTPART.fields_by_name['id']._serialized_options = b'\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"'
    _ROBOTPART.fields_by_name['name']._options = None
    _ROBOTPART.fields_by_name['name']._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"name" json:"name"'
    _ROBOTPART.fields_by_name['dns_name']._options = None
    _ROBOTPART.fields_by_name['dns_name']._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"dns_name" json:"dns_name"'
    _ROBOTPART.fields_by_name['secret']._options = None
    _ROBOTPART.fields_by_name['secret']._serialized_options = b'\x9a\x84\x9e\x03%bson:"secret" json:"secret,omitempty"'
    _ROBOTPART.fields_by_name['robot']._options = None
    _ROBOTPART.fields_by_name['robot']._serialized_options = b'\x9a\x84\x9e\x03\x19bson:"robot" json:"robot"'
    _ROBOTPART.fields_by_name['location_id']._options = None
    _ROBOTPART.fields_by_name['location_id']._serialized_options = b'\x9a\x84\x9e\x03\x1bbson:"location_id" json:"-"'
    _ROBOTPART.fields_by_name['robot_config']._options = None
    _ROBOTPART.fields_by_name['robot_config']._serialized_options = b'\x9a\x84\x9e\x03!bson:"config" json:"robot_config"'
    _ROBOTPART.fields_by_name['last_access']._options = None
    _ROBOTPART.fields_by_name['last_access']._serialized_options = b'\x9a\x84\x9e\x03%bson:"last_access" json:"last_access"'
    _ROBOTPART.fields_by_name['user_supplied_info']._options = None
    _ROBOTPART.fields_by_name['user_supplied_info']._serialized_options = b'\x9a\x84\x9e\x033bson:"user_supplied_info" json:"user_supplied_info"'
    _ROBOTPART.fields_by_name['main_part']._options = None
    _ROBOTPART.fields_by_name['main_part']._serialized_options = b'\x9a\x84\x9e\x03!bson:"main_part" json:"main_part"'
    _ROBOTPART.fields_by_name['created_on']._options = None
    _ROBOTPART.fields_by_name['created_on']._serialized_options = b'\x9a\x84\x9e\x03\x11bson:"created_on"'
    _ROBOTPART.fields_by_name['secrets']._options = None
    _ROBOTPART.fields_by_name['secrets']._serialized_options = b'\x9a\x84\x9e\x03\x0ebson:"secrets"'
    _ROBOTPARTHISTORYENTRY.fields_by_name['part']._options = None
    _ROBOTPARTHISTORYENTRY.fields_by_name['part']._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"part" json:"part"'
    _ROBOTPARTHISTORYENTRY.fields_by_name['robot']._options = None
    _ROBOTPARTHISTORYENTRY.fields_by_name['robot']._serialized_options = b'\x9a\x84\x9e\x03\x19bson:"robot" json:"robot"'
    _ROBOTPARTHISTORYENTRY.fields_by_name['when']._options = None
    _ROBOTPARTHISTORYENTRY.fields_by_name['when']._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"when" json:"when"'
    _ROBOTPARTHISTORYENTRY.fields_by_name['old']._options = None
    _ROBOTPARTHISTORYENTRY.fields_by_name['old']._serialized_options = b'\x9a\x84\x9e\x03\x15bson:"old" json:"old"'
    _LOCATIONAUTH.fields_by_name['secret']._options = None
    _LOCATIONAUTH.fields_by_name['secret']._serialized_options = b'\x18\x01'
    _SHAREDSECRET.fields_by_name['id']._options = None
    _SHAREDSECRET.fields_by_name['id']._serialized_options = b'\x9a\x84\x9e\x03\tbson:"id"'
    _SHAREDSECRET.fields_by_name['secret']._options = None
    _SHAREDSECRET.fields_by_name['secret']._serialized_options = b'\x9a\x84\x9e\x03\rbson:"secret"'
    _SHAREDSECRET.fields_by_name['created_on']._options = None
    _SHAREDSECRET.fields_by_name['created_on']._serialized_options = b'\x9a\x84\x9e\x03#bson:"created_on" json:"created_on"'
    _SHAREDSECRET.fields_by_name['state']._options = None
    _SHAREDSECRET.fields_by_name['state']._serialized_options = b'\x9a\x84\x9e\x03\x0cbson:"state"'
    _FRAGMENT.fields_by_name['id']._options = None
    _FRAGMENT.fields_by_name['id']._serialized_options = b'\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"'
    _FRAGMENT.fields_by_name['name']._options = None
    _FRAGMENT.fields_by_name['name']._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"name" json:"name"'
    _FRAGMENT.fields_by_name['fragment']._options = None
    _FRAGMENT.fields_by_name['fragment']._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"fragment" json:"fragment"'
    _FRAGMENT.fields_by_name['organization_owner']._options = None
    _FRAGMENT.fields_by_name['organization_owner']._serialized_options = b'\x9a\x84\x9e\x03&bson:"organization_owner" json:"owner"'
    _FRAGMENT.fields_by_name['public']._options = None
    _FRAGMENT.fields_by_name['public']._serialized_options = b'\x9a\x84\x9e\x03\x1bbson:"public" json:"public"'
    _FRAGMENT.fields_by_name['created_on']._options = None
    _FRAGMENT.fields_by_name['created_on']._serialized_options = b'\x9a\x84\x9e\x03\x11bson:"created_on"'
    _VISIBILITY._serialized_start = 15148
    _VISIBILITY._serialized_end = 15235
    _ROBOT._serialized_start = 121
    _ROBOT._serialized_end = 485
    _ROBOTPART._serialized_start = 488
    _ROBOTPART._serialized_end = 1467
    _ROBOTPARTHISTORYENTRY._serialized_start = 1470
    _ROBOTPARTHISTORYENTRY._serialized_end = 1745
    _LISTORGANIZATIONSREQUEST._serialized_start = 1747
    _LISTORGANIZATIONSREQUEST._serialized_end = 1773
    _ORGANIZATION._serialized_start = 1776
    _ORGANIZATION._serialized_end = 1998
    _ORGANIZATIONMEMBER._serialized_start = 2001
    _ORGANIZATIONMEMBER._serialized_end = 2208
    _LISTORGANIZATIONSRESPONSE._serialized_start = 2210
    _LISTORGANIZATIONSRESPONSE._serialized_end = 2302
    _ORGANIZATIONINVITE._serialized_start = 2305
    _ORGANIZATIONINVITE._serialized_end = 2480
    _CREATEORGANIZATIONREQUEST._serialized_start = 2482
    _CREATEORGANIZATIONREQUEST._serialized_end = 2529
    _CREATEORGANIZATIONRESPONSE._serialized_start = 2531
    _CREATEORGANIZATIONRESPONSE._serialized_end = 2622
    _GETORGANIZATIONREQUEST._serialized_start = 2624
    _GETORGANIZATIONREQUEST._serialized_end = 2689
    _GETORGANIZATIONRESPONSE._serialized_start = 2691
    _GETORGANIZATIONRESPONSE._serialized_end = 2779
    _GETORGANIZATIONNAMESPACEAVAILABILITYREQUEST._serialized_start = 2781
    _GETORGANIZATIONNAMESPACEAVAILABILITYREQUEST._serialized_end = 2869
    _GETORGANIZATIONNAMESPACEAVAILABILITYRESPONSE._serialized_start = 2871
    _GETORGANIZATIONNAMESPACEAVAILABILITYRESPONSE._serialized_end = 2947
    _UPDATEORGANIZATIONREQUEST._serialized_start = 2950
    _UPDATEORGANIZATIONREQUEST._serialized_end = 3192
    _UPDATEORGANIZATIONRESPONSE._serialized_start = 3194
    _UPDATEORGANIZATIONRESPONSE._serialized_end = 3285
    _DELETEORGANIZATIONREQUEST._serialized_start = 3287
    _DELETEORGANIZATIONREQUEST._serialized_end = 3355
    _DELETEORGANIZATIONRESPONSE._serialized_start = 3357
    _DELETEORGANIZATIONRESPONSE._serialized_end = 3385
    _LISTORGANIZATIONMEMBERSREQUEST._serialized_start = 3387
    _LISTORGANIZATIONMEMBERSREQUEST._serialized_end = 3460
    _LISTORGANIZATIONMEMBERSRESPONSE._serialized_start = 3463
    _LISTORGANIZATIONMEMBERSRESPONSE._serialized_end = 3655
    _CREATEORGANIZATIONINVITEREQUEST._serialized_start = 3658
    _CREATEORGANIZATIONINVITEREQUEST._serialized_end = 3822
    _CREATEORGANIZATIONINVITERESPONSE._serialized_start = 3824
    _CREATEORGANIZATIONINVITERESPONSE._serialized_end = 3915
    _UPDATEORGANIZATIONINVITEAUTHORIZATIONSREQUEST._serialized_start = 3918
    _UPDATEORGANIZATIONINVITEAUTHORIZATIONSREQUEST._serialized_end = 4184
    _UPDATEORGANIZATIONINVITEAUTHORIZATIONSRESPONSE._serialized_start = 4186
    _UPDATEORGANIZATIONINVITEAUTHORIZATIONSRESPONSE._serialized_end = 4291
    _DELETEORGANIZATIONINVITEREQUEST._serialized_start = 4293
    _DELETEORGANIZATIONINVITEREQUEST._serialized_end = 4389
    _DELETEORGANIZATIONINVITERESPONSE._serialized_start = 4391
    _DELETEORGANIZATIONINVITERESPONSE._serialized_end = 4425
    _RESENDORGANIZATIONINVITEREQUEST._serialized_start = 4427
    _RESENDORGANIZATIONINVITEREQUEST._serialized_end = 4523
    _RESENDORGANIZATIONINVITERESPONSE._serialized_start = 4525
    _RESENDORGANIZATIONINVITERESPONSE._serialized_end = 4616
    _DELETEORGANIZATIONMEMBERREQUEST._serialized_start = 4618
    _DELETEORGANIZATIONMEMBERREQUEST._serialized_end = 4717
    _DELETEORGANIZATIONMEMBERRESPONSE._serialized_start = 4719
    _DELETEORGANIZATIONMEMBERRESPONSE._serialized_end = 4753
    _LOCATIONORGANIZATION._serialized_start = 4755
    _LOCATIONORGANIZATION._serialized_end = 4844
    _LOCATIONAUTH._serialized_start = 4847
    _LOCATIONAUTH._serialized_end = 4975
    _STORAGECONFIG._serialized_start = 4977
    _STORAGECONFIG._serialized_end = 5016
    _LOCATION._serialized_start = 5019
    _LOCATION._serialized_end = 5375
    _SHAREDSECRET._serialized_start = 5378
    _SHAREDSECRET._serialized_end = 5714
    _SHAREDSECRET_STATE._serialized_start = 5645
    _SHAREDSECRET_STATE._serialized_end = 5714
    _CREATELOCATIONREQUEST._serialized_start = 5717
    _CREATELOCATIONREQUEST._serialized_end = 5875
    _CREATELOCATIONRESPONSE._serialized_start = 5877
    _CREATELOCATIONRESPONSE._serialized_end = 5952
    _GETLOCATIONREQUEST._serialized_start = 5954
    _GETLOCATIONREQUEST._serialized_end = 6007
    _GETLOCATIONRESPONSE._serialized_start = 6009
    _GETLOCATIONRESPONSE._serialized_end = 6081
    _UPDATELOCATIONREQUEST._serialized_start = 6084
    _UPDATELOCATIONREQUEST._serialized_end = 6288
    _UPDATELOCATIONRESPONSE._serialized_start = 6290
    _UPDATELOCATIONRESPONSE._serialized_end = 6365
    _DELETELOCATIONREQUEST._serialized_start = 6367
    _DELETELOCATIONREQUEST._serialized_end = 6423
    _DELETELOCATIONRESPONSE._serialized_start = 6425
    _DELETELOCATIONRESPONSE._serialized_end = 6449
    _LISTLOCATIONSREQUEST._serialized_start = 6451
    _LISTLOCATIONSREQUEST._serialized_end = 6514
    _SHARELOCATIONREQUEST._serialized_start = 6516
    _SHARELOCATIONREQUEST._serialized_end = 6612
    _SHARELOCATIONRESPONSE._serialized_start = 6614
    _SHARELOCATIONRESPONSE._serialized_end = 6637
    _UNSHARELOCATIONREQUEST._serialized_start = 6639
    _UNSHARELOCATIONREQUEST._serialized_end = 6737
    _UNSHARELOCATIONRESPONSE._serialized_start = 6739
    _UNSHARELOCATIONRESPONSE._serialized_end = 6764
    _LISTLOCATIONSRESPONSE._serialized_start = 6766
    _LISTLOCATIONSRESPONSE._serialized_end = 6842
    _CREATELOCATIONSECRETREQUEST._serialized_start = 6844
    _CREATELOCATIONSECRETREQUEST._serialized_end = 6906
    _CREATELOCATIONSECRETRESPONSE._serialized_start = 6908
    _CREATELOCATIONSECRETRESPONSE._serialized_end = 6985
    _DELETELOCATIONSECRETREQUEST._serialized_start = 6987
    _DELETELOCATIONSECRETREQUEST._serialized_end = 7078
    _DELETELOCATIONSECRETRESPONSE._serialized_start = 7080
    _DELETELOCATIONSECRETRESPONSE._serialized_end = 7110
    _LOCATIONAUTHREQUEST._serialized_start = 7112
    _LOCATIONAUTHREQUEST._serialized_end = 7166
    _LOCATIONAUTHRESPONSE._serialized_start = 7168
    _LOCATIONAUTHRESPONSE._serialized_end = 7237
    _GETROBOTREQUEST._serialized_start = 7239
    _GETROBOTREQUEST._serialized_end = 7272
    _GETROVERRENTALROBOTSREQUEST._serialized_start = 7274
    _GETROVERRENTALROBOTSREQUEST._serialized_end = 7326
    _ROVERRENTALROBOT._serialized_start = 7329
    _ROVERRENTALROBOT._serialized_end = 7483
    _GETROVERRENTALROBOTSRESPONSE._serialized_start = 7485
    _GETROVERRENTALROBOTSRESPONSE._serialized_end = 7570
    _GETROBOTRESPONSE._serialized_start = 7572
    _GETROBOTRESPONSE._serialized_end = 7632
    _GETROBOTPARTSREQUEST._serialized_start = 7634
    _GETROBOTPARTSREQUEST._serialized_end = 7683
    _GETROBOTPARTSRESPONSE._serialized_start = 7685
    _GETROBOTPARTSRESPONSE._serialized_end = 7754
    _GETROBOTPARTREQUEST._serialized_start = 7756
    _GETROBOTPARTREQUEST._serialized_end = 7793
    _GETROBOTPARTRESPONSE._serialized_start = 7795
    _GETROBOTPARTRESPONSE._serialized_end = 7894
    _GETROBOTPARTLOGSREQUEST._serialized_start = 7897
    _GETROBOTPARTLOGSREQUEST._serialized_end = 8062
    _LOGENTRY._serialized_start = 8065
    _LOGENTRY._serialized_end = 8344
    _GETROBOTPARTLOGSRESPONSE._serialized_start = 8346
    _GETROBOTPARTLOGSRESPONSE._serialized_end = 8455
    _TAILROBOTPARTLOGSREQUEST._serialized_start = 8457
    _TAILROBOTPARTLOGSREQUEST._serialized_end = 8572
    _TAILROBOTPARTLOGSRESPONSE._serialized_start = 8574
    _TAILROBOTPARTLOGSRESPONSE._serialized_end = 8644
    _GETROBOTPARTHISTORYREQUEST._serialized_start = 8646
    _GETROBOTPARTHISTORYREQUEST._serialized_end = 8690
    _GETROBOTPARTHISTORYRESPONSE._serialized_start = 8692
    _GETROBOTPARTHISTORYRESPONSE._serialized_end = 8783
    _UPDATEROBOTPARTREQUEST._serialized_start = 8785
    _UPDATEROBOTPARTREQUEST._serialized_end = 8905
    _UPDATEROBOTPARTRESPONSE._serialized_start = 8907
    _UPDATEROBOTPARTRESPONSE._serialized_end = 8976
    _NEWROBOTPARTREQUEST._serialized_start = 8978
    _NEWROBOTPARTREQUEST._serialized_end = 9055
    _NEWROBOTPARTRESPONSE._serialized_start = 9057
    _NEWROBOTPARTRESPONSE._serialized_end = 9104
    _DELETEROBOTPARTREQUEST._serialized_start = 9106
    _DELETEROBOTPARTREQUEST._serialized_end = 9155
    _DELETEROBOTPARTRESPONSE._serialized_start = 9157
    _DELETEROBOTPARTRESPONSE._serialized_end = 9182
    _FRAGMENT._serialized_start = 9185
    _FRAGMENT._serialized_end = 9801
    _LISTFRAGMENTSREQUEST._serialized_start = 9803
    _LISTFRAGMENTSREQUEST._serialized_end = 9899
    _LISTFRAGMENTSRESPONSE._serialized_start = 9901
    _LISTFRAGMENTSRESPONSE._serialized_end = 9977
    _GETFRAGMENTREQUEST._serialized_start = 9979
    _GETFRAGMENTREQUEST._serialized_end = 10015
    _GETFRAGMENTRESPONSE._serialized_start = 10017
    _GETFRAGMENTRESPONSE._serialized_end = 10089
    _CREATEFRAGMENTREQUEST._serialized_start = 10092
    _CREATEFRAGMENTREQUEST._serialized_end = 10225
    _CREATEFRAGMENTRESPONSE._serialized_start = 10227
    _CREATEFRAGMENTRESPONSE._serialized_end = 10302
    _UPDATEFRAGMENTREQUEST._serialized_start = 10305
    _UPDATEFRAGMENTREQUEST._serialized_end = 10453
    _UPDATEFRAGMENTRESPONSE._serialized_start = 10455
    _UPDATEFRAGMENTRESPONSE._serialized_end = 10530
    _DELETEFRAGMENTREQUEST._serialized_start = 10532
    _DELETEFRAGMENTREQUEST._serialized_end = 10571
    _DELETEFRAGMENTRESPONSE._serialized_start = 10573
    _DELETEFRAGMENTRESPONSE._serialized_end = 10597
    _LISTROBOTSREQUEST._serialized_start = 10599
    _LISTROBOTSREQUEST._serialized_end = 10651
    _LISTROBOTSRESPONSE._serialized_start = 10653
    _LISTROBOTSRESPONSE._serialized_end = 10717
    _NEWROBOTREQUEST._serialized_start = 10719
    _NEWROBOTREQUEST._serialized_end = 10784
    _NEWROBOTRESPONSE._serialized_start = 10786
    _NEWROBOTRESPONSE._serialized_end = 10820
    _UPDATEROBOTREQUEST._serialized_start = 10822
    _UPDATEROBOTREQUEST._serialized_end = 10906
    _UPDATEROBOTRESPONSE._serialized_start = 10908
    _UPDATEROBOTRESPONSE._serialized_end = 10971
    _DELETEROBOTREQUEST._serialized_start = 10973
    _DELETEROBOTREQUEST._serialized_end = 11009
    _DELETEROBOTRESPONSE._serialized_start = 11011
    _DELETEROBOTRESPONSE._serialized_end = 11032
    _MARKPARTASMAINREQUEST._serialized_start = 11034
    _MARKPARTASMAINREQUEST._serialized_end = 11082
    _MARKPARTASMAINRESPONSE._serialized_start = 11084
    _MARKPARTASMAINRESPONSE._serialized_end = 11108
    _MARKPARTFORRESTARTREQUEST._serialized_start = 11110
    _MARKPARTFORRESTARTREQUEST._serialized_end = 11162
    _MARKPARTFORRESTARTRESPONSE._serialized_start = 11164
    _MARKPARTFORRESTARTRESPONSE._serialized_end = 11192
    _CREATEROBOTPARTSECRETREQUEST._serialized_start = 11194
    _CREATEROBOTPARTSECRETREQUEST._serialized_end = 11249
    _CREATEROBOTPARTSECRETRESPONSE._serialized_start = 11251
    _CREATEROBOTPARTSECRETRESPONSE._serialized_end = 11326
    _DELETEROBOTPARTSECRETREQUEST._serialized_start = 11328
    _DELETEROBOTPARTSECRETREQUEST._serialized_end = 11412
    _DELETEROBOTPARTSECRETRESPONSE._serialized_start = 11414
    _DELETEROBOTPARTSECRETRESPONSE._serialized_end = 11445
    _AUTHORIZATION._serialized_start = 11448
    _AUTHORIZATION._serialized_end = 11734
    _ADDROLEREQUEST._serialized_start = 11736
    _ADDROLEREQUEST._serialized_end = 11818
    _ADDROLERESPONSE._serialized_start = 11820
    _ADDROLERESPONSE._serialized_end = 11837
    _REMOVEROLEREQUEST._serialized_start = 11839
    _REMOVEROLEREQUEST._serialized_end = 11924
    _REMOVEROLERESPONSE._serialized_start = 11926
    _REMOVEROLERESPONSE._serialized_end = 11946
    _CHANGEROLEREQUEST._serialized_start = 11949
    _CHANGEROLEREQUEST._serialized_end = 12114
    _CHANGEROLERESPONSE._serialized_start = 12116
    _CHANGEROLERESPONSE._serialized_end = 12136
    _LISTAUTHORIZATIONSREQUEST._serialized_start = 12138
    _LISTAUTHORIZATIONSREQUEST._serialized_end = 12241
    _LISTAUTHORIZATIONSRESPONSE._serialized_start = 12243
    _LISTAUTHORIZATIONSRESPONSE._serialized_end = 12339
    _CHECKPERMISSIONSREQUEST._serialized_start = 12341
    _CHECKPERMISSIONSREQUEST._serialized_end = 12436
    _AUTHORIZEDPERMISSIONS._serialized_start = 12438
    _AUTHORIZEDPERMISSIONS._serialized_end = 12565
    _CHECKPERMISSIONSRESPONSE._serialized_start = 12567
    _CHECKPERMISSIONSRESPONSE._serialized_end = 12684
    _CREATEMODULEREQUEST._serialized_start = 12686
    _CREATEMODULEREQUEST._serialized_end = 12768
    _CREATEMODULERESPONSE._serialized_start = 12770
    _CREATEMODULERESPONSE._serialized_end = 12839
    _UPDATEMODULEREQUEST._serialized_start = 12842
    _UPDATEMODULEREQUEST._serialized_end = 13143
    _UPDATEMODULERESPONSE._serialized_start = 13145
    _UPDATEMODULERESPONSE._serialized_end = 13185
    _MODEL._serialized_start = 13187
    _MODEL._serialized_end = 13234
    _MODULEFILEINFO._serialized_start = 13237
    _MODULEFILEINFO._serialized_end = 13402
    _UPLOADMODULEFILEREQUEST._serialized_start = 13405
    _UPLOADMODULEFILEREQUEST._serialized_end = 13540
    _UPLOADMODULEFILERESPONSE._serialized_start = 13542
    _UPLOADMODULEFILERESPONSE._serialized_end = 13586
    _GETMODULEREQUEST._serialized_start = 13588
    _GETMODULEREQUEST._serialized_end = 13701
    _GETMODULERESPONSE._serialized_start = 13703
    _GETMODULERESPONSE._serialized_end = 13767
    _MODULE._serialized_start = 13770
    _MODULE._serialized_end = 14255
    _VERSIONHISTORY._serialized_start = 14258
    _VERSIONHISTORY._serialized_end = 14420
    _UPLOADS._serialized_start = 14422
    _UPLOADS._serialized_end = 14520
    _LISTMODULESREQUEST._serialized_start = 14522
    _LISTMODULESREQUEST._serialized_end = 14608
    _LISTMODULESRESPONSE._serialized_start = 14610
    _LISTMODULESRESPONSE._serialized_end = 14678
    _GETUSERIDBYEMAILREQUEST._serialized_start = 14680
    _GETUSERIDBYEMAILREQUEST._serialized_end = 14727
    _GETUSERIDBYEMAILRESPONSE._serialized_start = 14729
    _GETUSERIDBYEMAILRESPONSE._serialized_end = 14780
    _LISTORGANIZATIONSBYUSERREQUEST._serialized_start = 14782
    _LISTORGANIZATIONSBYUSERREQUEST._serialized_end = 14839
    _ORGDETAILS._serialized_start = 14841
    _ORGDETAILS._serialized_end = 14903
    _LISTORGANIZATIONSBYUSERRESPONSE._serialized_start = 14905
    _LISTORGANIZATIONSBYUSERRESPONSE._serialized_end = 14983
    _CREATEKEYREQUEST._serialized_start = 14985
    _CREATEKEYREQUEST._serialized_end = 15091
    _CREATEKEYRESPONSE._serialized_start = 15093
    _CREATEKEYRESPONSE._serialized_end = 15146
    _APPSERVICE._serialized_start = 15238
    _APPSERVICE._serialized_end = 20861