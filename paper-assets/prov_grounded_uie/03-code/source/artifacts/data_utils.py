"""Data loading and preprocessing for ProvUIE.

Handles DocRED → JSONL conversion and HuggingFace Dataset creation.
Input:  Raw DocRED JSON (train_annotated.json / dev.json) or preprocessed JSONL.
Output: HuggingFace Dataset with chat-format messages for SFT / GRPO.

Key dependency: datasets library.
"""

import json
from pathlib import Path
from datasets import Dataset


SYSTEM_PROMPT = (
    "You are a document-level relation extraction model. "
    "Given a document with numbered sentences and a list of entities, "
    "extract all relations and provide the evidence sentences supporting each relation. "
    "Output valid JSON only.\n/no_think"
)

# DocRED Wikidata property ID → human-readable name (all 96 relation types)
DOCRED_REL_NAMES = {
    "P6": "head of government", "P17": "country", "P19": "place of birth",
    "P20": "place of death", "P22": "father", "P25": "mother", "P26": "spouse",
    "P27": "country of citizenship", "P30": "continent", "P31": "instance of",
    "P35": "head of state", "P36": "capital", "P37": "official language",
    "P39": "position held", "P40": "child", "P50": "author",
    "P54": "member of sports team", "P57": "director", "P58": "screenwriter",
    "P69": "educated at", "P86": "composer", "P102": "member of political party",
    "P108": "employer", "P112": "founded by", "P118": "league",
    "P123": "publisher", "P127": "owned by",
    "P131": "located in the administrative territorial entity",
    "P136": "genre", "P137": "operator", "P140": "religion",
    "P150": "contains administrative territorial entity",
    "P155": "follows", "P156": "followed by", "P159": "headquarters location",
    "P161": "cast member", "P162": "producer", "P166": "award received",
    "P170": "creator", "P171": "parent taxon", "P172": "ethnic group",
    "P175": "performer", "P176": "manufacturer", "P178": "developer",
    "P179": "series", "P190": "sister city", "P194": "legislative body",
    "P205": "basin country", "P206": "located in or next to body of water",
    "P241": "military branch", "P264": "record label", "P272": "production company",
    "P276": "location", "P279": "subclass of", "P355": "subsidiary",
    "P361": "part of", "P364": "original language of work", "P400": "platform",
    "P403": "mouth of the watercourse", "P449": "original network",
    "P463": "member of", "P488": "chairperson", "P495": "country of origin",
    "P527": "has part", "P551": "residence", "P569": "date of birth",
    "P570": "date of death", "P571": "inception",
    "P576": "dissolved, abolished or demolished", "P577": "publication date",
    "P580": "start time", "P582": "end time", "P585": "point in time",
    "P607": "conflict", "P674": "characters", "P676": "lyrics by",
    "P706": "located on terrain feature", "P710": "participant",
    "P737": "influenced by", "P740": "location of formation",
    "P749": "parent organization", "P800": "notable work",
    "P807": "separated from", "P840": "narrative location",
    "P937": "work location", "P1001": "applies to jurisdiction",
    "P1056": "product or material produced", "P1198": "unemployment rate",
    "P1336": "territory claimed by", "P1344": "participant of",
    "P1365": "replaces", "P1366": "replaced by", "P1376": "capital of",
    "P1412": "languages spoken, written or signed", "P3373": "sibling",
}


def sentences_to_text(sents: list[list[str]]) -> list[str]:
    """Join tokenized sentence lists into strings."""
    return [" ".join(tokens) for tokens in sents]


def build_user_prompt(sentences: list[str], entity_names: list[str]) -> str:
    """Build the user-facing extraction prompt.

    Args:
        sentences: Document sentences.
        entity_names: Canonical entity names.
    """
    doc_lines = [f"[{i}] {s}" for i, s in enumerate(sentences)]
    return (
        f"Document:\n" + "\n".join(doc_lines) + "\n\n"
        f"Entities: {', '.join(entity_names)}\n\n"
        "Extract all relations between the listed entities. "
        "For each relation, output: head entity, tail entity, relation type, "
        "and evidence (the sentence(s) supporting the relation).\n\n"
        "Output format:\n"
        '{"relations": [{"head": "...", "tail": "...", "relation": "...", '
        '"evidence": ["sentence 1", "sentence 2"]}]}'
    )


def build_gold_completion(relations: list[dict]) -> str:
    """Build the gold completion JSON string."""
    return json.dumps({"relations": relations}, ensure_ascii=False)


