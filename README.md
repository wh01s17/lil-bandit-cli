# lil-bandit-cli

`lil-bandit-cli` es una herramienta de línea de comandos escrita en Python que utiliza **Typer** para crear comandos simples, rápidos y extensibles.  
Este proyecto sirve como base para futuras utilidades CLI relacionadas con automatización, análisis y flujos personalizados.

---

## 🚀 Características

-   Arquitectura basada en `src/` (estándar moderno recomendado por PyPA).
-   CLI construida con **Typer**, con soporte para subcomandos.
-   Separación clara entre:
    -   **Interfaz CLI** (`cli.py`)
    -   **Lógica interna** (`core/`)
-   Instalación editable para desarrollo.
-   Estructura preparada para testing.

---

## 📦 Instalación (modo desarrollo)

Clona el repositorio y entra en el directorio:

```bash
git clone https://github.com/tu_usuario/lil-bandit-cli.git
cd lil-bandit-cli
```

Crea un entorno virtual (opcional, recomendado):

```bash
python -m venv venv
source venv/bin/activate
```

Instala en modo editable:

```bash
pip install -e .
```

Esto permitirá que cualquier cambio en el código se refleje inmediatamente al ejecutar el comando.

## 🧩 Uso básico

Ejecuta el comando principal:

```bash
lil-bandit-cli --help
```

Ejemplo de uso del comando hola:

```bash
lil-bandit-cli hola wh01s17
```

Salida esperada:

```bash
Hola wh01s17
```

📁 Estructura del proyecto

```bash
lil-bandit-cli/
├── pyproject.toml
├── README.md
├── src/
│ └── lil_bandit_cli/
│ ├── cli.py
│ ├── core/
│ │ ├── __init__.py
│ │ ├── scanner.py
│ │ └── utils.py
│ └── __init__.py
└── tests/
├── __init__.py
└── test_basic.py
```

Explicación rápida

-   cli.py → Punto de entrada de comandos (Typer).

-   core/ → Lógica interna (módulos independientes).

-   tests/ → Tests automatizados.

-   pyproject.toml → Configuración del proyecto y dependencias.

## 🛠️ Desarrollo

Para ejecutar el CLI localmente sin instalar:

```bash
python -m lil_bandit_cli.cli hola wh01s17
```

Para agregar nuevos comandos, edita cli.py:

```python
@app.command()
def nuevo_comando(...):
    ...
```

Si agregas archivos o módulos nuevos dentro de core/, puedes importarlos en cli.py:

```python
from .core.scanner import alguna_funcion
```

🧪 Tests

Ejecuta todos los tests:

```bash
pytest
```

🤝 Contribuciones

Las contribuciones son bienvenidas.
Sigue estas reglas:

1. Crea una rama con una descripción clara.

2. Haz cambios pequeños y legibles.

3. Asegúrate de que los tests pasen.

📄 Licencia

MIT License.
Puedes usar, modificar y distribuir libremente el código.
