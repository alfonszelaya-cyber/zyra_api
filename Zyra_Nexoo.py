import os
import shutil

# Definición de la estructura base de ZYRA_PLATFORM
BASE_DIRS = [
    "core/config", "core/security", "core/events", "core/database", 
    "core/regions", "core/domain", "core/services", "core/shared",
    "gateway", "bus",
    "foundations/identity", "foundations/trust", "foundations/verification", 
    "foundations/ledger", "foundations/audit", "foundations/governance",
    "ecosystem/nexo", "ecosystem/semilla", "ecosystem/axis", "ecosystem/agro", 
    "ecosystem/mi_primer_empleo", "ecosystem/subastas", "ecosystem/reciclaje_digital", 
    "ecosystem/arqueologia_digital", "ecosystem/controlador_espacios", 
    "ecosystem/decisiones_reales", "ecosystem/governance_portal", 
    "ecosystem/security_command", "ecosystem/rednew", "ecosystem/cerebrotic",
    "sdk", "generator", "infrastructure", "deployments", 
    "monitoring", "tests", "docs", "docker"
]

# Archivos base que se generan automáticamente
BASE_FILES = {
    "docker/docker-compose.yml": """version: '3.8'

services:
  gateway:
    build: ../gateway
    ports:
      - "8080:8080"
    environment:
      - NODE_ENV=development
    networks:
      - zyra_network

  event_bus:
    build: ../bus
    ports:
      - "9090:9090"
    networks:
      - zyra_network

networks:
  zyra_network:
    driver: bridge
""",
    "gateway/Dockerfile": """FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 8080
CMD ["node", "server.js"]
""",
    "gateway/server.js": """const express = require('express');
const app = express();
const PORT = 8080;

app.get('/health', (req, res) => res.status(200).send('ZYRA Gateway OK'));
app.listen(PORT, () => console.log(`ZYRA Gateway running on port ${PORT}`));
""",
    "bus/Dockerfile": """FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 9090
CMD ["python", "bus_main.py"]
""",
    "bus/bus_main.py": """print("ZYRA Event Bus Iniciado...")
""",
    "core/config/config.json": """{\n  "platform": "ZYRA",\n  "version": "1.0.0",\n  "environment": "auto-generated"\n}""",
    "ecosystem/manifest.json": """{\n  "apps": ["nexo", "semilla", "axis", "agro", "rednew"]\n}""",
    "README.md": "# ZYRA PLATFORM\\nInfraestructura generada automáticamente. Red de microservicios activa."
}

def create_zyra_structure():
    root_dir = "ZYRA_PLATFORM"
    
    # Crear directorios
    for d in BASE_DIRS:
        os.makedirs(os.path.join(root_dir, d), exist_ok=True)
        # Añadir .gitkeep para que git reconozca las carpetas vacías
        open(os.path.join(root_dir, d, ".gitkeep"), "w").close()
    
    # Crear archivos base
    for filepath, content in BASE_FILES.items():
        full_path = os.path.join(root_dir, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
            
    print(f"✅ Estructura de ZYRA_PLATFORM creada exitosamente en ./{root_dir}")

if __name__ == "__main__":
    create_zyra_structure()
