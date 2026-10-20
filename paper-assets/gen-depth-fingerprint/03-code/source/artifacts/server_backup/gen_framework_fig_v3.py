"""Framework figure v3: fix specific issues from v2."""
import os, json, base64, subprocess, sys, tempfile, re, shutil
from pathlib import Path
from datetime import datetime
import httpx

API_KEY = [REDACTED]"OPENROUTER_API_KEY", "")
API_BASE = os.environ.get("OPENROUTER_API_BASE", "http://47.94.22.126/v1")
MODEL = os.environ.get("VLM_MODEL", "gpt-4o")
MAX_ITER = int(os.environ.get("MAX_ITER", "5"))

OUTPUT_DIR = Path("/root/gen-depth-fingerprint/outputs") / f"run_v3_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

INTENT = """Create a three-panel academic framework figure. EXACT specifications:

FIGURE: fig, axes = plt.subplots(1, 3, figsize=(16, 5.5), gridspec_kw={'width_ratios': [0.35, 0.35, 0.30], 'wspace': 0.15})
For each ax: ax.axis('off'); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
Use transform=ax.transAxes for ALL coordinates.

COLOR PALETTE:
- gen0_blue = '#B3D9FF'  (light blue)
- gen1_blue = '#4DA6FF'  (medium blue)
- gen2_blue = '#0066CC'  (dark blue, use white text)
- teal_dark = '#2E8B57'  (dark green/teal)
- teal_light = '#A8DBC5' (light teal)
- orange_held = '#E8712B' (held-out orange)
- gray_box = '#F0F0F0'   (generator box fill)
- yellow_box = '#FFF3CD'  (classifier box)

PANEL (a) — ax=axes[0], title '(a) Recursive Generation Chain' at (0.5, 0.97):

Elements positioned with GENEROUS spacing, all within x=[0.15, 0.85]:
- (0.5, 0.88): FancyBboxPatch centered, width=0.55, height=0.07, fill=gen0_blue, text='Human Text (gen-0)', fontsize=9
  At (0.08, 0.88): text 'd=0', fontsize=8, color='gray', ha='center'
- (0.5, 0.72): FancyBboxPatch, width=0.55, height=0.09, fill=gray_box, text='Generator G', fontsize=10, bold
  Below at (0.5, 0.665): text '8 LLMs | 5 families | 0.6B–8B', fontsize=7, italic, color='#666666'
- Arrow from (0.5, 0.845) to (0.5, 0.77), color='#555', lw=1.2
- (0.5, 0.53): FancyBboxPatch, width=0.45, height=0.07, fill=gen1_blue, text='gen-1', fontsize=9
  At (0.08, 0.53): text 'd=1'
- Arrow from (0.5, 0.63) to (0.5, 0.57)
- LOOP ARROW: curved arrow from right side of gen-1 (0.75, 0.53) going right and up to right side of Generator G (0.75, 0.72). Use connectionstyle='arc3,rad=-0.4'
- (0.5, 0.35): FancyBboxPatch, width=0.45, height=0.07, fill=gen2_blue, text='gen-2', fontsize=9, color='white'
  At (0.08, 0.35): text 'd=2+'
- Arrow from gen-1 bottom to gen-2 top
- (0.5, 0.22): text 'gen-3, gen-4...', fontsize=8, color='#BBBBBB', style='italic'
- (0.5, 0.08): text '$x^{(k)} = G(x^{(k-1)})$', fontsize=10

PANEL (b) — ax=axes[1], title '(b) Feature Extraction' at (0.5, 0.97):

- (0.5, 0.88): Small rect 'Input Text', width=0.35, height=0.06, fill='white', edge='#888'
- Arrow (0.5, 0.85) to (0.5, 0.78)
- (0.5, 0.72): FancyBboxPatch 'Pythia-410M', width=0.55, height=0.08, fill='white', edge=teal_dark, lw=1.5
  Below: '(Reference Model)', fontsize=7, color='#666'
- Arrow (0.5, 0.67) to (0.5, 0.60)
- (0.5, 0.57): text 'NLL Distribution', fontsize=8, style='italic'
- TWO GROUPS side by side at y=0.35-0.50:
  LEFT group centered at x=0.3, y_center=0.40:
    Outer box: FancyBboxPatch width=0.38, height=0.22, fill=teal_light, alpha=0.3
    Title 'NLL Statistics' at top, fontsize=8, bold, color=teal_dark
    5 items stacked (fontsize=7, monospace): entropy_mean, entropy_std, entropy_max, entropy_min, tail_decay
  RIGHT group centered at x=0.75, y_center=0.43:
    Outer box: width=0.28, height=0.14, fill='#E0F0E0'
    Title 'Surface' at top, fontsize=8, bold
    2 items (fontsize=7, monospace): TTR, hapax_ratio
- Arrow from left group bottom to (0.5, 0.17)
- Arrow from right group bottom to (0.5, 0.17)
- (0.5, 0.10): FancyBboxPatch '7 DDR Features', width=0.55, height=0.07, fill=teal_dark, text color='white', fontsize=9, bold

PANEL (c) — ax=axes[2], title '(c) LOGO Evaluation' at (0.5, 0.97):

- 2×4 GRID of generator boxes, y=[0.78, 0.88] and y=[0.66, 0.76]:
  Each box: width=0.19, height=0.08, fontsize=6.5
  Row 1 at y=0.84: Pythia-2.8B | Pythia-1B | OLMo-2-1B | Qwen3-1.7B
  Row 2 at y=0.72: Qwen3-0.6B | Qwen3-8B | Llama-3.2-3B | Mistral-7B
  x positions: [0.12, 0.33, 0.54, 0.75]
  ALL fill=gen1_blue EXCEPT Mistral-7B fill=orange_held
- At (0.5, 0.62): text '← train (7)          test (1) →', fontsize=7, color='#888'
- Arrow (0.5, 0.59) to (0.5, 0.48)
- (0.5, 0.42): FancyBboxPatch 'XGBoost Classifier', width=0.55, height=0.08, fill=yellow_box, fontsize=9
- Arrow (0.5, 0.37) to (0.5, 0.27)
- 3 boxes side by side at y=0.20:
  (0.2, 0.20): 'gen-0', fill=gen0_blue, width=0.18, height=0.07
  (0.5, 0.20): 'gen-1', fill=gen1_blue, width=0.18, height=0.07
  (0.8, 0.20): 'gen-2+', fill=gen2_blue, width=0.18, height=0.07, white text
- (0.5, 0.08): text 'Leave-One-Generator-Out', fontsize=8, style='italic', color='#666'

IMPORTANT RULES:
- FancyBboxPatch: use boxstyle='round,pad=0.02', coordinates are (x-w/2, y-h/2) for centering
- Arrows: use FancyArrowPatch with arrowstyle='->', mutation_scale=12, lw=1.0, color='#555'
- plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight', pad_inches=0.1, facecolor='white')
- fig.patch.set_facecolor('white')
"""

