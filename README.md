# 🚀 AI Crew for Instagram Post

An **AI-powered Instagram content generation system** built using the **CrewAI framework**.
This project demonstrates how multiple autonomous AI agents collaborate to generate a complete Instagram post—**from idea to caption to hashtags**—based on a single input topic.

---

## 📌 Project Overview

This project uses **CrewAI agents** to automate Instagram post creation by dividing responsibilities across specialized roles:

* 🧠 **Content Strategist** – Generates the post idea
* ✍️ **Caption Writer** – Writes an engaging caption
* 🔍 **Hashtag Specialist** – Creates optimized hashtags

All agents work together using a shared topic input.

---

## 🧩 Features

* Topic-based Instagram post generation
* Multi-agent collaboration
* Clean YAML-based agent & task configuration
* Easy to extend (Reels, Carousel, Image prompts)
* Beginner & interview friendly example of **Agentic AI**

---

## 🏗️ Project Structure

```
instagram_post/
│
├── agents.yaml        # Defines AI agents and their roles
├── tasks.yaml         # Defines tasks with {topic} injection
├── crew.py            # Main execution file
├── requirements.txt   # Python dependencies
└── README.md
```

---

## ⚙️ Prerequisites

* Python **3.9+**
* OpenAI / Azure OpenAI API Key
* Basic understanding of Python

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/husenbasha443/crewai_insta_post_generator.git
cd crewai_insta_post_generator
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
GROQ_API_KEY=your_api_key_here
```

*(Use Azure OpenAI variables if applicable)*

---

## 🧠 Agents Configuration (`agents.yaml`)

Defines individual AI agents and their responsibilities:

* Content Strategist
* Caption Writer
* Hashtag Specialist

Each agent has:

* Role
* Goal
* Backstory
* Delegation control

---

## 🧩 Tasks Configuration (`tasks.yaml`)

Tasks dynamically use the `{topic}` variable:

```yaml
Generate an Instagram post for the topic: {topic}
```

Task flow:

1. Content idea generation
2. Caption writing
3. Hashtag optimization

---

## ▶️ Running the Project

Update `crew.py` with your topic input:

```python
crew.kickoff(
    inputs={
        "topic": "AI Agents in Real-World Applications"
    }
)
```

Run the project:

```bash
python crew.py
```

---

## 🧪 Sample Output

```
📌 Post Idea:
AI agents are transforming how businesses automate decisions...

📝 Caption:
🤖 AI agents are no longer the future—they're here!...

#️⃣ Hashtags:
#AIAgents #ArtificialIntelligence #TechTrends #Automation
```

---

## 🔄 Customization Ideas

* Add **Image Prompt Agent**
* Add **Reels Caption Agent**
* Add **Multi-language Support**
* Integrate **MCP Servers**
* Schedule posts automatically

---

## 🎯 Use Cases

* Social media automation
* AI agent demos
* Learning CrewAI
* Interview & portfolio projects
* Content marketing workflows

---

## 📚 Technologies Used

* Python
* CrewAI
* YAML
* OpenAI / Azure OpenAI
* GROQ

---

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

* CrewAI Framework
* OpenAI
* Agentic AI Community

---

### ⭐ If you find this helpful, give it a star on GitHub!
