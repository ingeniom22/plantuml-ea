#!/bin/bash

# Define the path to the PlantUML JAR file (adjust the path accordingly)
PLANTUML_JAR_PATH="plantuml-1.2023.13.jar"

# Ensure the /out folder exists
mkdir -p out

# Render all .puml files in the /sequences folder
for file in usecases_puml/*.puml; do
    if [[ -f "$file" ]]; then
        echo "Rendering $file..."
        java -jar "$PLANTUML_JAR_PATH" "$file" -o "out"
    fi
done

echo "Rendering completed."
