"""DocRED 数据预处理模块。

加载 DocRED 数据集（train_annotated / dev / test），解析实体、关系、
evidence 标注，构建含 hard negatives 的训练样本。

输入: DocRED JSON 文件目录或 HuggingFace dataset
输出: List[RelationSample]，每个样本包含 gold evidence 和 hard negative 句子
依赖: datasets (可选，用于 HF 加载)
"""

import json
import os
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

DOCRED_REL_INFO = {
    "P6": "head of government", "P17": "country", "P19": "place of birth",
    "P20": "place of death", "P22": "father", "P25": "mother",
    "P26": "spouse", "P27": "country of citizenship", "P30": "continent",
    "P31": "instance of", "P35": "head of state", "P36": "capital",
    "P37": "official language", "P39": "position held", "P40": "child",
    "P50": "author", "P54": "member of sports team", "P57": "director",
    "P58": "screenwriter", "P69": "educated at", "P86": "composer",
    "P102": "member of political party", "P108": "employer",
    "P112": "founded by", "P118": "league", "P123": "publisher",
    "P127": "owned by",
    "P131": "located in the administrative territorial entity",
    "P136": "genre", "P137": "operator", "P140": "religion",
    "P150": "contains administrative territorial entity",
    "P155": "follows", "P156": "followed by",
    "P159": "headquarters location", "P161": "cast member",
    "P162": "producer", "P166": "award received", "P170": "creator",
    "P171": "parent taxon", "P172": "ethnic group", "P175": "performer",
    "P176": "manufacturer", "P178": "developer", "P179": "series",
    "P190": "sister city", "P194": "legislative body",
    "P205": "basin country",
    "P206": "located in or next to body of water",
    "P241": "military branch", "P264": "record label",
    "P272": "production company", "P276": "location",
    "P279": "subclass of", "P355": "subsidiary", "P361": "part of",
    "P364": "original language of work", "P400": "platform",
    "P403": "mouth of the watercourse", "P449": "original network",
    "P463": "member of", "P488": "chairperson",
    "P495": "country of origin", "P527": "has part",
    "P551": "residence", "P569": "date of birth",
    "P570": "date of death", "P571": "inception",
    "P576": "dissolved, abolished or demolished",
    "P577": "publication date", "P580": "start time",
    "P582": "end time", "P585": "point in time", "P607": "conflict",
    "P674": "characters", "P676": "lyrics by",
    "P706": "located on terrain feature", "P710": "participant",
    "P737": "influenced by", "P740": "location of formation",
    "P749": "parent organization", "P800": "notable work",
    "P807": "separated from", "P840": "narrative location",
    "P937": "work location", "P1001": "applies to jurisdiction",
    "P1056": "product or material produced",
    "P1198": "unemployment rate", "P1336": "territory claimed by",
    "P1344": "participant of", "P1365": "replaces",
    "P1366": "replaced by", "P1376": "capital of",
    "P1412": "languages spoken, written or signed",
    "P1441": "present in work", "P3373": "sibling",
}

SPLIT_FILENAMES = {
    "train": "train_annotated.json",
    "train_annotated": "train_annotated.json",
    "train_distant": "train_distant.json",
    "dev": "dev.json",
    "test": "test.json",
    "train_revised": "train_revised.json",
    "dev_revised": "dev_revised.json",
    "test_revised": "test_revised.json",
}


@dataclass
class EntityMention:
    name: str
    sent_id: int
    pos: tuple[int, int]
    entity_type: str


@dataclass
class Entity:
    entity_id: int
    mentions: list[EntityMention]

    @property
    def name(self) -> str:
        return self.mentions[0].name

    @property
    def sent_ids(self) -> set[int]:
        return {m.sent_id for m in self.mentions}


@dataclass
class RelationSample:
    doc_id: str
    document: str
    sents: list[str]
    head: Entity
    tail: Entity
    relation: str
    relation_name: str
    evidence_sent_ids: list[int]
    hard_negative_sent_ids: list[int]