def docred_to_record(example: dict, rel_names: dict | None = None) -> dict | None:
    """Convert a single DocRED document to a training record.

    Returns dict with keys: messages, prompt, gold_relations, sentences, document_text.
    Returns None if the document has no annotated relations (labels).
    """
    if rel_names is None:
        rel_names = DOCRED_REL_NAMES

    sents = example.get("sents", [])
    sentences = sentences_to_text(sents)
    vertexSet = example.get("vertexSet", [])
    labels = example.get("labels", [])

    if not labels:
        return None

    entity_names = []
    for vs in vertexSet:
        entity_names.append(vs[0]["name"])

    gold_relations = []
    for label in labels:
        h_idx = label["h"]
        t_idx = label["t"]
        rel_id = label["r"]
        evidence_idxs = label.get("evidence", [])

        head_name = entity_names[h_idx]
        tail_name = entity_names[t_idx]
        rel_name = rel_names.get(rel_id, rel_id)
        evidence_texts = [sentences[i] for i in evidence_idxs if i < len(sentences)]

        gold_relations.append({
            "head": head_name,
            "tail": tail_name,
            "relation": rel_name,
            "evidence": evidence_texts,
        })

    user_prompt = build_user_prompt(sentences, entity_names)
    completion = build_gold_completion(gold_relations)

    return {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": completion},
        ],
        "prompt": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "gold_relations": json.dumps(gold_relations, ensure_ascii=False),
        "sentences": json.dumps(sentences, ensure_ascii=False),
        "document_text": " ".join(sentences),
    }


# ---------------------------------------------------------------------------
# Data preparation: DocRED JSON → JSONL
# ---------------------------------------------------------------------------

def load_docred_raw(path: str) -> list[dict]:
    """Load raw DocRED JSON file."""
    with open(path) as f:
        return json.load(f)


def prepare_and_save(raw_data: list[dict], output_path: str,
                     rel_names: dict | None = None) -> int:
    """Convert raw DocRED documents to JSONL. Returns count of saved records."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with open(output_path, "w") as f:
        for example in raw_data:
            record = docred_to_record(example, rel_names)
            if record is None:
                continue
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
    print(f"Saved {count} records → {output_path}")
    return count


# ---------------------------------------------------------------------------
# Dataset loading: JSONL → HuggingFace Dataset
# ---------------------------------------------------------------------------

def load_sft_dataset(jsonl_path: str, max_samples: int | None = None) -> Dataset:
    """Load JSONL as Dataset for SFT. Returns dataset with 'messages' column."""
    records = []
    with open(jsonl_path) as f:
        for line in f:
            rec = json.loads(line)
            records.append({"messages": rec["messages"]})
            if max_samples and len(records) >= max_samples:
                break
    return Dataset.from_list(records)


def load_grpo_dataset(jsonl_path: str, max_samples: int | None = None) -> Dataset:
    """Load JSONL as Dataset for GRPO.

    Returns dataset with 'prompt' (chat messages) + gold metadata columns.
    Metadata fields are JSON strings; reward functions deserialize them.
    """
    records = []
    with open(jsonl_path) as f:
        for line in f:
            rec = json.loads(line)
            prompt = rec["prompt"]
            for msg in prompt:
                if msg["role"] == "system" and "/no_think" not in msg["content"]:
                    msg["content"] += "\n/no_think"
            records.append({
                "prompt": prompt,
                "gold_relations": rec["gold_relations"],
                "sentences": rec["sentences"],
                "document_text": rec["document_text"],
            })
            if max_samples and len(records) >= max_samples:
                break
    return Dataset.from_list(records)


# ---------------------------------------------------------------------------
# CLI entry point for data preparation
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Prepare DocRED data for ProvUIE")
    parser.add_argument("--raw_dir", type=str, required=True,
                        help="Dir with train_annotated.json / dev.json")
    parser.add_argument("--output_dir", type=str, default="./data",
                        help="Output dir for JSONL files")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    out_dir = Path(args.output_dir)

    for split, fname in [("train", "train_annotated.json"), ("dev", "dev.json")]:
        src = raw_dir / fname
        if src.exists():
            print(f"Processing {src} ...")
            data = load_docred_raw(str(src))
            prepare_and_save(data, str(out_dir / f"docred_{split}.jsonl"))
        else:
            print(f"Skipping {src} (not found)")
