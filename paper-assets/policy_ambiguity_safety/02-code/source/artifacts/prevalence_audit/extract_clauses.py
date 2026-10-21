#!/usr/bin/env python3
"""Phase 2: Extract operational clauses from raw policy documents."""

import json
import os
import re
from pathlib import Path

RAW_DIR = Path(__file__).parent / "raw_docs"
OUT_FILE = Path(__file__).parent / "clauses.jsonl"

COMPANY_MAP = {
    "delta": "Delta", "emirates": "Emirates", "frontier": "Frontier",
    "southwest": "Southwest", "target": "Target", "ikea": "IKEA",
    "nordstrom": "Nordstrom", "zappos": "Zappos", "apple": "Apple",
}


def parse_metadata(lines):
    """Extract metadata from header comments."""
    meta = {}
    for line in lines:
        line = line.strip()
        if not line.startswith("#"):
            break
        if "Type:" in line:
            meta["doc_type"] = line.split("Type:", 1)[1].strip()
        elif "Source:" in line:
            meta["source"] = line.split("Source:", 1)[1].strip()
    return meta


def extract_company_domain(filename):
    """Extract domain and company from filename like airline_delta_baggage_policy.txt."""
    parts = filename.replace(".txt", "").split("_")
    domain = parts[0]
    company_key = parts[1]
    return domain, COMPANY_MAP.get(company_key, company_key.title())


def split_into_clauses(text):
    """Split document text into operational clause candidates.

    An operational clause is any sentence or multi-sentence block that
    prescribes, constrains, or conditions a specific agent action or decision.
    """
    lines = text.split("\n")
    meta = parse_metadata(lines)

    # Skip metadata header lines
    content_lines = []
    past_header = False
    for line in lines:
        stripped = line.strip()
        if not past_header:
            if stripped.startswith("# ") and not stripped.startswith("# Source") and not stripped.startswith("# Date") and not stripped.startswith("# Fetched") and not stripped.startswith("# Type") and not stripped.startswith("# Policy"):
                past_header = True
                continue
            elif stripped and not stripped.startswith("#"):
                past_header = True
            else:
                continue
        content_lines.append(line)

    # Join and split into blocks by section headers or blank lines
    blocks = []
    current_section = ""
    current_block_lines = []

    for line in content_lines:
        stripped = line.strip()

        # Section header
        if stripped.startswith("##"):
            if current_block_lines:
                blocks.append((current_section, "\n".join(current_block_lines).strip()))
                current_block_lines = []
            current_section = stripped.lstrip("#").strip()
            continue

        # Blank line = block separator
        if not stripped:
            if current_block_lines:
                blocks.append((current_section, "\n".join(current_block_lines).strip()))
                current_block_lines = []
            continue

        current_block_lines.append(line)

    if current_block_lines:
        blocks.append((current_section, "\n".join(current_block_lines).strip()))

    # Process blocks into clauses
    clauses = []
    for section, block_text in blocks:
        if not block_text.strip():
            continue

        # Check if block contains multiple bullet points
        bullet_pattern = re.compile(r"^[\-\*\d]+[\.\)]\s", re.MULTILINE)
        bullets = bullet_pattern.split(block_text)

        if len(bullets) > 1:
            # Has bullet structure — split into individual items
            raw_items = re.split(r"\n(?=[\-\*]|\d+[\.\)])", block_text)
            for item in raw_items:
                item = item.strip()
                item = re.sub(r"^[\-\*\d]+[\.\)]\s*", "", item).strip()
                if item and len(item) > 15:
                    clauses.append({"section": section, "text": item})
        else:
            # Prose block — split into sentences if long, keep together if short
            sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", block_text)
            if len(sentences) <= 3:
                clauses.append({"section": section, "text": block_text})
            else:
                # Group into chunks of 1-2 sentences for manageable clauses
                for sent in sentences:
                    sent = sent.strip()
                    if sent and len(sent) > 15:
                        clauses.append({"section": section, "text": sent})

    # Filter: keep only operational clauses (prescribe/constrain/condition)
    operational = []
    for c in clauses:
        text_lower = c["text"].lower()
        # Skip pure definitions, titles, or very short fragments
        if len(c["text"]) < 20:
            continue
        # Skip lines that are just labels/titles
        if ":" in c["text"] and len(c["text"].split(":")[0]) < 40 and len(c["text"].split(":", 1)[1].strip()) == 0:
            continue
        operational.append(c)

    return operational, meta


def main():
    all_clauses = []
    doc_files = sorted(RAW_DIR.glob("*.txt"))

    for doc_path in doc_files:
        filename = doc_path.stem
        domain, company = extract_company_domain(doc_path.name)
        text = doc_path.read_text(encoding="utf-8")

        clauses, meta = split_into_clauses(text)
        doc_type = meta.get("doc_type", "Policy")

        for i, clause in enumerate(clauses, 1):
            clause_id = f"{filename}_{i:03d}"
            context = clause.get("section", "")
            record = {
                "doc_id": filename,
                "company": company,
                "domain": domain,
                "doc_type": doc_type,
                "clause_id": clause_id,
                "clause_text": clause["text"],
                "context_sentence": f"Section: {context}" if context else "",
            }
            all_clauses.append(record)

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        for record in all_clauses:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    # Summary
    docs = set(r["doc_id"] for r in all_clauses)
    companies = set(r["company"] for r in all_clauses)
    print(f"Extracted {len(all_clauses)} clauses from {len(docs)} documents ({len(companies)} companies)")
    for domain in ["airline", "retail"]:
        domain_clauses = [r for r in all_clauses if r["domain"] == domain]
        domain_docs = set(r["doc_id"] for r in domain_clauses)
        print(f"  {domain}: {len(domain_clauses)} clauses from {len(domain_docs)} docs")


if __name__ == "__main__":
    main()
