# Data loading, schema definitions, and prompt formatting for IE tasks.
# Supports ACE2005 (NER+RE), SciERC (NER+RE), and CrossNER (NER-only) datasets.
# Prompt templates follow a structured schema representation inspired by GoLLIE.
# Depends on: json, os, re (stdlib). Optional: datasets (HuggingFace).

import json
import os
import re
from typing import Any, Optional


# ============================================================================
# Schema Definitions
# ============================================================================

ACE2005_SCHEMA = {
    "entity_types": ["PER", "ORG", "GPE", "LOC", "FAC", "WEA", "VEH"],
    "relation_types": [
        {"name": "PHYS", "arg1_types": ["PER", "GPE", "ORG", "LOC", "FAC"], "arg2_types": ["GPE", "LOC", "FAC"]},
        {"name": "PART-WHOLE", "arg1_types": ["GPE", "ORG", "LOC", "FAC", "VEH", "WEA"], "arg2_types": ["GPE", "ORG", "LOC", "FAC", "VEH", "WEA"]},
        {"name": "PER-SOC", "arg1_types": ["PER"], "arg2_types": ["PER"]},
        {"name": "ORG-AFF", "arg1_types": ["PER", "ORG", "GPE"], "arg2_types": ["ORG", "GPE"]},
        {"name": "ART", "arg1_types": ["PER", "ORG", "GPE"], "arg2_types": ["FAC", "VEH", "WEA"]},
        {"name": "GEN-AFF", "arg1_types": ["PER", "ORG", "GPE"], "arg2_types": ["PER", "ORG", "GPE", "LOC"]},
    ],
}

ACE2005_ENTITY_DESCRIPTIONS = {
    "PER": "Person — names of people",
    "ORG": "Organization — companies, agencies, institutions",
    "GPE": "Geo-Political Entity — countries, cities, states",
    "LOC": "Location — non-GPE locations (mountains, rivers, regions)",
    "FAC": "Facility — buildings, airports, highways, bridges",
    "WEA": "Weapon — weapons",
    "VEH": "Vehicle — vehicles",
}

ACE2005_RELATION_DESCRIPTIONS = {
    "PHYS": "Physical — physical location or proximity",
    "PART-WHOLE": "Part-Whole — subsidiary, membership, geographical containment",
    "PER-SOC": "Person-Social — family, business, or lasting personal relations",
    "ORG-AFF": "Org-Affiliation — employment, membership, ownership",
    "ART": "Artifact — user/owner/inventor of artifact",
    "GEN-AFF": "Gen-Affiliation — citizenship, ethnicity, religion",
}

SCIERC_SCHEMA = {
    "entity_types": ["Task", "Method", "Metric", "Material", "OtherScientificTerm", "Generic"],
    "relation_types": [
        {"name": "Used-for", "arg1_types": ["Method", "Material", "OtherScientificTerm", "Generic", "Metric"], "arg2_types": ["Task", "Method", "OtherScientificTerm", "Material"]},
        {"name": "Feature-of", "arg1_types": ["Task", "Method", "Material", "OtherScientificTerm", "Metric", "Generic"], "arg2_types": ["Task", "Method", "Material", "OtherScientificTerm"]},
        {"name": "Hyponym-of", "arg1_types": ["Task", "Method", "Material", "OtherScientificTerm", "Metric", "Generic"], "arg2_types": ["Task", "Method", "Material", "OtherScientificTerm", "Metric", "Generic"]},
        {"name": "Part-of", "arg1_types": ["Task", "Method", "Material", "OtherScientificTerm", "Metric", "Generic"], "arg2_types": ["Task", "Method", "Material", "OtherScientificTerm"]},
        {"name": "Compare", "arg1_types": ["Method", "Material", "Metric", "Task", "OtherScientificTerm"], "arg2_types": ["Method", "Material", "Metric", "Task", "OtherScientificTerm"]},
        {"name": "Conjunction", "arg1_types": ["Task", "Method", "Material", "OtherScientificTerm", "Metric", "Generic"], "arg2_types": ["Task", "Method", "Material", "OtherScientificTerm", "Metric", "Generic"]},
        {"name": "Evaluate-for", "arg1_types": ["Metric", "Method", "OtherScientificTerm"], "arg2_types": ["Task", "Method", "OtherScientificTerm"]},
    ],
}

