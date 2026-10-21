"""
Iterative LLM+VLM figure generation for OntoCoDec framework diagram.
Round 1: LLM generates matplotlib code from intent
Round 2+: VLM critiques rendered image, LLM fixes code
"""
import os
import sys
import base64
import subprocess
import tempfile
from openai import OpenAI

BASE_URL = "http://47.94.22.126/v1"
API_KEY = "[REDACTED]"
CODE_MODEL = "gpt-4.1"
VISION_MODEL = "gpt-4o"
NUM_ROUNDS = 4

FIGURES_DIR = os.path.dirname(os.path.abspath(__file__))

client = OpenAI(base_url=BASE_URL, api_key=[REDACTED]

INTENT = r"""Write a Python matplotlib script that generates a three-panel academic framework diagram for "OntoCoDec", a two-layer constrained decoding system for Information Extraction.

Requirements:
- Figure size: 17x6.5 inches, 300 DPI, white background
- Three panels left to right, each with light gray (#F5F5F5) background
- NO overlapping text or boxes anywhere
- Clean academic style, no shadows, no gradients
- Save as both PNG and PDF
- Use matplotlib.use('Agg') at the very top before any other matplotlib imports
- Set OUTPUT_DIR from the script's own directory: OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

COLOR SCHEME:
- Blue palette: #D6E8F7 (light), #4A90D9 (mid), #1B5E9E (dark) — for Grammar/structural components
- Orange palette: #FDE8D0 (light), #E8913A (mid), #B85C00 (dark) — for Semantic components
- Green #4CAF50 for "No/valid" branch
- Red #E57373 for "Yes/fallback" branch
- Text: #2D2D2D (dark), #666666 (gray)

PANEL 1 — "Schema Compilation" (top subtitle: "offline, once per schema"):
- Top center: rounded box "IE Ontology O = (E, R, σ)" with dark border, bold. Use LaTeX: $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$
- Two parallel vertical paths descend from ontology:
  LEFT PATH (blue):
    "JSON Schema" (light blue #D6E8F7, blue border)
    ↓ arrow
    "XGrammar" (medium blue #B3D4F0, blue border)
    ↓ arrow
    "Grammar Automaton M_g" (dark blue #1B5E9E bg, white text, bold). Use LaTeX: $M_g$
  RIGHT PATH (orange):
    "σ(r) type pairs" (light orange #FDE8D0, orange border). Use LaTeX: $\sigma(r)$
    ↓ arrow
    "TC Processor" (medium orange #F5CBA0, orange border)
    ↓ arrow
    "Semantic Rules" (dark orange #B85C00 bg, white text, bold)
- Arrows from ontology split into both paths

PANEL 2 — "Constraint Layers" (no subtitle):
- TWO sub-panels stacked vertically with gap between them:
  TOP sub-panel (Grammar Layer):
    - Light blue background (#D6E8F7, alpha=0.5), blue border
    - Title: "Grammar Layer" (bold, dark blue #1B5E9E)
    - Subtitle: "Level 1: Context-Free" (italic, blue)
    - Central box: "$G(t) \subseteq V$" (blue #4A90D9 bg, white text, bold, larger font ~11pt)
    - Below box: "JSON structure + vocabulary membership" (small gray text)
  BOTTOM sub-panel (Semantic Layer):
    - Light orange background (#FDE8D0, alpha=0.5), orange border
    - Title: "Semantic Layer" (bold, dark orange #B85C00)
    - Subtitle: "Level 2: Prefix-Decidable" (italic, orange)
    - Central box: "$S(t) \subseteq V$" (orange #E8913A bg, white text, bold, ~11pt)
    - Below box: "Domain/range type constraints" (small gray text)
    - Dashed box at very bottom: "$\mathcal{D}$: entity registry (runtime state)" (light orange bg, dashed orange border)
- CRITICAL: Vertical dashed arrow from Grammar Layer down to Semantic Layer, with label "enabling" rotated 90°, bold italic, dark blue text, with a light blue badge/background box around the text. This represents the key enabling dependency.

PANEL 3 — "Token Masking" (top subtitle: "online, per step $t$"):
- Top: gray box "$M_{\mathrm{final}}(t) = G(t) \cap S(t)$" (bold)
- Below: yellow diamond (#FFF9C4) decision node with text "$G \cap S = \emptyset$?"
- Arrow from M_final down to diamond
- LEFT branch from diamond (labeled "No" in green, bold):
    Green box (#C8E6C9, green border): "Sample from $G \cap S$" (bold, dark green text)
- RIGHT branch from diamond (labeled "Yes" in red, bold, dashed arrow):
    Red box (#FFCDD2, red border): "Fallback: $G(t)$ only" (dark red text)
    Below: "(CF risk)" in italic red
- Both branches converge down to: white box "$y_t \rightarrow$ next step" (bold)
- Dashed curved arrow from y_t back up to M_final on the right side, labeled "auto-regressive" (vertical italic gray text)

CROSS-PANEL ARROWS (thick, colored):
- Dark blue arrow: Grammar Automaton (Panel 1) → G(t) box (Panel 2)
- Dark orange arrow: Semantic Rules (Panel 1) → S(t) box (Panel 2)
- Dark blue arrow: G(t) box (Panel 2) → M_final (Panel 3, upper part)
- Dark orange arrow: S(t) box (Panel 2) → M_final (Panel 3, lower part)

PANEL NUMBERS:
- Large watermark-style numbers "1", "2", "3" in bottom-left of each panel (font size ~20, light gray #D5D5D5)

Use matplotlib FancyBboxPatch for rounded boxes, FancyArrowPatch for arrows, and plt.Polygon for the diamond. Use LaTeX math rendering where appropriate.

LAYOUT REFERENCE (approximate coordinates in a 17x6.5 space):
- Panel 1: x=0.3, y=0.3, w=5.0, h=5.9
- Panel 2: x=5.6, y=0.3, w=5.2, h=5.9
- Panel 3: x=11.2, y=0.3, w=5.5, h=5.9
- Within Panel 1: Ontology box near y=5.0, paths go from y=4.15 down to y=2.35
- Within Panel 2: Grammar sub-panel y=3.55 h=2.25, Semantic sub-panel y=0.6 h=2.65
- Within Panel 3: M_final near y=4.9, diamond at y=3.9, branches at y=2.55, yt at y=1.85

Output file names:
- PNG: os.path.join(OUTPUT_DIR, "fig1_framework.png")
- PDF: os.path.join(OUTPUT_DIR, "fig1_framework.pdf")

IMPORTANT: The script must be completely self-contained and runnable with `python3 script.py`.
Print the output file sizes at the end.
"""


def extract_code(text):
    """Extract Python code from LLM response."""
    if "```python" in text:
        code = text.split("```python")[1].split("```")[0]
    elif "```" in text:
        code = text.split("```")[1].split("```")[0]
    else:
        code = text
    return code.strip()


def generate_code(round_num, intent, previous_code=None, critique=None):
    """Use LLM to generate/fix matplotlib code."""
    if round_num == 1:
        messages = [
            {"role": "system", "content": "You are an expert matplotlib programmer. Generate complete, runnable Python scripts. Output ONLY the code in a ```python``` block, no explanations."},
            {"role": "user", "content": f"Generate a matplotlib script for this figure:\n\n{intent}"}
        ]
    else:
        messages = [
            {"role": "system", "content": "You are an expert matplotlib programmer. Fix the code based on the critique. Output ONLY the complete updated code in a ```python``` block, no explanations."},
            {"role": "user", "content": f"Original intent:\n{intent}\n\nCurrent code:\n```python\n{previous_code}\n```\n\nVLM critique of the rendered image:\n{critique}\n\nFix ALL issues mentioned in the critique. Return the COMPLETE updated script."}
        ]

    print(f"  [Round {round_num}] Calling {CODE_MODEL} for code generation...")
    resp = client.chat.completions.create(
        model=CODE_MODEL,
        messages=messages,
        temperature=0.3,
        max_tokens=8000,
    )
    return extract_code(resp.choices[0].message.content)


def critique_image(image_path, round_num):
    """Use VLM to critique the rendered image."""
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()

    messages = [
        {"role": "system", "content": "You are a critical reviewer of academic figures. Be specific and actionable in your critique."},
        {"role": "user", "content": [
            {"type": "text", "text": """Review this academic framework diagram for "OntoCoDec". It should have three panels:
Panel 1 "Schema Compilation": IE Ontology at top, two parallel paths (blue Grammar path, orange Semantic path) going down.
Panel 2 "Constraint Layers": Grammar Layer (blue, top) and Semantic Layer (orange, bottom) with "enabling" arrow between them.
Panel 3 "Token Masking": M_final at top, diamond decision, No/Yes branches, y_t at bottom with autoregressive loop.
Cross-panel arrows connecting panels.

List SPECIFIC issues:
1. Any overlapping text or boxes (this is critical - be very precise about which elements overlap)
2. Misaligned or poorly positioned elements
3. Arrows that are unclear, missing, or point wrong direction
4. Text that is too small, cut off, or hard to read
5. Missing elements compared to the specification
6. Any visual clutter or spacing problems
7. Color coding issues

Be precise about WHAT needs to change and WHERE. Focus on the most impactful issues first."""},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}}
        ]}
    ]

    print(f"  [Round {round_num}] Calling {VISION_MODEL} for image critique...")
    resp = client.chat.completions.create(
        model=VISION_MODEL,
        messages=messages,
        temperature=0.3,
        max_tokens=2000,
    )
    return resp.choices[0].message.content