class DocREDProcessor:
    """DocRED 数据加载与预处理。"""

    def __init__(self, data_dir: Optional[str] = None):
        self.data_dir = Path(data_dir) if data_dir else None

    def load_split(self, split: str) -> list[dict]:
        if self.data_dir is not None:
            fname = SPLIT_FILENAMES.get(split, f"{split}.json")
            path = self.data_dir / fname
            if not path.exists():
                raise FileNotFoundError(f"DocRED file not found: {path}")
            with open(path) as f:
                data = json.load(f)
            logger.info("Loaded %d documents from %s", len(data), path)
            return data

        if os.environ.get("HF_HUB_OFFLINE") == "1" or os.environ.get("TRANSFORMERS_OFFLINE") == "1":
            raise ValueError(
                "data_dir must be provided in offline mode. "
                "Pass --data_dir pointing to a directory with DocRED JSON files."
            )
        from datasets import load_dataset
        ds = load_dataset("thunlp/docred", split=split, trust_remote_code=True)
        data = [row for row in ds]
        logger.info("Loaded %d documents from HuggingFace (split=%s)", len(data), split)
        return data

    def _tokens_to_text(self, tokens: list[str]) -> str:
        if not tokens:
            return ""
        result = tokens[0]
        no_space_before = {".", ",", "!", "?", ";", ":", "'", ")", "]", "}",
                           "'s", "'t", "'re", "'ve", "'ll", "'d", "'m", "n't"}
        for tok in tokens[1:]:
            if tok in no_space_before or tok.startswith("'"):
                result += tok
            else:
                result += " " + tok
        return result

    def _parse_document(self, doc: dict) -> tuple[str, list[str], list[Entity]]:
        sents_tokens = doc["sents"]
        sents = [self._tokens_to_text(s) for s in sents_tokens]
        document = " ".join(sents)

        entities = []
        for eidx, entity_mentions in enumerate(doc["vertexSet"]):
            mentions = []
            for m in entity_mentions:
                mentions.append(EntityMention(
                    name=m["name"],
                    sent_id=m["sent_id"],
                    pos=(m["pos"][0], m["pos"][1]),
                    entity_type=m.get("type", "UNK"),
                ))
            entities.append(Entity(entity_id=eidx, mentions=mentions))

        return document, sents, entities

    def _find_hard_negatives(
        self, head: Entity, tail: Entity, evidence: list[int], n_sents: int
    ) -> list[int]:
        evidence_set = set(evidence)
        head_sents = head.sent_ids
        tail_sents = tail.sent_ids
        cooccur = (head_sents & tail_sents) - evidence_set
        if cooccur:
            return sorted(cooccur)
        single_entity = (head_sents | tail_sents) - evidence_set
        return sorted(single_entity)

    def process(self, split: str) -> list[RelationSample]:
        raw_docs = self.load_split(split)
        samples = []
        n_no_hard_neg = 0

        for doc in raw_docs:
            doc_id = doc.get("title", "")
            document, sents, entities = self._parse_document(doc)

            labels = doc.get("labels", [])
            for label in labels:
                h_idx, t_idx = label["h"], label["t"]
                relation = label["r"]
                evidence = label.get("evidence", [])

                head = entities[h_idx]
                tail = entities[t_idx]
                hard_negs = self._find_hard_negatives(
                    head, tail, evidence, len(sents)
                )
                if not hard_negs:
                    n_no_hard_neg += 1

                samples.append(RelationSample(
                    doc_id=doc_id,
                    document=document,
                    sents=sents,
                    head=head,
                    tail=tail,
                    relation=relation,
                    relation_name=DOCRED_REL_INFO.get(relation, relation),
                    evidence_sent_ids=evidence,
                    hard_negative_sent_ids=hard_negs,
                ))

        logger.info(
            "Processed %d relation samples from %d documents "
            "(%d samples without hard negatives)",
            len(samples), len(raw_docs), n_no_hard_neg,
        )
        return samples

    def group_by_document(
        self, samples: list[RelationSample]
    ) -> dict[str, list[RelationSample]]:
        groups: dict[str, list[RelationSample]] = {}
        for s in samples:
            groups.setdefault(s.doc_id, []).append(s)
        return groups

    def format_sft_sample(
        self, doc_samples: list[RelationSample], include_evidence: bool = True
    ) -> dict[str, str]:
        if not doc_samples:
            return {"instruction": "", "input": "", "output": ""}

        ref = doc_samples[0]
        numbered_sents = "\n".join(
            f"[{i}] {s}" for i, s in enumerate(ref.sents)
        )

        entity_list = set()
        for s in doc_samples:
            entity_list.add(f"{s.head.name} ({s.head.mentions[0].entity_type})")
            entity_list.add(f"{s.tail.name} ({s.tail.mentions[0].entity_type})")
        entity_str = ", ".join(sorted(entity_list))

        if include_evidence:
            instruction = (
                "Extract all relation triples from the document. "
                "For each triple, provide the head entity, relation, tail entity, "
                "and the sentence IDs that serve as evidence. "
                "Output as a JSON list."
            )
        else:
            instruction = (
                "Extract all relation triples from the document. "
                "For each triple, provide the head entity, relation, and tail entity. "
                "Output as a JSON list."
            )

        input_text = (
            f"Document:\n{numbered_sents}\n\n"
            f"Entities: {entity_str}"
        )

        triples = []
        for s in doc_samples:
            triple = {
                "head": s.head.name,
                "relation": s.relation_name,
                "tail": s.tail.name,
            }
            if include_evidence:
                triple["evidence"] = s.evidence_sent_ids
            triples.append(triple)
        output_text = json.dumps(triples, ensure_ascii=False)

        return {
            "instruction": instruction,
            "input": input_text,
            "output": output_text,
        }


