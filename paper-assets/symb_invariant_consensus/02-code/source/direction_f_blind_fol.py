#!/usr/bin/env python3
"""
Direction F: Blind FOL Extraction
Extract FOL from premises only (blind to hypothesis), use Z3 entailment check.
Compare with SC baseline (54.41%) and standard SICA (59.31%).
"""

import json
import os
import re
import sys
import time
import random
from collections import Counter

import httpx
import z3

# ─── Config ───
FOLIO_PATH = "/root/symb_invariant_consensus/data/folio_full.json"
API_BASE = "http://localhost:8000/v1"
K = 12
TEMP_PREMISE = 0.7
TEMP_CONCLUSION = 0.3
RESULTS_DIR = "/root/symb_invariant_consensus/results/direction_f_blind_fol"
SEED = 42
Z3_TIMEOUT_MS = 10000
MODEL_ID = None

random.seed(SEED)

# ─── Prompts ───
BLIND_PREMISE_PROMPT = """You are a formal logic translator. Translate the natural language premises below into Z3-compatible boolean first-order logic formulas. Do NOT reason or draw any conclusions. ONLY translate each premise.

Rules:
- Identify all named entities (people, objects) from the premises
- Variable naming: predicate_entity in lowercase with underscores (e.g., kind_anne, manager_james, likes_bob_alice)
- Universal rules like "All/Every X who P are Q" or "If people P then Q": ground as Implies(P_entity, Q_entity) for EACH named entity
- Disjunction "X or Y": Or(X, Y)
- Conjunction "X and Y": And(X, Y)
- Negation "not X" / "no X": Not(X)
- "Either both A and B, or neither A nor B": Or(And(A, B), And(Not(A), Not(B)))
- "Either A or B" (exclusive): Or(And(A, Not(B)), And(Not(A), B))
- Z3 operators: Implies, And, Or, Not

Output ONLY valid JSON (no explanation, no markdown):
{"variables": ["var1", "var2"], "premises": [{"nl": "premise text", "z3": "Z3 formula"}], "entities": ["entity1"]}

Premises:
"""

CONCLUSION_PROMPT = """Translate this conclusion into a Z3 boolean formula using ONLY the variables listed below. Do NOT reason. ONLY translate.

Available variables: {variables}
Entities: {entities}

Conclusion: "{conclusion}"

Output ONLY the Z3 formula string (e.g., "Implies(manager_james, Not(remote_james))"), nothing else."""


def extract_premises_text(problem_text):
    parts = problem_text.split("Determine whether")
    if len(parts) >= 2:
        premises = parts[0].strip()
        premises = re.sub(r'^Given the following premises:\s*\n?', '', premises).strip()
        return premises
    return problem_text.strip()


def extract_conclusion_text(problem_text):
    parts = problem_text.split("Determine whether")
    if len(parts) >= 2:
        conclusion = parts[1].strip()
        conclusion = re.sub(
            r'^the following conclusion is true,?\s*false,?\s*or uncertain:\s*\n?',
            '', conclusion, flags=re.IGNORECASE
        ).strip()
        return conclusion
    return ""