CODEGEN_SYSTEM = """You are an expert matplotlib programmer. Generate COMPLETE self-contained Python code.
Output ONLY code in a ```python``` block. Requirements:
1. Import matplotlib.pyplot, matplotlib.patches, matplotlib.text
2. Use FancyBboxPatch for all rounded boxes
3. Use FancyArrowPatch for all arrows
4. Save to OUTPUT_PATH variable (injected before your code)
5. NO plt.show(), NO interactive mode
6. ALL coordinates use ax.transAxes (normalized 0-1)
7. Ensure ALL text is readable and never overlapping"""

CRITIC_SYSTEM = """Score this academic framework figure 1-10:
layout, consistency, completeness, aesthetics, readability.
JSON: {"scores":{...},"overall":N,"needs_revision":bool,"issues":[...],"suggestions":[...]}
needs_revision=false only if overall >= 8.5 AND readability >= 8."""


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
        s = response.index("```python") + len("```python")
        e = response.index("```", s)
        return response[s:e].strip()
    elif "```" in response:
        s = response.index("```") + 3
        e = response.index("```", s)
        return response[s:e].strip()
    return response.strip()

def execute_code(code, output_path):
    code = re.sub(r'^OUTPUT_PATH\s*=\s*["\'].*["\']\s*$', "", code, flags=re.MULTILINE)
    full = f'OUTPUT_PATH = "{output_path}"\n{code}'
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(full); tp = f.name
    try:
        r = subprocess.run([sys.executable, tp], capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            print(f"  ERR: {r.stderr[:600]}")
            return False, r.stderr[:600]
        return Path(output_path).exists(), ""
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    finally:
        Path(tp).unlink(missing_ok=True)

def main():
    print(f"=== v3 === Model: {MODEL}, Iter: {MAX_ITER}, Out: {OUTPUT_DIR}\n")
    best_img, best_sc, crit = None, 0, {}

    for i in range(1, MAX_ITER + 1):
        print(f"--- Iter {i}/{MAX_ITER} ---")
        if i == 1:
            umsg = f"Create this figure:\n\n{INTENT}"
        else:
            fb = "\n".join(f"- {x}" for x in crit.get("issues", []))
            sg = "\n".join(f"- {x}" for x in crit.get("suggestions", []))
            umsg = f"Create this figure:\n\n{INTENT}\n\nFIX THESE ISSUES:\n{fb}\n\nSUGGESTIONS:\n{sg}"

        print("  Gen code...")
        cr = call_llm([{"role":"system","content":CODEGEN_SYSTEM},
                       {"role":"user","content":umsg}],
                      temperature=max(0.2, 0.5 - i*0.1), max_tokens=10000)
        code = extract_code(cr)
        (OUTPUT_DIR / f"iter_{i}.py").write_text(code)

        img = str(OUTPUT_DIR / f"iter_{i}.png")
        print("  Execute...")
        ok, err = execute_code(code, img)
        if not ok:
            print("  Fix attempt...")
            cr2 = call_llm([{"role":"system","content":CODEGEN_SYSTEM},
                            {"role":"user","content":f"Fix error: {err}\n\nIntent:\n{INTENT}\n\nCode:\n```python\n{code}\n```"}],
                           temperature=0.2, max_tokens=10000)
            code = extract_code(cr2)
            (OUTPUT_DIR / f"iter_{i}_fix.py").write_text(code)
            ok, _ = execute_code(code, img)
            if not ok: print("  Skip"); continue

        sz = Path(img).stat().st_size / 1024
        print(f"  Image: {sz:.0f} KB")

        print("  Critique...")
        try:
            raw = call_vlm_with_image(img,
                f"Evaluate this figure:\n\n{INTENT}", system_prompt=CRITIC_SYSTEM)
            crit = json.loads(raw)
        except Exception as e:
            print(f"  Critique err: {e}")
            crit = {"overall":5,"needs_revision":True,"issues":[str(e)],"suggestions":[]}

        ov = crit.get("overall", 0)
        sc = crit.get("scores", {})
        print(f"  {ov}/10 | {sc}")
        (OUTPUT_DIR / f"iter_{i}_crit.json").write_text(json.dumps(crit, indent=2))

        if ov > best_sc: best_sc, best_img = ov, img
        if not crit.get("needs_revision", True):
            print("  Done!"); break
        for x in crit.get("issues", [])[:3]: print(f"    ! {x}")

    if best_img:
        fin = OUTPUT_DIR / "final_output.png"
        shutil.copy2(best_img, str(fin))
        print(f"\n=== DONE: {best_sc}/10 => {fin} ===")

if __name__ == "__main__":
    main()
