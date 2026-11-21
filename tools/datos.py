"""Datos del portal: ciclos, asignaturas y relación de conceptos entre asignaturas.

Para añadir una asignatura, añádela a la lista «asignaturas» de su ciclo y ejecuta:
    python3 tools/generar.py
Una asignatura que pertenece a varios ciclos (Bases de datos, Digitalización) se escribe una vez
en ASIGNATURAS y se nombra por su clave en cada ciclo.
"""

GH = "https://lorenalresusta.github.io/"
REPO = "https://github.com/LorenaLResusta/"

ASIGNATURAS = {
    "gbd": {
        "nombre": "Gestión de bases de datos", "codigo": "0372", "curso": "1.º ASIR", "horas": "160 h",
        "web": GH + "GBD/", "repo": REPO + "GBD",
        "resumen": "Diseño lógico y físico, SQL (DDL, consultas, modificación) y aseguramiento de la información.",
        "temas": ["SGBD", "Diseño", "SQL", "Copias y usuarios"],
    },
    "sad": {
        "nombre": "Seguridad y alta disponibilidad", "codigo": "0378", "curso": "2.º ASIR", "horas": "",
        "web": GH + "Seguridad-y-Alta-Disponibilidad/", "repo": REPO + "Seguridad-y-Alta-Disponibilidad",
        "resumen": "Riesgos y marco legal, copias, criptografía, fortificación, monitorización, seguridad perimetral y alta disponibilidad.",
        "temas": ["Copias", "Criptografía", "Cortafuegos", "Alta disponibilidad"],
    },
    "bbdd": {
        "nombre": "Bases de datos", "codigo": "0484", "curso": "1.º DAM y DAW", "horas": "",
        "web": GH + "BBDD/", "repo": REPO + "BBDD",
        "resumen": "Modelo entidad/relación, modelo relacional, normalización, SQL, transacciones, PL/SQL y NoSQL.",
        "temas": ["Modelo E/R", "SQL", "PL/SQL", "NoSQL"],
    },
    "digitalizacion": {
        "nombre": "Digitalización aplicada a los sectores productivos", "codigo": "1665", "curso": "Ciclos de grado superior", "horas": "",
        "web": GH + "Digitalizacion/", "repo": REPO + "Digitalizacion",
        "resumen": "Transformación digital de los sectores productivos y tecnologías habilitadoras.",
        "temas": ["Transformación digital", "Nube", "Datos"],
    },
    "despliegue": {
        "nombre": "Despliegue de plataformas de ejecución de contenedores", "codigo": "5166", "curso": "Curso de especialización", "horas": "120 h",
        "web": GH + "Despliegue-Contenedores/", "repo": REPO + "Despliegue-Contenedores",
        "resumen": "Contenedores y virtualización ligera, Docker y Podman, Kubernetes, redes y almacenamiento, seguridad y monitorización.",
        "temas": ["Docker", "Kubernetes", "Redes", "Seguridad"],
    },
    "mantenimiento": {
        "nombre": "Mantenimiento del sistema de contenedores desplegado", "codigo": "5169", "curso": "Curso de especialización", "horas": "45 h",
        "web": GH + "Mantenimiento-Contenedores/", "repo": REPO + "Mantenimiento-Contenedores",
        "resumen": "Monitorización y alarmas, validación, extracción de datos, copias y actualizaciones, y baja segura del servicio.",
        "temas": ["Prometheus", "Pruebas", "Copias", "Baja segura"],
    },
    "bbdd-nube": {
        "nombre": "Administración de bases de datos y almacenamiento en la nube", "codigo": "5162", "curso": "Curso de especialización", "horas": "100 h",
        "web": GH + "BBDD-Nube/", "repo": REPO + "BBDD-Nube",
        "resumen": "Almacenamiento de objetos, bloques y ficheros, bases de datos administradas, transferencia, nube híbrida y analítica.",
        "temas": ["Objetos (S3)", "Bases de datos", "Nube híbrida"],
    },
    "aei": {
        "nombre": "Aprendizaje y enseñanza de la informática", "codigo": "Bloque II", "curso": "Máster de Profesorado · UA", "horas": "",
        "web": GH + "AEI/", "repo": REPO + "AEI",
        "resumen": "La programación didáctica en Formación Profesional de Informática.",
        "temas": ["Programación didáctica"],
    },
}

