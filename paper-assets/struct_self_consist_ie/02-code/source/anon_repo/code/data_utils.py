"""Data processing utilities for structured self-consistency IE experiments.

Handles loading, converting, and splitting datasets into the unified UIE JSON format.
Supported datasets: SciERC (fully implemented), ACE05 (interface only).
"""

from __future__ import annotations

import json
import os
import random
from typing import Any, TypedDict


# ---------------------------------------------------------------------------
# Shared type definitions (UIE JSON format)
# ---------------------------------------------------------------------------

class Entity(TypedDict):
    text: str
    type: str
    start: int
    end: int


class Relation(TypedDict):
    head: str
    tail: str
    type: str
    head_start: int
    head_end: int
    tail_start: int
    tail_end: int


class EventArgument(TypedDict):
    text: str
    role: str
    start: int
    end: int


class Trigger(TypedDict):
    text: str
    type: str
    start: int
    end: int


class Event(TypedDict):
    trigger: Trigger
    arguments: list[EventArgument]


class Extraction(TypedDict, total=False):
    entities: list[Entity]
    relations: list[Relation]
    events: list[Event]


class Instance(TypedDict, total=False):
    id: str
    text: str
    entities: list[Entity]
    relations: list[Relation]
    events: list[Event]


# ---------------------------------------------------------------------------
# SciERC
# ---------------------------------------------------------------------------

def _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:
    """Compute (char_start, char_end) for each token when joined by single spaces."""
    offsets = []
    pos = 0
    for tok in tokens:
        offsets.append((pos, pos + len(tok)))
        pos += len(tok) + 1  # +1 for the space
    return offsets


def _parse_scierc_sentence(
    doc_key: str,
    sent_idx: int,
    tokens: list[str],
    ner_spans: list[list],
    rel_spans: list[list],
    global_token_offset: int,
) -> Instance:
    """Convert one SciERC sentence into a UIE Instance.

    Args:
        doc_key: Document identifier.
        sent_idx: Sentence index within the document.
        tokens: List of tokens for this sentence.
        ner_spans: NER annotations [[start, end, type], ...] with global token indices (inclusive).
        rel_spans: Relation annotations [[s1, e1, s2, e2, type], ...] with global token indices.
        global_token_offset: Token index of the first token of this sentence in the document.

    Returns:
        A UIE Instance dict.
    """
    text = " ".join(tokens)
    offsets = _token_offsets(tokens)

    def _local(global_idx: int) -> int:
        return global_idx - global_token_offset

    # --- entities ---
    entities: list[Entity] = []
    span_to_text: dict[tuple[int, int], str] = {}
    for span in ner_spans:
        tok_start, tok_end, etype = span[0], span[1], span[2]
        local_s, local_e = _local(tok_start), _local(tok_end)
        if local_s < 0 or local_e >= len(tokens):
            continue
        char_start = offsets[local_s][0]
        char_end = offsets[local_e][1]
        entity_text = text[char_start:char_end]
        entities.append(Entity(text=entity_text, type=etype, start=char_start, end=char_end))
        span_to_text[(tok_start, tok_end)] = entity_text

    # --- relations ---
    relations: list[Relation] = []
    for span in rel_spans:
        s1, e1, s2, e2, rtype = span[0], span[1], span[2], span[3], span[4]
        local_s1, local_e1 = _local(s1), _local(e1)
        local_s2, local_e2 = _local(s2), _local(e2)
        if any(idx < 0 for idx in (local_s1, local_e1, local_s2, local_e2)):
            continue
        if local_e1 >= len(tokens) or local_e2 >= len(tokens):
            continue
        head_cs = offsets[local_s1][0]
        head_ce = offsets[local_e1][1]
        tail_cs = offsets[local_s2][0]
        tail_ce = offsets[local_e2][1]
        relations.append(Relation(
            head=span_to_text.get((s1, e1), text[head_cs:head_ce]),
            tail=span_to_text.get((s2, e2), text[tail_cs:tail_ce]),
            type=rtype,
            head_start=head_cs,
            head_end=head_ce,
            tail_start=tail_cs,
            tail_end=tail_ce,
        ))

    return Instance(
        id=f"{doc_key}_sent{sent_idx:03d}",
        text=text,
        entities=entities,
        relations=relations,
        events=[],
    )


def load_scierc(data_dir: str) -> dict[str, list[Instance]]:
    """Load SciERC dataset and convert to UIE JSON format.

    Args:
        data_dir: Path to the SciERC directory containing {train,dev,test}.json.

    Returns:
        Dict with keys "train", "dev", "test", each mapping to a list of Instance dicts.
    """
    splits: dict[str, list[Instance]] = {}
    for split in ("train", "dev", "test"):
        filepath = os.path.join(data_dir, f"{split}.json")
        instances: list[Instance] = []
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                doc = json.loads(line)
                doc_key = doc["doc_key"]
                sentences = doc["sentences"]
                ner_all = doc.get("ner", [[] for _ in sentences])
                rel_all = doc.get("relations", [[] for _ in sentences])

                global_offset = 0
                for sent_idx, tokens in enumerate(sentences):
                    ner_spans = ner_all[sent_idx] if sent_idx < len(ner_all) else []
                    rel_spans = rel_all[sent_idx] if sent_idx < len(rel_all) else []
                    inst = _parse_scierc_sentence(
                        doc_key, sent_idx, tokens, ner_spans, rel_spans, global_offset,
                    )
                    instances.append(inst)
                    global_offset += len(tokens)

        splits[split] = instances
    return splits


