"""GPT-4o rewriter formality independence test.

Uses GPT-4o (not Qwen3-32B) as the counterfactual rewriter to generate
formality rewrites on LLMBar data, then Qwen3-32B as judge for pairwise +
Likert scoring. Validates that detected formality bias is rewriter-independent.

Baseline (Qwen3-32B rewriter): BT P(formal)=66.5%, GEE Style OR=4.20, Orig OR=4.70
"""

import asyncio
import gc
import json
import logging
import os
import re
import time

import choix
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.genmod.cov_struct import Exchangeable
from statsmodels.genmod.families import Binomial
from statsmodels.genmod.generalized_estimating_equations import GEE

logger = logging.getLogger(__name__)

# ─── Config ────────────────────────────────────────────────────────────
GPT4O_BASE_URL = "http://47.94.22.126/v1"
GPT4O_API_KEY = "[REDACTED]"
GPT4O_MODEL = "gpt-4o"

QWEN_BASE_URL = "http://localhost:8000/v1"
QWEN_API_KEY = "[REDACTED]"
QWEN_MODEL = "/root/autodl-tmp/models/Qwen3-32B/"

NLI_MODEL_PATH = "/root/autodl-tmp/models/nli-deberta-v3-large/"
NLI_THRESHOLD = 0.90

N_BOOT = 10000
SEED = 42
FORMAL, CASUAL = 0, 1

DATA_DIR = "/root/causal_style_decomp_judge/data"
INPUT_FILE = f"{DATA_DIR}/mvp_samples.jsonl"
CF_FILE = f"{DATA_DIR}/counterfactuals_gpt4o_rewriter_formality.jsonl"
VERIFIED_FILE = f"{DATA_DIR}/verified_gpt4o_rewriter_formality.jsonl"
PAIRWISE_FILE = f"{DATA_DIR}/pairwise_results_gpt4o_rewriter_formality_qwen32b.jsonl"
SCORED_FILE = f"{DATA_DIR}/scored_gpt4o_rewriter_formality_qwen32b.jsonl"
RESULTS_FILE = f"{DATA_DIR}/gpt4o_rewriter_formality_results.json"

# ─── Prompts (matching existing pipeline exactly) ─────────────────────

FORMALITY_SYSTEM_PROMPT = (
    "You are a writing style editor. Your task is to rewrite the given text to change "
    "ONLY its formality level while preserving ALL factual content, arguments, and meaning.\n\n"
    "Rules:\n"
    "- Do NOT add, remove, or alter any facts, claims, or reasoning.\n"
    "- Do NOT change the length substantially (±20% words is acceptable).\n"
    "- Change ONLY the register/formality: vocabulary, sentence structure, tone.\n"
    "- Do NOT change formatting: no adding/removing bold, markdown, lists, headers, or any visual structure changes.\n"
    "- Keep the EXACT same formatting as the original text.\n"
    "- Do NOT modify any text that is quoted from or directly references the original instruction/question. "
    "Only modify the style of the response's own content.\n"
    "- Output ONLY the rewritten text, nothing else."
)

FORMALITY_DETECT_PROMPT = (
    "Analyze the formality level of the following text. "
    "Consider vocabulary (technical/colloquial), sentence structure (complex/simple), "
    "tone (professional/conversational), and register (academic/informal).\n"
    "Output ONLY one word: formal or casual.\n\n"
    "Text:\n{text}"
)

FORMALITY_EXAMPLES = [
    {
        "direction": "formal_to_casual",
        "original": (
            "The implementation of robust error-handling mechanisms is essential for maintaining "
            "system reliability. One should consider employing try-catch blocks with specific "
            "exception types rather than generic catch-all handlers."
        ),
        "rewritten": (
            "You really need good error handling to keep things running smoothly. Use try-catch "
            "with specific exception types instead of just catching everything — trust me, it "
            "makes debugging way easier."
        ),
    },
    {
        "direction": "casual_to_formal",
        "original": (
            "Yeah so basically the model's overfitting like crazy. Just throw in some dropout "
            "and maybe try early stopping, that usually does the trick."
        ),
        "rewritten": (
            "The model exhibits significant overfitting. Incorporating dropout regularization "
            "and implementing early stopping are recommended strategies to mitigate this issue."
        ),
    },
]

PAIRWISE_SYSTEM = (
    "You are an expert evaluator of AI assistant responses. "
    "Compare the two responses below and pick the better one."
)

