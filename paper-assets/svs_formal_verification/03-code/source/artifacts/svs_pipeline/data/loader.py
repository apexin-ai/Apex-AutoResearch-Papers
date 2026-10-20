"""ProofWriter / FOLIO / LogiQA data loader for the SVS pipeline.

Loads logical reasoning problems from HuggingFace datasets or local files.
Returns list[Problem] for downstream chain sampling.

Dependencies: datasets (HuggingFace), json, random
"""

import json
import logging
import random
from pathlib import Path

from ..types import Problem

logger = logging.getLogger(__name__)

_CACHE_DIR = Path(__file__).parent


def _parse_proofwriter_premises(context: str) -> list[str]:
    """Split ProofWriter context string into individual premise sentences."""
    sentences = [s.strip() for s in context.split(".") if s.strip()]
    return [s + "." for s in sentences]


def load_proofwriter(
    subset: str = "depth-5",
    num_problems: int = 50,
    seed: int = 42,
) -> list[Problem]:
    """Load ProofWriter problems, filtering by proof depth.

    Tries HuggingFace datasets first, falls back to local cache JSON.
    """
    problems = _load_proofwriter_hf(subset)
    if problems is None:
        problems = _load_proofwriter_cache()

    if not problems:
        raise RuntimeError("Failed to load ProofWriter data from both HF and local cache")

    rng = random.Random(seed)
    if len(problems) > num_problems:
        problems = rng.sample(problems, num_problems)

    logger.info("Loaded %d ProofWriter %s problems", len(problems), subset)
    return problems


def _load_proofwriter_hf(subset: str) -> list[Problem] | None:
    """Try loading ProofWriter from HuggingFace datasets."""
    try:
        from datasets import load_dataset

        ds = load_dataset("allenai/proofwriter-dataset-v2", "depth-5")
        split = ds.get("test") or ds.get("validation") or ds[list(ds.keys())[0]]

        depth_num = subset.replace("depth-", "") if subset.startswith("depth-") else subset

        problems = []
        for i, row in enumerate(split):
            if "proof_depth" in row and str(row["proof_depth"]) != depth_num:
                continue

            label_raw = row.get("answer", row.get("label", ""))
            label = _normalize_label(label_raw)
            if label is None:
                continue

            context = row.get("theory", row.get("context", row.get("premises", "")))
            hypothesis = row.get("hypothesis", row.get("question", ""))

            problems.append(Problem(
                id=f"pw_{i}",
                premises=_parse_proofwriter_premises(context),
                hypothesis=hypothesis,
                label=label,
                dataset="proofwriter",
                raw=dict(row),
            ))

        logger.info("Loaded %d problems from HuggingFace (subset=%s)", len(problems), subset)
        return problems if problems else None

    except Exception as e:
        logger.warning("HuggingFace load failed: %s. Falling back to local cache.", e)
        return None


def _load_proofwriter_cache() -> list[Problem] | None:
    """Load ProofWriter from local JSON cache."""
    cache_path = _CACHE_DIR / "proofwriter_cache.json"
    if not cache_path.exists():
        logger.warning("Local cache not found at %s", cache_path)
        return None

    with open(cache_path) as f:
        data = json.load(f)

    problems = []
    for i, row in enumerate(data):
        label = _normalize_label(row.get("answer", row.get("label", "")))
        if label is None:
            continue

        context = row.get("theory", row.get("context", row.get("premises", "")))
        hypothesis = row.get("hypothesis", row.get("question", ""))

        if isinstance(context, list):
            premises = context
        else:
            premises = _parse_proofwriter_premises(context)

        problems.append(Problem(
            id=f"pw_{i}",
            premises=premises,
            hypothesis=hypothesis,
            label=label,
            dataset="proofwriter",
            raw=row,
        ))

    logger.info("Loaded %d problems from local cache", len(problems))
    return problems


def load_folio(
    subset: str = "validation",
    num_problems: int = 50,
    seed: int = 42,
) -> list[Problem]:
    """Load FOLIO problems. Tries HF → local JSONL → JSON cache."""
    problems = _load_folio_hf(subset)
    if problems is None:
        problems = _load_folio_local(subset)
    if problems is None:
        cache_path = _CACHE_DIR / "folio_cache.json"
        if cache_path.exists():
            with open(cache_path) as f:
                data = json.load(f)
            problems = []
            for i, row in enumerate(data):
                label = _normalize_label(row.get("label", ""))
                if label is None:
                    continue
                premises = row.get("premises", [])
                if isinstance(premises, str):
                    premises = _parse_proofwriter_premises(premises)
                problems.append(Problem(
                    id=f"folio_{subset}_{i}",
                    premises=premises,
                    hypothesis=row.get("conclusion", row.get("hypothesis", "")),
                    label=label,
                    dataset="folio",
                    raw=row,
                ))

    if not problems:
        raise RuntimeError("Failed to load FOLIO data from HF, local JSONL, and cache")

    rng = random.Random(seed)
    if num_problems > 0 and len(problems) > num_problems:
        problems = rng.sample(problems, num_problems)

    logger.info("Loaded %d FOLIO problems", len(problems))
    return problems


