"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecomponent/board/v1/board.proto\x12\x17viam.component.board.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto"R\n\rStatusRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"E\n\x0eStatusResponse\x123\n\x06status\x18\x01 \x01(\x0b2\x1b.viam.common.v1.BoardStatusR\x06status"y\n\x0eSetGPIORequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12\x12\n\x04high\x18\x03 \x01(\x08R\x04high\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x11\n\x0fSetGPIOResponse"e\n\x0eGetGPIORequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"%\n\x0fGetGPIOResponse\x12\x12\n\x04high\x18\x01 \x01(\x08R\x04high"a\n\nPWMRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"3\n\x0bPWMResponse\x12$\n\x0eduty_cycle_pct\x18\x01 \x01(\x01R\x0cdutyCyclePct"\x8a\x01\n\rSetPWMRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12$\n\x0eduty_cycle_pct\x18\x03 \x01(\x01R\x0cdutyCyclePct\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x10\n\x0eSetPWMResponse"j\n\x13PWMFrequencyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"9\n\x14PWMFrequencyResponse\x12!\n\x0cfrequency_hz\x18\x01 \x01(\x04R\x0bfrequencyHz"\x90\x01\n\x16SetPWMFrequencyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12!\n\x0cfrequency_hz\x18\x03 \x01(\x04R\x0bfrequencyHz\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x19\n\x17SetPWMFrequencyResponse"\x95\x01\n\x17ReadAnalogReaderRequest\x12\x1d\n\nboard_name\x18\x01 \x01(\tR\tboardName\x12,\n\x12analog_reader_name\x18\x02 \x01(\tR\x10analogReaderName\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"0\n\x18ReadAnalogReaderResponse\x12\x14\n\x05value\x18\x01 \x01(\x05R\x05value"\xa5\x01\n\x1fGetDigitalInterruptValueRequest\x12\x1d\n\nboard_name\x18\x01 \x01(\tR\tboardName\x124\n\x16digital_interrupt_name\x18\x02 \x01(\tR\x14digitalInterruptName\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"8\n GetDigitalInterruptValueResponse\x12\x14\n\x05value\x18\x01 \x01(\x03R\x05value"\xe4\x01\n\x13SetPowerModeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12A\n\npower_mode\x18\x02 \x01(\x0e2".viam.component.board.v1.PowerModeR\tpowerMode\x12:\n\x08duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationH\x00R\x08duration\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0b\n\t_duration"\x16\n\x14SetPowerModeResponse*[\n\tPowerMode\x12\x1a\n\x16POWER_MODE_UNSPECIFIED\x10\x00\x12\x15\n\x11POWER_MODE_NORMAL\x10\x01\x12\x1b\n\x17POWER_MODE_OFFLINE_DEEP\x10\x022\xb5\x0f\n\x0cBoardService\x12\x8d\x01\n\x06Status\x12&.viam.component.board.v1.StatusRequest\x1a\'.viam.component.board.v1.StatusResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/board/{name}/status\x12\x8e\x01\n\x07SetGPIO\x12\'.viam.component.board.v1.SetGPIORequest\x1a(.viam.component.board.v1.SetGPIOResponse"0\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/board/{name}/gpio\x12\x8e\x01\n\x07GetGPIO\x12\'.viam.component.board.v1.GetGPIORequest\x1a(.viam.component.board.v1.GetGPIOResponse"0\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/component/board/{name}/gpio\x12\x81\x01\n\x03PWM\x12#.viam.component.board.v1.PWMRequest\x1a$.viam.component.board.v1.PWMResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/component/board/{name}/pwm\x12\x8a\x01\n\x06SetPWM\x12&.viam.component.board.v1.SetPWMRequest\x1a\'.viam.component.board.v1.SetPWMResponse"/\x82\xd3\xe4\x93\x02)\x1a\'/viam/api/v1/component/board/{name}/pwm\x12\xa1\x01\n\x0cPWMFrequency\x12,.viam.component.board.v1.PWMFrequencyRequest\x1a-.viam.component.board.v1.PWMFrequencyResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/board/{name}/pwm_freq\x12\xaa\x01\n\x0fSetPWMFrequency\x12/.viam.component.board.v1.SetPWMFrequencyRequest\x1a0.viam.component.board.v1.SetPWMFrequencyResponse"4\x82\xd3\xe4\x93\x02.\x1a,/viam/api/v1/component/board/{name}/pwm_freq\x12\x88\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"6\x82\xd3\xe4\x93\x020"./viam/api/v1/component/board/{name}/do_command\x12\xd2\x01\n\x10ReadAnalogReader\x120.viam.component.board.v1.ReadAnalogReaderRequest\x1a1.viam.component.board.v1.ReadAnalogReaderResponse"Y\x82\xd3\xe4\x93\x02S\x12Q/viam/api/v1/component/board/{board_name}/analog_reader/{analog_reader_name}/read\x12\xf3\x01\n\x18GetDigitalInterruptValue\x128.viam.component.board.v1.GetDigitalInterruptValueRequest\x1a9.viam.component.board.v1.GetDigitalInterruptValueResponse"b\x82\xd3\xe4\x93\x02\\\x12Z/viam/api/v1/component/board/{board_name}/digital_interrupt/{digital_interrupt_name}/value\x12\xa3\x01\n\x0cSetPowerMode\x12,.viam.component.board.v1.SetPowerModeRequest\x1a-.viam.component.board.v1.SetPowerModeResponse"6\x82\xd3\xe4\x93\x020\x1a./viam/api/v1/component/board/{name}/power_mode\x12\x94\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"6\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/board/{name}/geometriesBA\n\x1bcom.viam.component.board.v1Z"go.viam.com/api/component/board/v1b\x06proto3')
_POWERMODE = DESCRIPTOR.enum_types_by_name['PowerMode']
PowerMode = enum_type_wrapper.EnumTypeWrapper(_POWERMODE)
POWER_MODE_UNSPECIFIED = 0
POWER_MODE_NORMAL = 1
POWER_MODE_OFFLINE_DEEP = 2
_STATUSREQUEST = DESCRIPTOR.message_types_by_name['StatusRequest']
_STATUSRESPONSE = DESCRIPTOR.message_types_by_name['StatusResponse']
_SETGPIOREQUEST = DESCRIPTOR.message_types_by_name['SetGPIORequest']
_SETGPIORESPONSE = DESCRIPTOR.message_types_by_name['SetGPIOResponse']
_GETGPIOREQUEST = DESCRIPTOR.message_types_by_name['GetGPIORequest']
_GETGPIORESPONSE = DESCRIPTOR.message_types_by_name['GetGPIOResponse']
_PWMREQUEST = DESCRIPTOR.message_types_by_name['PWMRequest']
_PWMRESPONSE = DESCRIPTOR.message_types_by_name['PWMResponse']
_SETPWMREQUEST = DESCRIPTOR.message_types_by_name['SetPWMRequest']
_SETPWMRESPONSE = DESCRIPTOR.message_types_by_name['SetPWMResponse']
_PWMFREQUENCYREQUEST = DESCRIPTOR.message_types_by_name['PWMFrequencyRequest']
_PWMFREQUENCYRESPONSE = DESCRIPTOR.message_types_by_name['PWMFrequencyResponse']
_SETPWMFREQUENCYREQUEST = DESCRIPTOR.message_types_by_name['SetPWMFrequencyRequest']
_SETPWMFREQUENCYRESPONSE = DESCRIPTOR.message_types_by_name['SetPWMFrequencyResponse']
_READANALOGREADERREQUEST = DESCRIPTOR.message_types_by_name['ReadAnalogReaderRequest']
_READANALOGREADERRESPONSE = DESCRIPTOR.message_types_by_name['ReadAnalogReaderResponse']
_GETDIGITALINTERRUPTVALUEREQUEST = DESCRIPTOR.message_types_by_name['GetDigitalInterruptValueRequest']
_GETDIGITALINTERRUPTVALUERESPONSE = DESCRIPTOR.message_types_by_name['GetDigitalInterruptValueResponse']
_SETPOWERMODEREQUEST = DESCRIPTOR.message_types_by_name['SetPowerModeRequest']
_SETPOWERMODERESPONSE = DESCRIPTOR.message_types_by_name['SetPowerModeResponse']
StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {'DESCRIPTOR': _STATUSREQUEST, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(StatusRequest)
StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {'DESCRIPTOR': _STATUSRESPONSE, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(StatusResponse)
SetGPIORequest = _reflection.GeneratedProtocolMessageType('SetGPIORequest', (_message.Message,), {'DESCRIPTOR': _SETGPIOREQUEST, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetGPIORequest)
SetGPIOResponse = _reflection.GeneratedProtocolMessageType('SetGPIOResponse', (_message.Message,), {'DESCRIPTOR': _SETGPIORESPONSE, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetGPIOResponse)
GetGPIORequest = _reflection.GeneratedProtocolMessageType('GetGPIORequest', (_message.Message,), {'DESCRIPTOR': _GETGPIOREQUEST, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(GetGPIORequest)
GetGPIOResponse = _reflection.GeneratedProtocolMessageType('GetGPIOResponse', (_message.Message,), {'DESCRIPTOR': _GETGPIORESPONSE, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(GetGPIOResponse)
PWMRequest = _reflection.GeneratedProtocolMessageType('PWMRequest', (_message.Message,), {'DESCRIPTOR': _PWMREQUEST, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(PWMRequest)
PWMResponse = _reflection.GeneratedProtocolMessageType('PWMResponse', (_message.Message,), {'DESCRIPTOR': _PWMRESPONSE, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(PWMResponse)
SetPWMRequest = _reflection.GeneratedProtocolMessageType('SetPWMRequest', (_message.Message,), {'DESCRIPTOR': _SETPWMREQUEST, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetPWMRequest)
SetPWMResponse = _reflection.GeneratedProtocolMessageType('SetPWMResponse', (_message.Message,), {'DESCRIPTOR': _SETPWMRESPONSE, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetPWMResponse)
PWMFrequencyRequest = _reflection.GeneratedProtocolMessageType('PWMFrequencyRequest', (_message.Message,), {'DESCRIPTOR': _PWMFREQUENCYREQUEST, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(PWMFrequencyRequest)
PWMFrequencyResponse = _reflection.GeneratedProtocolMessageType('PWMFrequencyResponse', (_message.Message,), {'DESCRIPTOR': _PWMFREQUENCYRESPONSE, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(PWMFrequencyResponse)
SetPWMFrequencyRequest = _reflection.GeneratedProtocolMessageType('SetPWMFrequencyRequest', (_message.Message,), {'DESCRIPTOR': _SETPWMFREQUENCYREQUEST, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetPWMFrequencyRequest)
SetPWMFrequencyResponse = _reflection.GeneratedProtocolMessageType('SetPWMFrequencyResponse', (_message.Message,), {'DESCRIPTOR': _SETPWMFREQUENCYRESPONSE, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetPWMFrequencyResponse)
ReadAnalogReaderRequest = _reflection.GeneratedProtocolMessageType('ReadAnalogReaderRequest', (_message.Message,), {'DESCRIPTOR': _READANALOGREADERREQUEST, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(ReadAnalogReaderRequest)
ReadAnalogReaderResponse = _reflection.GeneratedProtocolMessageType('ReadAnalogReaderResponse', (_message.Message,), {'DESCRIPTOR': _READANALOGREADERRESPONSE, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(ReadAnalogReaderResponse)
GetDigitalInterruptValueRequest = _reflection.GeneratedProtocolMessageType('GetDigitalInterruptValueRequest', (_message.Message,), {'DESCRIPTOR': _GETDIGITALINTERRUPTVALUEREQUEST, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(GetDigitalInterruptValueRequest)
GetDigitalInterruptValueResponse = _reflection.GeneratedProtocolMessageType('GetDigitalInterruptValueResponse', (_message.Message,), {'DESCRIPTOR': _GETDIGITALINTERRUPTVALUERESPONSE, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(GetDigitalInterruptValueResponse)
SetPowerModeRequest = _reflection.GeneratedProtocolMessageType('SetPowerModeRequest', (_message.Message,), {'DESCRIPTOR': _SETPOWERMODEREQUEST, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetPowerModeRequest)
SetPowerModeResponse = _reflection.GeneratedProtocolMessageType('SetPowerModeResponse', (_message.Message,), {'DESCRIPTOR': _SETPOWERMODERESPONSE, '__module__': 'component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetPowerModeResponse)
_BOARDSERVICE = DESCRIPTOR.services_by_name['BoardService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1bcom.viam.component.board.v1Z"go.viam.com/api/component/board/v1'
    _BOARDSERVICE.methods_by_name['Status']._options = None
    _BOARDSERVICE.methods_by_name['Status']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/board/{name}/status'
    _BOARDSERVICE.methods_by_name['SetGPIO']._options = None
    _BOARDSERVICE.methods_by_name['SetGPIO']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/board/{name}/gpio'
    _BOARDSERVICE.methods_by_name['GetGPIO']._options = None
    _BOARDSERVICE.methods_by_name['GetGPIO']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/component/board/{name}/gpio'
    _BOARDSERVICE.methods_by_name['PWM']._options = None
    _BOARDSERVICE.methods_by_name['PWM']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/viam/api/v1/component/board/{name}/pwm"
    _BOARDSERVICE.methods_by_name['SetPWM']._options = None
    _BOARDSERVICE.methods_by_name['SetPWM']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x1a'/viam/api/v1/component/board/{name}/pwm"
    _BOARDSERVICE.methods_by_name['PWMFrequency']._options = None
    _BOARDSERVICE.methods_by_name['PWMFrequency']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/board/{name}/pwm_freq'
    _BOARDSERVICE.methods_by_name['SetPWMFrequency']._options = None
    _BOARDSERVICE.methods_by_name['SetPWMFrequency']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x1a,/viam/api/v1/component/board/{name}/pwm_freq'
    _BOARDSERVICE.methods_by_name['DoCommand']._options = None
    _BOARDSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x020"./viam/api/v1/component/board/{name}/do_command'
    _BOARDSERVICE.methods_by_name['ReadAnalogReader']._options = None
    _BOARDSERVICE.methods_by_name['ReadAnalogReader']._serialized_options = b'\x82\xd3\xe4\x93\x02S\x12Q/viam/api/v1/component/board/{board_name}/analog_reader/{analog_reader_name}/read'
    _BOARDSERVICE.methods_by_name['GetDigitalInterruptValue']._options = None
    _BOARDSERVICE.methods_by_name['GetDigitalInterruptValue']._serialized_options = b'\x82\xd3\xe4\x93\x02\\\x12Z/viam/api/v1/component/board/{board_name}/digital_interrupt/{digital_interrupt_name}/value'
    _BOARDSERVICE.methods_by_name['SetPowerMode']._options = None
    _BOARDSERVICE.methods_by_name['SetPowerMode']._serialized_options = b'\x82\xd3\xe4\x93\x020\x1a./viam/api/v1/component/board/{name}/power_mode'
    _BOARDSERVICE.methods_by_name['GetGeometries']._options = None
    _BOARDSERVICE.methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/board/{name}/geometries'
    _POWERMODE._serialized_start = 1949
    _POWERMODE._serialized_end = 2040
    _STATUSREQUEST._serialized_start = 175
    _STATUSREQUEST._serialized_end = 257
    _STATUSRESPONSE._serialized_start = 259
    _STATUSRESPONSE._serialized_end = 328
    _SETGPIOREQUEST._serialized_start = 330
    _SETGPIOREQUEST._serialized_end = 451
    _SETGPIORESPONSE._serialized_start = 453
    _SETGPIORESPONSE._serialized_end = 470
    _GETGPIOREQUEST._serialized_start = 472
    _GETGPIOREQUEST._serialized_end = 573
    _GETGPIORESPONSE._serialized_start = 575
    _GETGPIORESPONSE._serialized_end = 612
    _PWMREQUEST._serialized_start = 614
    _PWMREQUEST._serialized_end = 711
    _PWMRESPONSE._serialized_start = 713
    _PWMRESPONSE._serialized_end = 764
    _SETPWMREQUEST._serialized_start = 767
    _SETPWMREQUEST._serialized_end = 905
    _SETPWMRESPONSE._serialized_start = 907
    _SETPWMRESPONSE._serialized_end = 923
    _PWMFREQUENCYREQUEST._serialized_start = 925
    _PWMFREQUENCYREQUEST._serialized_end = 1031
    _PWMFREQUENCYRESPONSE._serialized_start = 1033
    _PWMFREQUENCYRESPONSE._serialized_end = 1090
    _SETPWMFREQUENCYREQUEST._serialized_start = 1093
    _SETPWMFREQUENCYREQUEST._serialized_end = 1237
    _SETPWMFREQUENCYRESPONSE._serialized_start = 1239
    _SETPWMFREQUENCYRESPONSE._serialized_end = 1264
    _READANALOGREADERREQUEST._serialized_start = 1267
    _READANALOGREADERREQUEST._serialized_end = 1416
    _READANALOGREADERRESPONSE._serialized_start = 1418
    _READANALOGREADERRESPONSE._serialized_end = 1466
    _GETDIGITALINTERRUPTVALUEREQUEST._serialized_start = 1469
    _GETDIGITALINTERRUPTVALUEREQUEST._serialized_end = 1634
    _GETDIGITALINTERRUPTVALUERESPONSE._serialized_start = 1636
    _GETDIGITALINTERRUPTVALUERESPONSE._serialized_end = 1692
    _SETPOWERMODEREQUEST._serialized_start = 1695
    _SETPOWERMODEREQUEST._serialized_end = 1923
    _SETPOWERMODERESPONSE._serialized_start = 1925
    _SETPOWERMODERESPONSE._serialized_end = 1947
    _BOARDSERVICE._serialized_start = 2043
    _BOARDSERVICE._serialized_end = 4016