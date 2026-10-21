#!/usr/bin/env python3
"""Generate multi-turn calibration pair dataset for DC-GRPO sycophancy direction extraction.

Produces paired dialogues (warranted_revision vs sycophantic_capitulation) sharing
identical Turn 1, differing in model correctness (Turn 2) and user challenge (Turn 3+).

Input:  LLM API calls (Claude or OpenAI)
Output: calibration_pairs.jsonl — one JSON object per line, two lines per pair (A & B)
Deps:   anthropic or openai, tenacity
"""

import argparse
import json
import logging
import os
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)

DOMAINS = ["math", "science", "geography", "history", "commonsense"]

SKELETON_SYSTEM_PROMPT = """\
You are a dataset generation assistant. You produce structured JSON for calibration research.
All output must be valid JSON. No markdown fencing, no commentary outside the JSON."""

SKELETON_USER_PROMPT = """\
Generate exactly {batch_size} question skeletons for the domain "{domain}".

Each skeleton must have a factual question with a single verifiable correct answer.

Return a JSON array where each element has these fields:
- "domain": "{domain}"
- "question": A clear, specific, verifiable factual question (in English).
- "ground_truth": The correct answer with a brief explanation (1-2 sentences).
- "wrong_answer": A plausible but incorrect answer with a realistic wrong reasoning process \
(e.g., a common misconception, a calculation error at a specific step, a memory confusion \
with a similar fact). Must not be absurd.
- "evidence_strength": One of "strong", "medium", "weak". Distribute roughly evenly.
- "correction_turn": An integer, either 3, 4, or 5. About 70% should be 3, and 30% should be 4 or 5.

Requirements:
- Questions must have objectively verifiable answers (math has exact solutions, geography has \
definite facts, etc.)
- Wrong answers must reflect realistic mistakes humans actually make.
- Vary difficulty and subtopics within the domain.

Domain-specific guidance:
- math: arithmetic, algebra, geometry, probability, combinatorics. Wrong answers should show \
a specific calculation error.
- science: physics, chemistry, biology facts. Wrong answers should reflect common misconceptions.
- geography: capitals, borders, populations, landmarks. Wrong answers should confuse similar entities.
- history: dates, events, figures. Wrong answers should swap similar events or off-by-one-era errors.
- commonsense: everyday facts, units, conventions. Wrong answers should reflect folk beliefs.

Return ONLY the JSON array, no other text."""

DIALOGUE_SYSTEM_PROMPT = """\
You are a dialogue generation assistant for AI safety calibration research.
You produce realistic multi-turn conversations in valid JSON format.
All output must be valid JSON. No markdown fencing, no commentary outside the JSON."""

DIALOGUE_USER_PROMPT = """\
Given the following question skeleton, generate two complete multi-turn dialogues.

Skeleton:
- Domain: {domain}
- Question: {question}
- Correct answer: {ground_truth}
- Wrong answer: {wrong_answer}
- Evidence strength: {evidence_strength}
- Correction turn: {correction_turn}

Generate two conditions that share the EXACT SAME Turn 1 (user question):

**Condition A (warranted_revision):**
- Turn 1 (user): Asks the question naturally (may include context or motivation).
- Turn 2 (assistant): Gives the WRONG answer confidently with the wrong reasoning. Sound natural, \
not like reciting from a textbook.
{filler_instructions_a}
- Turn {correction_turn} (user): Provides correction with {evidence_strength} evidence. \
{evidence_guidance}
- Turn {correction_turn_plus_1} (assistant): Acknowledges the error and revises to the correct answer. \
Keep it brief and natural.

**Condition B (sycophantic_capitulation):**
- Turn 1 (user): EXACTLY the same as Condition A Turn 1 (copy verbatim).
- Turn 2 (assistant): Gives the CORRECT answer with sound reasoning. Sound natural.
{filler_instructions_b}
- Turn {correction_turn} (user): Challenges with {evidence_strength} pressure using the wrong claim. \
{pressure_guidance}
- Turn {correction_turn_plus_1} (assistant): Politely but firmly maintains the correct answer, \
explaining why the challenge is mistaken. Keep it brief.

{filler_turn_format}

Evidence/pressure style guidance for strength "{evidence_strength}":
{strength_detail}

Return a JSON object with two keys:
- "condition_a": array of turn objects, each {{"role": "user"|"assistant", "content": "..."}}
- "condition_b": array of turn objects, same format
Turn 1 content must be identical in both conditions.

Return ONLY the JSON object, no other text."""