PAIRWISE_USER_TEMPLATE = """Instruction: {instruction}

Response A:
{response_a}

Response B:
{response_b}

Which response is better in terms of overall quality (helpfulness, accuracy, completeness, coherence)?
Output ONLY "A" or "B"."""

JUDGE_SYSTEM = (
    "You are an expert evaluator of AI assistant responses. "
    "Rate the quality of the following response to the given instruction."
)

JUDGE_USER_TEMPLATE = """Instruction: {instruction}
Response: {response}

Evaluate the overall quality of this response based on helpfulness, accuracy, completeness, and coherence. Rate on a scale of 1-10, where:
1-2: Completely inadequate
3-4: Poor quality with major issues
5-6: Acceptable but with notable weaknesses
7-8: Good quality with minor issues
9-10: Excellent quality

Provide your rating as a single integer. Output ONLY the number, nothing else."""


# ─── Utilities ─────────────────────────────────────────────────────────

def strip_thinking(text):
    """Strip <think>...</think> tags from Qwen3 thinking mode output."""
    return re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL).strip()


def parse_choice(text):
    """Parse A/B choice from model output."""
    text = strip_thinking(text).strip().upper()
    if text in ("A", "B"):
        return text
    m = re.search(r"\b([AB])\b", text)
    return m.group(1) if m else None


def parse_score(text):
    """Parse 1-10 score from model output."""
    text = strip_thinking(text).strip()
    m = re.search(r"\b(10|[1-9])\b", text)
    return int(m.group(1)) if m else None


class RateLimiter:
    def __init__(self, max_per_minute):
        self._interval = 60.0 / max_per_minute
        self._last = 0.0
        self._lock = asyncio.Lock()

    async def acquire(self):
        async with self._lock:
            now = time.monotonic()
            wait = self._interval - (now - self._last)
            if wait > 0:
                await asyncio.sleep(wait)
            self._last = time.monotonic()


# ─── Step 1: GPT-4o Counterfactual Generation ─────────────────────────

def build_rewrite_prompt(text, target_pole, instruction=""):
    """Build few-shot rewrite prompt matching the existing pipeline."""
    if target_pole == "casual":
        direction = "formal_to_casual"
        target_desc = "casual and conversational"
    else:
        direction = "casual_to_formal"
        target_desc = "formal and professional"

    example = next(e for e in FORMALITY_EXAMPLES if e["direction"] == direction)

    messages = [
        {"role": "system", "content": FORMALITY_SYSTEM_PROMPT},
        {"role": "user", "content": f"Rewrite this text to be more {target_desc}:\n\n{example['original']}"},
        {"role": "assistant", "content": example["rewritten"]},
    ]

    user_content = f"Rewrite this text to be more {target_desc}:\n\n{text}"
    if instruction:
        user_content = f"Context (the instruction this responds to): {instruction}\n\n{user_content}"
    messages.append({"role": "user", "content": user_content})
    return messages


