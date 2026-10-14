import os
import glob
import re
from openai import OpenAI

# 1. Initialize CSCS Client
client = OpenAI(
    base_url="https://api.inference.cscs.ch/v1",
    api_key="YOUR_ACTUAL_API_KEY_HERE"  # Use your CSCS key when running locally
)

target_folder = "test_cases"
test_files = glob.glob(os.path.join(target_folder, "*.py"))

if not test_files:
    print(f"No .py files found in '{target_folder}/'.")
    exit(1)

system_prompt = (
    "You are an expert Cybersecurity Auditor specializing in code reviews and OWASP Top 10.\n"
    "Analyze the provided Python code snippet and output a clean security audit in Markdown.\n\n"
    "STRICT OUTPUT RULES:\n"
    "1. Do NOT wrap your entire response in ```markdown ``` code fences.\n"
    "2. Include line: '**Severity:** <HIGH/MEDIUM/LOW>'\n"
    "3. Structure your response using these exact headers:\n\n"
    "### ⚠️ Identified Vulnerability\n"
    "**Name:** <Vulnerability Name>\n"
    "**Severity:** <HIGH/MEDIUM/LOW>\n\n"
    "### 🔍 Impact Analysis\n"
    "<Brief explanation of the risk.>\n\n"
    "### 🛠️ Remediation & Patch\n"
    "```python\n"
    "# Corrected secure code patch\n"
    "```\n"
)

audited_results = []
total_high = 0
total_medium = 0
total_low = 0

print(f"🔍 Scanning {len(test_files)} file(s) in '{target_folder}/'...\n")

# 2. Batch Audit Loop
for idx, file_path in enumerate(test_files, 1):
    file_name = os.path.basename(file_path)
    print(f"[{idx}/{len(test_files)}] Auditing: {file_name}...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        code_content = f.read()

    response = client.chat.completions.create(
        model="swiss-ai/Apertus-v1.5-8B",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Audit file `{file_name}`:\n\n```python\n{code_content}\n```"}
        ]
    )
    
    analysis = response.choices[0].message.content
    
    # Track severity counts for scoring
    if "**Severity:** HIGH" in analysis or "HIGH" in analysis:
        total_high += 1
    elif "**Severity:** MEDIUM" in analysis or "MEDIUM" in analysis:
        total_medium += 1
    else:
        total_low += 1

    # Extract patch code block for auto-fixing
    patch_match = re.search(r"```python\n(.*?)```", analysis, re.DOTALL)
    patch_code = patch_match.group(1).strip() if patch_match else None

    audited_results.append({
        "file_name": file_name,
        "file_path": file_path,
        "analysis": analysis,
        "patch_code": patch_code
    })

# 3. Feature 2: Calculate Security Score & Generate Badges
total_vulnerabilities = total_high + total_medium + total_low
base_score = 100 - (total_high * 25 + total_medium * 15 + total_low * 5)
security_score = max(0, base_score)

badge_color = "red" if security_score < 50 else ("yellow" if security_score < 80 else "green")
score_badge = f"![Security Score](https://img.shields.io/badge/Apertus_Security_Score-{security_score}%25-{badge_color})"
owasp_badge = f"![Audited Files](https://img.shields.io/badge/Files_Audited-{len(test_files)}-blue)"

# Build Final Report Header
full_report = f"# 🛡️ Apertus Sentinel — Security Audit Report\n\n"
full_report += f"{score_badge} {owasp_badge}\n\n"
full_report += f"**Target Directory:** `{target_folder}/` | **Model:** `swiss-ai/Apertus-v1.5-8B` | **High Risks Found:** {total_high}\n\n"
full_report += "---\n\n"

for item in audited_results:
    full_report += f"## File: `{item['file_name']}`\n\n"
    full_report += item["analysis"] + "\n\n---\n\n"

# Save Report
output_filename = "FINAL_SECURITY_AUDIT_REPORT.md"
with open(output_filename, "w", encoding="utf-8") as out_file:
    out_file.write(full_report)

print("\n==================================================")
print(f"✅ Audit Complete! Security Score: {security_score}%")
print(f"📄 Report saved to '{output_filename}'")
print("==================================================\n")

# 4. Feature 1: Interactive Auto-Fixer
apply_fix = input("⚡ Would you like Apertus Sentinel to automatically generate patched files? (y/n): ").strip().lower()

if apply_fix == 'y':
    patched_dir = "patched_files"
    os.makedirs(patched_dir, exist_ok=True)
    
    for item in audited_results:
        if item["patch_code"]:
            patched_filename = os.path.join(patched_dir, f"patched_{item['file_name']}")
            with open(patched_filename, "w", encoding="utf-8") as pf:
                pf.write(item["patch_code"])
            print(f"  └─ Patched file created: '{patched_filename}'")
        else:
            print(f"  └─ No patch block found for '{item['file_name']}'")
            
    print(f"\n🎉 All patched scripts have been saved to the '{patched_dir}/' folder!")
else:
    print("Auto-patching skipped.")