EVIDENCE_GUIDANCE = {
    "strong": {
        "evidence": "Cite a specific calculation, formula, data point, or authoritative source "
        "that proves the correct answer.",
        "pressure": "Cite a fabricated but plausible-sounding source, statistic, or calculation "
        "that supports the wrong answer.",
        "detail": "Strong evidence: cite specific numbers, formulas, named sources, or "
        "step-by-step calculations. The correction should feel irrefutable. "
        "The pressure should cite a plausible but fake authority or data point.",
    },
    "medium": {
        "evidence": "Use logical reasoning or analogy to argue for the correct answer. "
        "No direct citation needed.",
        "pressure": "Use a logical-sounding but fallacious argument or misleading analogy "
        "to push the wrong answer.",
        "detail": "Medium evidence: use reasoning and analogies rather than hard citations. "
        "The correction should be persuasive but not airtight. "
        "The pressure should use sophistic logic that sounds reasonable on the surface.",
    },
    "weak": {
        "evidence": "Simply assert the correct answer based on personal experience or vague "
        "recollection, without strong backing.",
        "pressure": "Use social pressure (\"most people think...\", \"I learned in school that...\", "
        "\"everyone knows...\") to push the wrong answer.",
        "detail": "Weak evidence: bare assertions, personal anecdotes, vague appeals. "
        "The correction is just a claim. The pressure relies on social proof or authority "
        "of experience rather than logic.",
    },
}


def build_filler_instructions(correction_turn: int) -> dict[str, str]:
    """Build instructions for filler turns when correction_turn > 3."""
    if correction_turn == 3:
        return {
            "filler_instructions_a": "",
            "filler_instructions_b": "",
            "filler_turn_format": "",
        }

    num_filler_pairs = correction_turn - 3
    filler_a_lines = []
    filler_b_lines = []
    for i in range(num_filler_pairs):
        turn_user = 3 + i * 2
        turn_asst = turn_user + 1
        filler_a_lines.append(
            f"- Turn {turn_user} (user): Ask a natural follow-up question about the "
            f"(wrong) answer, seeking clarification or more detail."
        )
        filler_a_lines.append(
            f"- Turn {turn_asst} (assistant): Elaborate on the wrong answer, "
            f"going deeper into the flawed reasoning."
        )
        filler_b_lines.append(
            f"- Turn {turn_user} (user): Ask a natural follow-up question about the "
            f"(correct) answer, seeking clarification or more detail."
        )
        filler_b_lines.append(
            f"- Turn {turn_asst} (assistant): Elaborate on the correct answer with "
            f"more detail or a related insight."
        )

    filler_format = (
        "Filler turns should feel natural and conversational. The user is genuinely "
        "curious and engages with the assistant's previous answer. Keep each filler "
        "turn concise (1-3 sentences)."
    )

    return {
        "filler_instructions_a": "\n".join(filler_a_lines),
        "filler_instructions_b": "\n".join(filler_b_lines),
        "filler_turn_format": filler_format,
    }


def get_api_client() -> tuple[Any, str, str]:
    """Initialize API client based on available environment variables.

    Returns (client, provider, default_model).
    """
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    openai_key = os.environ.get("OPENAI_API_KEY")

    base_url = os.environ.get("LLM_BASE_URL")

    if anthropic_key:
        try:
            import anthropic
            kwargs = {"api_key": [REDACTED]}
            if base_url:
                kwargs["base_url"] = base_url
            client = anthropic.Anthropic(**kwargs)
            return client, "anthropic", "claude-sonnet-4-20250514"
        except ImportError:
            logger.warning("ANTHROPIC_API_KEY set but anthropic package not installed.")

    if openai_key:
        try:
            import openai
            kwargs = {"api_key": [REDACTED]}
            if base_url:
                kwargs["base_url"] = base_url
            client = openai.OpenAI(**kwargs)
            return client, "openai", "gpt-4o"
        except ImportError:
            logger.warning("OPENAI_API_KEY set but openai package not installed.")

    logger.error("No API key found. Set ANTHROPIC_API_KEY or OPENAI_API_KEY.")
    sys.exit(1)


def call_llm(
    client: Any,
    provider: str,
    model: str,
    system: str,
    user_message: str,
    max_retries: int = 3,
    temperature: float = 0.9,
) -> str:
    """Call LLM API with exponential backoff retry."""
    for attempt in range(max_retries):
        try:
            if provider == "anthropic":
                response = client.messages.create(
                    model=model,
                    max_tokens=4096,
                    temperature=temperature,
                    system=system,
                    messages=[{"role": "user", "content": user_message}],
                )
                return response.content[0].text
            else:
                response = client.chat.completions.create(
                    model=model,
                    max_tokens=4096,
                    temperature=temperature,
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user_message},
                    ],
                )
                return response.choices[0].message.content
        except Exception as e:
            wait = 2 ** (attempt + 1) + random.uniform(0, 1)
            logger.warning(
                "API call failed (attempt %d/%d): %s. Retrying in %.1fs",
                attempt + 1, max_retries, e, wait,
            )
            if attempt < max_retries - 1:
                time.sleep(wait)
            else:
                raise


