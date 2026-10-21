"""
PaperBanana-equivalent: GPT-4o generates matplotlib code for framework diagram,
VLM critic evaluates rendered image, iterates up to N rounds.
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

INTENT = """Three-panel academic framework figure for a generation-depth profiling paper.
The figure flows left to right with three panels (a), (b), (c) on a white background.
Full textwidth (~6.5 inches wide, ~2.5 inches tall), 300 DPI, publication quality.

Panel (a) 'Recursive Generation Chain' (leftmost, ~35% width):
- Top: a document icon labeled 'Human Text (gen-0)' with subtle Wikipedia 'W' mark
- Arrow down into a rounded box labeled 'Generator G' with subtitle '8 LLMs | 5 families | 0.6B-8B'
- Arrow down to 'gen-1' document icon
- Arrow looping back up to Generator G box, then arrow down to 'gen-2' document
- Dashed arrow down to 'gen-3, gen-4...' (faded/lighter)
- Left margin: depth labels d=0, d=1, d=2+
- Color gradient: gen-0 in light blue (#B3D9FF), gen-1 in medium blue (#4DA6FF), gen-2+ in dark blue (#0066CC)
- Small formula below: $x^{(k)} = G(x^{(k-1)})$

Panel (b) 'Feature Extraction' (middle, ~35% width):
- Top: document icon flowing into a rounded box 'Pythia-410M (Reference Model)'
- Below: small sketch of NLL distribution curve
- Below that: two groups of features in rounded boxes:
  Group 1 'NLL Statistics' (stacked): mean, std, max, min, tail_decay
  Group 2 'Surface Features': TTR, hapax_ratio
- Bottom: features merge into a single vector bar labeled '7 DDR Features'
- Color: green/teal (#2E8B57) for feature boxes, lighter teal for backgrounds

Panel (c) 'LOGO Evaluation' (rightmost, ~30% width):
- Top: 2x4 grid of 8 small rounded boxes with generator names:
  Row 1: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B
  Row 2: Qwen3-0.6B, Qwen3-8B, Llama-3.2-3B, Mistral-7B
  7 boxes in blue (train set), 1 in orange/red (#E8712B, held-out test)
- Arrow down to rounded box 'XGBoost Classifier'
- Arrow down to three prediction output boxes: gen-0, gen-1, gen-2+ (using blue gradient from panel a)
- Small text below: 'Leave-One-Generator-Out'

Style requirements:
- Clean, minimal, NO heavy borders
- Thin connecting arrows (linewidth ~1.0)
- Sans-serif font (DejaVu Sans or similar)
- Subtle rounded rectangles with light fill and thin border
- Panel titles (a), (b), (c) in bold at top of each panel
- White background, no grid lines
- Professional academic style matching EMNLP/ACL papers
- No matplotlib default styling, use clean custom styling
- Use FancyBboxPatch for rounded rectangles
- Use FancyArrowPatch for arrows
"""

CODEGEN_SYSTEM = """You are an expert matplotlib programmer specializing in academic paper figures.
Generate COMPLETE, SELF-CONTAINED Python code using matplotlib to create the requested figure.
Rules:
- Use matplotlib.patches (FancyBboxPatch, FancyArrowPatch) for boxes and arrows
- Use ax.text() for labels
- Set figure size and DPI as specified
- Save to OUTPUT_PATH variable (will be injected)
- Use plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight', pad_inches=0.05)
- Do NOT use plt.show()
- Import everything needed at the top
- The code must be complete and runnable
- Use clean academic styling, no default matplotlib chrome
- Wrap all drawing code in a main block
- Output ONLY the Python code in a ```python ... ``` block, nothing else
"""

CRITIC_SYSTEM = """You are an academic figure critic evaluating publication-quality diagrams.
Score the figure on these dimensions (1-10 each):
1. Layout clarity: Are panels well-organized and readable?
2. Visual consistency: Are colors, fonts, arrows consistent?
3. Information completeness: Does it convey all required information?
4. Aesthetics: Does it match publication standards (EMNLP/ACL)?
5. Text readability: Are all labels legible and well-placed?

Respond in JSON format:
{
  "scores": {"layout": N, "consistency": N, "completeness": N, "aesthetics": N, "readability": N},
  "overall": N,
  "needs_revision": true/false,
  "issues": ["issue1", "issue2"],
  "suggestions": ["suggestion1", "suggestion2"]
}

Set needs_revision=false if overall >= 7.
"""

def call_llm(messages, temperature=0.7, max_tokens=4096, response_format=None):
    """Call OpenAI-compatible API."""
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if response_format:
        payload["response_format"] = response_format

    with httpx.Client(base_url=API_BASE, timeout=120.0) as client:
        r = client.post(
            "/chat/completions",
            json=payload,
            headers={"Authorization": [REDACTED]"Bearer {API_KEY}", "Content-Type": "application/json"},
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]


def call_vlm_with_image(image_path, prompt, system_prompt=None):
    """Call VLM with an image for critique."""
    with open(image_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
            {"type": "text", "text": prompt},
        ],
    })

    return call_llm(messages, temperature=0.3, max_tokens=2048,
                     response_format={"type": "json_object"})


def extract_code(response):
    """Extract Python code from LLM response."""
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
    """Execute matplotlib code in subprocess."""
    code = re.sub(r'^OUTPUT_PATH\s*=\s*["\'].*["\']\s*$', "", code, flags=re.MULTILINE)
    full_code = f'OUTPUT_PATH = "{output_path}"\n{code}'

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(full_code)
        temp_path = f.name

    try:
        result = subprocess.run(
            [sys.executable, temp_path],
            capture_output=True, text=True, timeout=60,
        )
        if result.returncode != 0:
            print(f"  Code execution error:\n{result.stderr[:500]}")
            return False
        return Path(output_path).exists()
    except subprocess.TimeoutExpired:
        print("  Code execution timed out")
        return False
    finally:
        Path(temp_path).unlink(missing_ok=True)


def main():
    print(f"=== Framework Figure Generator ===")
    print(f"Model: {MODEL}")
    print(f"Max iterations: {MAX_ITER}")
    print(f"Output dir: {OUTPUT_DIR}")
    print()

    description = INTENT
    best_image = None
    best_score = 0

    for i in range(1, MAX_ITER + 1):
        print(f"--- Iteration {i}/{MAX_ITER} ---")

        # Step 1: Generate matplotlib code
        print(f"  Generating code...")
        if i == 1:
            messages = [
                {"role": "system", "content": CODEGEN_SYSTEM},
                {"role": "user", "content": f"Create this figure:\n\n{description}"},
            ]
        else:
            messages = [
                {"role": "system", "content": CODEGEN_SYSTEM},
                {"role": "user", "content": (
                    f"Create this figure:\n\n{description}\n\n"
                    f"Previous attempt had these issues:\n"
                    + "\n".join(f"- {issue}" for issue in critique_data.get("issues", []))
                    + "\n\nSuggestions for improvement:\n"
                    + "\n".join(f"- {s}" for s in critique_data.get("suggestions", []))
                )},
            ]

        code_response = call_llm(messages, temperature=0.5, max_tokens=8192)
        code = extract_code(code_response)

        # Save code
        code_path = OUTPUT_DIR / f"iter_{i}_code.py"
        code_path.write_text(code)
        print(f"  Code saved: {code_path}")

        # Step 2: Execute code
        image_path = str(OUTPUT_DIR / f"iter_{i}.png")
        print(f"  Executing code...")
        success = execute_code(code, image_path)

        if not success:
            print(f"  Execution failed, retrying with error fix...")
            # Try once more with error context
            fix_messages = [
                {"role": "system", "content": CODEGEN_SYSTEM},
                {"role": "user", "content": (
                    f"The previous code failed. Fix it and output the complete corrected code.\n\n"
                    f"Original intent:\n{description}\n\n"
                    f"Failed code:\n```python\n{code}\n```"
                )},
            ]
            code_response = call_llm(fix_messages, temperature=0.3, max_tokens=8192)
            code = extract_code(code_response)
            code_path = OUTPUT_DIR / f"iter_{i}_code_fixed.py"
            code_path.write_text(code)
            success = execute_code(code, image_path)
            if not success:
                print(f"  Still failed, skipping to next iteration")
                continue

        print(f"  Image saved: {image_path}")

        # Step 3: Critique
        print(f"  Critiquing...")
        try:
            critique_raw = call_vlm_with_image(
                image_path,
                f"Evaluate this academic framework figure. It should match this description:\n\n{description}",
                system_prompt=CRITIC_SYSTEM,
            )
            critique_data = json.loads(critique_raw)
        except Exception as e:
            print(f"  Critique failed: {e}")
            critique_data = {"overall": 5, "needs_revision": True, "issues": ["Critique failed"], "suggestions": []}

        overall = critique_data.get("overall", 0)
        print(f"  Overall score: {overall}/10")
        print(f"  Scores: {critique_data.get('scores', {})}")

        if overall > best_score:
            best_score = overall
            best_image = image_path

        # Save critique
        (OUTPUT_DIR / f"iter_{i}_critique.json").write_text(json.dumps(critique_data, indent=2))

        if not critique_data.get("needs_revision", True):
            print(f"  No further revision needed!")
            break

        if critique_data.get("issues"):
            print(f"  Issues: {critique_data['issues'][:3]}")

    # Copy best result
    if best_image:
        final_path = OUTPUT_DIR / "final_output.png"
        shutil.copy2(best_image, str(final_path))
        print(f"\n=== Done! ===")
        print(f"Best score: {best_score}/10")
        print(f"Final output: {final_path}")
        print(f"Total iterations: {min(i, MAX_ITER)}")
    else:
        print("\n=== Failed: no successful renders ===")


if __name__ == "__main__":
    main()