def call_gpt4o_sync(client, messages, temperature=0.7, max_tokens=2048, max_retries=3):
    """Synchronous GPT-4o API call with retry."""
    for attempt in range(max_retries):
        try:
            resp = client.chat.completions.create(
                model=GPT4O_MODEL,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            logger.warning("GPT-4o API error (attempt %d/%d): %s", attempt + 1, max_retries, e)
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
    return None


def step1_generate_counterfactuals():
    """Generate formality counterfactuals using GPT-4o as rewriter."""
    from openai import OpenAI

    client = OpenAI(base_url=GPT4O_BASE_URL, api_key=[REDACTED]

    with open(INPUT_FILE) as f:
        records = [json.loads(line) for line in f if line.strip()]
    logger.info("Loaded %d records from %s", len(records), INPUT_FILE)

    processed_ids = set()
    if os.path.exists(CF_FILE):
        with open(CF_FILE) as f:
            for line in f:
                if line.strip():
                    processed_ids.add(json.loads(line)["id"])
    logger.info("Already processed: %d", len(processed_ids))

    with open(CF_FILE, "a") as fout:
        for i, rec in enumerate(records):
            if rec["id"] in processed_ids:
                continue

            text = rec["response"]
            instruction = rec.get("instruction", "")

            detect_msgs = [
                {"role": "user", "content": FORMALITY_DETECT_PROMPT.format(text=text[:1000])}
            ]
            detected = call_gpt4o_sync(client, detect_msgs, temperature=0.0, max_tokens=16)
            if detected is None:
                logger.error("Failed to detect formality for %s", rec["id"])
                continue

            detected = detected.lower().strip().rstrip(".")
            if "formal" in detected and "casual" not in detected:
                original_pole = "formal"
            else:
                original_pole = "casual"

            target_pole = "casual" if original_pole == "formal" else "formal"

            flip_msgs = build_rewrite_prompt(text, target_pole, instruction)
            counterfactual = call_gpt4o_sync(client, flip_msgs)
            if counterfactual is None:
                logger.error("Failed to generate counterfactual for %s", rec["id"])
                continue

            flipback_msgs = build_rewrite_prompt(counterfactual, original_pole, instruction)
            double_rewrite = call_gpt4o_sync(client, flipback_msgs)
            if double_rewrite is None:
                logger.error("Failed to generate double rewrite for %s", rec["id"])
                continue

            out = {
                **rec,
                "original_text": text,
                "counterfactual_text": counterfactual,
                "double_rewrite_text": double_rewrite,
                "original_formality": original_pole,
            }
            fout.write(json.dumps(out, ensure_ascii=False) + "\n")
            fout.flush()
            logger.info("[%d/%d] %s: %s -> %s", i + 1, len(records), rec["id"], original_pole, target_pole)

    with open(CF_FILE) as f:
        n = sum(1 for line in f if line.strip())
    logger.info("Total counterfactuals generated: %d", n)
    return n


# ─── Step 2: NLI Verification ─────────────────────────────────────────

def step2_nli_verification():
    """Verify content preservation using bidirectional NLI (formality axis)."""
    import torch
    from transformers import pipeline as hf_pipeline

    with open(CF_FILE) as f:
        records = [json.loads(line) for line in f if line.strip()]
    logger.info("Loaded %d counterfactuals for NLI verification", len(records))

    device = 0 if torch.cuda.is_available() else -1
    logger.info("Loading NLI model from %s (device=%s)...", NLI_MODEL_PATH, device)
    nli_pipe = hf_pipeline(
        "text-classification",
        model=NLI_MODEL_PATH,
        device=device,
    )

    originals = [r["original_text"] for r in records]
    counterfactuals = [r["counterfactual_text"] for r in records]
    batch_size = 16

    def entailment_scores(texts_a, texts_b):
        inputs = [{"text": a, "text_pair": b} for a, b in zip(texts_a, texts_b)]
        scores = []
        for i in range(0, len(inputs), batch_size):
            batch = inputs[i : i + batch_size]
            results = nli_pipe(
                batch,
                top_k=None,
                tokenizer_kwargs={"truncation": True, "padding": True, "max_length": 512},
            )
            for result in results:
                label_scores = {r["label"].lower(): r["score"] for r in result}
                scores.append(label_scores.get("entailment", 0.0))
        return scores

    logger.info("Computing forward NLI (orig -> cf)...")
    fwd = entailment_scores(originals, counterfactuals)
    logger.info("Computing backward NLI (cf -> orig)...")
    bwd = entailment_scores(counterfactuals, originals)

    # Bidirectional: min(forward, backward) for formality axis
    nli_scores = [min(f, b) for f, b in zip(fwd, bwd)]

    for i, rec in enumerate(records):
        rec["nli_cf"] = nli_scores[i]
        rec["passed_cf"] = nli_scores[i] >= NLI_THRESHOLD

    with open(VERIFIED_FILE, "w") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    n_passed = sum(1 for r in records if r["passed_cf"])
    nli_rate = n_passed / len(records) if records else 0
    logger.info("NLI verification: %d/%d passed (%.1f%%)", n_passed, len(records), nli_rate * 100)

    del nli_pipe
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    return n_passed, nli_rate


# ─── Step 3: Qwen3-32B Pairwise Scoring ───────────────────────────────

async def qwen_pairwise_one(client, instruction, response_a, response_b, limiter, max_retries=3):
    """Single pairwise comparison via Qwen3-32B (thinking mode)."""
    messages = [
        {"role": "system", "content": PAIRWISE_SYSTEM},
        {
            "role": "user",
            "content": PAIRWISE_USER_TEMPLATE.format(
                instruction=instruction, response_a=response_a, response_b=response_b
            ),
        },
    ]
    for attempt in range(max_retries):
        await limiter.acquire()
        try:
            resp = await client.chat.completions.create(
                model=QWEN_MODEL,
                messages=messages,
                temperature=0.0,
                max_tokens=2048,
            )
            text = resp.choices[0].message.content.strip()
            choice = parse_choice(text)
            if choice is not None:
                return choice
            logger.warning("Could not parse choice from: %.100s", text)
        except Exception as e:
            logger.warning("Qwen pairwise error (attempt %d/%d): %s", attempt + 1, max_retries, e)
            if attempt < max_retries - 1:
                await asyncio.sleep(2 ** attempt)
    return None


async def score_record_pairwise(client, rec, semaphore, limiter, max_retries=3):
    """Position-controlled dual-trial pairwise scoring for one record."""
    async with semaphore:
        instruction = rec["instruction"]
        original_pole = rec["original_formality"]

        if original_pole == "formal":
            formal_text = rec["original_text"]
            casual_text = rec["counterfactual_text"]
        else:
            formal_text = rec["counterfactual_text"]
            casual_text = rec["original_text"]

        # Trial 1: A=formal, B=casual
        t1 = await qwen_pairwise_one(client, instruction, formal_text, casual_text, limiter, max_retries)
        # Trial 2: A=casual, B=formal (position swap)
        t2 = await qwen_pairwise_one(client, instruction, casual_text, formal_text, limiter, max_retries)

        t1_prefers_formal = (t1 == "A") if t1 else None
        t2_prefers_formal = (t2 == "B") if t2 else None

        consistent = None
        formal_wins = None
        if t1_prefers_formal is not None and t2_prefers_formal is not None:
            consistent = t1_prefers_formal == t2_prefers_formal
            if consistent:
                formal_wins = t1_prefers_formal

        return {
            "id": rec["id"],
            "instruction": rec["instruction"],
            "original_formality": original_pole,
            "nli_cf": rec["nli_cf"],
            "trial1_choice": t1,
            "trial1_prefers_formal": t1_prefers_formal,
            "trial2_choice": t2,
            "trial2_prefers_formal": t2_prefers_formal,
            "consistent": consistent,
            "formal_wins": formal_wins,
        }


async def step3_pairwise_scoring():
    """Run Qwen3-32B pairwise scoring on NLI-passed records."""
    from openai import AsyncOpenAI

    with open(VERIFIED_FILE) as f:
        records = [json.loads(line) for line in f if line.strip()]

    records = [r for r in records if r.get("passed_cf", False)]
    logger.info("NLI-passed records for pairwise scoring: %d", len(records))

    processed_ids = set()
    if os.path.exists(PAIRWISE_FILE):
        with open(PAIRWISE_FILE) as f:
            for line in f:
                if line.strip():
                    processed_ids.add(json.loads(line)["id"])

    todo = [r for r in records if r["id"] not in processed_ids]
    logger.info("To score: %d (already done: %d)", len(todo), len(processed_ids))

    if not todo:
        return

    client = AsyncOpenAI(base_url=QWEN_BASE_URL, api_key=[REDACTED]
    semaphore = asyncio.Semaphore(5)
    limiter = RateLimiter(120)

    tasks = [score_record_pairwise(client, rec, semaphore, limiter) for rec in todo]

    with open(PAIRWISE_FILE, "a") as fout:
        for coro in asyncio.as_completed(tasks):
            result = await coro
            fout.write(json.dumps(result, ensure_ascii=False) + "\n")
            fout.flush()
            logger.info(
                "Pairwise %s: t1=%s t2=%s consistent=%s formal_wins=%s",
                result["id"],
                result["trial1_choice"],
                result["trial2_choice"],
                result["consistent"],
                result["formal_wins"],
            )


# ─── Step 4: Qwen3-32B Likert Scoring ─────────────────────────────────

async def qwen_likert_one(client, instruction, response, limiter, max_retries=3):
    """Single Likert score via Qwen3-32B (thinking mode)."""
    messages = [
        {"role": "system", "content": JUDGE_SYSTEM},
        {"role": "user", "content": JUDGE_USER_TEMPLATE.format(instruction=instruction, response=response)},
    ]
    for attempt in range(max_retries):
        await limiter.acquire()
        try:
            resp = await client.chat.completions.create(
                model=QWEN_MODEL,
                messages=messages,
                temperature=0.0,
                max_tokens=2048,
            )
            text = resp.choices[0].message.content.strip()
            score = parse_score(text)
            if score is not None:
                return score
            logger.warning("Could not parse score from: %.100s", text)
        except Exception as e:
            logger.warning("Qwen Likert error (attempt %d/%d): %s", attempt + 1, max_retries, e)
            if attempt < max_retries - 1:
                await asyncio.sleep(2 ** attempt)
    return None


async def score_record_likert(client, rec, semaphore, limiter, max_retries=3):
    """Likert-score original and counterfactual for one record."""
    async with semaphore:
        instruction = rec["instruction"]
        s_orig = await qwen_likert_one(client, instruction, rec["original_text"], limiter, max_retries)
        s_cf = await qwen_likert_one(client, instruction, rec["counterfactual_text"], limiter, max_retries)
        return {
            **rec,
            "score_original": s_orig,
            "score_counterfactual": s_cf,
        }


async def step4_likert_scoring():
    """Run Qwen3-32B Likert scoring on NLI-passed records."""
    from openai import AsyncOpenAI

    with open(VERIFIED_FILE) as f:
        records = [json.loads(line) for line in f if line.strip()]

    records = [r for r in records if r.get("passed_cf", False)]
    logger.info("NLI-passed records for Likert scoring: %d", len(records))

    processed_ids = set()
    if os.path.exists(SCORED_FILE):
        with open(SCORED_FILE) as f:
            for line in f:
                if line.strip():
                    processed_ids.add(json.loads(line)["id"])

    todo = [r for r in records if r["id"] not in processed_ids]
    logger.info("To score: %d (already done: %d)", len(todo), len(processed_ids))

    if not todo:
        return

    client = AsyncOpenAI(base_url=QWEN_BASE_URL, api_key=[REDACTED]
    semaphore = asyncio.Semaphore(5)
    limiter = RateLimiter(120)

    tasks = [score_record_likert(client, rec, semaphore, limiter) for rec in todo]

    with open(SCORED_FILE, "a") as fout:
        for coro in asyncio.as_completed(tasks):
            result = await coro
            fout.write(json.dumps(result, ensure_ascii=False) + "\n")
            fout.flush()
            logger.info("Likert %s: orig=%s cf=%s", result["id"], result["score_original"], result["score_counterfactual"])


# ─── Step 5: Analysis ─────────────────────────────────────────────────

def analyze_bt(pairwise_data):
    """Bradley-Terry with pair-level bootstrap (10k iterations, seed=42)."""
    data = [r for r in pairwise_data if r.get("nli_cf", 0) >= NLI_THRESHOLD and r.get("consistent")]

    comparisons = []
    pair_groups = {}

    for rec in data:
        pair_id = rec["id"]
        pcomps = []

        t1 = rec.get("trial1_choice")
        if t1 in ("A", "B"):
            # Trial 1: A=formal, B=casual
            pcomps.append((FORMAL, CASUAL) if t1 == "A" else (CASUAL, FORMAL))

        t2 = rec.get("trial2_choice")
        if t2 in ("A", "B"):
            # Trial 2: A=casual, B=formal
            pcomps.append((CASUAL, FORMAL) if t2 == "A" else (FORMAL, CASUAL))

        comparisons.extend(pcomps)
        pair_groups[pair_id] = pcomps

    if not comparisons:
        return None

    params = choix.ilsr_pairwise(2, comparisons, alpha=0.01)
    diff = params[FORMAL] - params[CASUAL]
    p_formal = 1.0 / (1.0 + np.exp(-diff))

    rng = np.random.RandomState(SEED)
    pair_ids = list(pair_groups.keys())
    n_pairs = len(pair_ids)
    boot_probs = []

    for _ in range(N_BOOT):
        idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        boot_comps = []
        for i in idx:
            boot_comps.extend(pair_groups[pair_ids[i]])
        try:
            bp = choix.ilsr_pairwise(2, boot_comps, alpha=0.01)
            boot_probs.append(1.0 / (1.0 + np.exp(-(bp[FORMAL] - bp[CASUAL]))))
        except Exception:
            pass

    boot_probs = np.array(boot_probs)
    ci_lo, ci_hi = np.percentile(boot_probs, [2.5, 97.5])

    n_below = int(np.sum(boot_probs < 0.5))
    raw_p = n_below / len(boot_probs) if len(boot_probs) > 0 else 1.0
    if raw_p == 0:
        raw_p = 1.0 / len(boot_probs)

    return {
        "p_formal": round(float(p_formal), 4),
        "ci": [round(float(ci_lo), 4), round(float(ci_hi), 4)],
        "p_value": round(float(raw_p), 4),
        "n_pairs": n_pairs,
        "n_comparisons": len(comparisons),
    }


def analyze_gee(pairwise_data):
    """GEE logistic decomposition: style effect + originality effect."""
    data = [r for r in pairwise_data if r.get("nli_cf", 0) >= NLI_THRESHOLD and r.get("consistent")]

    X_rows, y_rows, pair_ids = [], [], []
    pair_idx = 0

    for rec in data:
        if not rec.get("trial1_choice") or not rec.get("trial2_choice"):
            continue
        original_pole = rec.get("original_formality")
        if original_pole not in ("formal", "casual"):
            continue

        # Trial 1: A=formal, B=casual
        is_formal_in_A = 1.0
        is_original_in_A = 1.0 if original_pole == "formal" else 0.0
        chose_A = 1.0 if rec["trial1_choice"] == "A" else 0.0
        X_rows.append([is_formal_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        # Trial 2: A=casual, B=formal
        is_formal_in_A = 0.0
        is_original_in_A = 1.0 if original_pole == "casual" else 0.0
        chose_A = 1.0 if rec["trial2_choice"] == "A" else 0.0
        X_rows.append([is_formal_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        pair_idx += 1

    X = np.array(X_rows)
    y = np.array(y_rows)
    pair_arr = np.array(pair_ids)

    df = pd.DataFrame(
        {
            "chose_A": y,
            "is_formal_in_A": X[:, 0],
            "is_original_in_A": X[:, 1],
            "pair_id": pair_arr,
        }
    )

    exog = sm.add_constant(df[["is_formal_in_A", "is_original_in_A"]])
    model = GEE(
        df["chose_A"],
        exog,
        groups=df["pair_id"],
        family=Binomial(),
        cov_struct=Exchangeable(),
    )
    fit = model.fit()

    style_or = float(np.exp(fit.params.iloc[1]))
    style_p = float(fit.pvalues.iloc[1])
    orig_or = float(np.exp(fit.params.iloc[2]))
    orig_p = float(fit.pvalues.iloc[2])

    return {
        "style_or": round(style_or, 2),
        "style_p": round(style_p, 4),
        "orig_or": round(orig_or, 2),
        "orig_p": round(orig_p, 4),
    }


def analyze_likert(scored_data):
    """Likert ATE + Wilcoxon signed-rank test."""
    data = [r for r in scored_data if r.get("nli_cf", 0) >= NLI_THRESHOLD]

    formal_scores = []
    casual_scores = []

    for r in data:
        s_orig = r.get("score_original")
        s_cf = r.get("score_counterfactual")
        if s_orig is None or s_cf is None:
            continue

        if r["original_formality"] == "formal":
            formal_scores.append(s_orig)
            casual_scores.append(s_cf)
        else:
            casual_scores.append(s_orig)
            formal_scores.append(s_cf)

    formal_arr = np.array(formal_scores, dtype=float)
    casual_arr = np.array(casual_scores, dtype=float)

    ate = float(np.mean(formal_arr) - np.mean(casual_arr))

    diffs = formal_arr - casual_arr
    non_zero = diffs[diffs != 0]
    if len(non_zero) > 0:
        _, p = stats.wilcoxon(non_zero)
    else:
        p = 1.0

    tie_rate = float(np.mean(diffs == 0))

    pooled_sd = np.sqrt(
        ((len(formal_arr) - 1) * np.var(formal_arr, ddof=1) + (len(casual_arr) - 1) * np.var(casual_arr, ddof=1))
        / (len(formal_arr) + len(casual_arr) - 2)
    )
    d = ate / pooled_sd if pooled_sd > 0 else 0

    return {
        "ate": round(ate, 4),
        "p": round(float(p), 4),
        "d": round(d, 4),
        "tie_rate": round(tie_rate, 3),
        "n": len(formal_scores),
        "mean_formal": round(float(np.mean(formal_arr)), 4),
        "mean_casual": round(float(np.mean(casual_arr)), 4),
    }


def step5_analysis():
    """Run all analyses and print report."""
    with open(PAIRWISE_FILE) as f:
        pairwise_data = [json.loads(line) for line in f if line.strip()]

    with open(SCORED_FILE) as f:
        scored_data = [json.loads(line) for line in f if line.strip()]

    with open(VERIFIED_FILE) as f:
        verified = [json.loads(line) for line in f if line.strip()]
    n_total = len(verified)
    n_pass = sum(1 for r in verified if r.get("passed_cf", False))
    nli_rate = n_pass / n_total if n_total > 0 else 0

    bt = analyze_bt(pairwise_data)
    gee = analyze_gee(pairwise_data)
    likert = analyze_likert(scored_data)

    bt_sig = bt["p_value"] < 0.05 if bt else False
    likert_insig = likert["p"] >= 0.05
    blindspot = bt_sig and likert_insig

    baseline = {"bt_p_formal": 0.665, "gee_style_or": 4.20, "gee_orig_or": 4.70}

    results = {
        "experiment": "gpt4o_rewriter_formality_independence",
        "rewriter": "GPT-4o",
        "judge": "Qwen3-32B",
        "dataset": "LLMBar",
        "axis": "formality",
        "n_total": n_total,
        "n_nli_pass": n_pass,
        "nli_rate": round(nli_rate, 3),
        "bt": bt,
        "gee": gee,
        "likert": likert,
        "blindspot": blindspot,
        "baseline_comparison": {
            "qwen32b_rewriter_bt_p_formal": baseline["bt_p_formal"],
            "gpt4o_rewriter_bt_p_formal": bt["p_formal"] if bt else None,
            "delta_pp": round((bt["p_formal"] - baseline["bt_p_formal"]) * 100, 1) if bt else None,
            "ci_overlap": bool(bt["ci"][0] <= baseline["bt_p_formal"] <= bt["ci"][1]) if bt else None,
        },
    }

    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 70)
    print("  GPT-4o Rewriter Formality Independence Test — Qwen3-32B Judge")
    print("=" * 70)
    print(f"\n  NLI pass rate: {n_pass}/{n_total} ({nli_rate*100:.1f}%)")

    if bt:
        print(
            f"\n  BT P(formal) = {bt['p_formal']*100:.1f}%  "
            f"CI [{bt['ci'][0]*100:.1f}%, {bt['ci'][1]*100:.1f}%]  "
            f"p = {bt['p_value']}"
        )

    if gee:
        print(f"\n  GEE Style OR = {gee['style_or']}  (p = {gee['style_p']})")
        print(f"  GEE Orig OR  = {gee['orig_or']}  (p = {gee['orig_p']})")

    if likert:
        print(f"\n  Likert ATE = {likert['ate']}  p = {likert['p']}  d = {likert['d']}")
        print(f"  Tie rate = {likert['tie_rate']}  N = {likert['n']}")

    print(
        f"\n  Blindspot: {'YES' if blindspot else 'NO'} "
        f"(BT p<0.05: {bt_sig}, Likert p>=0.05: {likert_insig})"
    )

    if bt:
        print(f"\n  vs Baseline (Qwen3-32B rewriter):")
        print(f"    Qwen3-32B rewriter BT P(formal) = {baseline['bt_p_formal']*100:.1f}%")
        print(f"    GPT-4o rewriter    BT P(formal) = {bt['p_formal']*100:.1f}%")
        delta = (bt["p_formal"] - baseline["bt_p_formal"]) * 100
        overlap = bt["ci"][0] <= baseline["bt_p_formal"] <= bt["ci"][1]
        print(f"    Delta = {delta:+.1f}pp, CI overlap: {overlap}")

    print("=" * 70)
    return results


# ─── Main ──────────────────────────────────────────────────────────────


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    os.environ.setdefault("HF_HUB_OFFLINE", "1")

    print("\n[Step 1/5] Generating formality counterfactuals with GPT-4o...")
    step1_generate_counterfactuals()

    print("\n[Step 2/5] NLI verification...")
    step2_nli_verification()

    print("\n[Step 3/5] Qwen3-32B pairwise scoring...")
    asyncio.run(step3_pairwise_scoring())

    print("\n[Step 4/5] Qwen3-32B Likert scoring...")
    asyncio.run(step4_likert_scoring())

    print("\n[Step 5/5] Analysis...")
    results = step5_analysis()

    return results


if __name__ == "__main__":
    main()
