## List Apps
data_management_apps = frozenset(['Aplikasi Servicedesk', 'Jabar Open Data (Landing Page Portal Data Jabar)', 'Login Data Pembangunan Jawa Barat', 'Login Executive Dashboard', 'Aplikasi Data Tidak Terstruktur', 'Web Open Data Jawa Barat', 'Sistem Repository Prov Jabar'])
communication_apps = frozenset(['Website resmi Dinas Komunikasi dan Informatika', 'Website Resmi Pemerintah Provinsi Jawa Barat', 'Aplikasi e-Mail (Zimbra)', 'Forum terkait Covid-19'])
logistics_apps = frozenset(['Logistik Alat Kesehatan'])
mapping_apps = frozenset(['Web Satu Peta Jawa Barat', 'GIS Aset Tanah dan Bangunan'])
dashboard_apps = frozenset(['Executive Dashboard', 'Kewilayahan Dashboard', 'Dashboard Monitoring Proyek Infrastruktur'])
covid_related_apps = frozenset(['Web site Pikobar', 'Sistem Test masif Pikobar', 'Admin Test Masif Pikobar', 'Sistem Online Penerima Bantuan Bansos', 'Web Bansos Pikobar'])
event_related_apps = frozenset(['Web site Event Jabar Prov'])
community_service_apps = frozenset(['Sapawarga'])
media_related_apps = frozenset(['web site KPID'])
storage_apps = frozenset(['Drive Jabarprov'])

## List Use Case 
operations_crud = ["Create", "Read", "Update", "Delete"]
data_management_apps_usecases = ['Data entry', 'Data analysis', 'Data visualization', 'Data reporting', 'Data cleaning', 'Data integration', "Input Data", "Read Data", "Update Data", "Delete Data"]
communication_apps_usecases = ['Internal communication', 'External communication', 'Email management', 'Forum discussion', 'Information dissemination']
logistics_apps_usecases = ['Inventory management', 'Supply chain management', 'Delivery tracking', 'Order processing']
mapping_apps_usecases = ['Geospatial analysis', 'Asset tracking', 'Route planning', 'Location-based service']
dashboard_apps_usecases = ['Performance tracking', 'Real-time reporting', 'Data visualization', 'Decision making support']
covid_related_apps_usecases = ['Covid-19 testing', 'Covid-19 case tracking', 'Covid-19 information dissemination', 'Social assistance distribution during Covid-19']
event_related_apps_usecases = ['Event planning', 'Event promotion', 'Ticket sales', 'Event scheduling']
community_service_apps_usecases = ['Community engagement', 'Public service delivery', 'Citizen feedback collection', 'Community information dissemination']
media_related_apps_usecases = ['Media content management', 'Media content distribution', 'Media content creation', 'Media content analysis']
storage_apps_usecases = ['File storage', 'File sharing', 'File backup', 'File synchronization']

apps_ops_mappings = {
    'data_management_apps': data_management_apps_usecases,
    'communication_apps': communication_apps_usecases,
    'logistics_apps': logistics_apps_usecases,
    'mapping_apps': mapping_apps_usecases,
    'dashboard_apps': dashboard_apps_usecases,
    'covid_related_apps': covid_related_apps_usecases,
    'event_related_apps': event_related_apps_usecases,
    'community_service_apps': community_service_apps_usecases,
    'media_related_apps': media_related_apps_usecases,
    'storage_apps': storage_apps_usecases,
}

for apps_category, ops in apps_ops_mappings.items():
    for app in eval(apps_category):
        with open(f"usecases_puml/{app.replace(' ', '_')}.puml", "w") as file:
            file.write(f"@startuml {app}\n")
            file.write(":User: as User\n")
            file.write(f"rectangle {app.replace(' ', '_')}_usecases {{\n")
            for op in ops:
                file.write(f"({op}) as ({op.replace(' ', '')})\n")
            file.write("}\n")
            for op in ops:
                file.write(f"User --> ({op.replace(' ', '')})\n")
            file.write("@enduml\n")