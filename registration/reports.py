from registration.models import Delivery
from model_report.report import reports, ReportAdmin

class DeliveryReport(ReportAdmin):
    title = ('Delivery Report')
    model = Delivery
    fields = [
        'Delivery_ID',
        'Delivery_Reg_Time',
        'Delivery_Total',
    ]
    list_order_by = ('Delivery_ID', 'Delivery_Reg_Time', 'Delivery_Total')
    type = 'report'

reports.register('anymodel-report', DeliveryReport)