def run_code(code, round_num):
    """Execute the matplotlib code and return success status."""
    script_path = os.path.join(FIGURES_DIR, f"_tmp_round{round_num}.py")
    with open(script_path, "w") as f:
        f.write(code)

    print(f"  [Round {round_num}] Executing code...")
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True, text=True, timeout=60, cwd=FIGURES_DIR
    )

    if result.returncode != 0:
        print(f"  [Round {round_num}] ERROR:\n{result.stderr[:1000]}")
        return False, result.stderr[:1000]

    print(f"  [Round {round_num}] Success: {result.stdout.strip()}")

    round_png = os.path.join(FIGURES_DIR, f"fig1_round{round_num}.png")
    final_png = os.path.join(FIGURES_DIR, "fig1_framework.png")
    if os.path.exists(final_png):
        import shutil
        shutil.copy2(final_png, round_png)
        print(f"  Saved round snapshot: {round_png}")

    os.remove(script_path)
    return True, result.stdout


def main():
    print("=" * 60)
    print("OntoCoDec Figure 1: Iterative LLM+VLM Generation")
    print("=" * 60)

    code = None
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\n{'='*40} ROUND {round_num} {'='*40}")

        if round_num == 1:
            code = generate_code(round_num, INTENT)
        else:
            png_path = os.path.join(FIGURES_DIR, "fig1_framework.png")
            if not os.path.exists(png_path):
                print(f"  No image to critique, regenerating...")
                code = generate_code(round_num, INTENT, code, "Previous code failed to produce an image. Fix all errors.")
            else:
                critique = critique_image(png_path, round_num)
                print(f"\n  VLM Critique:\n  {critique[:500]}...\n")
                code = generate_code(round_num, INTENT, code, critique)

        success, output = run_code(code, round_num)

        if not success:
            print(f"  Code execution failed, will fix in next round...")
            if round_num < NUM_ROUNDS:
                code = generate_code(round_num + 1, INTENT, code, f"Code execution error:\n{output}\nFix all errors and return working code.")
                success, output = run_code(code, round_num)

    final_script = os.path.join(FIGURES_DIR, "gen_fig1_pb.py")
    with open(final_script, "w") as f:
        f.write(code)
    print(f"\nFinal code saved to: {final_script}")

    png = os.path.join(FIGURES_DIR, "fig1_framework.png")
    pdf = os.path.join(FIGURES_DIR, "fig1_framework.pdf")
    if os.path.exists(png):
        sz = os.path.getsize(png)
        print(f"Final PNG: {sz} bytes ({'OK' if sz > 100000 else 'WARNING: too small'})")
    if os.path.exists(pdf):
        print(f"Final PDF: {os.path.getsize(pdf)} bytes")

    print("\nDone!")


if __name__ == "__main__":
    main()
