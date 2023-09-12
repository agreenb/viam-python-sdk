"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14app/v1/billing.proto\x12\x0bviam.app.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\x97\x05\n\x18CurrentMonthUsageSummary\x12.\n\x13cloud_storage_usage\x18\x01 \x01(\x01R\x11cloudStorageUsage\x127\n\x18cloud_storage_usage_cost\x18\x02 \x01(\x01R\x15cloudStorageUsageCost\x123\n\x16data_upload_usage_cost\x18\x03 \x01(\x01R\x13dataUploadUsageCost\x12;\n\x1adata_upload_usage_quantity\x18\x04 \x01(\x01R\x17dataUploadUsageQuantity\x121\n\x15data_egres_usage_cost\x18\x05 \x01(\x01R\x12dataEgresUsageCost\x129\n\x19data_egres_usage_quantity\x18\x06 \x01(\x01R\x16dataEgresUsageQuantity\x12=\n\x1bstandard_compute_usage_cost\x18\x07 \x01(\x01R\x18standardComputeUsageCost\x12E\n\x1fstandard_compute_usage_quantity\x18\x08 \x01(\x01R\x1cstandardComputeUsageQuantity\x120\n\x14total_usage_quantity\x18\t \x01(\x01R\x12totalUsageQuantity\x129\n\x19total_usage_with_discount\x18\n \x01(\x01R\x16totalUsageWithDiscount\x12?\n\x1ctotal_usage_without_discount\x18\x0b \x01(\x01R\x19totalUsageWithoutDiscount"\x8e\x02\n\x0eInvoiceSummary\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12=\n\x0cinvoice_date\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0binvoiceDate\x12%\n\x0einvoice_amount\x18\x03 \x01(\x01R\rinvoiceAmount\x12\x16\n\x06status\x18\x04 \x01(\tR\x06status\x125\n\x08due_date\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07dueDate\x127\n\tpaid_date\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\x08paidDate"\x8b\x02\n\x15BillableResourceEvent\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12%\n\x0eusage_quantity\x18\x03 \x01(\x01R\rusageQuantity\x12.\n\x13usage_quantity_unit\x18\x04 \x01(\tR\x11usageQuantityUnit\x12\x1d\n\nusage_cost\x18\x05 \x01(\tR\tusageCost\x12;\n\x0boccurred_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\noccurredAt\x12\x1b\n\tuser_name\x18\x07 \x01(\tR\x08userName"\xa7\x02\n\x07Invoice\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12=\n\x0cinvoice_date\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0binvoiceDate\x12%\n\x0einvoice_amount\x18\x03 \x01(\x01R\rinvoiceAmount\x12\x16\n\x06status\x18\x04 \x01(\tR\x06status\x125\n\x08due_date\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07dueDate\x128\n\x05items\x18\x06 \x03(\x0b2".viam.app.v1.BillableResourceEventR\x05items\x12\x1d\n\nemailed_to\x18\x07 \x01(\tR\temailedTo"S\n\x11PaymentMethodCard\x12\x14\n\x05brand\x18\x01 \x01(\tR\x05brand\x12(\n\x10last_four_digits\x18\x02 \x01(\tR\x0elastFourDigits";\n"GetCurrentMonthUsageSummaryRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\xa2\x05\n#GetCurrentMonthUsageSummaryResponse\x12.\n\x13cloud_storage_usage\x18\x01 \x01(\x01R\x11cloudStorageUsage\x127\n\x18cloud_storage_usage_cost\x18\x02 \x01(\x01R\x15cloudStorageUsageCost\x123\n\x16data_upload_usage_cost\x18\x03 \x01(\x01R\x13dataUploadUsageCost\x12;\n\x1adata_upload_usage_quantity\x18\x04 \x01(\x01R\x17dataUploadUsageQuantity\x121\n\x15data_egres_usage_cost\x18\x05 \x01(\x01R\x12dataEgresUsageCost\x129\n\x19data_egres_usage_quantity\x18\x06 \x01(\x01R\x16dataEgresUsageQuantity\x12=\n\x1bstandard_compute_usage_cost\x18\x07 \x01(\x01R\x18standardComputeUsageCost\x12E\n\x1fstandard_compute_usage_quantity\x18\x08 \x01(\x01R\x1cstandardComputeUsageQuantity\x120\n\x14total_usage_quantity\x18\t \x01(\x01R\x12totalUsageQuantity\x129\n\x19total_usage_with_discount\x18\n \x01(\x01R\x16totalUsageWithDiscount\x12?\n\x1ctotal_usage_without_discount\x18\x0b \x01(\x01R\x19totalUsageWithoutDiscount"4\n\x1bGetCurrentMonthUsageRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\xd0\x04\n\x1cGetCurrentMonthUsageResponse\x129\n\nstart_date\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\tstartDate\x125\n\x08end_date\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07endDate\x127\n\x18cloud_storage_usage_cost\x18\x03 \x01(\x01R\x15cloudStorageUsageCost\x123\n\x16data_upload_usage_cost\x18\x04 \x01(\x01R\x13dataUploadUsageCost\x121\n\x15data_egres_usage_cost\x18\x05 \x01(\x01R\x12dataEgresUsageCost\x129\n\x19remote_control_usage_cost\x18\x06 \x01(\x01R\x16remoteControlUsageCost\x12=\n\x1bstandard_compute_usage_cost\x18\x07 \x01(\x01R\x18standardComputeUsageCost\x12\'\n\x0fdiscount_amount\x18\x08 \x01(\x01R\x0ediscountAmount\x129\n\x19total_usage_with_discount\x18\t \x01(\x01R\x16totalUsageWithDiscount\x12?\n\x1ctotal_usage_without_discount\x18\n \x01(\x01R\x19totalUsageWithoutDiscount"0\n\x17GetUnpaidBalanceRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\x94\x01\n\x18GetUnpaidBalanceResponse\x12%\n\x0eunpaid_balance\x18\x01 \x01(\x01R\runpaidBalance\x12Q\n\x17unpaid_balance_due_date\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x14unpaidBalanceDueDate"1\n\x18GetInvoiceHistoryRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"T\n\x19GetInvoiceHistoryResponse\x127\n\x08invoices\x18\x01 \x03(\x0b2\x1b.viam.app.v1.InvoiceSummaryR\x08invoices"+\n\x19GetItemizedInvoiceRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"L\n\x1aGetItemizedInvoiceResponse\x12.\n\x07invoice\x18\x01 \x01(\x0b2\x14.viam.app.v1.InvoiceR\x07invoice"8\n\x1fGetOrgBillingInformationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\xfc\x01\n GetOrgBillingInformationResponse\x122\n\x04type\x18\x01 \x01(\x0e2\x1e.viam.app.v1.PaymentMethodTypeR\x04type\x12#\n\rbilling_email\x18\x02 \x01(\tR\x0cbillingEmail\x12;\n\x06method\x18\x03 \x01(\x0b2\x1e.viam.app.v1.PaymentMethodCardH\x00R\x06method\x88\x01\x01\x12&\n\x0cbilling_tier\x18\x04 \x01(\tH\x01R\x0bbillingTier\x88\x01\x01B\t\n\x07_methodB\x0f\n\r_billing_tier"2\n\x19GetInvoicesSummaryRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\x86\x01\n\x1aGetInvoicesSummaryResponse\x12/\n\x13outstanding_balance\x18\x01 \x01(\x01R\x12outstandingBalance\x127\n\x08invoices\x18\x02 \x03(\x0b2\x1b.viam.app.v1.InvoiceSummaryR\x08invoices"1\n\x18GetBillingSummaryRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"\xe7\x03\n\x19GetBillingSummaryResponse\x12J\n\rusage_summary\x18\x01 \x01(\x0b2%.viam.app.v1.CurrentMonthUsageSummaryR\x0cusageSummary\x127\n\x08invoices\x18\x02 \x03(\x0b2\x1b.viam.app.v1.InvoiceSummaryR\x08invoices\x12+\n\x11statement_balance\x18\x03 \x01(\x01R\x10statementBalance\x12\'\n\x0fcurrent_balance\x18\x04 \x01(\x01R\x0ecurrentBalance\x122\n\x15current_month_balance\x18\x05 \x01(\x01R\x13currentMonthBalance\x12O\n\x16current_month_due_date\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampR\x13currentMonthDueDate\x12#\n\rinvoice_email\x18\x08 \x01(\tR\x0cinvoiceEmail\x12E\n\x0epayment_method\x18\t \x01(\x0b2\x1e.viam.app.v1.PaymentMethodCardR\rpaymentMethod"=\n\x14GetInvoicePdfRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId"-\n\x15GetInvoicePdfResponse\x12\x14\n\x05chunk\x18\x01 \x01(\x0cR\x05chunk*V\n\x11PaymentMethodType\x12#\n\x1fPAYMENT_METHOD_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18PAYMENT_METHOD_TYPE_CARD\x10\x012\xca\x07\n\x0eBillingService\x12\x80\x01\n\x1bGetCurrentMonthUsageSummary\x12/.viam.app.v1.GetCurrentMonthUsageSummaryRequest\x1a0.viam.app.v1.GetCurrentMonthUsageSummaryResponse\x12_\n\x10GetUnpaidBalance\x12$.viam.app.v1.GetUnpaidBalanceRequest\x1a%.viam.app.v1.GetUnpaidBalanceResponse\x12b\n\x11GetInvoiceHistory\x12%.viam.app.v1.GetInvoiceHistoryRequest\x1a&.viam.app.v1.GetInvoiceHistoryResponse\x12e\n\x12GetItemizedInvoice\x12&.viam.app.v1.GetItemizedInvoiceRequest\x1a\'.viam.app.v1.GetItemizedInvoiceResponse\x12b\n\x11GetBillingSummary\x12%.viam.app.v1.GetBillingSummaryRequest\x1a&.viam.app.v1.GetBillingSummaryResponse\x12k\n\x14GetCurrentMonthUsage\x12(.viam.app.v1.GetCurrentMonthUsageRequest\x1a).viam.app.v1.GetCurrentMonthUsageResponse\x12w\n\x18GetOrgBillingInformation\x12,.viam.app.v1.GetOrgBillingInformationRequest\x1a-.viam.app.v1.GetOrgBillingInformationResponse\x12e\n\x12GetInvoicesSummary\x12&.viam.app.v1.GetInvoicesSummaryRequest\x1a\'.viam.app.v1.GetInvoicesSummaryResponse\x12X\n\rGetInvoicePdf\x12!.viam.app.v1.GetInvoicePdfRequest\x1a".viam.app.v1.GetInvoicePdfResponse0\x01B\x18Z\x16go.viam.com/api/app/v1b\x06proto3')
_PAYMENTMETHODTYPE = DESCRIPTOR.enum_types_by_name['PaymentMethodType']
PaymentMethodType = enum_type_wrapper.EnumTypeWrapper(_PAYMENTMETHODTYPE)
PAYMENT_METHOD_TYPE_UNSPECIFIED = 0
PAYMENT_METHOD_TYPE_CARD = 1
_CURRENTMONTHUSAGESUMMARY = DESCRIPTOR.message_types_by_name['CurrentMonthUsageSummary']
_INVOICESUMMARY = DESCRIPTOR.message_types_by_name['InvoiceSummary']
_BILLABLERESOURCEEVENT = DESCRIPTOR.message_types_by_name['BillableResourceEvent']
_INVOICE = DESCRIPTOR.message_types_by_name['Invoice']
_PAYMENTMETHODCARD = DESCRIPTOR.message_types_by_name['PaymentMethodCard']
_GETCURRENTMONTHUSAGESUMMARYREQUEST = DESCRIPTOR.message_types_by_name['GetCurrentMonthUsageSummaryRequest']
_GETCURRENTMONTHUSAGESUMMARYRESPONSE = DESCRIPTOR.message_types_by_name['GetCurrentMonthUsageSummaryResponse']
_GETCURRENTMONTHUSAGEREQUEST = DESCRIPTOR.message_types_by_name['GetCurrentMonthUsageRequest']
_GETCURRENTMONTHUSAGERESPONSE = DESCRIPTOR.message_types_by_name['GetCurrentMonthUsageResponse']
_GETUNPAIDBALANCEREQUEST = DESCRIPTOR.message_types_by_name['GetUnpaidBalanceRequest']
_GETUNPAIDBALANCERESPONSE = DESCRIPTOR.message_types_by_name['GetUnpaidBalanceResponse']
_GETINVOICEHISTORYREQUEST = DESCRIPTOR.message_types_by_name['GetInvoiceHistoryRequest']
_GETINVOICEHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['GetInvoiceHistoryResponse']
_GETITEMIZEDINVOICEREQUEST = DESCRIPTOR.message_types_by_name['GetItemizedInvoiceRequest']
_GETITEMIZEDINVOICERESPONSE = DESCRIPTOR.message_types_by_name['GetItemizedInvoiceResponse']
_GETORGBILLINGINFORMATIONREQUEST = DESCRIPTOR.message_types_by_name['GetOrgBillingInformationRequest']
_GETORGBILLINGINFORMATIONRESPONSE = DESCRIPTOR.message_types_by_name['GetOrgBillingInformationResponse']
_GETINVOICESSUMMARYREQUEST = DESCRIPTOR.message_types_by_name['GetInvoicesSummaryRequest']
_GETINVOICESSUMMARYRESPONSE = DESCRIPTOR.message_types_by_name['GetInvoicesSummaryResponse']
_GETBILLINGSUMMARYREQUEST = DESCRIPTOR.message_types_by_name['GetBillingSummaryRequest']
_GETBILLINGSUMMARYRESPONSE = DESCRIPTOR.message_types_by_name['GetBillingSummaryResponse']
_GETINVOICEPDFREQUEST = DESCRIPTOR.message_types_by_name['GetInvoicePdfRequest']
_GETINVOICEPDFRESPONSE = DESCRIPTOR.message_types_by_name['GetInvoicePdfResponse']
CurrentMonthUsageSummary = _reflection.GeneratedProtocolMessageType('CurrentMonthUsageSummary', (_message.Message,), {'DESCRIPTOR': _CURRENTMONTHUSAGESUMMARY, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(CurrentMonthUsageSummary)
InvoiceSummary = _reflection.GeneratedProtocolMessageType('InvoiceSummary', (_message.Message,), {'DESCRIPTOR': _INVOICESUMMARY, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(InvoiceSummary)
BillableResourceEvent = _reflection.GeneratedProtocolMessageType('BillableResourceEvent', (_message.Message,), {'DESCRIPTOR': _BILLABLERESOURCEEVENT, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(BillableResourceEvent)
Invoice = _reflection.GeneratedProtocolMessageType('Invoice', (_message.Message,), {'DESCRIPTOR': _INVOICE, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(Invoice)
PaymentMethodCard = _reflection.GeneratedProtocolMessageType('PaymentMethodCard', (_message.Message,), {'DESCRIPTOR': _PAYMENTMETHODCARD, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(PaymentMethodCard)
GetCurrentMonthUsageSummaryRequest = _reflection.GeneratedProtocolMessageType('GetCurrentMonthUsageSummaryRequest', (_message.Message,), {'DESCRIPTOR': _GETCURRENTMONTHUSAGESUMMARYREQUEST, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetCurrentMonthUsageSummaryRequest)
GetCurrentMonthUsageSummaryResponse = _reflection.GeneratedProtocolMessageType('GetCurrentMonthUsageSummaryResponse', (_message.Message,), {'DESCRIPTOR': _GETCURRENTMONTHUSAGESUMMARYRESPONSE, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetCurrentMonthUsageSummaryResponse)
GetCurrentMonthUsageRequest = _reflection.GeneratedProtocolMessageType('GetCurrentMonthUsageRequest', (_message.Message,), {'DESCRIPTOR': _GETCURRENTMONTHUSAGEREQUEST, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetCurrentMonthUsageRequest)
GetCurrentMonthUsageResponse = _reflection.GeneratedProtocolMessageType('GetCurrentMonthUsageResponse', (_message.Message,), {'DESCRIPTOR': _GETCURRENTMONTHUSAGERESPONSE, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetCurrentMonthUsageResponse)
GetUnpaidBalanceRequest = _reflection.GeneratedProtocolMessageType('GetUnpaidBalanceRequest', (_message.Message,), {'DESCRIPTOR': _GETUNPAIDBALANCEREQUEST, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetUnpaidBalanceRequest)
GetUnpaidBalanceResponse = _reflection.GeneratedProtocolMessageType('GetUnpaidBalanceResponse', (_message.Message,), {'DESCRIPTOR': _GETUNPAIDBALANCERESPONSE, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetUnpaidBalanceResponse)
GetInvoiceHistoryRequest = _reflection.GeneratedProtocolMessageType('GetInvoiceHistoryRequest', (_message.Message,), {'DESCRIPTOR': _GETINVOICEHISTORYREQUEST, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetInvoiceHistoryRequest)
GetInvoiceHistoryResponse = _reflection.GeneratedProtocolMessageType('GetInvoiceHistoryResponse', (_message.Message,), {'DESCRIPTOR': _GETINVOICEHISTORYRESPONSE, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetInvoiceHistoryResponse)
GetItemizedInvoiceRequest = _reflection.GeneratedProtocolMessageType('GetItemizedInvoiceRequest', (_message.Message,), {'DESCRIPTOR': _GETITEMIZEDINVOICEREQUEST, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetItemizedInvoiceRequest)
GetItemizedInvoiceResponse = _reflection.GeneratedProtocolMessageType('GetItemizedInvoiceResponse', (_message.Message,), {'DESCRIPTOR': _GETITEMIZEDINVOICERESPONSE, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetItemizedInvoiceResponse)
GetOrgBillingInformationRequest = _reflection.GeneratedProtocolMessageType('GetOrgBillingInformationRequest', (_message.Message,), {'DESCRIPTOR': _GETORGBILLINGINFORMATIONREQUEST, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetOrgBillingInformationRequest)
GetOrgBillingInformationResponse = _reflection.GeneratedProtocolMessageType('GetOrgBillingInformationResponse', (_message.Message,), {'DESCRIPTOR': _GETORGBILLINGINFORMATIONRESPONSE, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetOrgBillingInformationResponse)
GetInvoicesSummaryRequest = _reflection.GeneratedProtocolMessageType('GetInvoicesSummaryRequest', (_message.Message,), {'DESCRIPTOR': _GETINVOICESSUMMARYREQUEST, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetInvoicesSummaryRequest)
GetInvoicesSummaryResponse = _reflection.GeneratedProtocolMessageType('GetInvoicesSummaryResponse', (_message.Message,), {'DESCRIPTOR': _GETINVOICESSUMMARYRESPONSE, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetInvoicesSummaryResponse)
GetBillingSummaryRequest = _reflection.GeneratedProtocolMessageType('GetBillingSummaryRequest', (_message.Message,), {'DESCRIPTOR': _GETBILLINGSUMMARYREQUEST, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetBillingSummaryRequest)
GetBillingSummaryResponse = _reflection.GeneratedProtocolMessageType('GetBillingSummaryResponse', (_message.Message,), {'DESCRIPTOR': _GETBILLINGSUMMARYRESPONSE, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetBillingSummaryResponse)
GetInvoicePdfRequest = _reflection.GeneratedProtocolMessageType('GetInvoicePdfRequest', (_message.Message,), {'DESCRIPTOR': _GETINVOICEPDFREQUEST, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetInvoicePdfRequest)
GetInvoicePdfResponse = _reflection.GeneratedProtocolMessageType('GetInvoicePdfResponse', (_message.Message,), {'DESCRIPTOR': _GETINVOICEPDFRESPONSE, '__module__': 'app.v1.billing_pb2'})
_sym_db.RegisterMessage(GetInvoicePdfResponse)
_BILLINGSERVICE = DESCRIPTOR.services_by_name['BillingService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x16go.viam.com/api/app/v1'
    _PAYMENTMETHODTYPE._serialized_start = 4663
    _PAYMENTMETHODTYPE._serialized_end = 4749
    _CURRENTMONTHUSAGESUMMARY._serialized_start = 71
    _CURRENTMONTHUSAGESUMMARY._serialized_end = 734
    _INVOICESUMMARY._serialized_start = 737
    _INVOICESUMMARY._serialized_end = 1007
    _BILLABLERESOURCEEVENT._serialized_start = 1010
    _BILLABLERESOURCEEVENT._serialized_end = 1277
    _INVOICE._serialized_start = 1280
    _INVOICE._serialized_end = 1575
    _PAYMENTMETHODCARD._serialized_start = 1577
    _PAYMENTMETHODCARD._serialized_end = 1660
    _GETCURRENTMONTHUSAGESUMMARYREQUEST._serialized_start = 1662
    _GETCURRENTMONTHUSAGESUMMARYREQUEST._serialized_end = 1721
    _GETCURRENTMONTHUSAGESUMMARYRESPONSE._serialized_start = 1724
    _GETCURRENTMONTHUSAGESUMMARYRESPONSE._serialized_end = 2398
    _GETCURRENTMONTHUSAGEREQUEST._serialized_start = 2400
    _GETCURRENTMONTHUSAGEREQUEST._serialized_end = 2452
    _GETCURRENTMONTHUSAGERESPONSE._serialized_start = 2455
    _GETCURRENTMONTHUSAGERESPONSE._serialized_end = 3047
    _GETUNPAIDBALANCEREQUEST._serialized_start = 3049
    _GETUNPAIDBALANCEREQUEST._serialized_end = 3097
    _GETUNPAIDBALANCERESPONSE._serialized_start = 3100
    _GETUNPAIDBALANCERESPONSE._serialized_end = 3248
    _GETINVOICEHISTORYREQUEST._serialized_start = 3250
    _GETINVOICEHISTORYREQUEST._serialized_end = 3299
    _GETINVOICEHISTORYRESPONSE._serialized_start = 3301
    _GETINVOICEHISTORYRESPONSE._serialized_end = 3385
    _GETITEMIZEDINVOICEREQUEST._serialized_start = 3387
    _GETITEMIZEDINVOICEREQUEST._serialized_end = 3430
    _GETITEMIZEDINVOICERESPONSE._serialized_start = 3432
    _GETITEMIZEDINVOICERESPONSE._serialized_end = 3508
    _GETORGBILLINGINFORMATIONREQUEST._serialized_start = 3510
    _GETORGBILLINGINFORMATIONREQUEST._serialized_end = 3566
    _GETORGBILLINGINFORMATIONRESPONSE._serialized_start = 3569
    _GETORGBILLINGINFORMATIONRESPONSE._serialized_end = 3821
    _GETINVOICESSUMMARYREQUEST._serialized_start = 3823
    _GETINVOICESSUMMARYREQUEST._serialized_end = 3873
    _GETINVOICESSUMMARYRESPONSE._serialized_start = 3876
    _GETINVOICESSUMMARYRESPONSE._serialized_end = 4010
    _GETBILLINGSUMMARYREQUEST._serialized_start = 4012
    _GETBILLINGSUMMARYREQUEST._serialized_end = 4061
    _GETBILLINGSUMMARYRESPONSE._serialized_start = 4064
    _GETBILLINGSUMMARYRESPONSE._serialized_end = 4551
    _GETINVOICEPDFREQUEST._serialized_start = 4553
    _GETINVOICEPDFREQUEST._serialized_end = 4614
    _GETINVOICEPDFRESPONSE._serialized_start = 4616
    _GETINVOICEPDFRESPONSE._serialized_end = 4661
    _BILLINGSERVICE._serialized_start = 4752
    _BILLINGSERVICE._serialized_end = 5722