def call_llm(messages, temperature=0.7, max_tokens=2048):
    payload = {
        "model": MODEL_ID,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    try:
        resp = httpx.post(f"{API_BASE}/chat/completions", json=payload, timeout=120)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"ERROR: {str(e)[:200]}"


def parse_json_response(text):
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
    # Remove markdown code fences
    text = re.sub(r'```json\s*', '', text)
    text = re.sub(r'```\s*', '', text)
    # Try to find JSON
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            pass
    # Fix trailing commas
    cleaned = re.sub(r',\s*([}\]])', r'\1', text)
    json_match = re.search(r'\{[\s\S]*\}', cleaned)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            pass
    return None


def compile_z3_formula(formula_str):
    if not formula_str or not formula_str.strip():
        return None

    s = formula_str.strip()
    s = s.replace('¬', 'Not ')
    s = re.sub(r'[∀∃]\s*\w+\s*[:.]?\s*', '', s)
    s = re.sub(r'~(\w+)', r'Not(\1)', s)

    tokens = set(re.findall(r'\b([a-zA-Z_]\w*)\b', s))
    reserved = {'True', 'False', 'And', 'Or', 'Not', 'Implies', 'If', 'Xor', 'Bool'}
    var_names = tokens - reserved

    ns = {}
    for name in var_names:
        ns[name] = z3.Bool(name)
    ns.update({
        'And': z3.And, 'Or': z3.Or, 'Not': z3.Not,
        'Implies': z3.Implies, 'If': z3.If, 'Xor': z3.Xor,
        'True': True, 'False': False,
    })

    try:
        result = eval(s, {"__builtins__": {}}, ns)
        if isinstance(result, z3.BoolRef):
            return result
        if isinstance(result, bool):
            return z3.BoolVal(result)
        return None
    except Exception:
        return None


def z3_entailment_check(premise_z3_list, conclusion_z3, timeout_ms=10000):
    if not premise_z3_list or conclusion_z3 is None:
        return "Error"

    # Check premises consistency first
    s0 = z3.Solver()
    s0.set("timeout", timeout_ms)
    for p in premise_z3_list:
        s0.add(p)
    if s0.check() == z3.unsat:
        return "Unknown"  # contradictory premises

    # Check 1: premises ∧ ¬conclusion UNSAT → entails (True)
    s1 = z3.Solver()
    s1.set("timeout", timeout_ms)
    for p in premise_z3_list:
        s1.add(p)
    s1.add(z3.Not(conclusion_z3))
    r1 = s1.check()

    # Check 2: premises ∧ conclusion UNSAT → contradicts (False)
    s2 = z3.Solver()
    s2.set("timeout", timeout_ms)
    for p in premise_z3_list:
        s2.add(p)
    s2.add(conclusion_z3)
    r2 = s2.check()

    if r1 == z3.unsat:
        return "True"
    elif r2 == z3.unsat:
        return "False"
    else:
        return "Unknown"


def blind_extract_premises(premises_text, temperature=0.7):
    messages = [{"role": "user", "content": BLIND_PREMISE_PROMPT + premises_text}]
    raw = call_llm(messages, temperature=temperature, max_tokens=2048)
    parsed = parse_json_response(raw)
    return raw, parsed


def translate_conclusion(conclusion_text, variables, entities, temperature=0.3):
    prompt = CONCLUSION_PROMPT.format(
        variables=", ".join(variables[:50]),
        entities=", ".join(entities[:20]),
        conclusion=conclusion_text,
    )
    messages = [{"role": "user", "content": prompt}]
    raw = call_llm(messages, temperature=temperature, max_tokens=512)
    raw_clean = re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL).strip()
    raw_clean = re.sub(r'```\w*\n?', '', raw_clean).strip()
    # Try JSON
    json_data = parse_json_response(raw_clean)
    if json_data:
        for key in ("z3", "z3_formula", "formula"):
            if key in json_data:
                return raw, json_data[key]
    # Take first non-empty line as formula
    for line in raw_clean.split('\n'):
        line = line.strip().strip('"').strip("'")
        if line and not line.startswith('#') and not line.startswith('//'):
            return raw, line
    return raw, raw_clean


def process_one_trace(premises_text, conclusion_text, trace_idx):
    result = {
        "trace_idx": trace_idx,
        "premise_extraction_success": False,
        "conclusion_translation_success": False,
        "z3_compilation_success": False,
        "entailment_result": "Error",
        "num_premises_compiled": 0,
        "num_premises_total": 0,
    }

    # Phase 1: Blind premise extraction
    raw_premise, parsed = blind_extract_premises(premises_text, temperature=TEMP_PREMISE)
    result["raw_premise_response"] = raw_premise[:1500]

    if parsed is None:
        return result

    premises_data = parsed.get("premises", [])
    variables = parsed.get("variables", [])
    entities = parsed.get("entities", [])

    if not premises_data:
        return result

    result["premise_extraction_success"] = True
    result["num_premises_total"] = len(premises_data)

    # Compile premise formulas
    premise_z3 = []
    premise_strs = []
    for p in premises_data:
        z3_str = p.get("z3") or p.get("z3_formula", "")
        z3_f = compile_z3_formula(z3_str)
        if z3_f is not None:
            premise_z3.append(z3_f)
            premise_strs.append(z3_str)

    result["num_premises_compiled"] = len(premise_z3)

    if not premise_z3:
        return result

    # Extract variable names from compiled formulas if not provided
    if not variables:
        all_vars = set()
        for s in premise_strs:
            tokens = re.findall(r'\b([a-z_]\w*)\b', s.lower())
            reserved = {'true', 'false', 'and', 'or', 'not', 'implies', 'if', 'xor'}
            all_vars.update(t for t in tokens if t not in reserved)
        variables = sorted(all_vars)

    # Phase 2: Translate conclusion
    raw_concl, concl_formula_str = translate_conclusion(
        conclusion_text, variables, entities, temperature=TEMP_CONCLUSION
    )
    result["raw_conclusion_response"] = raw_concl[:500]
    result["conclusion_formula_str"] = concl_formula_str

    conclusion_z3 = compile_z3_formula(concl_formula_str)
    if conclusion_z3 is None:
        return result

    result["conclusion_translation_success"] = True
    result["z3_compilation_success"] = True

    # Phase 3: Z3 entailment check
    entailment = z3_entailment_check(premise_z3, conclusion_z3, Z3_TIMEOUT_MS)
    result["entailment_result"] = entailment

    return result


def run_problem(idx, item, n_traces=K):
    premises_text = extract_premises_text(item["problem"])
    conclusion_text = extract_conclusion_text(item["problem"])
    gold_label = item["answer"]

    traces = []
    for k in range(n_traces):
        trace_result = process_one_trace(premises_text, conclusion_text, k)
        traces.append(trace_result)

    # Majority vote (exclude Error)
    predictions = [t["entailment_result"] for t in traces if t["entailment_result"] != "Error"]
    if predictions:
        vote_counts = Counter(predictions)
        predicted = vote_counts.most_common(1)[0][0]
    else:
        predicted = "Unknown"

    correct = (predicted == gold_label)

    return {
        "id": item["id"],
        "gold_label": gold_label,
        "predicted": predicted,
        "correct": correct,
        "num_valid_traces": len(predictions),
        "vote_distribution": dict(Counter(predictions)),
        "traces": traces,
        "premises_text": premises_text[:500],
        "conclusion_text": conclusion_text,
    }


