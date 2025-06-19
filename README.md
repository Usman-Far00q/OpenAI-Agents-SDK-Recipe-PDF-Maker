# Python Project with `uv`

This is a Python project that uses [`uv`](https://github.com/astral-sh/uv) for dependency management and virtual environment handling.

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have `uv` installed. If not, you can install it via:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

Or refer to the official [uv installation guide](https://github.com/astral-sh/uv#installation) for your platform.

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

### 3. Set Up the Environment

You can use `uv` to set up your Python environment in a modern and efficient way.

```bash
uv sync
```

This will:

* Automatically create and activate a `.venv` if one doesn't exist.
* Install dependencies declared in `pyproject.toml`.
* Use `uv.lock` if present for reproducible installs.

To update the lock file after changing dependencies:

```bash
uv add <new-package>
```

To activate the environment manually later:

* **Linux/macOS**:

  ```bash
  source .venv/bin/activate
  ```
* **Windows (PowerShell)**:

  ```powershell
  .venv\Scripts\Activate.ps1
  ```

### 4. Configure Environment Variables

This project uses a `.env` file to manage configuration values.

1. Copy the example file:

   ```bash
   cp .env.example .env
   ```

2. Open `.env` in a text editor and update the values as needed:

   ```env
   GROQ_API_KEY="you groq api key"
   ```

3. To run the code use the commad below:

   ```bash
   uv run meal_maker_groq_and_agents_sdk.py
   uv run guardrailed_meal_maker_groq_agents_sdk.py
   ```

> Make sure not to commit sensitive `.env` values to version control.

---

## 📄 License

This project is licensed under the MIT License.
