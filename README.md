# 🛡️ Apertus Sentinel — Automated Security & OWASP Code Auditor

A lightweight CLI tool leveraging Switzerland's sovereign LLM (`Apertus-v1.5-8B`) via CSCS Inference API to perform automated security audits, detect OWASP vulnerabilities, and generate secure code patches.

## 📌 Features
- **Multi-File Batch Auditing:** Automatically scans whole directories for Python security flaws.
- **OWASP Detection:** Identifies Command Injection, Hardcoded Credentials, SQL Injection, and more.
- **Automated Patch Generation:** Outputs secure refactored code snippets.
- **Markdown Reporting:** Generates structured `.md` security reports.

## 🛠️ How to Run

1. Clone repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/apertus-sentinel.git](https://github.com/YOUR_USERNAME/apertus-sentinel.git)
   cd apertus-sentinel