CICLOS = [
    {"id": "asir", "sigla": "ASIR", "icono": "🖥️", "color": "#2f6fb2",
     "nombre": "Administración de Sistemas Informáticos en Red", "tipo": "Ciclo de grado superior",
     "grupos": [("1.º curso", ["gbd"]), ("2.º curso", ["sad"]), ("Común a los ciclos de grado superior", ["digitalizacion"])]},
    {"id": "dam", "sigla": "DAM", "icono": "💻", "color": "#8a4fb8",
     "nombre": "Desarrollo de Aplicaciones Multiplataforma", "tipo": "Ciclo de grado superior",
     "grupos": [("1.º curso", ["bbdd"]), ("Común a los ciclos de grado superior", ["digitalizacion"])]},
    {"id": "daw", "sigla": "DAW", "icono": "🌐", "color": "#c46a1b",
     "nombre": "Desarrollo de Aplicaciones Web", "tipo": "Ciclo de grado superior",
     "grupos": [("1.º curso", ["bbdd"]), ("Común a los ciclos de grado superior", ["digitalizacion"])]},
    {"id": "especializacion", "sigla": "Especialización", "icono": "🐳", "color": "#1f8a70",
     "nombre": "Cursos de especialización de FP", "tipo": "Grado superior · tras ASIR, DAM o DAW",
     "grupos": [("Despliegue de productos software en contenedores (RD 144/2026)", ["despliegue", "mantenimiento"]),
                ("Recursos y servicios en la nube (RD 145/2026)", ["bbdd-nube"])]},
    {"id": "master", "sigla": "Máster", "icono": "🎓", "color": "#6b6b6b",
     "nombre": "Máster de Profesorado de Secundaria", "tipo": "Especialidad de Informática · Universidad de Alicante",
     "grupos": [("Bloque II", ["aei"])]},
]