SCIERC_ENTITY_DESCRIPTIONS = {
    "Task": "Task — research problem or objective (e.g., machine translation, parsing)",
    "Method": "Method — technique, model, or algorithm (e.g., BERT, attention mechanism)",
    "Metric": "Metric — evaluation measure (e.g., F1 score, BLEU, accuracy)",
    "Material": "Material — dataset, corpus, or resource (e.g., Penn Treebank, Wikipedia)",
    "OtherScientificTerm": "OtherScientificTerm — domain-specific term not covered above",
    "Generic": "Generic — generic reference (e.g., 'this method', 'the approach')",
}

SCIERC_RELATION_DESCRIPTIONS = {
    "Used-for": "Used-for — A is used for B (method/material applied to task)",
    "Feature-of": "Feature-of — A is a feature/property of B",
    "Hyponym-of": "Hyponym-of — A is a subtype/instance of B",
    "Part-of": "Part-of — A is a component/part of B",
    "Compare": "Compare — A is compared with B",
    "Conjunction": "Conjunction — A and B are coordinated/listed together",
    "Evaluate-for": "Evaluate-for — A (metric) evaluates B (task/method)",
}

DYGIEPP_TO_SCHEMA_REL_TYPE = {
    "USED-FOR": "Used-for",
    "FEATURE-OF": "Feature-of",
    "HYPONYM-OF": "Hyponym-of",
    "PART-OF": "Part-of",
    "COMPARE": "Compare",
    "CONJUNCTION": "Conjunction",
    "EVALUATE-FOR": "Evaluate-for",
}

DATASET_SCHEMAS = {
    "ace2005": ACE2005_SCHEMA,
    "scierc": SCIERC_SCHEMA,
}

CROSSNER_SCHEMAS = {
    "politics": {
        "entity_types": [
            "politician", "person", "organisation", "political_party",
            "event", "election", "country", "location", "misc",
        ],
        "relation_types": [],
    },
    "science": {
        "entity_types": [
            "scientist", "person", "university", "organisation", "country",
            "location", "discipline", "enzyme", "protein", "chemicalelement",
            "chemicalcompound", "astronomicalobject", "academicjournal",
            "event", "theory", "award", "misc",
        ],
        "relation_types": [],
    },
    "music": {
        "entity_types": [
            "musicgenre", "song", "band", "album", "musicalartist",
            "musicalinstrument", "award", "event", "country", "location",
            "organisation", "person", "misc",
        ],
        "relation_types": [],
    },
    "literature": {
        "entity_types": [
            "book", "writer", "award", "poem", "event", "magazine",
            "literarygenre", "person", "location", "organisation", "country", "misc",
        ],
        "relation_types": [],
    },
    "ai": {
        "entity_types": [
            "field", "task", "product", "algorithm", "researcher", "metrics",
            "university", "country", "person", "organisation", "location",
            "programlang", "conference", "misc",
        ],
        "relation_types": [],
    },
}

CROSSNER_ENTITY_DESCRIPTIONS = {
    "politician": "Politician — political figures",
    "political_party": "Political party",
    "election": "Election event",
    "scientist": "Scientist — researchers",
    "university": "University or academic institution",
    "discipline": "Academic discipline or field",
    "enzyme": "Enzyme",
    "protein": "Protein",
    "chemicalelement": "Chemical element",
    "chemicalcompound": "Chemical compound",
    "astronomicalobject": "Astronomical object",
    "academicjournal": "Academic journal",
    "theory": "Scientific theory",
    "musicgenre": "Music genre",
    "song": "Song",
    "band": "Band or musical group",
    "album": "Music album",
    "musicalartist": "Musical artist",
    "musicalinstrument": "Musical instrument",
    "book": "Book",
    "writer": "Writer or author",
    "poem": "Poem",
    "magazine": "Magazine",
    "literarygenre": "Literary genre",
    "field": "AI/ML field or subfield",
    "task": "ML task (e.g., classification, generation)",
    "product": "Product or system",
    "algorithm": "Algorithm or model architecture",
    "researcher": "Researcher",
    "metrics": "Evaluation metrics",
    "programlang": "Programming language",
    "conference": "Academic conference",
    "person": "Person",
    "organisation": "Organization",
    "country": "Country",
    "location": "Location",
    "event": "Event",
    "award": "Award",
    "misc": "Miscellaneous entity",
}


# ============================================================================
# Data Loading — ACE2005
# ============================================================================

