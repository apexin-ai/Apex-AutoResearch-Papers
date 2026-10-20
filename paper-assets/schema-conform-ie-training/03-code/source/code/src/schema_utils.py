# Schema parsing and validation for structured IE output.
# Parses schema definitions, validates model outputs, computes conformance metrics.
# No external dependencies (pure Python + json).

import json
import re
from dataclasses import dataclass, field
from typing import Any


@dataclass
class RelationType:
    name: str
    arg1_types: set[str] = field(default_factory=set)
    arg2_types: set[str] = field(default_factory=set)


@dataclass
class SchemaDefinition:
    entity_types: set[str] = field(default_factory=set)
    relation_types: dict[str, RelationType] = field(default_factory=dict)


def parse_schema(schema_dict: dict) -> SchemaDefinition:
    """Parse a raw schema dict into a SchemaDefinition."""
    entity_types = set(schema_dict.get("entity_types", []))
    relation_types = {}
    for rt in schema_dict.get("relation_types", []):
        name = rt["name"]
        relation_types[name] = RelationType(
            name=name,
            arg1_types=set(rt.get("arg1_types", [])),
            arg2_types=set(rt.get("arg2_types", [])),
        )
    return SchemaDefinition(entity_types=entity_types, relation_types=relation_types)


def _strip_thinking(text: str) -> str:
    """Remove <think>...</think> blocks (Qwen3 thinking mode)."""
    return re.sub(r"(<think>)?.*?</think>", "", text, flags=re.DOTALL).strip()


def _extract_json_object(text: str) -> str | None:
    """Extract the first top-level JSON object from text."""
    depth = 0
    start = None
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                return text[start : i + 1]
    return None


def parse_model_output(output_str: str) -> tuple[dict | None, str | None]:
    """Parse model output, handling <think> tags and extracting JSON."""
    cleaned = _strip_thinking(output_str)
    try:
        result = json.loads(cleaned)
        if isinstance(result, dict):
            return result, None
    except (json.JSONDecodeError, TypeError):
        pass
    snippet = _extract_json_object(cleaned)
    if snippet:
        try:
            result = json.loads(snippet)
            if isinstance(result, dict):
                return result, None
        except (json.JSONDecodeError, TypeError):
            pass
    return None, "No valid JSON object found"


def validate_output_structure(output_dict: dict) -> tuple[bool, list[str]]:
    """Check whether output dict has all required structural fields.

    Returns (is_valid, issues_list).
    """
    issues: list[str] = []

    if "entities" not in output_dict:
        issues.append("Missing 'entities' field")
    elif not isinstance(output_dict["entities"], list):
        issues.append("'entities' is not a list")
    else:
        for i, ent in enumerate(output_dict["entities"]):
            if not isinstance(ent, dict):
                issues.append(f"Entity {i} is not a dict")
                continue
            for key in ("type", "text"):
                if key not in ent:
                    issues.append(f"Entity {i} missing '{key}'")

    if "relations" not in output_dict:
        issues.append("Missing 'relations' field")
    elif not isinstance(output_dict["relations"], list):
        issues.append("'relations' is not a list")
    else:
        for i, rel in enumerate(output_dict["relations"]):
            if not isinstance(rel, dict):
                issues.append(f"Relation {i} is not a dict")
                continue
            for key in ("type", "arg1", "arg2"):
                if key not in rel:
                    issues.append(f"Relation {i} missing '{key}'")
            for arg_key in ("arg1", "arg2"):
                if arg_key in rel and isinstance(rel[arg_key], dict):
                    for key in ("type", "text"):
                        if key not in rel[arg_key]:
                            issues.append(f"Relation {i} {arg_key} missing '{key}'")

    return (len(issues) == 0), issues


def check_type_conformance(
    entities: list[dict], relations: list[dict], schema: SchemaDefinition
) -> float:
    """Proportion of extracted entity/relation types that exist in the schema."""
    total = 0
    conforming = 0

    for ent in entities:
        if isinstance(ent, dict) and "type" in ent:
            total += 1
            if ent["type"] in schema.entity_types:
                conforming += 1

    for rel in relations:
        if isinstance(rel, dict) and "type" in rel:
            total += 1
            if rel["type"] in schema.relation_types:
                conforming += 1

    return 0.0 if total == 0 else conforming / total


def check_relational_constraints(
    relations: list[dict], schema: SchemaDefinition
) -> float:
    """Proportion of relations where arg types satisfy schema type-pair constraints."""
    if not relations:
        return 0.0

    total = 0
    satisfying = 0

    for rel in relations:
        if not isinstance(rel, dict):
            continue
        rel_type = rel.get("type")
        arg1 = rel.get("arg1", {})
        arg2 = rel.get("arg2", {})
        if not isinstance(arg1, dict) or not isinstance(arg2, dict):
            total += 1
            continue

        total += 1
        if rel_type not in schema.relation_types:
            continue

        rt = schema.relation_types[rel_type]
        if arg1.get("type", "") in rt.arg1_types and arg2.get("type", "") in rt.arg2_types:
            satisfying += 1

    return 1.0 if total == 0 else satisfying / total


def check_structural_completeness(output_dict: dict) -> float:
    """Proportion of required structural checkpoints that are satisfied.

    Checkpoints: top-level entities/relations fields, per-entity type+text,
    per-relation type+arg1+arg2, per-arg type+text.
    """
    checks_total = 0
    checks_passed = 0

    # Top-level fields
    checks_total += 2
    has_entities = "entities" in output_dict and isinstance(output_dict["entities"], list)
    has_relations = "relations" in output_dict and isinstance(output_dict["relations"], list)
    if has_entities:
        checks_passed += 1
    if has_relations:
        checks_passed += 1

    # Empty lists = nothing extracted, penalize
    if has_entities and len(output_dict["entities"]) == 0 and has_relations and len(output_dict["relations"]) == 0:
        return 0.0

    # Entity sub-fields
    if has_entities:
        for ent in output_dict["entities"]:
            checks_total += 2  # type, text
            if isinstance(ent, dict):
                checks_passed += sum(1 for k in ("type", "text") if k in ent)

    # Relation sub-fields
    if has_relations:
        for rel in output_dict["relations"]:
            checks_total += 3  # type, arg1, arg2
            if isinstance(rel, dict):
                checks_passed += sum(1 for k in ("type", "arg1", "arg2") if k in rel)
                for arg_key in ("arg1", "arg2"):
                    arg = rel.get(arg_key)
                    if isinstance(arg, dict):
                        checks_total += 2  # type, text
                        checks_passed += sum(1 for k in ("type", "text") if k in arg)

    return 1.0 if checks_total == 0 else checks_passed / checks_total