def _load_folio_hf(subset: str = "validation") -> list[Problem] | None:
    try:
        from datasets import load_dataset

        ds = load_dataset("yale-nlp/FOLIO")
        split = ds.get(subset) or ds.get("validation") or ds[list(ds.keys())[0]]

        problems = []
        for i, row in enumerate(split):
            label = _normalize_label(row.get("label", ""))
            if label is None:
                continue

            premises_raw = row.get("premises", row.get("context", ""))
            if isinstance(premises_raw, list):
                premises = premises_raw
            else:
                premises = _parse_proofwriter_premises(premises_raw)

            hypothesis = row.get("conclusion", row.get("hypothesis", ""))

            problems.append(Problem(
                id=f"folio_{subset}_{i}",
                premises=premises,
                hypothesis=hypothesis,
                label=label,
                dataset="folio",
                raw=dict(row),
            ))

        logger.info("Loaded %d FOLIO problems from HuggingFace", len(problems))
        return problems if problems else None

    except Exception as e:
        logger.warning("HuggingFace FOLIO load failed: %s", e)
        return None


def _load_folio_local(subset: str = "validation") -> list[Problem] | None:
    data_dir = Path("/root/autodl-tmp/data/folio")
    for pattern in [f"folio-{subset}.jsonl", f"{subset}.jsonl", f"folio_{subset}.jsonl"]:
        path = data_dir / pattern
        if path.exists():
            break
    else:
        logger.warning("FOLIO local JSONL not found in %s for subset=%s", data_dir, subset)
        return None

    problems = []
    with open(path) as f:
        for i, line in enumerate(f):
            item = json.loads(line)
            label = _normalize_label(item.get("label", "Unknown"))
            if label is None:
                continue
            premises = item.get("premises", [])
            if isinstance(premises, str):
                premises = _parse_proofwriter_premises(premises)
            problems.append(Problem(
                id=f"folio_{subset}_{i}",
                premises=premises,
                hypothesis=item.get("conclusion", ""),
                label=label,
                dataset="folio",
                raw=item,
            ))

    logger.info("Loaded %d FOLIO problems from local JSONL: %s", len(problems), path)
    return problems if problems else None


def load_logiqa(
    subset: str = "test",
    num_problems: int = 0,
    seed: int = 42,
) -> list[Problem]:
    """Load LogiQA dataset (multi-choice logical reasoning).

    Each problem has a context, question, 4 options (A-D), and a correct
    answer. Label is the uppercase answer letter (A/B/C/D).
    """
    subset_map = {"test": "Test.txt", "train": "Train.txt", "eval": "Eval.txt", "validation": "Eval.txt"}
    filename = subset_map.get(subset.lower(), "Test.txt")

    data_dir = Path("/root/autodl-tmp/data/logiqa")
    path = data_dir / filename
    if not path.exists():
        raise RuntimeError(f"LogiQA data not found at {path}. Download from GitHub first.")

    problems = _parse_logiqa_file(path, subset)

    if not problems:
        raise RuntimeError(f"No problems parsed from {path}")

    rng = random.Random(seed)
    if num_problems > 0 and len(problems) > num_problems:
        problems = rng.sample(problems, num_problems)

    logger.info("Loaded %d LogiQA %s problems", len(problems), subset)
    return problems


def _parse_logiqa_file(path: Path, subset: str) -> list[Problem]:
    """Parse LogiQA txt format: blank-line separated blocks of
    [answer, context, question, optionA, optionB, optionC, optionD].
    """
    with open(path) as f:
        content = f.read()

    blocks = [b.strip() for b in content.split("\n\n") if b.strip()]
    problems = []

    for i, block in enumerate(blocks):
        lines = block.split("\n")
        if len(lines) < 6:
            logger.debug("Skipping block %d: only %d lines", i, len(lines))
            continue

        answer = lines[0].strip().upper()
        if answer not in ("A", "B", "C", "D"):
            logger.debug("Skipping block %d: invalid answer '%s'", i, answer)
            continue

        context = lines[1].strip()
        question = lines[2].strip()
        options = [l.strip() for l in lines[3:7]]

        option_texts = []
        for opt in options:
            for prefix in ["A.", "B.", "C.", "D.", "A ", "B ", "C ", "D "]:
                if opt.startswith(prefix):
                    opt = opt[len(prefix):].strip()
                    break
            option_texts.append(opt)

        problems.append(Problem(
            id=f"logiqa_{subset}_{i}",
            premises=[context],
            hypothesis=question,
            label=answer,
            dataset="logiqa",
            raw={
                "context": context,
                "question": question,
                "options": option_texts,
                "option_labels": ["A", "B", "C", "D"],
                "answer": answer,
            },
        ))

    return problems


def load_problems(
    dataset: str,
    subset: str = "",
    num_problems: int = 50,
    seed: int = 42,
) -> list[Problem]:
    """Unified entry point — dispatches to dataset-specific loaders."""
    dataset = dataset.lower().strip()
    if dataset == "proofwriter":
        return load_proofwriter(subset=subset or "depth-5", num_problems=num_problems, seed=seed)
    elif dataset == "folio":
        return load_folio(subset=subset or "validation", num_problems=num_problems, seed=seed)
    elif dataset == "logiqa":
        return load_logiqa(subset=subset or "test", num_problems=num_problems, seed=seed)
    else:
        raise ValueError(f"Unknown dataset: {dataset}. Supported: proofwriter, folio, logiqa")


def _normalize_label(raw) -> str | None:
    """Normalize answer labels to 'True' / 'False' / 'Unknown'."""
    if isinstance(raw, bool):
        return "True" if raw else "False"
    s = str(raw).strip().lower()
    mapping = {
        "true": "True",
        "proved": "True",
        "entailment": "True",
        "false": "False",
        "disproved": "False",
        "contradiction": "False",
        "unknown": "Unknown",
        "uncertain": "Unknown",
        "neutral": "Unknown",
    }
    return mapping.get(s)
