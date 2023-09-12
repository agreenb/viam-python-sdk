"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...app.v1 import app_pb2 as app_dot_v1_dot_app__pb2
from ...common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ...tagger.v1 import tagger_pb2 as tagger_dot_v1_dot_tagger__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12app/v1/robot.proto\x12\x0bviam.app.v1\x1a\x10app/v1/app.proto\x1a\x16common/v1/common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x16tagger/v1/tagger.proto"\x89\x05\n\x0bRobotConfig\x12.\n\x05cloud\x18\x01 \x01(\x0b2\x18.viam.app.v1.CloudConfigR\x05cloud\x123\n\x07remotes\x18\x02 \x03(\x0b2\x19.viam.app.v1.RemoteConfigR\x07remotes\x12<\n\ncomponents\x18\x03 \x03(\x0b2\x1c.viam.app.v1.ComponentConfigR\ncomponents\x128\n\tprocesses\x18\x04 \x03(\x0b2\x1a.viam.app.v1.ProcessConfigR\tprocesses\x126\n\x08services\x18\x05 \x03(\x0b2\x1a.viam.app.v1.ServiceConfigR\x08services\x129\n\x07network\x18\x06 \x01(\x0b2\x1a.viam.app.v1.NetworkConfigH\x00R\x07network\x88\x01\x01\x120\n\x04auth\x18\x07 \x01(\x0b2\x17.viam.app.v1.AuthConfigH\x01R\x04auth\x88\x01\x01\x12\x19\n\x05debug\x18\x08 \x01(\x08H\x02R\x05debug\x88\x01\x01\x123\n\x07modules\x18\t \x03(\x0b2\x19.viam.app.v1.ModuleConfigR\x07modules\x127\n\x15disable_partial_start\x18\n \x01(\x08H\x03R\x13disablePartialStart\x88\x01\x01\x126\n\x08packages\x18\x0b \x03(\x0b2\x1a.viam.app.v1.PackageConfigR\x08packagesB\n\n\x08_networkB\x07\n\x05_authB\x08\n\x06_debugB\x18\n\x16_disable_partial_start"8\n\x0eLocationSecret\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06secret\x18\x02 \x01(\tR\x06secret"\xd8\x02\n\x0bCloudConfig\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04fqdn\x18\x02 \x01(\tR\x04fqdn\x12\x1d\n\nlocal_fqdn\x18\x03 \x01(\tR\tlocalFqdn\x12\x1d\n\nmanaged_by\x18\x04 \x01(\tR\tmanagedBy\x12+\n\x11signaling_address\x18\x05 \x01(\tR\x10signalingAddress\x12-\n\x12signaling_insecure\x18\x06 \x01(\x08R\x11signalingInsecure\x12+\n\x0flocation_secret\x18\x07 \x01(\tB\x02\x18\x01R\x0elocationSecret\x12\x16\n\x06secret\x18\x08 \x01(\tR\x06secret\x12F\n\x10location_secrets\x18\t \x03(\x0b2\x1b.viam.app.v1.LocationSecretR\x0flocationSecrets"\xef\x02\n\x0fComponentConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1c\n\tnamespace\x18\x02 \x01(\tR\tnamespace\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x12\x14\n\x05model\x18\x04 \x01(\tR\x05model\x12(\n\x05frame\x18\x05 \x01(\x0b2\x12.viam.app.v1.FrameR\x05frame\x12\x1d\n\ndepends_on\x18\x06 \x03(\tR\tdependsOn\x12l\n\x0fservice_configs\x18\x07 \x03(\x0b2\'.viam.app.v1.ResourceLevelServiceConfigB\x1a\x9a\x84\x9e\x03\x15json:"service_config"R\x0eserviceConfigs\x127\n\nattributes\x18\x08 \x01(\x0b2\x17.google.protobuf.StructR\nattributes\x12\x10\n\x03api\x18\t \x01(\tR\x03api"i\n\x1aResourceLevelServiceConfig\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x127\n\nattributes\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\nattributes"\xe5\x01\n\rProcessConfig\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x12\n\x04args\x18\x03 \x03(\tR\x04args\x12\x10\n\x03cwd\x18\x04 \x01(\tR\x03cwd\x12\x19\n\x08one_shot\x18\x05 \x01(\x08R\x07oneShot\x12\x10\n\x03log\x18\x06 \x01(\x08R\x03log\x12\x1f\n\x0bstop_signal\x18\x07 \x01(\x05R\nstopSignal\x12<\n\x0cstop_timeout\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationR\x0bstopTimeout"\xc3\x02\n\rServiceConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1c\n\tnamespace\x18\x02 \x01(\tR\tnamespace\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\x127\n\nattributes\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\nattributes\x12\x1d\n\ndepends_on\x18\x05 \x03(\tR\tdependsOn\x12\x14\n\x05model\x18\x06 \x01(\tR\x05model\x12\x10\n\x03api\x18\t \x01(\tR\x03api\x12l\n\x0fservice_configs\x18\n \x03(\x0b2\'.viam.app.v1.ResourceLevelServiceConfigB\x1a\x9a\x84\x9e\x03\x15json:"service_config"R\x0eserviceConfigs"\xc5\x01\n\rNetworkConfig\x12\x12\n\x04fqdn\x18\x01 \x01(\tR\x04fqdn\x12!\n\x0cbind_address\x18\x02 \x01(\tR\x0bbindAddress\x12"\n\rtls_cert_file\x18\x03 \x01(\tR\x0btlsCertFile\x12 \n\x0ctls_key_file\x18\x04 \x01(\tR\ntlsKeyFile\x127\n\x08sessions\x18\x05 \x01(\x0b2\x1b.viam.app.v1.SessionsConfigR\x08sessions"V\n\x0eSessionsConfig\x12D\n\x10heartbeat_window\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationR\x0fheartbeatWindow"\xe5\x01\n\nAuthConfig\x12:\n\x08handlers\x18\x01 \x03(\x0b2\x1e.viam.app.v1.AuthHandlerConfigR\x08handlers\x12*\n\x11tls_auth_entities\x18\x02 \x03(\tR\x0ftlsAuthEntities\x12V\n\x14external_auth_config\x18\x03 \x01(\x0b2\x1f.viam.app.v1.ExternalAuthConfigH\x00R\x12externalAuthConfig\x88\x01\x01B\x17\n\x15_external_auth_config"7\n\x08JWKSFile\x12+\n\x04json\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x04json"?\n\x12ExternalAuthConfig\x12)\n\x04jwks\x18\x01 \x01(\x0b2\x15.viam.app.v1.JWKSFileR\x04jwks"v\n\x11AuthHandlerConfig\x120\n\x04type\x18\x01 \x01(\x0e2\x1c.viam.app.v1.CredentialsTypeR\x04type\x12/\n\x06config\x18\x05 \x01(\x0b2\x17.google.protobuf.StructR\x06config"\xcd\x01\n\x05Frame\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12:\n\x0btranslation\x18\x02 \x01(\x0b2\x18.viam.app.v1.TranslationR\x0btranslation\x12:\n\x0borientation\x18\x03 \x01(\x0b2\x18.viam.app.v1.OrientationR\x0borientation\x124\n\x08geometry\x18\x04 \x01(\x0b2\x18.viam.common.v1.GeometryR\x08geometry"7\n\x0bTranslation\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z"\xd0\x07\n\x0bOrientation\x12O\n\x0eno_orientation\x18\x01 \x01(\x0b2&.viam.app.v1.Orientation.NoOrientationH\x00R\rnoOrientation\x12Z\n\x0evector_radians\x18\x02 \x01(\x0b21.viam.app.v1.Orientation.OrientationVectorRadiansH\x00R\rvectorRadians\x12Z\n\x0evector_degrees\x18\x03 \x01(\x0b21.viam.app.v1.Orientation.OrientationVectorDegreesH\x00R\rvectorDegrees\x12I\n\x0ceuler_angles\x18\x04 \x01(\x0b2$.viam.app.v1.Orientation.EulerAnglesH\x00R\x0beulerAngles\x12F\n\x0baxis_angles\x18\x05 \x01(\x0b2#.viam.app.v1.Orientation.AxisAnglesH\x00R\naxisAngles\x12E\n\nquaternion\x18\x06 \x01(\x0b2#.viam.app.v1.Orientation.QuaternionH\x00R\nquaternion\x1a\x0f\n\rNoOrientation\x1aj\n\x18OrientationVectorRadians\x12$\n\x05theta\x18\x01 \x01(\x01B\x0e\x9a\x84\x9e\x03\tjson:"th"R\x05theta\x12\x0c\n\x01x\x18\x02 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x03 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x04 \x01(\x01R\x01z\x1aj\n\x18OrientationVectorDegrees\x12$\n\x05theta\x18\x01 \x01(\x01B\x0e\x9a\x84\x9e\x03\tjson:"th"R\x05theta\x12\x0c\n\x01x\x18\x02 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x03 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x04 \x01(\x01R\x01z\x1aI\n\x0bEulerAngles\x12\x12\n\x04roll\x18\x01 \x01(\x01R\x04roll\x12\x14\n\x05pitch\x18\x02 \x01(\x01R\x05pitch\x12\x10\n\x03yaw\x18\x03 \x01(\x01R\x03yaw\x1a\\\n\nAxisAngles\x12$\n\x05theta\x18\x01 \x01(\x01B\x0e\x9a\x84\x9e\x03\tjson:"th"R\x05theta\x12\x0c\n\x01x\x18\x02 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x03 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x04 \x01(\x01R\x01z\x1aD\n\nQuaternion\x12\x0c\n\x01w\x18\x01 \x01(\x01R\x01w\x12\x0c\n\x01x\x18\x02 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x03 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x04 \x01(\x01R\x01zB\x06\n\x04type"\xf5\x03\n\x0cRemoteConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07address\x18\x02 \x01(\tR\x07address\x12(\n\x05frame\x18\x03 \x01(\x0b2\x12.viam.app.v1.FrameR\x05frame\x12+\n\x04auth\x18\x04 \x01(\x0b2\x17.viam.app.v1.RemoteAuthR\x04auth\x12\x1d\n\nmanaged_by\x18\x05 \x01(\tR\tmanagedBy\x12\x1a\n\x08insecure\x18\x06 \x01(\x08R\x08insecure\x12U\n\x19connection_check_interval\x18\x07 \x01(\x0b2\x19.google.protobuf.DurationR\x17connectionCheckInterval\x12H\n\x12reconnect_interval\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationR\x11reconnectInterval\x12l\n\x0fservice_configs\x18\t \x03(\x0b2\'.viam.app.v1.ResourceLevelServiceConfigB\x1a\x9a\x84\x9e\x03\x15json:"service_config"R\x0eserviceConfigs\x12\x16\n\x06secret\x18\n \x01(\tR\x06secret"\xc6\x01\n\nRemoteAuth\x12E\n\x0bcredentials\x18\x01 \x01(\x0b2#.viam.app.v1.RemoteAuth.CredentialsR\x0bcredentials\x12\x16\n\x06entity\x18\x02 \x01(\tR\x06entity\x1aY\n\x0bCredentials\x120\n\x04type\x18\x01 \x01(\x0e2\x1c.viam.app.v1.CredentialsTypeR\x04type\x12\x18\n\x07payload\x18\x02 \x01(\tR\x07payload"\xac\x01\n\tAgentInfo\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x0e\n\x02os\x18\x02 \x01(\tR\x02os\x12\x10\n\x03ips\x18\x03 \x03(\tR\x03ips\x12\x18\n\x07version\x18\x04 \x01(\tR\x07version\x12!\n\x0cgit_revision\x18\x05 \x01(\tR\x0bgitRevision\x12\x1f\n\x08platform\x18\x06 \x01(\tH\x00R\x08platform\x88\x01\x01B\x0b\n\t_platform"j\n\rConfigRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12:\n\nagent_info\x18\x02 \x01(\x0b2\x16.viam.app.v1.AgentInfoH\x00R\tagentInfo\x88\x01\x01B\r\n\x0b_agent_info"B\n\x0eConfigResponse\x120\n\x06config\x18\x01 \x01(\x0b2\x18.viam.app.v1.RobotConfigR\x06config"$\n\x12CertificateRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"v\n\x13CertificateResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\'\n\x0ftls_certificate\x18\x02 \x01(\tR\x0etlsCertificate\x12&\n\x0ftls_private_key\x18\x03 \x01(\tR\rtlsPrivateKey"G\n\nLogRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12)\n\x04logs\x18\x02 \x03(\x0b2\x15.viam.app.v1.LogEntryR\x04logs"\r\n\x0bLogResponse"%\n\x13NeedsRestartRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x9a\x01\n\x14NeedsRestartResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12!\n\x0cmust_restart\x18\x02 \x01(\x08R\x0bmustRestart\x12O\n\x16restart_check_interval\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationR\x14restartCheckInterval"S\n\x0cModuleConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x12\x1b\n\tlog_level\x18\x03 \x01(\tR\x08logLevel"k\n\rPackageConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07package\x18\x02 \x01(\tR\x07package\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version\x12\x12\n\x04type\x18\x04 \x01(\tR\x04type*\xbf\x01\n\x0fCredentialsType\x12 \n\x1cCREDENTIALS_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19CREDENTIALS_TYPE_INTERNAL\x10\x01\x12\x1c\n\x18CREDENTIALS_TYPE_API_KEY\x10\x02\x12!\n\x1dCREDENTIALS_TYPE_ROBOT_SECRET\x10\x03\x12*\n&CREDENTIALS_TYPE_ROBOT_LOCATION_SECRET\x10\x042\xb2\x02\n\x0cRobotService\x12A\n\x06Config\x12\x1a.viam.app.v1.ConfigRequest\x1a\x1b.viam.app.v1.ConfigResponse\x12P\n\x0bCertificate\x12\x1f.viam.app.v1.CertificateRequest\x1a .viam.app.v1.CertificateResponse\x128\n\x03Log\x12\x17.viam.app.v1.LogRequest\x1a\x18.viam.app.v1.LogResponse\x12S\n\x0cNeedsRestart\x12 .viam.app.v1.NeedsRestartRequest\x1a!.viam.app.v1.NeedsRestartResponseB\x18Z\x16go.viam.com/api/app/v1b\x06proto3')
_CREDENTIALSTYPE = DESCRIPTOR.enum_types_by_name['CredentialsType']
CredentialsType = enum_type_wrapper.EnumTypeWrapper(_CREDENTIALSTYPE)
CREDENTIALS_TYPE_UNSPECIFIED = 0
CREDENTIALS_TYPE_INTERNAL = 1
CREDENTIALS_TYPE_API_KEY = 2
CREDENTIALS_TYPE_ROBOT_SECRET = 3
CREDENTIALS_TYPE_ROBOT_LOCATION_SECRET = 4
_ROBOTCONFIG = DESCRIPTOR.message_types_by_name['RobotConfig']
_LOCATIONSECRET = DESCRIPTOR.message_types_by_name['LocationSecret']
_CLOUDCONFIG = DESCRIPTOR.message_types_by_name['CloudConfig']
_COMPONENTCONFIG = DESCRIPTOR.message_types_by_name['ComponentConfig']
_RESOURCELEVELSERVICECONFIG = DESCRIPTOR.message_types_by_name['ResourceLevelServiceConfig']
_PROCESSCONFIG = DESCRIPTOR.message_types_by_name['ProcessConfig']
_SERVICECONFIG = DESCRIPTOR.message_types_by_name['ServiceConfig']
_NETWORKCONFIG = DESCRIPTOR.message_types_by_name['NetworkConfig']
_SESSIONSCONFIG = DESCRIPTOR.message_types_by_name['SessionsConfig']
_AUTHCONFIG = DESCRIPTOR.message_types_by_name['AuthConfig']
_JWKSFILE = DESCRIPTOR.message_types_by_name['JWKSFile']
_EXTERNALAUTHCONFIG = DESCRIPTOR.message_types_by_name['ExternalAuthConfig']
_AUTHHANDLERCONFIG = DESCRIPTOR.message_types_by_name['AuthHandlerConfig']
_FRAME = DESCRIPTOR.message_types_by_name['Frame']
_TRANSLATION = DESCRIPTOR.message_types_by_name['Translation']
_ORIENTATION = DESCRIPTOR.message_types_by_name['Orientation']
_ORIENTATION_NOORIENTATION = _ORIENTATION.nested_types_by_name['NoOrientation']
_ORIENTATION_ORIENTATIONVECTORRADIANS = _ORIENTATION.nested_types_by_name['OrientationVectorRadians']
_ORIENTATION_ORIENTATIONVECTORDEGREES = _ORIENTATION.nested_types_by_name['OrientationVectorDegrees']
_ORIENTATION_EULERANGLES = _ORIENTATION.nested_types_by_name['EulerAngles']
_ORIENTATION_AXISANGLES = _ORIENTATION.nested_types_by_name['AxisAngles']
_ORIENTATION_QUATERNION = _ORIENTATION.nested_types_by_name['Quaternion']
_REMOTECONFIG = DESCRIPTOR.message_types_by_name['RemoteConfig']
_REMOTEAUTH = DESCRIPTOR.message_types_by_name['RemoteAuth']
_REMOTEAUTH_CREDENTIALS = _REMOTEAUTH.nested_types_by_name['Credentials']
_AGENTINFO = DESCRIPTOR.message_types_by_name['AgentInfo']
_CONFIGREQUEST = DESCRIPTOR.message_types_by_name['ConfigRequest']
_CONFIGRESPONSE = DESCRIPTOR.message_types_by_name['ConfigResponse']
_CERTIFICATEREQUEST = DESCRIPTOR.message_types_by_name['CertificateRequest']
_CERTIFICATERESPONSE = DESCRIPTOR.message_types_by_name['CertificateResponse']
_LOGREQUEST = DESCRIPTOR.message_types_by_name['LogRequest']
_LOGRESPONSE = DESCRIPTOR.message_types_by_name['LogResponse']
_NEEDSRESTARTREQUEST = DESCRIPTOR.message_types_by_name['NeedsRestartRequest']
_NEEDSRESTARTRESPONSE = DESCRIPTOR.message_types_by_name['NeedsRestartResponse']
_MODULECONFIG = DESCRIPTOR.message_types_by_name['ModuleConfig']
_PACKAGECONFIG = DESCRIPTOR.message_types_by_name['PackageConfig']
RobotConfig = _reflection.GeneratedProtocolMessageType('RobotConfig', (_message.Message,), {'DESCRIPTOR': _ROBOTCONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(RobotConfig)
LocationSecret = _reflection.GeneratedProtocolMessageType('LocationSecret', (_message.Message,), {'DESCRIPTOR': _LOCATIONSECRET, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(LocationSecret)
CloudConfig = _reflection.GeneratedProtocolMessageType('CloudConfig', (_message.Message,), {'DESCRIPTOR': _CLOUDCONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(CloudConfig)
ComponentConfig = _reflection.GeneratedProtocolMessageType('ComponentConfig', (_message.Message,), {'DESCRIPTOR': _COMPONENTCONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(ComponentConfig)
ResourceLevelServiceConfig = _reflection.GeneratedProtocolMessageType('ResourceLevelServiceConfig', (_message.Message,), {'DESCRIPTOR': _RESOURCELEVELSERVICECONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(ResourceLevelServiceConfig)
ProcessConfig = _reflection.GeneratedProtocolMessageType('ProcessConfig', (_message.Message,), {'DESCRIPTOR': _PROCESSCONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(ProcessConfig)
ServiceConfig = _reflection.GeneratedProtocolMessageType('ServiceConfig', (_message.Message,), {'DESCRIPTOR': _SERVICECONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(ServiceConfig)
NetworkConfig = _reflection.GeneratedProtocolMessageType('NetworkConfig', (_message.Message,), {'DESCRIPTOR': _NETWORKCONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(NetworkConfig)
SessionsConfig = _reflection.GeneratedProtocolMessageType('SessionsConfig', (_message.Message,), {'DESCRIPTOR': _SESSIONSCONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(SessionsConfig)
AuthConfig = _reflection.GeneratedProtocolMessageType('AuthConfig', (_message.Message,), {'DESCRIPTOR': _AUTHCONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(AuthConfig)
JWKSFile = _reflection.GeneratedProtocolMessageType('JWKSFile', (_message.Message,), {'DESCRIPTOR': _JWKSFILE, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(JWKSFile)
ExternalAuthConfig = _reflection.GeneratedProtocolMessageType('ExternalAuthConfig', (_message.Message,), {'DESCRIPTOR': _EXTERNALAUTHCONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(ExternalAuthConfig)
AuthHandlerConfig = _reflection.GeneratedProtocolMessageType('AuthHandlerConfig', (_message.Message,), {'DESCRIPTOR': _AUTHHANDLERCONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(AuthHandlerConfig)
Frame = _reflection.GeneratedProtocolMessageType('Frame', (_message.Message,), {'DESCRIPTOR': _FRAME, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(Frame)
Translation = _reflection.GeneratedProtocolMessageType('Translation', (_message.Message,), {'DESCRIPTOR': _TRANSLATION, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(Translation)
Orientation = _reflection.GeneratedProtocolMessageType('Orientation', (_message.Message,), {'NoOrientation': _reflection.GeneratedProtocolMessageType('NoOrientation', (_message.Message,), {'DESCRIPTOR': _ORIENTATION_NOORIENTATION, '__module__': 'app.v1.robot_pb2'}), 'OrientationVectorRadians': _reflection.GeneratedProtocolMessageType('OrientationVectorRadians', (_message.Message,), {'DESCRIPTOR': _ORIENTATION_ORIENTATIONVECTORRADIANS, '__module__': 'app.v1.robot_pb2'}), 'OrientationVectorDegrees': _reflection.GeneratedProtocolMessageType('OrientationVectorDegrees', (_message.Message,), {'DESCRIPTOR': _ORIENTATION_ORIENTATIONVECTORDEGREES, '__module__': 'app.v1.robot_pb2'}), 'EulerAngles': _reflection.GeneratedProtocolMessageType('EulerAngles', (_message.Message,), {'DESCRIPTOR': _ORIENTATION_EULERANGLES, '__module__': 'app.v1.robot_pb2'}), 'AxisAngles': _reflection.GeneratedProtocolMessageType('AxisAngles', (_message.Message,), {'DESCRIPTOR': _ORIENTATION_AXISANGLES, '__module__': 'app.v1.robot_pb2'}), 'Quaternion': _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), {'DESCRIPTOR': _ORIENTATION_QUATERNION, '__module__': 'app.v1.robot_pb2'}), 'DESCRIPTOR': _ORIENTATION, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(Orientation)
_sym_db.RegisterMessage(Orientation.NoOrientation)
_sym_db.RegisterMessage(Orientation.OrientationVectorRadians)
_sym_db.RegisterMessage(Orientation.OrientationVectorDegrees)
_sym_db.RegisterMessage(Orientation.EulerAngles)
_sym_db.RegisterMessage(Orientation.AxisAngles)
_sym_db.RegisterMessage(Orientation.Quaternion)
RemoteConfig = _reflection.GeneratedProtocolMessageType('RemoteConfig', (_message.Message,), {'DESCRIPTOR': _REMOTECONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(RemoteConfig)
RemoteAuth = _reflection.GeneratedProtocolMessageType('RemoteAuth', (_message.Message,), {'Credentials': _reflection.GeneratedProtocolMessageType('Credentials', (_message.Message,), {'DESCRIPTOR': _REMOTEAUTH_CREDENTIALS, '__module__': 'app.v1.robot_pb2'}), 'DESCRIPTOR': _REMOTEAUTH, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(RemoteAuth)
_sym_db.RegisterMessage(RemoteAuth.Credentials)
AgentInfo = _reflection.GeneratedProtocolMessageType('AgentInfo', (_message.Message,), {'DESCRIPTOR': _AGENTINFO, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(AgentInfo)
ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), {'DESCRIPTOR': _CONFIGREQUEST, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(ConfigRequest)
ConfigResponse = _reflection.GeneratedProtocolMessageType('ConfigResponse', (_message.Message,), {'DESCRIPTOR': _CONFIGRESPONSE, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(ConfigResponse)
CertificateRequest = _reflection.GeneratedProtocolMessageType('CertificateRequest', (_message.Message,), {'DESCRIPTOR': _CERTIFICATEREQUEST, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(CertificateRequest)
CertificateResponse = _reflection.GeneratedProtocolMessageType('CertificateResponse', (_message.Message,), {'DESCRIPTOR': _CERTIFICATERESPONSE, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(CertificateResponse)
LogRequest = _reflection.GeneratedProtocolMessageType('LogRequest', (_message.Message,), {'DESCRIPTOR': _LOGREQUEST, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(LogRequest)
LogResponse = _reflection.GeneratedProtocolMessageType('LogResponse', (_message.Message,), {'DESCRIPTOR': _LOGRESPONSE, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(LogResponse)
NeedsRestartRequest = _reflection.GeneratedProtocolMessageType('NeedsRestartRequest', (_message.Message,), {'DESCRIPTOR': _NEEDSRESTARTREQUEST, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(NeedsRestartRequest)
NeedsRestartResponse = _reflection.GeneratedProtocolMessageType('NeedsRestartResponse', (_message.Message,), {'DESCRIPTOR': _NEEDSRESTARTRESPONSE, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(NeedsRestartResponse)
ModuleConfig = _reflection.GeneratedProtocolMessageType('ModuleConfig', (_message.Message,), {'DESCRIPTOR': _MODULECONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(ModuleConfig)
PackageConfig = _reflection.GeneratedProtocolMessageType('PackageConfig', (_message.Message,), {'DESCRIPTOR': _PACKAGECONFIG, '__module__': 'app.v1.robot_pb2'})
_sym_db.RegisterMessage(PackageConfig)
_ROBOTSERVICE = DESCRIPTOR.services_by_name['RobotService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x16go.viam.com/api/app/v1'
    _CLOUDCONFIG.fields_by_name['location_secret']._options = None
    _CLOUDCONFIG.fields_by_name['location_secret']._serialized_options = b'\x18\x01'
    _COMPONENTCONFIG.fields_by_name['service_configs']._options = None
    _COMPONENTCONFIG.fields_by_name['service_configs']._serialized_options = b'\x9a\x84\x9e\x03\x15json:"service_config"'
    _SERVICECONFIG.fields_by_name['service_configs']._options = None
    _SERVICECONFIG.fields_by_name['service_configs']._serialized_options = b'\x9a\x84\x9e\x03\x15json:"service_config"'
    _ORIENTATION_ORIENTATIONVECTORRADIANS.fields_by_name['theta']._options = None
    _ORIENTATION_ORIENTATIONVECTORRADIANS.fields_by_name['theta']._serialized_options = b'\x9a\x84\x9e\x03\tjson:"th"'
    _ORIENTATION_ORIENTATIONVECTORDEGREES.fields_by_name['theta']._options = None
    _ORIENTATION_ORIENTATIONVECTORDEGREES.fields_by_name['theta']._serialized_options = b'\x9a\x84\x9e\x03\tjson:"th"'
    _ORIENTATION_AXISANGLES.fields_by_name['theta']._options = None
    _ORIENTATION_AXISANGLES.fields_by_name['theta']._serialized_options = b'\x9a\x84\x9e\x03\tjson:"th"'
    _REMOTECONFIG.fields_by_name['service_configs']._options = None
    _REMOTECONFIG.fields_by_name['service_configs']._serialized_options = b'\x9a\x84\x9e\x03\x15json:"service_config"'
    _CREDENTIALSTYPE._serialized_start = 5954
    _CREDENTIALSTYPE._serialized_end = 6145
    _ROBOTCONFIG._serialized_start = 164
    _ROBOTCONFIG._serialized_end = 813
    _LOCATIONSECRET._serialized_start = 815
    _LOCATIONSECRET._serialized_end = 871
    _CLOUDCONFIG._serialized_start = 874
    _CLOUDCONFIG._serialized_end = 1218
    _COMPONENTCONFIG._serialized_start = 1221
    _COMPONENTCONFIG._serialized_end = 1588
    _RESOURCELEVELSERVICECONFIG._serialized_start = 1590
    _RESOURCELEVELSERVICECONFIG._serialized_end = 1695
    _PROCESSCONFIG._serialized_start = 1698
    _PROCESSCONFIG._serialized_end = 1927
    _SERVICECONFIG._serialized_start = 1930
    _SERVICECONFIG._serialized_end = 2253
    _NETWORKCONFIG._serialized_start = 2256
    _NETWORKCONFIG._serialized_end = 2453
    _SESSIONSCONFIG._serialized_start = 2455
    _SESSIONSCONFIG._serialized_end = 2541
    _AUTHCONFIG._serialized_start = 2544
    _AUTHCONFIG._serialized_end = 2773
    _JWKSFILE._serialized_start = 2775
    _JWKSFILE._serialized_end = 2830
    _EXTERNALAUTHCONFIG._serialized_start = 2832
    _EXTERNALAUTHCONFIG._serialized_end = 2895
    _AUTHHANDLERCONFIG._serialized_start = 2897
    _AUTHHANDLERCONFIG._serialized_end = 3015
    _FRAME._serialized_start = 3018
    _FRAME._serialized_end = 3223
    _TRANSLATION._serialized_start = 3225
    _TRANSLATION._serialized_end = 3280
    _ORIENTATION._serialized_start = 3283
    _ORIENTATION._serialized_end = 4259
    _ORIENTATION_NOORIENTATION._serialized_start = 3781
    _ORIENTATION_NOORIENTATION._serialized_end = 3796
    _ORIENTATION_ORIENTATIONVECTORRADIANS._serialized_start = 3798
    _ORIENTATION_ORIENTATIONVECTORRADIANS._serialized_end = 3904
    _ORIENTATION_ORIENTATIONVECTORDEGREES._serialized_start = 3906
    _ORIENTATION_ORIENTATIONVECTORDEGREES._serialized_end = 4012
    _ORIENTATION_EULERANGLES._serialized_start = 4014
    _ORIENTATION_EULERANGLES._serialized_end = 4087
    _ORIENTATION_AXISANGLES._serialized_start = 4089
    _ORIENTATION_AXISANGLES._serialized_end = 4181
    _ORIENTATION_QUATERNION._serialized_start = 4183
    _ORIENTATION_QUATERNION._serialized_end = 4251
    _REMOTECONFIG._serialized_start = 4262
    _REMOTECONFIG._serialized_end = 4763
    _REMOTEAUTH._serialized_start = 4766
    _REMOTEAUTH._serialized_end = 4964
    _REMOTEAUTH_CREDENTIALS._serialized_start = 4875
    _REMOTEAUTH_CREDENTIALS._serialized_end = 4964
    _AGENTINFO._serialized_start = 4967
    _AGENTINFO._serialized_end = 5139
    _CONFIGREQUEST._serialized_start = 5141
    _CONFIGREQUEST._serialized_end = 5247
    _CONFIGRESPONSE._serialized_start = 5249
    _CONFIGRESPONSE._serialized_end = 5315
    _CERTIFICATEREQUEST._serialized_start = 5317
    _CERTIFICATEREQUEST._serialized_end = 5353
    _CERTIFICATERESPONSE._serialized_start = 5355
    _CERTIFICATERESPONSE._serialized_end = 5473
    _LOGREQUEST._serialized_start = 5475
    _LOGREQUEST._serialized_end = 5546
    _LOGRESPONSE._serialized_start = 5548
    _LOGRESPONSE._serialized_end = 5561
    _NEEDSRESTARTREQUEST._serialized_start = 5563
    _NEEDSRESTARTREQUEST._serialized_end = 5600
    _NEEDSRESTARTRESPONSE._serialized_start = 5603
    _NEEDSRESTARTRESPONSE._serialized_end = 5757
    _MODULECONFIG._serialized_start = 5759
    _MODULECONFIG._serialized_end = 5842
    _PACKAGECONFIG._serialized_start = 5844
    _PACKAGECONFIG._serialized_end = 5951
    _ROBOTSERVICE._serialized_start = 6148
    _ROBOTSERVICE._serialized_end = 6454