def load_ace2005_dygiepp(data_dir: str, split: str = "train") -> list[dict]:
    """Load ACE2005 from DyGIE++ preprocessed format (one JSON doc per line).

    DyGIE++ uses document-level token indices and inclusive spans [start, end].
    Each sentence becomes one sample in our format.
    """
    path = None
    for ext in (".json", ".jsonl"):
        candidate = os.path.join(data_dir, f"{split}{ext}")
        if os.path.exists(candidate):
            path = candidate
            break
    if path is None:
        raise FileNotFoundError(f"No {split}.json(l) in {data_dir}")

    samples: list[dict] = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            doc = json.loads(line)
            samples.extend(_convert_dygiepp_doc(doc, schema=ACE2005_SCHEMA))
    return samples


def load_scierc_dygiepp(data_dir: str, split: str = "train") -> list[dict]:
    """Load SciERC from DyGIE++ preprocessed format."""
    path = None
    for ext in (".json", ".jsonl"):
        candidate = os.path.join(data_dir, f"{split}{ext}")
        if os.path.exists(candidate):
            path = candidate
            break
    if path is None:
        raise FileNotFoundError(f"No {split}.json(l) in {data_dir}")

    samples: list[dict] = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            doc = json.loads(line)
            samples.extend(_convert_dygiepp_doc(doc, schema=SCIERC_SCHEMA))
    return samples


def _convert_dygiepp_doc(doc: dict, schema: dict | None = None) -> list[dict]:
    """Convert one DyGIE++ document into per-sentence samples."""
    if schema is None:
        schema = ACE2005_SCHEMA
    sentences = doc.get("sentences", [])
    ner_annotations = doc.get("ner", [])
    rel_annotations = doc.get("relations", [])

    results: list[dict] = []
    sent_token_offset = 0

    for sent_idx, sent_tokens in enumerate(sentences):
        sent_text = " ".join(sent_tokens)

        # Precompute char offsets for each token in the sentence
        token_char_starts: list[int] = []
        offset = 0
        for tok in sent_tokens:
            token_char_starts.append(offset)
            offset += len(tok) + 1  # +1 for space

        # --- NER ---
        entities: list[dict] = []
        sent_ner = ner_annotations[sent_idx] if sent_idx < len(ner_annotations) else []
        for ann in sent_ner:
            if len(ann) < 3:
                continue
            start_tok, end_tok, ent_type = ann[0], ann[1], ann[2]
            local_start = start_tok - sent_token_offset
            local_end = end_tok - sent_token_offset
            if local_start < 0 or local_end >= len(sent_tokens):
                continue
            char_start = token_char_starts[local_start]
            char_end = token_char_starts[local_end] + len(sent_tokens[local_end])
            entities.append({
                "type": ent_type,
                "span": [char_start, char_end],
                "text": sent_text[char_start:char_end],
            })

        # --- Relations ---
        relations: list[dict] = []
        sent_rels = rel_annotations[sent_idx] if sent_idx < len(rel_annotations) else []
        for ann in sent_rels:
            if len(ann) < 5:
                continue
            s1, e1, s2, e2, rel_type = ann[0], ann[1], ann[2], ann[3], ann[4]
            arg1 = _resolve_entity(
                entities, s1 - sent_token_offset, e1 - sent_token_offset,
                sent_tokens, token_char_starts, sent_text,
            )
            arg2 = _resolve_entity(
                entities, s2 - sent_token_offset, e2 - sent_token_offset,
                sent_tokens, token_char_starts, sent_text,
            )
            if arg1 is not None and arg2 is not None:
                mapped_type = DYGIEPP_TO_SCHEMA_REL_TYPE.get(rel_type, rel_type)
                relations.append({"type": mapped_type, "arg1": arg1, "arg2": arg2})

        results.append({
            "text": sent_text,
            "schema": schema,
            "gold": {"entities": entities, "relations": relations},
        })
        sent_token_offset += len(sent_tokens)

    return results


def _resolve_entity(
    entities: list[dict],
    local_start: int,
    local_end: int,
    tokens: list[str],
    token_char_starts: list[int],
    sent_text: str,
) -> dict | None:
    """Find the entity matching a token span, or construct one from token range."""
    if local_start < 0 or local_end >= len(tokens):
        return None
    char_start = token_char_starts[local_start]
    char_end = token_char_starts[local_end] + len(tokens[local_end])
    for ent in entities:
        if ent["span"] == [char_start, char_end]:
            return dict(ent)
    return {"type": "UNK", "span": [char_start, char_end], "text": sent_text[char_start:char_end]}