# Relación de conceptos: cada concepto, con dónde se trabaja en cada asignatura (clave, ruta dentro de su web, texto)
CONCEPTOS = [
    ("Bases de datos relacionales y SQL", "Se diseñan y consultan en los ciclos; en la nube se administran y en contenedores se mantienen en producción.", [
        ("gbd", "", "Temas 1-5"), ("bbdd", "", "UD01-UD07"), ("bbdd-nube", "ud04-bases-datos/", "UD04 · Bases de datos administradas"),
        ("despliegue", "ud03-kubernetes/ud03-teoria/#62-statefulset", "UD03 · PostgreSQL como StatefulSet")]),
    ("Copias de seguridad y recuperación", "De la copia de una base de datos a la política 3-2-1 de un servicio en producción.", [
        ("gbd", "tema6-aseguramiento/", "Tema 6 · Aseguramiento"), ("sad", "ud02/", "UD02 · Seguridad pasiva y copias"),
        ("mantenimiento", "ud04-backup-actualizaciones/ud04-teoria/#1-rpo-rto-y-política-de-copias", "UD04 · RPO, RTO, pg_dump y Velero")]),
    ("Almacenamiento de objetos (S3)", "El almacén donde se guardan copias, registros y datos en la nube.", [
        ("bbdd-nube", "ud02-almacenamiento-objetos/", "UD02 · Almacenamiento de objetos"),
        ("mantenimiento", "ud04-backup-actualizaciones/ud04-teoria/#4-el-medio-externo-almacenamiento-de-objetos", "UD04 · Copias en Garage")]),
    ("Volúmenes, bloques y ficheros", "Dónde viven los datos persistentes y qué pasa con ellos al borrar.", [
        ("bbdd-nube", "ud03-bloques-ficheros/", "UD03 · Bloques y ficheros en red"),
        ("despliegue", "ud04-redes-almacenamiento/ud04-teoria/#6-almacenamiento-en-kubernetes", "UD04 · PV, PVC y StorageClass"),
        ("mantenimiento", "ud05-terminacion/ud05-teoria/#2-lo-que-sobrevive-a-kubectl-delete", "UD05 · Lo que sobrevive a un borrado")]),
    ("Criptografía y borrado seguro", "Cifrar para proteger y destruir la clave para borrar.", [
        ("sad", "ud03/", "UD03 · Criptografía"),
        ("mantenimiento", "ud05-terminacion/ud05-teoria/#4-borrado-seguro-y-sus-límites", "UD05 · Borrado seguro y criptográfico")]),
    ("Fortificación y control de acceso", "Mínimo privilegio en el sistema operativo, en el contenedor y en el clúster.", [
        ("sad", "ud04/", "UD04 · Fortificación de hosts"),
        ("despliegue", "ud05-seguridad-monitorizacion/ud05-teoria/#3-endurecimiento-de-contenedores", "UD05 · Endurecimiento y RBAC"),
        ("mantenimiento", "ud03-extraccion-datos/ud03-teoria/#4-accesos-al-sistema", "UD03 · Accesos fallidos y fail2ban")]),
    ("Monitorización, detección y respuesta", "Observar el sistema, detectar lo anormal y actuar.", [
        ("sad", "ud05/", "UD05 · Monitorización y detección"),
        ("despliegue", "ud05-seguridad-monitorizacion/ud05-teoria/#8-observabilidad", "UD05 · Observabilidad"),
        ("mantenimiento", "ud01-monitorizacion-alarmas/ud01-teoria/", "UD01 · Prometheus y Alertmanager"),
        ("mantenimiento", "ud03-extraccion-datos/ud03-teoria/", "UD03 · Registros con Loki")]),
    ("Cortafuegos y segmentación de red", "Del cortafuegos perimetral a las políticas de red entre contenedores.", [
        ("sad", "ud06/", "UD06 · Seguridad perimetral"),
        ("despliegue", "ud05-seguridad-monitorizacion/ud05-teoria/#6-políticas-de-red", "UD05 · NetworkPolicy"),
        ("mantenimiento", "ud01-monitorizacion-alarmas/ud01-teoria/#7-seguridad-de-la-monitorización", "UD01 · Proteger la monitorización")]),
    ("Virtualización y alta disponibilidad", "Máquinas virtuales, contenedores y réplicas para que el servicio no se detenga.", [
        ("sad", "ud07/", "UD07 · Alta disponibilidad y continuidad"),
        ("despliegue", "ud01-virtualizacion-ligera/ud01-teoria/#2-tipos-de-virtualización", "UD01 · Tipos de virtualización"),
        ("despliegue", "ud05-seguridad-monitorizacion/ud05-teoria/#9-alta-disponibilidad-y-tolerancia-a-fallos", "UD05 · Alta disponibilidad"),
        ("mantenimiento", "ud02-validacion-sistema/ud02-teoria/#3-del-acuerdo-de-nivel-de-servicio-a-los-indicadores", "UD02 · SLA, SLO y disponibilidad")]),
    ("Riesgos, marco legal y protección de datos", "Qué obliga la ley y cómo se cumple al operar y al dar de baja un servicio.", [
        ("sad", "ud01/", "UD01 · Riesgos y marco legal"),
        ("mantenimiento", "ud05-terminacion/ud05-teoria/#3-borrar-datos-personales-en-una-base-de-datos", "UD05 · Borrado de datos personales")]),
    ("Nube e infraestructura híbrida", "Servicios gestionados y su combinación con la infraestructura propia.", [
        ("bbdd-nube", "ud06-nube-hibrida/", "UD06 · Nube híbrida"), ("digitalizacion", "", "Tecnologías habilitadoras")]),
]
