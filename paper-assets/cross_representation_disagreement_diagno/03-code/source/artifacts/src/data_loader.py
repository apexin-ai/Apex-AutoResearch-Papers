"""
FOLIO 数据集加载器。
从本地 JSONL 文件加载 validation set，输出 (id, premises, conclusion, label) 结构。
"""

import json
from dataclasses import dataclass, asdict
from typing import List, Optional
from pathlib import Path

from config import PROJECT_ROOT

_LABEL_NORM = {
    "true": "True",
    "false": "False",
    "unknown": "Unknown",
    "uncertain": "Unknown",
}

FOLIO_PATH = PROJECT_ROOT / "data" / "folio-validation.jsonl"


@dataclass
class FolioExample:
    id: str
    premises: str
    conclusion: str
    label: str           # "True" / "False" / "Unknown"

    def to_dict(self):
        return asdict(self)


def _normalize_label(raw) -> str:
    if isinstance(raw, int):
        return ["True", "False", "Unknown"][raw]
    return _LABEL_NORM.get(str(raw).strip().lower(), "Unknown")


def _normalize_premises(raw) -> str:
    if isinstance(raw, list):
        return " ".join(raw)
    return str(raw)


def load_folio(
    max_examples: Optional[int] = None,
) -> List[FolioExample]:
    with open(FOLIO_PATH) as f:
        rows = [json.loads(line) for line in f if line.strip()]

    examples = []
    for i, row in enumerate(rows):
        if max_examples and i >= max_examples:
            break

        examples.append(FolioExample(
            id=f"folio_validation_{i}",
            premises=_normalize_premises(row["premises"]),
            conclusion=row["conclusion"],
            label=_normalize_label(row["label"]),
        ))

    return examples