def load_ace2005_json(data_path: str) -> list[dict]:
    """Load pre-converted ACE2005 data from JSON or JSONL file."""
    samples: list[dict] = []
    with open(data_path) as f:
        if data_path.endswith(".jsonl"):
            for line in f:
                if line.strip():
                    samples.append(json.loads(line))
        else:
            data = json.load(f)
            samples = data if isinstance(data, list) else [data]
    for s in samples:
        s.setdefault("schema", ACE2005_SCHEMA)
    return samples


# ============================================================================
# Data Loading — CrossNER
# ============================================================================

def conll_to_spans(tokens: list[str], tags: list[str]) -> list[dict]:
    """Convert BIO-tagged token sequence to entity span dicts with char offsets."""
    entities: list[dict] = []
    current_type: str | None = None
    current_start: int = 0

    def _flush(end_idx: int) -> None:
        if current_type is None:
            return
        char_start = sum(len(tokens[j]) + 1 for j in range(current_start))
        char_end = sum(len(tokens[j]) + 1 for j in range(end_idx)) - 1
        text = " ".join(tokens[current_start:end_idx])
        entities.append({"type": current_type, "span": [char_start, char_end], "text": text})

    for i, (token, tag) in enumerate(zip(tokens, tags)):
        if tag.startswith("B-"):
            _flush(i)
            current_type = tag[2:]
            current_start = i
        elif tag.startswith("I-"):
            tag_type = tag[2:]
            if current_type != tag_type:
                _flush(i)
                current_type = tag_type
                current_start = i
        else:  # O
            _flush(i)
            current_type = None

    _flush(len(tokens))
    return entities


def load_crossner_conll(file_path: str, domain: str) -> list[dict]:
    """Load CrossNER data from a CoNLL-format file."""
    schema = CROSSNER_SCHEMAS.get(domain, {"entity_types": [], "relation_types": []})
    samples: list[dict] = []
    current_tokens: list[str] = []
    current_tags: list[str] = []

    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("-DOCSTART-"):
                if current_tokens:
                    text = " ".join(current_tokens)
                    entities = conll_to_spans(current_tokens, current_tags)
                    samples.append({
                        "text": text,
                        "schema": schema,
                        "gold": {"entities": entities, "relations": []},
                    })
                    current_tokens = []
                    current_tags = []
                continue
            parts = line.split()
            if len(parts) >= 2:
                current_tokens.append(parts[0])
                current_tags.append(parts[-1])

    if current_tokens:
        text = " ".join(current_tokens)
        entities = conll_to_spans(current_tokens, current_tags)
        samples.append({
            "text": text,
            "schema": schema,
            "gold": {"entities": entities, "relations": []},
        })
    return samples


def load_crossner(data_dir: str, domain: str, split: str = "test") -> list[dict]:
    """Load CrossNER dataset for a specific domain. Tries common file layouts."""
    candidates = [
        os.path.join(data_dir, domain, f"{split}.txt"),
        os.path.join(data_dir, f"{domain}_{split}.txt"),
        os.path.join(data_dir, domain, f"{split}.conll"),
        os.path.join(data_dir, f"{domain}_{split}.conll"),
    ]
    for path in candidates:
        if os.path.exists(path):
            return load_crossner_conll(path, domain)
    raise FileNotFoundError(f"CrossNER {domain}/{split} not found. Tried: {candidates}")


# ============================================================================
# Prompt Templates
# ============================================================================

def _get_entity_descriptions(schema_dict: dict) -> dict[str, str]:
    """Look up human-readable descriptions for entity types."""
    all_descs = {**ACE2005_ENTITY_DESCRIPTIONS, **SCIERC_ENTITY_DESCRIPTIONS, **CROSSNER_ENTITY_DESCRIPTIONS}
    return {t: all_descs.get(t, t) for t in schema_dict.get("entity_types", [])}