def main():
    global MODEL_ID

    r = httpx.get(f"{API_BASE}/models", timeout=10)
    MODEL_ID = r.json()["data"][0]["id"]
    print(f"Model: {MODEL_ID}", flush=True)

    with open(FOLIO_PATH) as f:
        data = json.load(f)

    n = int(sys.argv[1]) if len(sys.argv) > 1 else len(data)
    data = data[:n]
    print(f"Running {len(data)} problems, K={K}, T_premise={TEMP_PREMISE}, T_conclusion={TEMP_CONCLUSION}", flush=True)

    os.makedirs(RESULTS_DIR, exist_ok=True)

    results = []
    correct = 0
    t_start = time.time()

    for idx, item in enumerate(data):
        t0 = time.time()
        result = run_problem(idx, item)
        results.append(result)
        if result["correct"]:
            correct += 1
        elapsed = time.time() - t0
        acc = correct / (idx + 1) * 100
        print(
            f"[{idx+1}/{len(data)}] {item['id']}: pred={result['predicted']} "
            f"gold={result['gold_label']} {'OK' if result['correct'] else 'X'} "
            f"valid={result['num_valid_traces']}/{K} acc={acc:.1f}% ({elapsed:.1f}s)",
            flush=True
        )

        # Save intermediate every 10 problems
        if (idx + 1) % 10 == 0:
            _save_results(results, correct, idx + 1, time.time() - t_start)

    total_time = time.time() - t_start
    _save_results(results, correct, len(data), total_time, final=True)


def _save_results(results, correct, total, total_time, final=False):
    accuracy = correct / total * 100 if total > 0 else 0

    all_traces = [t for r in results for t in r["traces"]]
    n_traces = len(all_traces) or 1
    premise_ok = sum(1 for t in all_traces if t["premise_extraction_success"])
    concl_ok = sum(1 for t in all_traces if t["conclusion_translation_success"])
    z3_ok = sum(1 for t in all_traces if t["z3_compilation_success"])

    summary = {
        "experiment": "direction_f_blind_fol",
        "model": MODEL_ID,
        "n_problems": total,
        "K": K,
        "T_premise": TEMP_PREMISE,
        "T_conclusion": TEMP_CONCLUSION,
        "seed": SEED,
        "accuracy": round(accuracy, 2),
        "correct": correct,
        "total": total,
        "sc_baseline_accuracy": 54.41,
        "sica_accuracy": 59.31,
        "extraction_stats": {
            "total_traces": len(all_traces),
            "premise_extraction_success": premise_ok,
            "premise_extraction_rate": round(premise_ok / n_traces * 100, 2),
            "conclusion_translation_success": concl_ok,
            "conclusion_translation_rate": round(concl_ok / n_traces * 100, 2),
            "z3_compilation_success": z3_ok,
            "z3_compilation_rate": round(z3_ok / n_traces * 100, 2),
        },
        "per_label_accuracy": {},
        "total_time_seconds": round(total_time, 1),
    }

    for label in ["True", "False", "Unknown"]:
        subset = [r for r in results if r["gold_label"] == label]
        if subset:
            lc = sum(1 for r in subset if r["correct"])
            summary["per_label_accuracy"][label] = {
                "correct": lc, "total": len(subset),
                "accuracy": round(lc / len(subset) * 100, 2),
            }

    output_path = os.path.join(RESULTS_DIR, "results.json")
    with open(output_path, "w") as f:
        json.dump({"summary": summary, "results": results}, f, indent=2, ensure_ascii=False)

    if final:
        print(f"\n{'='*60}")
        print(f"Direction F: Blind FOL Extraction Results")
        print(f"{'='*60}")
        print(f"Accuracy: {accuracy:.2f}% ({correct}/{total})")
        print(f"SC Baseline: 54.41%  |  Standard SICA: 59.31%")
        print(f"Delta vs SC: {accuracy - 54.41:+.2f}%  |  Delta vs SICA: {accuracy - 59.31:+.2f}%")
        print(f"\nExtraction Stats:")
        print(f"  Premise extraction rate: {summary['extraction_stats']['premise_extraction_rate']}%")
        print(f"  Conclusion translation rate: {summary['extraction_stats']['conclusion_translation_rate']}%")
        print(f"  Z3 compilation rate: {summary['extraction_stats']['z3_compilation_rate']}%")
        print(f"\nPer-label accuracy:")
        for label, stats in summary["per_label_accuracy"].items():
            print(f"  {label}: {stats['accuracy']:.2f}% ({stats['correct']}/{stats['total']})")
        print(f"\nTotal time: {total_time:.1f}s")
        print(f"Results saved to {output_path}")


if __name__ == "__main__":
    main()
