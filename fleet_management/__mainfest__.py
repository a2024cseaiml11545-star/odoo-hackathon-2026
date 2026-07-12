{
    'name': 'Fleet Management',
    'version': '1.0',
    'summary': 'Driver and Trip Management Module',
    'author': 'Team Hackathon',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/driver_views.xml',
        'views/trip_views.xml',
    ],
    'installable': True,
    'application': True,
}