def format_ie_prompt(text: str, schema_dict: dict) -> str:
    """Build a complete IE prompt with embedded schema definition."""
    ent_descs = _get_entity_descriptions(schema_dict)
    rel_descs = {**ACE2005_RELATION_DESCRIPTIONS, **SCIERC_RELATION_DESCRIPTIONS}

    parts: list[str] = []

    # Entity types
    parts.append("## Entity Types")
    for etype in schema_dict["entity_types"]:
        desc = ent_descs.get(etype, etype)
        parts.append(f"- {etype}: {desc}")

    # Relation types (if any)
    if schema_dict.get("relation_types"):
        parts.append("\n## Relation Types")
        for rt in schema_dict["relation_types"]:
            name = rt["name"]
            desc = rel_descs.get(name, "")
            desc_str = f" — {desc}" if desc else ""
            parts.append(f"- {name}{desc_str}")
            parts.append(f"  - arg1 must be: {', '.join(rt['arg1_types'])}")
            parts.append(f"  - arg2 must be: {', '.join(rt['arg2_types'])}")

    schema_section = "\n".join(parts)

    # Build output format example based on whether relations exist
    if schema_dict.get("relation_types"):
        output_example = (
            '{"entities": [{"type": "<TYPE>", "text": "<exact span>"}], '
            '"relations": [{"type": "<TYPE>", "arg1": {"type": "<TYPE>", "text": "<span>"}, '
            '"arg2": {"type": "<TYPE>", "text": "<span>"}}]}'
        )
    else:
        output_example = '{"entities": [{"type": "<TYPE>", "text": "<exact span>"}], "relations": []}'

    return (
        f"You are an information extraction system. Extract entities and relations "
        f"from the given text according to the schema.\n\n"
        f"{schema_section}\n\n"
        f"## Input Text\n{text}\n\n"
        f"## Instructions\n"
        f"Output a JSON object: {output_example}\n"
        f"The \"text\" field must be the exact substring from the input. "
        f"If nothing matches the schema, return empty lists. "
        f"Output only the JSON object."
    )


def format_ie_prompt_chat(text: str, schema_dict: dict) -> list[dict]:
    """Format IE prompt as chat messages [system, user]."""
    ent_descs = _get_entity_descriptions(schema_dict)
    rel_descs = ACE2005_RELATION_DESCRIPTIONS

    # System message: role + schema + output format
    sys_parts: list[str] = [
        "You are an information extraction system. Extract entities and relations "
        "from text according to the provided schema.\n",
        "# Entity Types",
    ]
    for etype in schema_dict["entity_types"]:
        desc = ent_descs.get(etype, etype)
        sys_parts.append(f"- {etype}: {desc}")

    if schema_dict.get("relation_types"):
        sys_parts.append("\n# Relation Types")
        for rt in schema_dict["relation_types"]:
            name = rt["name"]
            desc = rel_descs.get(name, "")
            desc_str = f" — {desc}" if desc else ""
            sys_parts.append(f"- {name}{desc_str}")
            sys_parts.append(f"  - arg1 must be: {', '.join(rt['arg1_types'])}")
            sys_parts.append(f"  - arg2 must be: {', '.join(rt['arg2_types'])}")

    if schema_dict.get("relation_types"):
        output_fmt = (
            '{"entities": [{"type": "<TYPE>", "text": "<exact span>"}], '
            '"relations": [{"type": "<TYPE>", "arg1": {"type": "<TYPE>", "text": "<span>"}, '
            '"arg2": {"type": "<TYPE>", "text": "<span>"}}]}'
        )
    else:
        output_fmt = '{"entities": [{"type": "<TYPE>", "text": "<exact span>"}], "relations": []}'

    sys_parts.append(
        f"\n# Output Format\n"
        f"Return a JSON object: {output_fmt}\n"
        f"The \"text\" field must be the exact substring from the input. "
        f"If nothing matches, return empty lists. "
        f"Do not include any reasoning, explanation, or thinking process. "
        f"Output ONLY the raw JSON object, nothing else."
    )

    return [
        {"role": "system", "content": "\n".join(sys_parts)},
        {"role": "user", "content": f"Extract entities and relations from:\n\n{text} /no_think"},
    ]


# ============================================================================
# Dataset Class
# ============================================================================

class IEDataset:
    """Wrapper for IE samples with conversion to HuggingFace Dataset."""

    def __init__(self, samples: list[dict], schema: dict | None = None):
        self.samples = samples
        self.schema = schema or (samples[0]["schema"] if samples else {})

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> dict:
        return self.samples[idx]

    def to_grpo_dataset(self):
        """Convert to HuggingFace Dataset for GRPOTrainer.

        Columns: prompt (chat messages), schema (json str), gold (json str).
        """
        from datasets import Dataset as HFDataset

        prompts: list[list[dict]] = []
        schemas: list[str] = []
        golds: list[str] = []

        for sample in self.samples:
            prompts.append(format_ie_prompt_chat(sample["text"], sample["schema"]))
            schemas.append(json.dumps(sample["schema"]))
            golds.append(json.dumps(sample["gold"]))

        return HFDataset.from_dict({"prompt": prompts, "schema": schemas, "gold": golds})


def get_entity_type_descriptions(schema_dict: dict) -> dict[str, str]:
    """Return human-readable descriptions for entity types in the schema."""
    return _get_entity_descriptions(schema_dict)
