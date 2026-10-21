"""
Framework figure generator v2: improved prompts, larger canvas, forced iterations.
"""
import os, json, base64, subprocess, sys, tempfile, re, shutil
from pathlib import Path
from datetime import datetime
import httpx

API_KEY = [REDACTED]"OPENROUTER_API_KEY", "")
API_BASE = os.environ.get("OPENROUTER_API_BASE", "http://47.94.22.126/v1")
MODEL = os.environ.get("VLM_MODEL", "gpt-4o")
MAX_ITER = int(os.environ.get("MAX_ITER", "5"))

OUTPUT_DIR = Path("/root/gen-depth-fingerprint/outputs") / f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

INTENT = """Create a three-panel academic framework figure with these STRICT layout rules:

FIGURE SIZE: figsize=(16, 6), dpi=300. This is a WIDE figure.
Use fig.subplots(1, 3, gridspec_kw={'width_ratios': [0.35, 0.35, 0.30]}) to create 3 panels.
Turn off all axes (ax.axis('off')).

CRITICAL RULES:
- Font sizes: panel titles 13pt bold, box labels 9pt, small labels 7.5pt
- ALL text must be non-overlapping. Add generous vertical spacing between elements.
- Use FancyBboxPatch with round,pad=0.02 for rounded boxes
- Use FancyArrowPatch for arrows, linewidth=1.0, arrowstyle='->'
- Each panel should have clear top-to-bottom flow
- Leave margins: each panel content should stay within 80% of panel width

Panel (a) — 'Recursive Generation Chain':
Title: '(a) Recursive Generation Chain' at top center, fontsize=13, fontweight='bold'
Layout (top to bottom, centered, with generous spacing y=0.85 to y=0.05):
  y=0.85: Rounded box 'Human Text (gen-0)' — light blue fill #B3D9FF, 8pt font
           Left margin: text 'd=0' in gray, fontsize=8
  y=0.68: Rounded box 'Generator G' — medium gray fill #E8E8E8
           Subtitle below: '8 LLMs | 5 families | 0.6B–8B' in 7pt italic
  y=0.52: Rounded box 'gen-1' — medium blue #4DA6FF
           Left margin: text 'd=1'
  y=0.40: Curved loop arrow from gen-1 box back up to Generator G and down
  y=0.32: Rounded box 'gen-2' — dark blue #0066CC, white text
           Left margin: text 'd=2+'
  y=0.18: Dashed text 'gen-3, gen-4...' in light gray
  y=0.05: Math formula: '$x^{(k)} = G(x^{(k-1)})$' fontsize=9

Panel (b) — 'Feature Extraction':
Title: '(b) Feature Extraction' at top center
Layout (top to bottom):
  y=0.85: Document icon (small rect) labeled 'Input Text'
  y=0.72: Arrow down
  y=0.65: Rounded box 'Pythia-410M' with subtitle '(Reference Model)', teal border
  y=0.55: Arrow down
  y=0.48: Small text 'NLL Distribution'
  y=0.35: Two side-by-side groups:
    Left group 'NLL Statistics' — green box (#2E8B57):
      5 items stacked vertically (each 7pt):
      entropy_mean, entropy_std, entropy_max, entropy_min, tail_decay
    Right group 'Surface' — teal box (#20B2AA):
      2 items: TTR, hapax_ratio
  y=0.12: Arrow from both groups merging down
  y=0.05: Single bar/box labeled '7 DDR Features' in dark green

Panel (c) — 'LOGO Evaluation':
Title: '(c) LOGO Evaluation' at top center
Layout (top to bottom):
  y=0.85-0.65: 2×4 grid of 8 small rounded boxes (each ~7pt text):
    Row 1: Pythia-2.8B | Pythia-1B | OLMo-2-1B | Qwen3-1.7B
    Row 2: Qwen3-0.6B | Qwen3-8B | Llama-3.2-3B | Mistral-7B
    7 boxes in soft blue (#4DA6FF), 1 box (Mistral-7B) in orange (#E8712B)
    Label below grid: '← train (7)     test (1) →'
  y=0.45: Arrow down from grid
  y=0.35: Rounded box 'XGBoost Classifier' — light yellow (#FFF3CD) fill
  y=0.22: Arrow down
  y=0.12: Three small boxes side by side: 'gen-0' (#B3D9FF) | 'gen-1' (#4DA6FF) | 'gen-2+' (#0066CC white text)
  y=0.03: Small italic text 'Leave-One-Generator-Out'

STYLING:
- White background
- No matplotlib spines, ticks, or grid
- Thin box borders (linewidth=0.8, edgecolor='#888888')
- Arrow color '#555555', linewidth=1.0
- Use fig.tight_layout(pad=1.0) at the end
"""

CODEGEN_SYSTEM = """You are an expert matplotlib programmer for academic figures.
Generate COMPLETE, SELF-CONTAINED Python code. The code MUST:
1. Use matplotlib.pyplot and matplotlib.patches (FancyBboxPatch, FancyArrowPatch)
2. Create fig with figsize=(16, 6) and dpi=300
3. Use 3 subplots with width_ratios=[0.35, 0.35, 0.30]
4. Turn off all axes with ax.axis('off') and set ax.set_xlim(0,1), ax.set_ylim(0,1)
5. Use ax.add_patch() for boxes and ax.annotate() or ax.add_patch(FancyArrowPatch) for arrows
6. Save to OUTPUT_PATH (variable injected before your code)
7. DO NOT use plt.show()
8. ALL text must be clearly readable, never overlapping
9. Use transform=ax.transAxes for positioning within each subplot

Output ONLY Python code in a ```python``` block. No explanations."""

