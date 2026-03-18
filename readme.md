# 🚀 AI Investment Memo Automator

A corporate-grade pipeline designed to automate the extraction, structuring, and injection of financial and operational data into Investment Memos (IC Memos). 

This system eliminates the bottleneck of manual Data Room processing, transforming hours of raw document analysis into standardized Word reports in a matter of seconds.

---

## 🎯 The Problem vs. The Solution

**Current Situation:**
Investment analysts spend between 8 and 12 hours per deal gathering fragmented data from PDFs, Excels, and JSONs, to later transcribe and format them manually into a Word document. This generates inconsistencies, operational latency, and a high cost in man-hours.

**The Solution (This Pipeline):**
An automated engine that ingests entire Data Room folders, standardizes the information to efficient formats (YAML/XML), uses the Anthropic API with an ultra-strict data schema (Tool Use / Function Calling), and automatically renders the final `.docx` document.

* **Execution time:** < 25 seconds per Deal.
  
* **Estimated cost per memo with the most advanced model maximizing quality:** 0.90 - 0.20 USD (It depends on the information intake)

---

## 🏗️ System Architecture (Hybrid Factory-Service)

The project is designed under a modular architecture, combining the **Factory Pattern** (for dynamic creation of file handlers and templates) and the **Service Pattern** (for business logic and external communication).

1. **`DataExtractorFactory` (Ingestion and Parsing)**
   * Uses a "Strategy" approach to dynamically route each file based on its extension (`.pdf`, `.json`, `.xlsx`, `.xlsm`).
   * **Data Cleansing:** Excels and JSONs are automatically transformed to `YAML`. This drastically reduces token usage and eliminates format "noise" before hitting the LLM.
   * **Context Isolation:** Packages each extracted document in XML tags (`<document name="...">`) to prevent "hallucinations" and cross-contamination of data in the AI.

2. **`IaService` (Strict Structuring)**
   * Does not use the AI as a "chatbot" to write free text.
   * Injects raw data and forces the model (via `tool_choice: "any"`) to respond by returning a JSON payload perfectly mapped against predefined schemas (`tools_structures_util.py`).
   * Calculates the USD cost in real-time based on the input and output tokens consumed in the transaction.

3. **`MemorandumFactory` (Assembly and Rendering)**
   * Dynamically scans the templates directory.
   * Receives the validated JSON payload from the `IaService` and uses `docxtpl` to inject the data into the corresponding Word template, preserving native Microsoft Word formatting and styles.

---

## ✨ Key Features

* 📄 **Multi-Format Support:** Reads and processes text from `.pdf`, complex tables from `.xlsx`/`.xls`, and structures from `.json`.
* 🛡️ **Fault Tolerance:** Built-in exception handling. If a file is corrupted, the Factory notifies it and continues with the rest of the stack without stopping execution.
* 🤖 **Anti-Hallucinations:** JSON schemas force the AI to return `null` if the information is not present in the source documents.
* 📊 **Terminal Cost Tracking:** Interactive UI (based on `rich` and `questionary`) that provides progress bars and details the exact USD spend for each generated report.

---

## 🚀 Requirements and Deployment

**Prerequisites:**
* Python 3.10 installed on your system with its environment variable set.
* Anthropic (Claude) API Key. With credits.
    
---

## ⚙️ Quick Start Guide

To initialize the system and the local execution environment, follow the steps below:

### 1. Clone the Repository

Open your terminal and download the source code:

```bash
git clone [https://github.com/ForecastSnow/DealForgeAI](https://github.com/ForecastSnow/DealForgeAI)
cd DealForgeAI
```

### 2. Environment Variables Configuration

The system requires authentication credentials to operate with the LLM.

1. Locate the `.env-example` file in the root directory.
2. Strictly rename it to `.env`.
3. Edit it and enter your Anthropic API Key.


### 3. Initialization and Execution

Next, instantiate the isolated virtual environment and run the orchestrator. Copy and paste the command block corresponding to your operating system into your terminal.

**For Windows environments:**

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src\main.py
```

**For Mac / Linux environments:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 src/main.py
```

> **Note:** Upon completion of the commands, the system's CLI interface will automatically initialize in your terminal, prompting for the selection of the Deal to process.