"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16app/data/v1/data.proto\x12\x10viam.app.data.v1\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa1\x01\n\x0bDataRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter\x12\x14\n\x05limit\x18\x02 \x01(\x04R\x05limit\x12\x12\n\x04last\x18\x03 \x01(\tR\x04last\x126\n\nsort_order\x18\x04 \x01(\x0e2\x17.viam.app.data.v1.OrderR\tsortOrder"\x8b\x04\n\x06Filter\x12%\n\x0ecomponent_name\x18\x01 \x01(\tR\rcomponentName\x12%\n\x0ecomponent_type\x18\x02 \x01(\tR\rcomponentType\x12\x16\n\x06method\x18\x04 \x01(\tR\x06method\x12\x1d\n\nrobot_name\x18\x06 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x07 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x08 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\t \x01(\tR\x06partId\x12!\n\x0clocation_ids\x18\n \x03(\tR\x0blocationIds\x12)\n\x10organization_ids\x18\x0b \x03(\tR\x0forganizationIds\x12\x1b\n\tmime_type\x18\x0c \x03(\tR\x08mimeType\x12=\n\x08interval\x18\r \x01(\x0b2!.viam.app.data.v1.CaptureIntervalR\x08interval\x12=\n\x0btags_filter\x18\x0e \x01(\x0b2\x1c.viam.app.data.v1.TagsFilterR\ntagsFilter\x12\x1f\n\x0bbbox_labels\x18\x0f \x03(\tR\nbboxLabelsJ\x04\x08\x03\x10\x04J\x04\x08\x05\x10\x06R\x0fcomponent_modelR\x04tags"V\n\nTagsFilter\x124\n\x04type\x18\x01 \x01(\x0e2 .viam.app.data.v1.TagsFilterTypeR\x04type\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags"\xc3\x04\n\x0fCaptureMetadata\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId\x12\x1d\n\nrobot_name\x18\x03 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x04 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x05 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\x06 \x01(\tR\x06partId\x12%\n\x0ecomponent_type\x18\x07 \x01(\tR\rcomponentType\x12%\n\x0ecomponent_name\x18\t \x01(\tR\rcomponentName\x12\x1f\n\x0bmethod_name\x18\n \x01(\tR\nmethodName\x12d\n\x11method_parameters\x18\x0b \x03(\x0b27.viam.app.data.v1.CaptureMetadata.MethodParametersEntryR\x10methodParameters\x12\x12\n\x04tags\x18\x0c \x03(\tR\x04tags\x12\x1b\n\tmime_type\x18\r \x01(\tR\x08mimeType\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01J\x04\x08\x08\x10\tR\x0fcomponent_model"q\n\x0fCaptureInterval\x120\n\x05start\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03end\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x03end"\xb1\x01\n\x1aTabularDataByFilterRequest\x12@\n\x0cdata_request\x18\x01 \x01(\x0b2\x1d.viam.app.data.v1.DataRequestR\x0bdataRequest\x12\x1d\n\ncount_only\x18\x02 \x01(\x08R\tcountOnly\x122\n\x15include_internal_data\x18\x03 \x01(\x08R\x13includeInternalData"\xe3\x01\n\x1bTabularDataByFilterResponse\x12=\n\x08metadata\x18\x01 \x03(\x0b2!.viam.app.data.v1.CaptureMetadataR\x08metadata\x121\n\x04data\x18\x02 \x03(\x0b2\x1d.viam.app.data.v1.TabularDataR\x04data\x12\x14\n\x05count\x18\x03 \x01(\x04R\x05count\x12\x12\n\x04last\x18\x04 \x01(\tR\x04last\x12(\n\x10total_size_bytes\x18\x05 \x01(\x04R\x0etotalSizeBytes"\xe5\x01\n\x0bTabularData\x12+\n\x04data\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x04data\x12%\n\x0emetadata_index\x18\x02 \x01(\rR\rmetadataIndex\x12A\n\x0etime_requested\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived"b\n\nBinaryData\x12\x16\n\x06binary\x18\x01 \x01(\x0cR\x06binary\x12<\n\x08metadata\x18\x02 \x01(\x0b2 .viam.app.data.v1.BinaryMetadataR\x08metadata"\xd7\x01\n\x19BinaryDataByFilterRequest\x12@\n\x0cdata_request\x18\x01 \x01(\x0b2\x1d.viam.app.data.v1.DataRequestR\x0bdataRequest\x12%\n\x0einclude_binary\x18\x02 \x01(\x08R\rincludeBinary\x12\x1d\n\ncount_only\x18\x03 \x01(\x08R\tcountOnly\x122\n\x15include_internal_data\x18\x04 \x01(\x08R\x13includeInternalData"\xa2\x01\n\x1aBinaryDataByFilterResponse\x120\n\x04data\x18\x01 \x03(\x0b2\x1c.viam.app.data.v1.BinaryDataR\x04data\x12\x14\n\x05count\x18\x02 \x01(\x04R\x05count\x12\x12\n\x04last\x18\x03 \x01(\tR\x04last\x12(\n\x10total_size_bytes\x18\x04 \x01(\x04R\x0etotalSizeBytes"m\n\x08BinaryID\x12\x17\n\x07file_id\x18\x01 \x01(\tR\x06fileId\x12\'\n\x0forganization_id\x18\x02 \x01(\tR\x0eorganizationId\x12\x1f\n\x0blocation_id\x18\x03 \x01(\tR\nlocationId"\x8a\x01\n\x16BinaryDataByIDsRequest\x12%\n\x0einclude_binary\x18\x02 \x01(\x08R\rincludeBinary\x129\n\nbinary_ids\x18\x03 \x03(\x0b2\x1a.viam.app.data.v1.BinaryIDR\tbinaryIdsJ\x04\x08\x01\x10\x02R\x08file_ids"a\n\x17BinaryDataByIDsResponse\x120\n\x04data\x18\x01 \x03(\x0b2\x1c.viam.app.data.v1.BinaryDataR\x04data\x12\x14\n\x05count\x18\x02 \x01(\x04R\x05count"\xdb\x01\n\x0bBoundingBox\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x14\n\x05label\x18\x02 \x01(\tR\x05label\x12(\n\x10x_min_normalized\x18\x03 \x01(\x01R\x0exMinNormalized\x12(\n\x10y_min_normalized\x18\x04 \x01(\x01R\x0eyMinNormalized\x12(\n\x10x_max_normalized\x18\x05 \x01(\x01R\x0exMaxNormalized\x12(\n\x10y_max_normalized\x18\x06 \x01(\x01R\x0eyMaxNormalized"D\n\x0bAnnotations\x125\n\x06bboxes\x18\x01 \x03(\x0b2\x1d.viam.app.data.v1.BoundingBoxR\x06bboxes"\xfd\x02\n\x0eBinaryMetadata\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12L\n\x10capture_metadata\x18\x02 \x01(\x0b2!.viam.app.data.v1.CaptureMetadataR\x0fcaptureMetadata\x12A\n\x0etime_requested\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived\x12\x1b\n\tfile_name\x18\x05 \x01(\tR\x08fileName\x12\x19\n\x08file_ext\x18\x06 \x01(\tR\x07fileExt\x12\x10\n\x03uri\x18\x07 \x01(\tR\x03uri\x12?\n\x0bannotations\x18\x08 \x01(\x0b2\x1d.viam.app.data.v1.AnnotationsR\x0bannotations"T\n DeleteTabularDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter"V\n!DeleteTabularDataByFilterResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCountJ\x04\x08\x02\x10\x03R\x06result"x\n\x18DeleteTabularDataRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x123\n\x16delete_older_than_days\x18\x02 \x01(\rR\x13deleteOlderThanDays"@\n\x19DeleteTabularDataResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCount"S\n\x1fDeleteBinaryDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter"U\n DeleteBinaryDataByFilterResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCountJ\x04\x08\x02\x10\x03R\x06result"i\n\x1cDeleteBinaryDataByIDsRequest\x129\n\nbinary_ids\x18\x02 \x03(\x0b2\x1a.viam.app.data.v1.BinaryIDR\tbinaryIdsJ\x04\x08\x01\x10\x02R\x08file_ids"R\n\x1dDeleteBinaryDataByIDsResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCountJ\x04\x08\x02\x10\x03R\x06result"\x80\x01\n\x1fAddTagsToBinaryDataByIDsRequest\x129\n\nbinary_ids\x18\x03 \x03(\x0b2\x1a.viam.app.data.v1.BinaryIDR\tbinaryIds\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tagsJ\x04\x08\x01\x10\x02R\x08file_ids""\n AddTagsToBinaryDataByIDsResponse"j\n"AddTagsToBinaryDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags"%\n#AddTagsToBinaryDataByFilterResponse"\x85\x01\n$RemoveTagsFromBinaryDataByIDsRequest\x129\n\nbinary_ids\x18\x03 \x03(\x0b2\x1a.viam.app.data.v1.BinaryIDR\tbinaryIds\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tagsJ\x04\x08\x01\x10\x02R\x08file_ids"L\n%RemoveTagsFromBinaryDataByIDsResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCount"o\n\'RemoveTagsFromBinaryDataByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags"O\n(RemoveTagsFromBinaryDataByFilterResponse\x12#\n\rdeleted_count\x18\x01 \x01(\x04R\x0cdeletedCount"G\n\x13TagsByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter"*\n\x14TagsByFilterResponse\x12\x12\n\x04tags\x18\x01 \x03(\tR\x04tags"\xa8\x02\n AddBoundingBoxToImageByIDRequest\x127\n\tbinary_id\x18\x07 \x01(\x0b2\x1a.viam.app.data.v1.BinaryIDR\x08binaryId\x12\x14\n\x05label\x18\x02 \x01(\tR\x05label\x12(\n\x10x_min_normalized\x18\x03 \x01(\x01R\x0exMinNormalized\x12(\n\x10y_min_normalized\x18\x04 \x01(\x01R\x0eyMinNormalized\x12(\n\x10x_max_normalized\x18\x05 \x01(\x01R\x0exMaxNormalized\x12(\n\x10y_max_normalized\x18\x06 \x01(\x01R\x0eyMaxNormalizedJ\x04\x08\x01\x10\x02R\x07file_id"<\n!AddBoundingBoxToImageByIDResponse\x12\x17\n\x07bbox_id\x18\x01 \x01(\tR\x06bboxId"\x88\x01\n%RemoveBoundingBoxFromImageByIDRequest\x127\n\tbinary_id\x18\x03 \x01(\x0b2\x1a.viam.app.data.v1.BinaryIDR\x08binaryId\x12\x17\n\x07bbox_id\x18\x02 \x01(\tR\x06bboxIdJ\x04\x08\x01\x10\x02R\x07file_id"(\n&RemoveBoundingBoxFromImageByIDResponse"T\n BoundingBoxLabelsByFilterRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter";\n!BoundingBoxLabelsByFilterResponse\x12\x16\n\x06labels\x18\x01 \x03(\tR\x06labels*I\n\x05Order\x12\x15\n\x11ORDER_UNSPECIFIED\x10\x00\x12\x14\n\x10ORDER_DESCENDING\x10\x01\x12\x13\n\x0fORDER_ASCENDING\x10\x02*\x90\x01\n\x0eTagsFilterType\x12 \n\x1cTAGS_FILTER_TYPE_UNSPECIFIED\x10\x00\x12 \n\x1cTAGS_FILTER_TYPE_MATCH_BY_OR\x10\x01\x12\x1b\n\x17TAGS_FILTER_TYPE_TAGGED\x10\x02\x12\x1d\n\x19TAGS_FILTER_TYPE_UNTAGGED\x10\x032\x90\x0f\n\x0bDataService\x12r\n\x13TabularDataByFilter\x12,.viam.app.data.v1.TabularDataByFilterRequest\x1a-.viam.app.data.v1.TabularDataByFilterResponse\x12o\n\x12BinaryDataByFilter\x12+.viam.app.data.v1.BinaryDataByFilterRequest\x1a,.viam.app.data.v1.BinaryDataByFilterResponse\x12f\n\x0fBinaryDataByIDs\x12(.viam.app.data.v1.BinaryDataByIDsRequest\x1a).viam.app.data.v1.BinaryDataByIDsResponse\x12\x84\x01\n\x19DeleteTabularDataByFilter\x122.viam.app.data.v1.DeleteTabularDataByFilterRequest\x1a3.viam.app.data.v1.DeleteTabularDataByFilterResponse\x12l\n\x11DeleteTabularData\x12*.viam.app.data.v1.DeleteTabularDataRequest\x1a+.viam.app.data.v1.DeleteTabularDataResponse\x12\x81\x01\n\x18DeleteBinaryDataByFilter\x121.viam.app.data.v1.DeleteBinaryDataByFilterRequest\x1a2.viam.app.data.v1.DeleteBinaryDataByFilterResponse\x12x\n\x15DeleteBinaryDataByIDs\x12..viam.app.data.v1.DeleteBinaryDataByIDsRequest\x1a/.viam.app.data.v1.DeleteBinaryDataByIDsResponse\x12\x81\x01\n\x18AddTagsToBinaryDataByIDs\x121.viam.app.data.v1.AddTagsToBinaryDataByIDsRequest\x1a2.viam.app.data.v1.AddTagsToBinaryDataByIDsResponse\x12\x8a\x01\n\x1bAddTagsToBinaryDataByFilter\x124.viam.app.data.v1.AddTagsToBinaryDataByFilterRequest\x1a5.viam.app.data.v1.AddTagsToBinaryDataByFilterResponse\x12\x90\x01\n\x1dRemoveTagsFromBinaryDataByIDs\x126.viam.app.data.v1.RemoveTagsFromBinaryDataByIDsRequest\x1a7.viam.app.data.v1.RemoveTagsFromBinaryDataByIDsResponse\x12\x99\x01\n RemoveTagsFromBinaryDataByFilter\x129.viam.app.data.v1.RemoveTagsFromBinaryDataByFilterRequest\x1a:.viam.app.data.v1.RemoveTagsFromBinaryDataByFilterResponse\x12]\n\x0cTagsByFilter\x12%.viam.app.data.v1.TagsByFilterRequest\x1a&.viam.app.data.v1.TagsByFilterResponse\x12\x84\x01\n\x19AddBoundingBoxToImageByID\x122.viam.app.data.v1.AddBoundingBoxToImageByIDRequest\x1a3.viam.app.data.v1.AddBoundingBoxToImageByIDResponse\x12\x93\x01\n\x1eRemoveBoundingBoxFromImageByID\x127.viam.app.data.v1.RemoveBoundingBoxFromImageByIDRequest\x1a8.viam.app.data.v1.RemoveBoundingBoxFromImageByIDResponse\x12\x84\x01\n\x19BoundingBoxLabelsByFilter\x122.viam.app.data.v1.BoundingBoxLabelsByFilterRequest\x1a3.viam.app.data.v1.BoundingBoxLabelsByFilterResponseB\x1dZ\x1bgo.viam.com/api/app/data/v1b\x06proto3')
_ORDER = DESCRIPTOR.enum_types_by_name['Order']
Order = enum_type_wrapper.EnumTypeWrapper(_ORDER)
_TAGSFILTERTYPE = DESCRIPTOR.enum_types_by_name['TagsFilterType']
TagsFilterType = enum_type_wrapper.EnumTypeWrapper(_TAGSFILTERTYPE)
ORDER_UNSPECIFIED = 0
ORDER_DESCENDING = 1
ORDER_ASCENDING = 2
TAGS_FILTER_TYPE_UNSPECIFIED = 0
TAGS_FILTER_TYPE_MATCH_BY_OR = 1
TAGS_FILTER_TYPE_TAGGED = 2
TAGS_FILTER_TYPE_UNTAGGED = 3
_DATAREQUEST = DESCRIPTOR.message_types_by_name['DataRequest']
_FILTER = DESCRIPTOR.message_types_by_name['Filter']
_TAGSFILTER = DESCRIPTOR.message_types_by_name['TagsFilter']
_CAPTUREMETADATA = DESCRIPTOR.message_types_by_name['CaptureMetadata']
_CAPTUREMETADATA_METHODPARAMETERSENTRY = _CAPTUREMETADATA.nested_types_by_name['MethodParametersEntry']
_CAPTUREINTERVAL = DESCRIPTOR.message_types_by_name['CaptureInterval']
_TABULARDATABYFILTERREQUEST = DESCRIPTOR.message_types_by_name['TabularDataByFilterRequest']
_TABULARDATABYFILTERRESPONSE = DESCRIPTOR.message_types_by_name['TabularDataByFilterResponse']
_TABULARDATA = DESCRIPTOR.message_types_by_name['TabularData']
_BINARYDATA = DESCRIPTOR.message_types_by_name['BinaryData']
_BINARYDATABYFILTERREQUEST = DESCRIPTOR.message_types_by_name['BinaryDataByFilterRequest']
_BINARYDATABYFILTERRESPONSE = DESCRIPTOR.message_types_by_name['BinaryDataByFilterResponse']
_BINARYID = DESCRIPTOR.message_types_by_name['BinaryID']
_BINARYDATABYIDSREQUEST = DESCRIPTOR.message_types_by_name['BinaryDataByIDsRequest']
_BINARYDATABYIDSRESPONSE = DESCRIPTOR.message_types_by_name['BinaryDataByIDsResponse']
_BOUNDINGBOX = DESCRIPTOR.message_types_by_name['BoundingBox']
_ANNOTATIONS = DESCRIPTOR.message_types_by_name['Annotations']
_BINARYMETADATA = DESCRIPTOR.message_types_by_name['BinaryMetadata']
_DELETETABULARDATABYFILTERREQUEST = DESCRIPTOR.message_types_by_name['DeleteTabularDataByFilterRequest']
_DELETETABULARDATABYFILTERRESPONSE = DESCRIPTOR.message_types_by_name['DeleteTabularDataByFilterResponse']
_DELETETABULARDATAREQUEST = DESCRIPTOR.message_types_by_name['DeleteTabularDataRequest']
_DELETETABULARDATARESPONSE = DESCRIPTOR.message_types_by_name['DeleteTabularDataResponse']
_DELETEBINARYDATABYFILTERREQUEST = DESCRIPTOR.message_types_by_name['DeleteBinaryDataByFilterRequest']
_DELETEBINARYDATABYFILTERRESPONSE = DESCRIPTOR.message_types_by_name['DeleteBinaryDataByFilterResponse']
_DELETEBINARYDATABYIDSREQUEST = DESCRIPTOR.message_types_by_name['DeleteBinaryDataByIDsRequest']
_DELETEBINARYDATABYIDSRESPONSE = DESCRIPTOR.message_types_by_name['DeleteBinaryDataByIDsResponse']
_ADDTAGSTOBINARYDATABYIDSREQUEST = DESCRIPTOR.message_types_by_name['AddTagsToBinaryDataByIDsRequest']
_ADDTAGSTOBINARYDATABYIDSRESPONSE = DESCRIPTOR.message_types_by_name['AddTagsToBinaryDataByIDsResponse']
_ADDTAGSTOBINARYDATABYFILTERREQUEST = DESCRIPTOR.message_types_by_name['AddTagsToBinaryDataByFilterRequest']
_ADDTAGSTOBINARYDATABYFILTERRESPONSE = DESCRIPTOR.message_types_by_name['AddTagsToBinaryDataByFilterResponse']
_REMOVETAGSFROMBINARYDATABYIDSREQUEST = DESCRIPTOR.message_types_by_name['RemoveTagsFromBinaryDataByIDsRequest']
_REMOVETAGSFROMBINARYDATABYIDSRESPONSE = DESCRIPTOR.message_types_by_name['RemoveTagsFromBinaryDataByIDsResponse']
_REMOVETAGSFROMBINARYDATABYFILTERREQUEST = DESCRIPTOR.message_types_by_name['RemoveTagsFromBinaryDataByFilterRequest']
_REMOVETAGSFROMBINARYDATABYFILTERRESPONSE = DESCRIPTOR.message_types_by_name['RemoveTagsFromBinaryDataByFilterResponse']
_TAGSBYFILTERREQUEST = DESCRIPTOR.message_types_by_name['TagsByFilterRequest']
_TAGSBYFILTERRESPONSE = DESCRIPTOR.message_types_by_name['TagsByFilterResponse']
_ADDBOUNDINGBOXTOIMAGEBYIDREQUEST = DESCRIPTOR.message_types_by_name['AddBoundingBoxToImageByIDRequest']
_ADDBOUNDINGBOXTOIMAGEBYIDRESPONSE = DESCRIPTOR.message_types_by_name['AddBoundingBoxToImageByIDResponse']
_REMOVEBOUNDINGBOXFROMIMAGEBYIDREQUEST = DESCRIPTOR.message_types_by_name['RemoveBoundingBoxFromImageByIDRequest']
_REMOVEBOUNDINGBOXFROMIMAGEBYIDRESPONSE = DESCRIPTOR.message_types_by_name['RemoveBoundingBoxFromImageByIDResponse']
_BOUNDINGBOXLABELSBYFILTERREQUEST = DESCRIPTOR.message_types_by_name['BoundingBoxLabelsByFilterRequest']
_BOUNDINGBOXLABELSBYFILTERRESPONSE = DESCRIPTOR.message_types_by_name['BoundingBoxLabelsByFilterResponse']
DataRequest = _reflection.GeneratedProtocolMessageType('DataRequest', (_message.Message,), {'DESCRIPTOR': _DATAREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(DataRequest)
Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {'DESCRIPTOR': _FILTER, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(Filter)
TagsFilter = _reflection.GeneratedProtocolMessageType('TagsFilter', (_message.Message,), {'DESCRIPTOR': _TAGSFILTER, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(TagsFilter)
CaptureMetadata = _reflection.GeneratedProtocolMessageType('CaptureMetadata', (_message.Message,), {'MethodParametersEntry': _reflection.GeneratedProtocolMessageType('MethodParametersEntry', (_message.Message,), {'DESCRIPTOR': _CAPTUREMETADATA_METHODPARAMETERSENTRY, '__module__': 'app.data.v1.data_pb2'}), 'DESCRIPTOR': _CAPTUREMETADATA, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(CaptureMetadata)
_sym_db.RegisterMessage(CaptureMetadata.MethodParametersEntry)
CaptureInterval = _reflection.GeneratedProtocolMessageType('CaptureInterval', (_message.Message,), {'DESCRIPTOR': _CAPTUREINTERVAL, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(CaptureInterval)
TabularDataByFilterRequest = _reflection.GeneratedProtocolMessageType('TabularDataByFilterRequest', (_message.Message,), {'DESCRIPTOR': _TABULARDATABYFILTERREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(TabularDataByFilterRequest)
TabularDataByFilterResponse = _reflection.GeneratedProtocolMessageType('TabularDataByFilterResponse', (_message.Message,), {'DESCRIPTOR': _TABULARDATABYFILTERRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(TabularDataByFilterResponse)
TabularData = _reflection.GeneratedProtocolMessageType('TabularData', (_message.Message,), {'DESCRIPTOR': _TABULARDATA, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(TabularData)
BinaryData = _reflection.GeneratedProtocolMessageType('BinaryData', (_message.Message,), {'DESCRIPTOR': _BINARYDATA, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(BinaryData)
BinaryDataByFilterRequest = _reflection.GeneratedProtocolMessageType('BinaryDataByFilterRequest', (_message.Message,), {'DESCRIPTOR': _BINARYDATABYFILTERREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(BinaryDataByFilterRequest)
BinaryDataByFilterResponse = _reflection.GeneratedProtocolMessageType('BinaryDataByFilterResponse', (_message.Message,), {'DESCRIPTOR': _BINARYDATABYFILTERRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(BinaryDataByFilterResponse)
BinaryID = _reflection.GeneratedProtocolMessageType('BinaryID', (_message.Message,), {'DESCRIPTOR': _BINARYID, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(BinaryID)
BinaryDataByIDsRequest = _reflection.GeneratedProtocolMessageType('BinaryDataByIDsRequest', (_message.Message,), {'DESCRIPTOR': _BINARYDATABYIDSREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(BinaryDataByIDsRequest)
BinaryDataByIDsResponse = _reflection.GeneratedProtocolMessageType('BinaryDataByIDsResponse', (_message.Message,), {'DESCRIPTOR': _BINARYDATABYIDSRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(BinaryDataByIDsResponse)
BoundingBox = _reflection.GeneratedProtocolMessageType('BoundingBox', (_message.Message,), {'DESCRIPTOR': _BOUNDINGBOX, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(BoundingBox)
Annotations = _reflection.GeneratedProtocolMessageType('Annotations', (_message.Message,), {'DESCRIPTOR': _ANNOTATIONS, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(Annotations)
BinaryMetadata = _reflection.GeneratedProtocolMessageType('BinaryMetadata', (_message.Message,), {'DESCRIPTOR': _BINARYMETADATA, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(BinaryMetadata)
DeleteTabularDataByFilterRequest = _reflection.GeneratedProtocolMessageType('DeleteTabularDataByFilterRequest', (_message.Message,), {'DESCRIPTOR': _DELETETABULARDATABYFILTERREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(DeleteTabularDataByFilterRequest)
DeleteTabularDataByFilterResponse = _reflection.GeneratedProtocolMessageType('DeleteTabularDataByFilterResponse', (_message.Message,), {'DESCRIPTOR': _DELETETABULARDATABYFILTERRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(DeleteTabularDataByFilterResponse)
DeleteTabularDataRequest = _reflection.GeneratedProtocolMessageType('DeleteTabularDataRequest', (_message.Message,), {'DESCRIPTOR': _DELETETABULARDATAREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(DeleteTabularDataRequest)
DeleteTabularDataResponse = _reflection.GeneratedProtocolMessageType('DeleteTabularDataResponse', (_message.Message,), {'DESCRIPTOR': _DELETETABULARDATARESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(DeleteTabularDataResponse)
DeleteBinaryDataByFilterRequest = _reflection.GeneratedProtocolMessageType('DeleteBinaryDataByFilterRequest', (_message.Message,), {'DESCRIPTOR': _DELETEBINARYDATABYFILTERREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(DeleteBinaryDataByFilterRequest)
DeleteBinaryDataByFilterResponse = _reflection.GeneratedProtocolMessageType('DeleteBinaryDataByFilterResponse', (_message.Message,), {'DESCRIPTOR': _DELETEBINARYDATABYFILTERRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(DeleteBinaryDataByFilterResponse)
DeleteBinaryDataByIDsRequest = _reflection.GeneratedProtocolMessageType('DeleteBinaryDataByIDsRequest', (_message.Message,), {'DESCRIPTOR': _DELETEBINARYDATABYIDSREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(DeleteBinaryDataByIDsRequest)
DeleteBinaryDataByIDsResponse = _reflection.GeneratedProtocolMessageType('DeleteBinaryDataByIDsResponse', (_message.Message,), {'DESCRIPTOR': _DELETEBINARYDATABYIDSRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(DeleteBinaryDataByIDsResponse)
AddTagsToBinaryDataByIDsRequest = _reflection.GeneratedProtocolMessageType('AddTagsToBinaryDataByIDsRequest', (_message.Message,), {'DESCRIPTOR': _ADDTAGSTOBINARYDATABYIDSREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(AddTagsToBinaryDataByIDsRequest)
AddTagsToBinaryDataByIDsResponse = _reflection.GeneratedProtocolMessageType('AddTagsToBinaryDataByIDsResponse', (_message.Message,), {'DESCRIPTOR': _ADDTAGSTOBINARYDATABYIDSRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(AddTagsToBinaryDataByIDsResponse)
AddTagsToBinaryDataByFilterRequest = _reflection.GeneratedProtocolMessageType('AddTagsToBinaryDataByFilterRequest', (_message.Message,), {'DESCRIPTOR': _ADDTAGSTOBINARYDATABYFILTERREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(AddTagsToBinaryDataByFilterRequest)
AddTagsToBinaryDataByFilterResponse = _reflection.GeneratedProtocolMessageType('AddTagsToBinaryDataByFilterResponse', (_message.Message,), {'DESCRIPTOR': _ADDTAGSTOBINARYDATABYFILTERRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(AddTagsToBinaryDataByFilterResponse)
RemoveTagsFromBinaryDataByIDsRequest = _reflection.GeneratedProtocolMessageType('RemoveTagsFromBinaryDataByIDsRequest', (_message.Message,), {'DESCRIPTOR': _REMOVETAGSFROMBINARYDATABYIDSREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(RemoveTagsFromBinaryDataByIDsRequest)
RemoveTagsFromBinaryDataByIDsResponse = _reflection.GeneratedProtocolMessageType('RemoveTagsFromBinaryDataByIDsResponse', (_message.Message,), {'DESCRIPTOR': _REMOVETAGSFROMBINARYDATABYIDSRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(RemoveTagsFromBinaryDataByIDsResponse)
RemoveTagsFromBinaryDataByFilterRequest = _reflection.GeneratedProtocolMessageType('RemoveTagsFromBinaryDataByFilterRequest', (_message.Message,), {'DESCRIPTOR': _REMOVETAGSFROMBINARYDATABYFILTERREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(RemoveTagsFromBinaryDataByFilterRequest)
RemoveTagsFromBinaryDataByFilterResponse = _reflection.GeneratedProtocolMessageType('RemoveTagsFromBinaryDataByFilterResponse', (_message.Message,), {'DESCRIPTOR': _REMOVETAGSFROMBINARYDATABYFILTERRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(RemoveTagsFromBinaryDataByFilterResponse)
TagsByFilterRequest = _reflection.GeneratedProtocolMessageType('TagsByFilterRequest', (_message.Message,), {'DESCRIPTOR': _TAGSBYFILTERREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(TagsByFilterRequest)
TagsByFilterResponse = _reflection.GeneratedProtocolMessageType('TagsByFilterResponse', (_message.Message,), {'DESCRIPTOR': _TAGSBYFILTERRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(TagsByFilterResponse)
AddBoundingBoxToImageByIDRequest = _reflection.GeneratedProtocolMessageType('AddBoundingBoxToImageByIDRequest', (_message.Message,), {'DESCRIPTOR': _ADDBOUNDINGBOXTOIMAGEBYIDREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(AddBoundingBoxToImageByIDRequest)
AddBoundingBoxToImageByIDResponse = _reflection.GeneratedProtocolMessageType('AddBoundingBoxToImageByIDResponse', (_message.Message,), {'DESCRIPTOR': _ADDBOUNDINGBOXTOIMAGEBYIDRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(AddBoundingBoxToImageByIDResponse)
RemoveBoundingBoxFromImageByIDRequest = _reflection.GeneratedProtocolMessageType('RemoveBoundingBoxFromImageByIDRequest', (_message.Message,), {'DESCRIPTOR': _REMOVEBOUNDINGBOXFROMIMAGEBYIDREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(RemoveBoundingBoxFromImageByIDRequest)
RemoveBoundingBoxFromImageByIDResponse = _reflection.GeneratedProtocolMessageType('RemoveBoundingBoxFromImageByIDResponse', (_message.Message,), {'DESCRIPTOR': _REMOVEBOUNDINGBOXFROMIMAGEBYIDRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(RemoveBoundingBoxFromImageByIDResponse)
BoundingBoxLabelsByFilterRequest = _reflection.GeneratedProtocolMessageType('BoundingBoxLabelsByFilterRequest', (_message.Message,), {'DESCRIPTOR': _BOUNDINGBOXLABELSBYFILTERREQUEST, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(BoundingBoxLabelsByFilterRequest)
BoundingBoxLabelsByFilterResponse = _reflection.GeneratedProtocolMessageType('BoundingBoxLabelsByFilterResponse', (_message.Message,), {'DESCRIPTOR': _BOUNDINGBOXLABELSBYFILTERRESPONSE, '__module__': 'app.data.v1.data_pb2'})
_sym_db.RegisterMessage(BoundingBoxLabelsByFilterResponse)
_DATASERVICE = DESCRIPTOR.services_by_name['DataService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1bgo.viam.com/api/app/data/v1'
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._options = None
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_options = b'8\x01'
    _ORDER._serialized_start = 6014
    _ORDER._serialized_end = 6087
    _TAGSFILTERTYPE._serialized_start = 6090
    _TAGSFILTERTYPE._serialized_end = 6234
    _DATAREQUEST._serialized_start = 135
    _DATAREQUEST._serialized_end = 296
    _FILTER._serialized_start = 299
    _FILTER._serialized_end = 822
    _TAGSFILTER._serialized_start = 824
    _TAGSFILTER._serialized_end = 910
    _CAPTUREMETADATA._serialized_start = 913
    _CAPTUREMETADATA._serialized_end = 1492
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_start = 1380
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_end = 1469
    _CAPTUREINTERVAL._serialized_start = 1494
    _CAPTUREINTERVAL._serialized_end = 1607
    _TABULARDATABYFILTERREQUEST._serialized_start = 1610
    _TABULARDATABYFILTERREQUEST._serialized_end = 1787
    _TABULARDATABYFILTERRESPONSE._serialized_start = 1790
    _TABULARDATABYFILTERRESPONSE._serialized_end = 2017
    _TABULARDATA._serialized_start = 2020
    _TABULARDATA._serialized_end = 2249
    _BINARYDATA._serialized_start = 2251
    _BINARYDATA._serialized_end = 2349
    _BINARYDATABYFILTERREQUEST._serialized_start = 2352
    _BINARYDATABYFILTERREQUEST._serialized_end = 2567
    _BINARYDATABYFILTERRESPONSE._serialized_start = 2570
    _BINARYDATABYFILTERRESPONSE._serialized_end = 2732
    _BINARYID._serialized_start = 2734
    _BINARYID._serialized_end = 2843
    _BINARYDATABYIDSREQUEST._serialized_start = 2846
    _BINARYDATABYIDSREQUEST._serialized_end = 2984
    _BINARYDATABYIDSRESPONSE._serialized_start = 2986
    _BINARYDATABYIDSRESPONSE._serialized_end = 3083
    _BOUNDINGBOX._serialized_start = 3086
    _BOUNDINGBOX._serialized_end = 3305
    _ANNOTATIONS._serialized_start = 3307
    _ANNOTATIONS._serialized_end = 3375
    _BINARYMETADATA._serialized_start = 3378
    _BINARYMETADATA._serialized_end = 3759
    _DELETETABULARDATABYFILTERREQUEST._serialized_start = 3761
    _DELETETABULARDATABYFILTERREQUEST._serialized_end = 3845
    _DELETETABULARDATABYFILTERRESPONSE._serialized_start = 3847
    _DELETETABULARDATABYFILTERRESPONSE._serialized_end = 3933
    _DELETETABULARDATAREQUEST._serialized_start = 3935
    _DELETETABULARDATAREQUEST._serialized_end = 4055
    _DELETETABULARDATARESPONSE._serialized_start = 4057
    _DELETETABULARDATARESPONSE._serialized_end = 4121
    _DELETEBINARYDATABYFILTERREQUEST._serialized_start = 4123
    _DELETEBINARYDATABYFILTERREQUEST._serialized_end = 4206
    _DELETEBINARYDATABYFILTERRESPONSE._serialized_start = 4208
    _DELETEBINARYDATABYFILTERRESPONSE._serialized_end = 4293
    _DELETEBINARYDATABYIDSREQUEST._serialized_start = 4295
    _DELETEBINARYDATABYIDSREQUEST._serialized_end = 4400
    _DELETEBINARYDATABYIDSRESPONSE._serialized_start = 4402
    _DELETEBINARYDATABYIDSRESPONSE._serialized_end = 4484
    _ADDTAGSTOBINARYDATABYIDSREQUEST._serialized_start = 4487
    _ADDTAGSTOBINARYDATABYIDSREQUEST._serialized_end = 4615
    _ADDTAGSTOBINARYDATABYIDSRESPONSE._serialized_start = 4617
    _ADDTAGSTOBINARYDATABYIDSRESPONSE._serialized_end = 4651
    _ADDTAGSTOBINARYDATABYFILTERREQUEST._serialized_start = 4653
    _ADDTAGSTOBINARYDATABYFILTERREQUEST._serialized_end = 4759
    _ADDTAGSTOBINARYDATABYFILTERRESPONSE._serialized_start = 4761
    _ADDTAGSTOBINARYDATABYFILTERRESPONSE._serialized_end = 4798
    _REMOVETAGSFROMBINARYDATABYIDSREQUEST._serialized_start = 4801
    _REMOVETAGSFROMBINARYDATABYIDSREQUEST._serialized_end = 4934
    _REMOVETAGSFROMBINARYDATABYIDSRESPONSE._serialized_start = 4936
    _REMOVETAGSFROMBINARYDATABYIDSRESPONSE._serialized_end = 5012
    _REMOVETAGSFROMBINARYDATABYFILTERREQUEST._serialized_start = 5014
    _REMOVETAGSFROMBINARYDATABYFILTERREQUEST._serialized_end = 5125
    _REMOVETAGSFROMBINARYDATABYFILTERRESPONSE._serialized_start = 5127
    _REMOVETAGSFROMBINARYDATABYFILTERRESPONSE._serialized_end = 5206
    _TAGSBYFILTERREQUEST._serialized_start = 5208
    _TAGSBYFILTERREQUEST._serialized_end = 5279
    _TAGSBYFILTERRESPONSE._serialized_start = 5281
    _TAGSBYFILTERRESPONSE._serialized_end = 5323
    _ADDBOUNDINGBOXTOIMAGEBYIDREQUEST._serialized_start = 5326
    _ADDBOUNDINGBOXTOIMAGEBYIDREQUEST._serialized_end = 5622
    _ADDBOUNDINGBOXTOIMAGEBYIDRESPONSE._serialized_start = 5624
    _ADDBOUNDINGBOXTOIMAGEBYIDRESPONSE._serialized_end = 5684
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDREQUEST._serialized_start = 5687
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDREQUEST._serialized_end = 5823
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDRESPONSE._serialized_start = 5825
    _REMOVEBOUNDINGBOXFROMIMAGEBYIDRESPONSE._serialized_end = 5865
    _BOUNDINGBOXLABELSBYFILTERREQUEST._serialized_start = 5867
    _BOUNDINGBOXLABELSBYFILTERREQUEST._serialized_end = 5951
    _BOUNDINGBOXLABELSBYFILTERRESPONSE._serialized_start = 5953
    _BOUNDINGBOXLABELSBYFILTERRESPONSE._serialized_end = 6012
    _DATASERVICE._serialized_start = 6237
    _DATASERVICE._serialized_end = 8173