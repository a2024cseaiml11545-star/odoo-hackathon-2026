{
    'name': 'TransitOps Fuel & Expense',
    'version': '1.0',
    'summary': 'Fuel and Expense Management',
    'author': 'Bhavna',
    'category': 'Fleet',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/fuel_log_views.xml',
        'views/expense_views.xml',
        'views/report_views.xml',
        'reports/fuel_report.xml',
        'reports/expense_report.xml',
    ],
    'installable': True,
    'application': True,
}