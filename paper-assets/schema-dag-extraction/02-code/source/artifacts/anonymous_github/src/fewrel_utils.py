"""FewRel relation extraction data loading utilities.

Input: FewRel parquet files (pre-processed by preprocess_fewrel.py)
       Each row: text, head_entity, head_pos, tail_entity, tail_pos, relation_type, relation_pid
Output: List of {"text": str, "head_entity": str, "tail_entity": str, "relation_type": str, ...}
Dependencies: pandas
"""
import json
import logging
import random
from typing import Dict, List, Optional, Set

import pandas as pd

logger = logging.getLogger(__name__)

DEFAULT_DATA_PATH = "./data/fewrel_parquet/val.parquet"


def load_fewrel(
    data_path: str = DEFAULT_DATA_PATH,
    max_samples: Optional[int] = None,
    relation_filter: Optional[List[str]] = None,
) -> List[Dict]:
    """Load FewRel RE data from parquet.

    Args:
        data_path: Path to parquet file.
        max_samples: If set, only return first N samples.
        relation_filter: If set, only keep samples with these relation types.

    Returns:
        List of dicts with: text, head_entity, tail_entity, relation_type, relation_pid
    """
    df = pd.read_parquet(data_path)
    if relation_filter:
        df = df[df["relation_type"].isin(relation_filter)]
    if max_samples is not None:
        df = df.head(max_samples)

    samples = []
    for _, row in df.iterrows():
        samples.append({
            "text": row["text"],
            "head_entity": row["head_entity"],
            "tail_entity": row["tail_entity"],
            "relation_type": row["relation_type"],
            "relation_pid": row["relation_pid"],
        })

    logger.info("Loaded %d FewRel samples from %s (%d unique relations)",
                len(samples), data_path, df["relation_type"].nunique())
    return samples


def get_all_relation_types(dataset: List[Dict]) -> List[str]:
    """Extract all unique relation type names from dataset."""
    return sorted(set(s["relation_type"] for s in dataset))


def sample_balanced(
    dataset: List[Dict],
    n_per_relation: int,
    relations: Optional[List[str]] = None,
    seed: int = 42,
) -> List[Dict]:
    """Sample n_per_relation samples per relation type (balanced)."""
    rng = random.Random(seed)

    by_rel: Dict[str, List[Dict]] = {}
    for s in dataset:
        by_rel.setdefault(s["relation_type"], []).append(s)

    if relations is None:
        relations = sorted(by_rel.keys())

    sampled = []
    for rel in relations:
        pool = by_rel.get(rel, [])
        k = min(n_per_relation, len(pool))
        sampled.extend(rng.sample(pool, k))

    return sampled


def filter_samples_by_relations(
    samples: List[Dict], relation_set: Set[str]
) -> List[Dict]:
    """Keep only samples whose relation_type is in relation_set."""
    return [s for s in samples if s["relation_type"] in relation_set]