CRITIC_SYSTEM = """You are an academic figure critic. Score 1-10 on:
1. layout: Panel organization, spacing, alignment
2. consistency: Color scheme, font sizes, arrow styles
3. completeness: All described elements present
4. aesthetics: Publication quality (EMNLP/ACL standard)
5. readability: All text legible, no overlapping, clear hierarchy

JSON response format:
{"scores": {"layout": N, "consistency": N, "completeness": N, "aesthetics": N, "readability": N},
 "overall": N, "needs_revision": true/false,
 "issues": ["..."], "suggestions": ["..."]}
Set needs_revision=false ONLY if ALL individual scores >= 8 AND overall >= 8.5."""


def call_llm(messages, temperature=0.7, max_tokens=4096, response_format=None):
    payload = {"model": MODEL, "messages": messages, "temperature": temperature, "max_tokens": max_tokens}
    if response_format:
        payload["response_format"] = response_format
    with httpx.Client(base_url=API_BASE, timeout=180.0) as client:
        r = client.post("/chat/completions", json=payload,
                        headers={"Authorization": [REDACTED]"Bearer {API_KEY}", "Content-Type": "application/json"})
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]


def call_vlm_with_image(image_path, prompt, system_prompt=None):
    with open(image_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
        {"type": "text", "text": prompt},
    ]})
    return call_llm(messages, temperature=0.3, max_tokens=2048,
                     response_format={"type": "json_object"})


def extract_code(response):
    if "```python" in response:
        start = response.index("```python") + len("```python")
        end = response.index("```", start)
        return response[start:end].strip()
    elif "```" in response:
        start = response.index("```") + 3
        end = response.index("```", start)
        return response[start:end].strip()
    return response.strip()


def execute_code(code, output_path):
    code = re.sub(r'^OUTPUT_PATH\s*=\s*["\'].*["\']\s*$', "", code, flags=re.MULTILINE)
    full_code = f'OUTPUT_PATH = "{output_path}"\n{code}'
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(full_code)
        temp_path = f.name
    try:
        result = subprocess.run([sys.executable, temp_path], capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            print(f"  ERROR:\n{result.stderr[:800]}")
            return False, result.stderr[:800]
        return Path(output_path).exists(), ""
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    finally:
        Path(temp_path).unlink(missing_ok=True)


def main():
    print(f"=== Framework Figure Generator v2 ===")
    print(f"Model: {MODEL}, Max iter: {MAX_ITER}, Output: {OUTPUT_DIR}\n")

    best_image = None
    best_score = 0
    critique_data = {}

    for i in range(1, MAX_ITER + 1):
        print(f"--- Iteration {i}/{MAX_ITER} ---")

        # Generate code
        print(f"  Generating code...")
        if i == 1:
            user_msg = f"Create this figure:\n\n{INTENT}"
        else:
            feedback = "\n".join(f"- {x}" for x in critique_data.get("issues", []))
            suggestions = "\n".join(f"- {x}" for x in critique_data.get("suggestions", []))
            user_msg = (f"Create this figure:\n\n{INTENT}\n\n"
                       f"PREVIOUS ATTEMPT ISSUES (MUST FIX):\n{feedback}\n\n"
                       f"SUGGESTIONS:\n{suggestions}")

        code_response = call_llm(
            [{"role": "system", "content": CODEGEN_SYSTEM},
             {"role": "user", "content": user_msg}],
            temperature=max(0.3, 0.6 - i * 0.1), max_tokens=8192)
        code = extract_code(code_response)
        (OUTPUT_DIR / f"iter_{i}_code.py").write_text(code)

        # Execute
        image_path = str(OUTPUT_DIR / f"iter_{i}.png")
        print(f"  Executing...")
        success, err = execute_code(code, image_path)

        if not success:
            print(f"  Failed, attempting fix...")
            fix_msg = (f"Fix this matplotlib code. Error: {err}\n\n"
                      f"Original intent:\n{INTENT}\n\nFailed code:\n```python\n{code}\n```")
            code2 = extract_code(call_llm(
                [{"role": "system", "content": CODEGEN_SYSTEM},
                 {"role": "user", "content": fix_msg}],
                temperature=0.2, max_tokens=8192))
            (OUTPUT_DIR / f"iter_{i}_code_fix.py").write_text(code2)
            success, _ = execute_code(code2, image_path)
            if not success:
                print(f"  Still failed, skipping")
                continue

        size_kb = Path(image_path).stat().st_size / 1024
        print(f"  Image: {image_path} ({size_kb:.0f} KB)")

        # Critique
        print(f"  Critiquing...")
        try:
            critique_raw = call_vlm_with_image(
                image_path,
                f"Evaluate this framework figure against this specification:\n\n{INTENT}",
                system_prompt=CRITIC_SYSTEM)
            critique_data = json.loads(critique_raw)
        except Exception as e:
            print(f"  Critique error: {e}")
            critique_data = {"overall": 5, "needs_revision": True,
                           "issues": [str(e)], "suggestions": []}

        overall = critique_data.get("overall", 0)
        scores = critique_data.get("scores", {})
        print(f"  Score: {overall}/10 | {scores}")
        (OUTPUT_DIR / f"iter_{i}_critique.json").write_text(json.dumps(critique_data, indent=2))

        if overall > best_score:
            best_score = overall
            best_image = image_path

        if not critique_data.get("needs_revision", True):
            print(f"  Satisfied!")
            break

        if critique_data.get("issues"):
            for iss in critique_data["issues"][:3]:
                print(f"    Issue: {iss}")

    if best_image:
        final = OUTPUT_DIR / "final_output.png"
        shutil.copy2(best_image, str(final))
        print(f"\n=== DONE ===")
        print(f"Best: {best_score}/10 | {final}")
    else:
        print("\n=== FAILED ===")


if __name__ == "__main__":
    main()