# ---------------------------------------------------------------------------
# ACE05 (interface only)
# ---------------------------------------------------------------------------

def load_ace05(data_dir: str, subtask: str = "ner") -> dict[str, list[Instance]]:
    """Load ACE05 dataset and convert to UIE JSON format.

    Args:
        data_dir: Path to preprocessed ACE05 directory.
        subtask: "ner" for entity extraction (7 types: PER, ORG, GPE, LOC, FAC, WEA, VEH),
                 "eae" for event argument extraction (33 event types).

    Returns:
        Dict with keys "train", "dev", "test".
    """
    if subtask not in ("ner", "eae"):
        raise ValueError(f"subtask must be 'ner' or 'eae', got '{subtask}'")

    # TODO: Implement ACE05 parsing once data format is confirmed.
    # ACE05 has multiple preprocessing formats (DyGIE++, OneIE, DEGREE, etc.).
    # The parsing logic depends on which preprocessed version we use.
    raise NotImplementedError(
        f"ACE05 loading for subtask='{subtask}' is not yet implemented. "
        "Awaiting data format confirmation."
    )


# ---------------------------------------------------------------------------
# Generic I/O utilities
# ---------------------------------------------------------------------------

def convert_to_uie_jsonl(instances: list[dict[str, Any]], output_path: str) -> None:
    """Save a list of UIE instances to a JSONL file.

    Args:
        instances: List of Instance dicts.
        output_path: Destination file path.
    """
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for inst in instances:
            f.write(json.dumps(inst, ensure_ascii=False) + "\n")


def load_uie_jsonl(path: str) -> list[dict[str, Any]]:
    """Load instances from a JSONL file.

    Args:
        path: Path to a JSONL file where each line is a JSON instance.

    Returns:
        List of instance dicts.
    """
    instances = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                instances.append(json.loads(line))
    return instances


def train_dev_test_split(
    instances: list,
    train_ratio: float = 0.8,
    dev_ratio: float = 0.1,
    seed: int = 42,
) -> dict[str, list]:
    """Split instances into train/dev/test sets.

    Args:
        instances: List of instances to split.
        train_ratio: Fraction for training set.
        dev_ratio: Fraction for dev set. Test gets the remainder.
        seed: Random seed for reproducibility.

    Returns:
        Dict with keys "train", "dev", "test".
    """
    rng = random.Random(seed)
    indices = list(range(len(instances)))
    rng.shuffle(indices)

    n = len(instances)
    n_train = int(n * train_ratio)
    n_dev = int(n * dev_ratio)

    train_idx = indices[:n_train]
    dev_idx = indices[n_train:n_train + n_dev]
    test_idx = indices[n_train + n_dev:]

    return {
        "train": [instances[i] for i in train_idx],
        "dev": [instances[i] for i in dev_idx],
        "test": [instances[i] for i in test_idx],
    }


# ---------------------------------------------------------------------------
# CoNLL-2003
# ---------------------------------------------------------------------------

def load_conll2003(data_dir: str) -> dict[str, list[Instance]]:
    """Load CoNLL-2003 UIE-format data.

    Args:
        data_dir: Path to directory containing train.json, dev.json, test.json (JSONL).

    Returns:
        Dict with keys "train", "dev", "test".
    """
    splits: dict[str, list[Instance]] = {}
    for split in ("train", "dev", "test"):
        path = os.path.join(data_dir, f"{split}.json")
        splits[split] = load_uie_jsonl(path)
    return splits


# ---------------------------------------------------------------------------
# WNUT-17
# ---------------------------------------------------------------------------

def load_wnut17(data_dir: str) -> dict[str, list[Instance]]:
    """Load WNUT-17 UIE-format data.

    Args:
        data_dir: Path to directory containing train.json, dev.json, test.json (JSONL).

    Returns:
        Dict with keys "train", "dev", "test".
    """
    splits: dict[str, list[Instance]] = {}
    for split in ("train", "dev", "test"):
        path = os.path.join(data_dir, f"{split}.json")
        splits[split] = load_uie_jsonl(path)
    return splits


# ---------------------------------------------------------------------------
# Few-NERD
# ---------------------------------------------------------------------------

def load_fewnerd(data_dir: str) -> dict[str, list[Instance]]:
    """Load Few-NERD UIE-format data.

    Args:
        data_dir: Path to directory containing train.json, dev.json, test.json (JSONL).

    Returns:
        Dict with keys "train", "dev", "test".
    """
    splits: dict[str, list[Instance]] = {}
    for split in ("train", "dev", "test"):
        path = os.path.join(data_dir, f"{split}.json")
        splits[split] = load_uie_jsonl(path)
    return splits
