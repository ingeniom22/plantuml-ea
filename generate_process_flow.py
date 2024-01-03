apps_crud = frozenset({1, 2, 3})
apps_x = frozenset({4, 5, 6})
apps_y = frozenset({7, 8, 9})
apps_z = frozenset({10, 11, 12})

operations_crud = ["Create", "Read", "Update", "Delete"]
operations_x = ["A", 'B']
operations_y = ["C", "D"]
operations_z = ["E", "F"]

apps_ops_mappings = {
    apps_crud: operations_crud,
    apps_x: operations_x,
    apps_y: operations_y,
    apps_z: operations_z,
}

for apps, ops in apps_ops_mappings.items():
    for app in apps:
        for op in ops:
            print(app, op)
            # # Define the PlantUML code for each combination
            # plantuml_code = f"""
            # @startuml
            # start
            # :User {op} {app[:-1]};
            # :View;
            # if (Valid Input?) then (yes)
            # :Copntrappplleapp;
            # if (Valid {op}?) then (yes)
            #     :Model;
            #     if ({app} {op} Successful?) then (yes)
            #     :Update {op} Record;
            #     else (no)
            #     :Display Error Message;
            #     endif
            # else (no)
            #     :Display Validation Error;
            # endif
            # else (no)
            # :Display Error Message;
            # endif
            # stop
            # @enduml
            # """

            # # Write the PlantUML code to a file
            # with open(f"activities/activity_{app}_{op}.puml", "w") as file:
            #     file.write(plantuml_code)

print("Activity diagrams generated successfully.")
