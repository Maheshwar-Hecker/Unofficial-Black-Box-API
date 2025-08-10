# 🖤 BlackBox API Integration
*Python wrapper for chat, image & code generation via BlackBox AI.*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen"/>
</p>

---

## ✨ Overview
`BlackBox` lets you:
- 💬 **Chat** — Ask questions & get structured replies (citations, code, etc.).
- 🖼️ **Generate Images** — Up to two AI-rendered visuals per request.
- 🧑‍💻 **Generate Code** — Multi-language snippets on demand.
- 📚 **Auto-References** — Extracts & formats citations from answers.

---

## 🔧 Installation
```

pip install requests

```

---

## 🚀 Quick Start
### 1. Import & Instantiate
```

from blackAPI import BlackBox
bb = BlackBox()

```

### 2. Chat
```

resp = bb.get_Response("What is the use of pg_scanf with an example?")
print(resp)

```

### 3. Image Generation
```

images = bb.getImage_Response("CSK winning the IPL in 2025", 2)
print(images)

```

### 4. Code Generation
```

code = bb.getCode_Response(
"Write Python code to generate random prime numbers from 1 to 100"
)
print(code)

```

<details>
<summary>📄 Full Example</summary>

```

if __name__ == "__main__":
bb = BlackBox()

    # Chat
    print(bb.get_Response(
        "What is the use of pg_scanf with an example?"
    ))
    
    # Images
    print(bb.getImage_Response(
        "CSK winning the IPL in 2025", 2
    ))
    
    # Code
    print(bb.getCode_Response(
        "Write Python code to generate random prime numbers from 1 to 100"
    ))
    ```
</details>

---

## 📚 Public API

| Method | Purpose |
|--------|---------|
| `get_Raw_Response(query, max_tokens=500, forced_web_search=False, image_generation=False, web_search_mode=False)` | Lowest-level helper; returns the unprocessed BlackBox JSON. |
| `get_Response(query, max_tokens=500, forced_web_search=False, web_search_mode=False)` | Chat answers with optional references (string). |
| `getImage_Response(query, numberOfImages)` | Returns up to **2** direct image URLs. |
| `getCode_Response(query)` | Dict with detected language & generated source. |

### Parameter Details

#### `get_Raw_Response`
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `query` | str | — | Question / prompt. |
| `max_tokens` | int | 500 | Length cap for reply. |
| `forced_web_search` | bool | False | Force web search even if model declines. |
| `image_generation` | bool | False | Toggle image mode. |
| `web_search_mode` | bool | False | Lightweight search without citations. |

_All other wrapper methods share the same first three parameters unless noted._

---

## 📝 Notes
- **Chat ID** — Grab yours by opening a new BlackBox chat (e.g. `https://www.blackbox.ai/chat/fXUwoqS`) and copy the slug.  
  - Example: **chatID = `"fXUwoqS"`**  
- Response quality depends heavily on prompt clarity. Tweak wording if results look off.

---

## 🤝 Contributing
Issues and PRs are welcome—help make BlackBox even better!

---

## 📄 License
MIT — see `LICENSE`.

---

## 📬 Contact
Open an issue or reach the repo owner directly. Happy coding! 🖤
```

