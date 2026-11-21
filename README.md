# FP · Portal de apuntes

Portal de los apuntes de Formación Profesional de Informática de Lorena López Resusta, organizado por **ciclo** y por **asignatura**, con una página que relaciona los conceptos que aparecen en varias asignaturas.

Publicado en GitHub Pages: <https://lorenalresusta.github.io/FP/> (*Settings → Pages → Deploy from a branch → `main` / raíz*).

## Estructura

```text
index.html            portada: ciclos
asir.html dam.html daw.html especializacion.html master.html    asignaturas de cada ciclo
conceptos.html        relación de conceptos entre asignaturas, con enlaces a cada apartado
css/style.css         estilos (claro y oscuro)
tools/datos.py        ciclos, asignaturas y conceptos  ← lo único que se edita
tools/generar.py      genera los HTML a partir de datos.py
```

## Añadir o cambiar una asignatura

1. Edita `tools/datos.py`: añade la asignatura a `ASIGNATURAS`, su clave al ciclo en `CICLOS` y, si comparte conceptos, a `CONCEPTOS`.
2. Ejecuta `python3 tools/generar.py`.
3. Sube los cambios: GitHub Pages publica los HTML tal cual, sin paso de construcción.
