## List Apps
landing_page_apps = frozenset(
    [
        "Jabar Open Data (Landing Page Portal Data Jabar)",
        "Website Resmi Dinas Komunikasi dan Informatika",
        "Website Resmi Pemerintah Provinsi Jawa Barat",
    ]
)

bansos_apps = frozenset(
    [
        "Sistem Online Penerima Bantuan Bansos",
        "Web Bansos Pikobar",
    ]
)

data_management_apps = frozenset(
    [
        "Aplikasi Servicedesk",
        "Login Data Pembangunan Jawa Barat",
        "Login Executive Dashboard",
        "Aplikasi Data Tidak Terstruktur",
        "Web Open Data Jawa Barat",
        "Sistem Repository Prov Jabar",
    ]
)
communication_apps = frozenset(
    [
        "Website Resmi Dinas Komunikasi dan Informatika",
        "Website Resmi Pemerintah Provinsi Jawa Barat",
        "Aplikasi e-Mail (Zimbra)",
        "Forum terkait Covid-19",
    ]
)
logistics_apps = frozenset(["Logistik Alat Kesehatan"])
mapping_apps = frozenset(["Web Satu Peta Jawa Barat", "GIS Aset Tanah dan Bangunan"])
dashboard_apps = frozenset(
    [
        "Executive Dashboard",
        "Kewilayahan Dashboard",
        "Dashboard Monitoring Proyek Infrastruktur",
    ]
)
covid_related_apps = frozenset(
    [
        "Web site Pikobar",
        "Sistem Test masif Pikobar",
        "Admin Test Masif Pikobar",
    ]
)
event_related_apps = frozenset(["Web site Event Jabar Prov"])
community_service_apps = frozenset(["Sapawarga"])
media_related_apps = frozenset(["web site KPID"])
storage_apps = frozenset(["Drive Jabarprov"])

## List Use Case
landing_page_apps_usecases = {
    "Admin": [
        "Pengelolaan Konten",
        "Pengelolaan akun dan permission",
    ],
    "User": ["Akses Informasi", "Contact support"],
}

bansos_apps_usecases = {
    "Admin": [
        "Kelola data penerima bansos",
        "Buat dan kelola formulir pendaftaran bansos",
        "Verifikasi kelayakan penerima bansos",
        "Proses pencairan bansos",
        "Laporkan pelaksanaan pemberian bansos",
    ],
    "User": [
        "Daftar sebagai penerima bansos",
        "Cek status pendaftaran bansos",
        "Laporkan masalah terkait bansos",
    ],
}

data_management_apps_usecases = [
    "Data entry",
    "Data analysis",
    "Data visualization",
    "Data reporting",
    "Data cleaning",
    "Data integration",
    "Input Data",
    "Read Data",
    "Update Data",
    "Delete Data",
]

communication_apps_usecases = [
    "Internal communication",
    "External communication",
    "Email management",
    "Forum discussion",
    "Information dissemination",
]

logistics_apps_usecases = [
    "Inventory management",
    "Supply chain management",
    "Delivery tracking",
    "Order processing",
]

mapping_apps_usecases = [
    "Geospatial analysis",
    "Asset tracking",
    "Route planning",
    "Location-based service",
]

dashboard_apps_usecases = [
    "Performance tracking",
    "Real-time reporting",
    "Data visualization",
    "Decision making support",
]

covid_related_apps_usecases = [
    "Covid-19 testing",
    "Covid-19 case tracking",
    "Covid-19 information dissemination",
    "Social assistance distribution during Covid-19",
]

event_related_apps_usecases = [
    "Event planning",
    "Event promotion",
    "Ticket sales",
    "Event scheduling",
]

community_service_apps_usecases = [
    "Community engagement",
    "Public service delivery",
    "Citizen feedback collection",
    "Community information dissemination",
]

media_related_apps_usecases = [
    "Media content management",
    "Media content distribution",
    "Media content creation",
    "Media content analysis",
]

storage_apps_usecases = [
    "File storage",
    "File sharing",
    "File backup",
    "File synchronization",
]

apps_ops_mappings = {
    "landing_page_apps": landing_page_apps_usecases,
    "bansos_apps": bansos_apps_usecases,
    # "data_management_apps": data_management_apps_usecases,
    # "communication_apps": communication_apps_usecases,
    # "logistics_apps": logistics_apps_usecases,
    # "mapping_apps": mapping_apps_usecases,
    # "dashboard_apps": dashboard_apps_usecases,
    # "covid_related_apps": covid_related_apps_usecases,
    # "event_related_apps": event_related_apps_usecases,
    # "community_service_apps": community_service_apps_usecases,
    # "media_related_apps": media_related_apps_usecases,
    # "storage_apps": storage_apps_usecases,
}

for apps_category, ops in apps_ops_mappings.items():
    for app in eval(apps_category):  # **Potential security risk:** Using eval
        with open(f"usecases_puml/{app.replace(' ', '_')}.puml", "w") as file:
            file.write(f"@startuml {app}\n")
            file.write("left to right direction\n")

            # Write actors only once
            for actor in ops:  # Optimized actor writing
                file.write(f":{actor}: as {actor}\n")

            file.write(f"rectangle {app.replace(' ', '_')} {{\n")
            for _, use_case_list in ops.items():
                for use_case in use_case_list:
                    file.write(f"({use_case}) as ({use_case.replace(' ', '_')})\n")  # Removed extra space
            file.write("}\n")

            for actor, use_case_list in ops.items():
                for use_case in use_case_list:
                    file.write(f"{actor} --> ({use_case.replace(' ', '_')})\n")

            file.write("@enduml\n")


            #  for actor, use_case_list in ops.items():
            #      file.write(f"({use_case} as ({use_case}) \n")

                


# for apps_category, ops in apps_ops_mappings.items():
#     for app in eval(apps_category):
#         with open(f"usecases_puml/{app.replace(' ', '_')}.puml", "w") as file:
#             file.write(f"@startuml {app}\n")
#             file.write(":User: as User\n")
#             file.write(":Admin: as Admin\n")
#             file.write(f"rectangle {app.replace(' ', '_')} {{\n")
#             for op in ops:
#                 file.write(f"({op}) as ({op.replace(' ', '')})\n")
#             file.write("}\n")
#             for op in ops:
#                 file.write(f"User --> ({op.replace(' ', '')})\n")
#             file.write("@enduml\n")
