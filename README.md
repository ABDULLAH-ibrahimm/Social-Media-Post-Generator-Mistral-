# Project 2 – Social Media Post Generator

## Overview
The **Social Media Post Generator** is an AI-powered tool that creates engaging, platform-specific posts based on a given topic, tone, and target platform.  
It leverages the **Mistral** language model via Ollama, with a FastAPI backend for processing and a Streamlit frontend for a simple, interactive interface.

This project is ideal for marketers, content creators, and businesses looking to streamline their social media content creation.

---

## ✨ Features
- Generate **three complete, unique posts** from a single prompt.
- Output includes:
  - **Title**
  - **Opening Line**
  - **Main Content**
  - **Call-to-Action**
- Choose topic, tone, and platform for tailored results.
- FastAPI backend for handling AI requests.
- Streamlit frontend for an easy user experience.
- Powered by **Ollama** and the **Mistral** LLM.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/social-media-post-generator.git](https://github.com/ABDULLAH-ibrahimm/Social-Media-Post-Generator-Mistral-.git
cd social-media-post-generator
```

### 2. Create & Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Pull the AI Model
Make sure Ollama is installed, then run:
```bash
ollama pull mistral
```

### 5. Start the Backend
```bash
uvicorn backend.main:app --reload
```

### 6. Start the Frontend
In a separate terminal:
```bash
streamlit run frontend/app.py
```

---

## 📌 Example Usage

**Input:**

- **Topic:** Artificial Intelligence in Healthcare  
- **Tone:** Professional  
- **Platform:** LinkedIn  

**Output:**

---

**Post 1**  
**Title:** Revolutionizing Healthcare: The Power of AI  
**Opening Line:** "Discover how Artificial Intelligence (AI) is transforming the future of healthcare delivery!"  
**Main Content:** In today's digital age, AI has emerged as a significant game-changer in various industries. One such area is healthcare, where AI applications are streamlining operations, improving patient care, and driving breakthroughs. From predictive analytics to virtual nursing assistants, AI is enhancing efficiency and accuracy across the board. Join us as we delve deeper into this transformative technology's impact on our health sector.  
**Call-to-Action:** Click the link below to explore how AI is revolutionizing healthcare.  
`#AIInHealthcare #DigitalHealth`

---

**Post 2**  
**Title:** AI and Personalized Medicine: A Match Made in Heaven  
**Opening Line:** "Unlock the potential of personalized medicine through the power of Artificial Intelligence!"  
**Main Content:** The era of one-size-fits-all treatment approaches is gradually fading away, thanks to the integration of AI in healthcare. By analyzing vast amounts of data, AI can tailor treatments to individual patients' unique genetic makeup, lifestyle factors, and disease histories. This targeted approach not only leads to better patient outcomes but also contributes significantly to cost savings. Stay ahead of the curve by understanding how AI is shaping the future of personalized medicine.  
**Call-to-Action:** Dive into the world of AI-driven personalized medicine. Learn more now!  
`#PersonalizedMedicine #AIHealthcare`

---

**Post 3**  
**Title:** The Future of Diagnostics: AI Meets Medical Imaging  
**Opening Line:** "Imagine a future where diagnostics are faster, more accurate, and less invasive—all thanks to Artificial Intelligence!"  
**Main Content:** AI is reshaping the landscape of medical imaging, enabling early and precise detection of diseases like cancer, heart disease, and neurological disorders. Through machine learning algorithms, AI can process vast amounts of data in a fraction of the time required by human experts. This allows for timely interventions, reduced costs, and improved patient outcomes. Stay tuned as we delve deeper into this exciting frontier of AI in healthcare!  
**Call-to-Action:** Get ready to witness the future of diagnostics. Join us on our journey exploring AI in medical imaging.  
`#AIImaging #FutureHealthcare`