def download_docred(output_dir: str) -> Path:
    from datasets import load_dataset

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    ds = load_dataset("thunlp/docred", trust_remote_code=True)
    for split_name, split_ds in ds.items():
        fname = SPLIT_FILENAMES.get(split_name, f"{split_name}.json")
        path = out / fname
        data = [row for row in split_ds]
        with open(path, "w") as f:
            json.dump(data, f, ensure_ascii=False)
        logger.info("Saved %d documents to %s", len(data), path)

    return out


if __name__ == "__main__":
    import argparse
    import sys

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    parser = argparse.ArgumentParser(description="DocRED 数据预处理")
    parser.add_argument("--data_dir", type=str, default=None)
    parser.add_argument("--split", type=str, default="dev")
    parser.add_argument("--output", type=str, default=None)
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()

    if args.download:
        if not args.data_dir:
            print("--download requires --data_dir", file=sys.stderr)
            sys.exit(1)
        download_docred(args.data_dir)
        sys.exit(0)

    processor = DocREDProcessor(data_dir=args.data_dir)
    samples = processor.process(args.split)

    print(f"Total samples: {len(samples)}")
    has_hard_neg = sum(1 for s in samples if s.hard_negative_sent_ids)
    print(f"Samples with hard negatives: {has_hard_neg} "
          f"({has_hard_neg / len(samples) * 100:.1f}%)")

    if samples:
        s = samples[0]
        print(f"\nExample: {s.head.name} --[{s.relation_name}]--> {s.tail.name}")
        print(f"  Evidence sents: {s.evidence_sent_ids}")
        print(f"  Hard negatives: {s.hard_negative_sent_ids}")

    if args.output:
        out_data = []
        for s in samples:
            out_data.append({
                "doc_id": s.doc_id,
                "head": s.head.name,
                "tail": s.tail.name,
                "relation": s.relation,
                "relation_name": s.relation_name,
                "evidence_sent_ids": s.evidence_sent_ids,
                "hard_negative_sent_ids": s.hard_negative_sent_ids,
            })
        with open(args.output, "w") as f:
            json.dump(out_data, f, ensure_ascii=False, indent=2)
        print(f"Saved to {args.output}")
