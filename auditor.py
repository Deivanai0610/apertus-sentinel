import os
import glob
from openai import OpenAI

# 1. Initialize client
client = OpenAI(
    base_url="https://api.inference.cscs.ch/v1",
    api_key="YOUR_CSCS_API_KEY"  # Keep your working API key here
)

# 2. Get all Python files in the test_cases directory
target_folder = "test_cases"
test_files = glob.glob(os.path.join(target_folder, "*.py"))

if not test_files:
    print(f"No .py files found in '{target_folder}/'. Please check the folder name.")
    exit(1)

system_prompt = (
    "You are an expert Cybersecurity Auditor. "
    "Analyze the provided Python code snippet for security risks (OWASP Top 10).\n\n"
    "Respond ONLY with the analysis itself. DO NOT wrap your entire response in ```markdown ``` code fences.\n\n"
    "Format:\n"
    "| Vulnerability Name | Severity | Impact Analysis | Remediation |\n"
    "|---|---|---|---|\n"
    "| [Name] | [HIGH/MEDIUM/LOW] | [Brief Analysis] | [Fix Strategy] |\n\n"
    "Provide the corrected secure Python code block below the table."
)

full_markdown_report = "# 🛡️ Apertus Sentinel — Automated Security Audit Report\n\n"
full_markdown_report += f"**Model:** `swiss-ai/Apertus-v1.5-8B` | **Files Audited:** {len(test_files)}\n\n---\n\n"

print(f"🔍 Found {len(test_files)} file(s) in '{target_folder}/'. Starting batch security audit...\n")

# 3. Loop through each file and run audit
for index, file_path in enumerate(test_files, 1):
    file_name = os.path.basename(file_path)
    print(f"[{index}/{len(test_files)}] Auditing '{file_name}'...")
    
    with open(file_path, "r") as f:
        code_content = f.read()

    response = client.chat.completions.create(
        model="swiss-ai/Apertus-v1.5-8B",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Audit file `{file_name}`:\n\n```python\n{code_content}\n```"}
        ]
    )
    
    analysis = response.choices[0].message.content
    
    full_markdown_report += f"## File: `{file_name}`\n\n"
    full_markdown_report += analysis + "\n\n---\n\n"

# 4. Save combined Markdown report
output_filename = "FINAL_SECURITY_AUDIT_REPORT.md"
with open(output_filename, "w", encoding="utf-8") as out_file:
    out_file.write(full_markdown_report)

print("\n==================================================")
print(f"✅ Audit Complete! Full report generated: '{output_filename}'")
print("==================================================")