#!/usr/bin/env python3
"""Genera las páginas HTML del portal de FP a partir de tools/datos.py.

Uso (desde la raíz del repositorio):  python3 tools/generar.py
Las páginas generadas (index.html, <ciclo>.html, conceptos.html) se suben al repositorio tal cual:
GitHub Pages las publica sin ningún paso de construcción.
"""
from html import escape as e
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from datos import ASIGNATURAS, CICLOS, CONCEPTOS  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent


def pagina(titulo, activo, cuerpo, descripcion):
    enlaces = [("index.html", "Inicio", "inicio")] + [(f"{c['id']}.html", c["sigla"], c["id"]) for c in CICLOS] \
        + [("conceptos.html", "Relación entre asignaturas", "conceptos")]
    menu = "\n".join(
        f'    <a href="{h}"{" aria-current=\"page\"" if k == activo else ""}>{e(t)}</a>' for h, t, k in enlaces)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(titulo)} · LorenaLResusta FP</title>
<meta name="description" content="{e(descripcion)}">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<nav class="menu" aria-label="Principal">
  <a class="marca" href="index.html">LorenaLResusta <b>FP</b></a>
  <div class="enlaces">
{menu}
  </div>
</nav>
{cuerpo}
<footer>
  <p>© Lorena López Resusta · Materiales de Formación Profesional de Informática · Curso 2026/27</p>
  <p><a href="https://github.com/LorenaLResusta">github.com/LorenaLResusta</a></p>
</footer>
</body>
</html>
"""


def tarjeta_asignatura(clave):
    a = ASIGNATURAS[clave]
    datos = " · ".join(x for x in (f"Módulo {a['codigo']}" if a["codigo"][0].isdigit() else a["codigo"], a["curso"], a["horas"]) if x)
    temas = "".join(f"<li>{e(t)}</li>" for t in a["temas"])
    return f"""      <article class="asignatura">
        <p class="datos">{e(datos)}</p>
        <h3><a href="{a['web']}">{e(a['nombre'])}</a></h3>
        <p>{e(a['resumen'])}</p>
        <ul class="etiquetas">{temas}</ul>
        <p class="acciones"><a class="boton" href="{a['web']}">Abrir los apuntes</a> <a href="{a['repo']}">Repositorio</a></p>
      </article>"""


def inicio():
    tarjetas = []
    for c in CICLOS:
        n = len({k for _, ks in c["grupos"] for k in ks})
        tarjetas.append(f"""    <a class="ciclo" href="{c['id']}.html" style="--c:{c['color']}">
      <span class="icono" aria-hidden="true">{c['icono']}</span>
      <h2>{e(c['sigla'])}</h2>
      <p class="nombre">{e(c['nombre'])}</p>
      <p class="tipo">{e(c['tipo'])} · {n} asignatura{'s' if n != 1 else ''}</p>
    </a>""")
    cuerpo = f"""<header class="portada">
  <h1>Formación Profesional de Informática</h1>
  <p>Apuntes, prácticas y recursos organizados por <b>ciclo</b> y por <b>asignatura</b>.</p>
</header>
<main>
  <section class="rejilla" aria-label="Ciclos">
{chr(10).join(tarjetas)}
  </section>
  <section class="aviso">
    <h2>Conceptos que conectan las asignaturas</h2>
    <p>Las copias de seguridad, la monitorización o el almacenamiento aparecen en varias asignaturas desde ángulos distintos.
    La página <a href="conceptos.html">Relación entre asignaturas</a> enlaza cada concepto con el apartado donde se trabaja en cada una.</p>
  </section>
</main>"""
    return pagina("Inicio", "inicio", cuerpo, "Portal de apuntes de Formación Profesional de Informática por ciclos y asignaturas.")


def ciclo(c):
    grupos = []
    for titulo, claves in c["grupos"]:
        grupos.append(f"""  <section>
    <h2>{e(titulo)}</h2>
    <div class="asignaturas">
{chr(10).join(tarjeta_asignatura(k) for k in claves)}
    </div>
  </section>""")
    relacionados = [con for con in CONCEPTOS if any(k in {x for _, ks in c["grupos"] for x in ks} for k, _, _ in con[2])]
    lista = "".join(f'<li><a href="conceptos.html#{slug(t)}">{e(t)}</a></li>' for t, _, _ in relacionados)
    cuerpo = f"""<header class="portada" style="--c:{c['color']}">
  <p class="migas"><a href="index.html">Inicio</a> › {e(c['sigla'])}</p>
  <h1><span aria-hidden="true">{c['icono']}</span> {e(c['sigla'])}</h1>
  <p>{e(c['nombre'])} · {e(c['tipo'])}</p>
</header>
<main>
{chr(10).join(grupos)}
  <section class="aviso">
    <h2>Conceptos compartidos con otras asignaturas</h2>
    <ul class="columnas">{lista}</ul>
  </section>
</main>"""
    return pagina(c["sigla"], c["id"], cuerpo, f"Asignaturas de {c['nombre']}.")


def slug(t):
    import unicodedata
    t = unicodedata.normalize("NFKD", t.lower()).encode("ascii", "ignore").decode()
    return "-".join("".join(ch if ch.isalnum() else " " for ch in t).split())


def conceptos():
    filas = []
    for titulo, desc, enlaces in CONCEPTOS:
        items = []
        for clave, ruta, texto in enlaces:
            a = ASIGNATURAS[clave]
            items.append(f'<li><a href="{a["web"]}{ruta}"><b>{e(a["nombre"])}</b><span>{e(texto)}</span></a></li>')
        filas.append(f"""  <section class="concepto" id="{slug(titulo)}">
    <h2>{e(titulo)}</h2>
    <p>{e(desc)}</p>
    <ol class="recorrido">{''.join(items)}</ol>
  </section>""")
    cuerpo = f"""<header class="portada">
  <p class="migas"><a href="index.html">Inicio</a> › Relación entre asignaturas</p>
  <h1>Relación entre asignaturas</h1>
  <p>Cada concepto, en el orden en que se suele aprender: de los ciclos a los cursos de especialización.</p>
</header>
<main>
{chr(10).join(filas)}
</main>"""
    return pagina("Relación entre asignaturas", "conceptos", cuerpo, "Conceptos que se trabajan en varias asignaturas, con enlaces a cada una.")


def main():
    (RAIZ / "index.html").write_text(inicio(), encoding="utf-8")
    for c in CICLOS:
        (RAIZ / f"{c['id']}.html").write_text(ciclo(c), encoding="utf-8")
    (RAIZ / "conceptos.html").write_text(conceptos(), encoding="utf-8")
    print("Generadas:", ", ".join(["index.html"] + [f"{c['id']}.html" for c in CICLOS] + ["conceptos.html"]))


if __name__ == "__main__":
    main()
