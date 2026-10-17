"""MAVEN event detection data loading utilities.

Input: MAVEN parquet files (pre-processed by preprocess_maven.py)
       Each row: doc_id, sent_id, text, tokens, entities, negative_triggers
       entities: [{"text": trigger, "type": event_type, "start": int, "end": int}]
Output: List of {"text": str, "entities": [{...}]}
Dependencies: pandas
"""
import json
import logging
from typing import Dict, List, Optional, Set

import pandas as pd

logger = logging.getLogger(__name__)

DEFAULT_DATA_PATH = "./data/maven_parquet/valid.parquet"


def load_maven(
    data_path: str = DEFAULT_DATA_PATH,
    max_samples: Optional[int] = None,
) -> List[Dict]:
    """Load MAVEN event detection data from parquet.

    Args:
        data_path: Path to parquet file.
        max_samples: If set, only return first N samples.

    Returns:
        List of dicts with "text" and "entities" (span-level, same format as Few-NERD).
    """
    df = pd.read_parquet(data_path)
    if max_samples is not None:
        df = df.head(max_samples)

    samples = []
    for _, row in df.iterrows():
        entities = row["entities"]
        if isinstance(entities, str):
            entities = json.loads(entities)
        samples.append({"text": row["text"], "entities": list(entities) if len(entities) > 0 else []})

    logger.info("Loaded %d samples from MAVEN: %s", len(samples), data_path)
    return samples


def get_all_types(dataset: List[Dict]) -> List[str]:
    """Extract all unique event type names from dataset."""
    types = set()
    for sample in dataset:
        for ent in sample["entities"]:
            types.add(ent["type"])
    return sorted(types)


def filter_entities_by_types(entities: List[Dict], type_set: Set[str]) -> List[Dict]:
    return [e for e in entities if e["type"] in type_set]