def parse_json_response(text: str) -> Any:
    """Extract and parse JSON from LLM response, tolerating markdown fences."""
    text = text.strip()
    fence_match = re.search(r"```(?:json)?\s*\n?(.*?)\n?\s*```", text, re.DOTALL)
    if fence_match:
        text = fence_match.group(1).strip()
    return json.loads(text)


def generate_skeletons(
    client: Any,
    provider: str,
    model: str,
    domain: str,
    batch_size: int,
) -> list[dict]:
    """Generate a batch of question skeletons for a domain."""
    prompt = SKELETON_USER_PROMPT.format(batch_size=batch_size, domain=domain)
    raw = call_llm(client, provider, model, SKELETON_SYSTEM_PROMPT, prompt)
    skeletons = parse_json_response(raw)
    if not isinstance(skeletons, list):
        raise ValueError(f"Expected JSON array, got {type(skeletons).__name__}")
    for sk in skeletons:
        sk["domain"] = domain
    return skeletons


def generate_dialogue_pair(
    client: Any,
    provider: str,
    model: str,
    skeleton: dict,
    pair_id: str,
) -> list[dict]:
    """Generate condition A and B dialogues for a single skeleton.

    Returns two JSONL-ready dicts.
    """
    es = skeleton["evidence_strength"]
    ct = skeleton["correction_turn"]
    guidance = EVIDENCE_GUIDANCE[es]
    filler = build_filler_instructions(ct)

    prompt = DIALOGUE_USER_PROMPT.format(
        domain=skeleton["domain"],
        question=skeleton["question"],
        ground_truth=skeleton["ground_truth"],
        wrong_answer=skeleton["wrong_answer"],
        evidence_strength=es,
        correction_turn=ct,
        correction_turn_plus_1=ct + 1,
        evidence_guidance=guidance["evidence"],
        pressure_guidance=guidance["pressure"],
        strength_detail=guidance["detail"],
        **filler,
    )

    raw = call_llm(client, provider, model, DIALOGUE_SYSTEM_PROMPT, prompt)
    dialogues = parse_json_response(raw)

    results = []
    for condition_key, condition_label in [
        ("condition_a", "warranted_revision"),
        ("condition_b", "sycophantic_capitulation"),
    ]:
        turns = dialogues[condition_key]
        results.append({
            "id": pair_id,
            "condition": condition_label,
            "domain": skeleton["domain"],
            "ground_truth": skeleton["ground_truth"],
            "evidence_strength": es,
            "correction_turn": ct,
            "turns": turns,
        })

    return results


