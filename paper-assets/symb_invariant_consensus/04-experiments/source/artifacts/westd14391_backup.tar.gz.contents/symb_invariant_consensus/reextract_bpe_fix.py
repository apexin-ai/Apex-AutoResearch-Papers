#!/usr/bin/env python3
"""
Re-extract constraints from R1-Distill SICA intermediates with BPE decoding fix.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import openai

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def _build_bpe_decoder() -> dict[str, int]:
    bs = (
        list(range(ord("!"), ord("~") + 1))
        + list(range(ord("¡"), ord("¬") + 1))
        + list(range(ord("®"), ord("ÿ") + 1))
    )
    cs = bs[:]
    n = 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return {chr(c): b for b, c in zip(bs, cs)}


_BPE_DECODER = _build_bpe_decoder()


def decode_bpe(text: str) -> str:
    if not any(ord(c) >= 256 for c in text):
        return text
    try:
        raw_bytes = bytes([_BPE_DECODER.get(c, ord(c)) for c in text])
        return raw_bytes.decode("utf-8", errors="replace")
    except Exception:
        return text.replace("Ġ", " ").replace("Ċ", "\n")


LOGIC_EXTRACTION_PROMPT = '''Extract logical constraints from this reasoning trace about a logic problem.

The problem has facts (base assertions), rules (grounded implications), and derived conclusions.
Convert each into a Z3 boolean formula.

Variable naming:
- Unary property: property_entity (e.g., kind_anne, red_charlie, round_fiona)
- Binary relation: relation_subject_object (e.g., eats_bear_squirrel, likes_lion_cat)
- Use lowercase with underscores only, no spaces or special characters

Constraint types:
- "fact": a given assertion, e.g., kind_anne == True
- "rule": a grounded implication over specific entities, e.g., Implies(kind_anne, nice_anne)
- "derived": an inferred conclusion from facts + rules, e.g., nice_anne == True

Z3 operators:
- Implies(a, b) for if-then rules
- And(a, b, ...) for conjunctive conditions
- Or(a, b, ...) for disjunctive conditions
- Not(a) for negation
- == True / == False for boolean assertions

Output ONLY the JSON below, nothing else:
{{"constraints": [{{"type": "fact", "expression": "kind(anne)", "z3_formula": "kind_anne == True", "source_step": 1}}], "answer": "True or False or Unknown", "variables": ["kind_anne"]}}

Trace:
{trace}'''


def strip_thinking(text: str) -> str:
    pattern = re.compile(r"<think>.*?</think>", re.DOTALL)
    cleaned = pattern.sub("", text).strip()
    return cleaned if cleaned else text.strip()


def extract_json_str(text: str) -> str | None:
    start = text.find("{")
    if start == -1:
        return None
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    return None


def repair_json(s: str) -> str:
    s = re.sub(r",\s*([}\]])", r"\1", s)
    s = s.replace("'", '"')
    return s


_LOGIC_TYPES = {"fact", "rule", "derived"}


def parse_extraction_response(raw: str, trace_preview: str) -> list[dict]:
    raw = decode_bpe(raw)
    text = strip_thinking(raw)
    if not text:
        return []
    json_str = extract_json_str(text)
    if json_str is None:
        logger.warning("No JSON found for: %s...", trace_preview[:60])
        return []
    data = None
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        try:
            data = json.loads(repair_json(json_str))
        except json.JSONDecodeError:
            logger.warning("JSON parse failed for: %s...", trace_preview[:60])
            return []
    constraints = data.get("constraints", [])
    if not constraints:
        return []
    valid = []
    for c in constraints:
        if not all(k in c for k in ("type", "expression", "z3_formula", "source_step")):
            continue
        if c["type"] not in _LOGIC_TYPES:
            continue
        valid.append(c)
    return valid


def reextract_problem(client, model, intermediate, max_tokens=2048, max_workers=4):
    sica = intermediate.get("sica_result", {})
    traces = sica.get("traces", [])
    if not traces:
        return {"pid": intermediate["problem"]["id"], "error": "no_traces", "per_trace": []}

    decoded_traces = [decode_bpe(t.get("trace", "")) for t in traces]
    prompts = [LOGIC_EXTRACTION_PROMPT.format(trace=dt) for dt in decoded_traces]
    results = [None] * len(prompts)

    def call_extraction(idx, prompt):
        for attempt in range(3):
            try:
                resp = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.1,
                    max_tokens=max_tokens,
                )
                return idx, resp.choices[0].message.content or ""
            except Exception as e:
                if attempt == 2:
                    logger.error("Extraction %d failed: %s", idx, e)
                    return idx, ""
                time.sleep(1)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(call_extraction, i, p) for i, p in enumerate(prompts)]
        for future in as_completed(futures):
            idx, raw = future.result()
            constraints = parse_extraction_response(raw, decoded_traces[idx][:60])
            results[idx] = {
                "trace_idx": traces[idx].get("trace_idx", idx),
                "answer": traces[idx].get("answer", ""),
                "constraints": constraints,
            }

    return {
        "pid": intermediate["problem"]["id"],
        "gt": intermediate["problem"].get("answer", ""),
        "per_trace": results,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--intermediates-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--api-base", default="http://localhost:8003/v1")
    parser.add_argument("--model", default=None)
    parser.add_argument("--max-tokens", type=int, default=2048)
    parser.add_argument("--max-workers", type=int, default=4)
    parser.add_argument("--dry-run", type=int, default=0, help="Only process N problems (0=all)")
    args = parser.parse_args()

    client = openai.OpenAI(base_url=args.api_base, api_key="[REDACTED]")
    if args.model:
        model = args.model
    else:
        models = client.models.list()
        model = models.data[0].id
        logger.info("Auto-detected model: %s", model)

    intermediates_dir = Path(args.intermediates_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    intermediate_files = sorted(intermediates_dir.glob("folio_*.json"))
    logger.info("Found %d intermediate files", len(intermediate_files))

    # Skip already-extracted files
    existing = {f.name for f in output_dir.glob("folio_*.json")}
    before = len(intermediate_files)
    intermediate_files = [f for f in intermediate_files if f.name not in existing]
    logger.info("Skipping %d already-extracted, processing %d remaining", len(existing), len(intermediate_files))

    if args.dry_run > 0:
        intermediate_files = intermediate_files[:args.dry_run]
        logger.info("Dry-run mode: processing only %d files", len(intermediate_files))

    total = len(intermediate_files)
    success_count = 0
    total_constraints = 0
    traces_with_constraints = 0
    times = []

    for i, fpath in enumerate(intermediate_files):
        with open(fpath) as f:
            intermediate = json.load(f)

        pid = intermediate["problem"]["id"]
        t0 = time.perf_counter()
        result = reextract_problem(client, model, intermediate, max_tokens=args.max_tokens, max_workers=args.max_workers)
        elapsed = time.perf_counter() - t0
        times.append(elapsed)

        n_constraints = sum(len(t["constraints"]) for t in result["per_trace"] if t)
        n_with = sum(1 for t in result["per_trace"] if t and t["constraints"])
        total_constraints += n_constraints
        traces_with_constraints += n_with
        if n_constraints > 0:
            success_count += 1

        out_path = output_dir / fpath.name
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2)

        avg_time = sum(times) / len(times)
        eta = avg_time * (total - i - 1) / 60
        logger.info("[%d/%d] %s: %d constraints from %d/%d traces (%.1fs) ETA: %.1f min",
                     i + 1, total, pid, n_constraints, n_with, len(result["per_trace"]), elapsed, eta)

    extraction_rate = success_count / max(total, 1)
    logger.info("=" * 60)
    logger.info("Re-extraction complete")
    logger.info("Problems: %d, With constraints: %d (%.1f%%)", total, success_count, extraction_rate * 100)
    logger.info("Total constraints: %d, Traces with constraints: %d", total_constraints, traces_with_constraints)

    summary = {
        "total_problems": total,
        "problems_with_constraints": success_count,
        "extraction_rate": extraction_rate,
        "total_constraints": total_constraints,
        "traces_with_constraints": traces_with_constraints,
    }
    with open(output_dir / "reextraction_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    logger.info("Summary: %s", output_dir / "reextraction_summary.json")


if __name__ == "__main__":
    main()