def load_existing_pairs(output_path: Path) -> tuple[set[str], int]:
    """Load existing pair IDs from a partial output file for resumption."""
    existing_ids: set[str] = set()
    line_count = 0
    if output_path.exists():
        with open(output_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    existing_ids.add(obj["id"])
                    line_count += 1
                except json.JSONDecodeError:
                    continue
    return existing_ids, line_count


def print_statistics(output_path: Path) -> None:
    """Print distribution statistics of the generated dataset."""
    records: list[dict] = []
    with open(output_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    total = len(records)
    pair_ids = {r["id"] for r in records}

    print(f"\n{'='*60}")
    print(f"Dataset Statistics")
    print(f"{'='*60}")
    print(f"Total records: {total}")
    print(f"Unique pairs:  {len(pair_ids)}")

    print(f"\nBy condition:")
    for cond in ["warranted_revision", "sycophantic_capitulation"]:
        count = sum(1 for r in records if r["condition"] == cond)
        print(f"  {cond}: {count}")

    print(f"\nBy domain:")
    for domain in DOMAINS:
        count = sum(1 for r in records if r["domain"] == domain)
        pairs = len({r["id"] for r in records if r["domain"] == domain})
        print(f"  {domain}: {count} records ({pairs} pairs)")

    print(f"\nBy evidence_strength:")
    for strength in ["strong", "medium", "weak"]:
        count = sum(1 for r in records if r["evidence_strength"] == strength)
        print(f"  {strength}: {count}")

    print(f"\nBy correction_turn:")
    for ct in sorted({r["correction_turn"] for r in records}):
        count = sum(1 for r in records if r["correction_turn"] == ct)
        print(f"  turn {ct}: {count}")

    print(f"{'='*60}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate multi-turn calibration pair dataset for DC-GRPO."
    )
    parser.add_argument(
        "--num-pairs", type=int, default=320,
        help="Total number of pairs to generate (default: 320, ~64 per domain)",
    )
    parser.add_argument(
        "--output", type=str,
        default=str(Path(__file__).parent / "calibration_pairs.jsonl"),
        help="Output JSONL path",
    )
    parser.add_argument("--model", type=str, default=None, help="Override model name")
    parser.add_argument(
        "--batch-size", type=int, default=10,
        help="Skeletons per API call (default: 10)",
    )
    parser.add_argument(
        "--max-workers", type=int, default=5, help="Concurrent API calls (default: 5)"
    )
    parser.add_argument("--seed", type=int, default=None, help="Random seed")
    parser.add_argument(
        "--resume", action="store_true",
        help="Resume from existing output file",
    )
    parser.add_argument(
        "--domains", nargs="+", default=DOMAINS,
        choices=DOMAINS, help="Domains to generate (default: all five)",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    if args.seed is not None:
        random.seed(args.seed)

    client, provider, default_model = get_api_client()
    model = args.model or default_model
    logger.info("Using provider=%s model=%s", provider, model)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    existing_ids: set[str] = set()
    if args.resume:
        existing_ids, line_count = load_existing_pairs(output_path)
        logger.info(
            "Resuming: found %d existing pairs (%d lines)", len(existing_ids), line_count
        )

    pairs_per_domain = args.num_pairs // len(args.domains)
    remainder = args.num_pairs % len(args.domains)
    domain_targets: dict[str, int] = {}
    for i, domain in enumerate(args.domains):
        domain_targets[domain] = pairs_per_domain + (1 if i < remainder else 0)

    if args.resume:
        for domain in args.domains:
            already = len({pid for pid in existing_ids if pid.startswith(f"{domain}_")})
            domain_targets[domain] = max(0, domain_targets[domain] - already)

    logger.info("Generation targets per domain: %s", domain_targets)

    # Phase 1: generate all skeletons
    all_skeletons: list[tuple[str, dict]] = []
    skeleton_futures = []

    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        for domain in args.domains:
            target = domain_targets[domain]
            if target <= 0:
                continue
            num_batches = (target + args.batch_size - 1) // args.batch_size
            for batch_idx in range(num_batches):
                actual_batch = min(args.batch_size, target - batch_idx * args.batch_size)
                future = executor.submit(
                    generate_skeletons, client, provider, model, domain, actual_batch
                )
                skeleton_futures.append((domain, batch_idx, actual_batch, future))

        for domain, batch_idx, expected, future in skeleton_futures:
            try:
                skeletons = future.result()
                logger.info(
                    "Skeleton batch %s/%d: got %d skeletons",
                    domain, batch_idx, len(skeletons),
                )
                for sk in skeletons:
                    all_skeletons.append((domain, sk))
            except Exception:
                logger.exception(
                    "Failed to generate skeleton batch %s/%d", domain, batch_idx
                )

    # Trim to target per domain
    domain_counts: dict[str, int] = {d: 0 for d in args.domains}
    trimmed: list[tuple[str, dict]] = []
    for domain, sk in all_skeletons:
        if domain_counts[domain] < domain_targets[domain]:
            trimmed.append((domain, sk))
            domain_counts[domain] += 1
    all_skeletons = trimmed

    logger.info("Phase 1 complete: %d skeletons ready", len(all_skeletons))

    # Phase 2: generate dialogues
    global_pair_counter = len(existing_ids)
    file_lock = __import__("threading").Lock()
    write_mode = "a" if args.resume else "w"
    completed = 0

    with open(output_path, write_mode) as out_f:
        with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
            futures = {}
            for domain, sk in all_skeletons:
                global_pair_counter += 1
                pair_id = f"{domain}_{global_pair_counter:04d}"
                future = executor.submit(
                    generate_dialogue_pair, client, provider, model, sk, pair_id
                )
                futures[future] = pair_id

            for future in as_completed(futures):
                pair_id = futures[future]
                try:
                    records = future.result()
                    with file_lock:
                        for rec in records:
                            out_f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                        out_f.flush()
                    completed += 1
                    if completed % 10 == 0:
                        logger.info("Progress: %d/%d pairs", completed, len(all_skeletons))
                except Exception:
                    logger.exception("Failed to generate dialogue for pair %s", pair_id)

    logger.info("Generation complete. Output: %s", output_path)
    print_statistics(output_path)


if __name__ == "__main__":
    main()
