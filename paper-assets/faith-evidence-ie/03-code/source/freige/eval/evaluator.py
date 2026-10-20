"""DocRED 关系抽取评测模块。

指标:
  - F1 / Ign-F1: 关系三元组级别 micro-F1，Ign-F1 排除训练集中出现的三元组
  - Evi-F1: 对正确预测的三元组，计算 evidence 句子级 F1
  - EDCR: Evidence Distractor Citation Rate，预测 evidence 中非 gold 的比例

输入: 预测列表 + gold 标注列表（每个元素为文档级标注）
输出: 指标字典
"""

import json
import logging
from collections import defaultdict
from typing import Optional

logger = logging.getLogger(__name__)


def _triple_key(doc_id: str, head: str, tail: str, relation: str) -> tuple:
    return (doc_id, head.lower().strip(), tail.lower().strip(), relation.lower().strip())


class DocREDEvaluator:
    """DocRED 评测器。

    Args:
        train_triples: 训练集中的三元组集合，用于计算 Ign-F1。
                       每个元素为 (doc_title, head_name, tail_name, relation)。
                       为 None 时 Ign-F1 = F1。
    """

    def __init__(self, train_triples: Optional[set[tuple]] = None, train_facts: Optional[set[tuple]] = None):
        self.train_triples = train_triples or set()
        self.train_facts = train_facts or set()

    @classmethod
    def from_train_file(cls, train_path: str) -> "DocREDEvaluator":
        """从训练集 JSON 文件构建 evaluator，自动提取训练集三元组。"""
        from freige.data.docred_processor import DOCRED_REL_INFO

        with open(train_path) as f:
            train_data = json.load(f)

        train_triples = set()
        train_facts = set()
        for doc in train_data:
            doc_id = doc.get("title", "")
            vertex_set = doc["vertexSet"]
            for label in doc.get("labels", []):
                h_name = vertex_set[label["h"]][0]["name"]
                t_name = vertex_set[label["t"]][0]["name"]
                rel_name = DOCRED_REL_INFO.get(label["r"], label["r"])
                train_triples.add(
                    _triple_key(doc_id, h_name, t_name, rel_name)
                )
                train_facts.add((h_name.lower().strip(), t_name.lower().strip(), rel_name.lower().strip()))

        logger.info("Loaded %d training triples (%d unique facts) for Ign-F1", len(train_triples), len(train_facts))
        return cls(train_triples=train_triples, train_facts=train_facts)

    def compute_f1(
        self,
        predictions: list[dict],
        gold: list[dict],
    ) -> dict:
        """计算 F1 和 Ign-F1。"""
        pred_set = set()
        for p in predictions:
            pred_set.add(_triple_key(
                p["doc_id"], p["head"], p["tail"], p["relation"]
            ))

        gold_set = set()
        for g in gold:
            gold_set.add(_triple_key(
                g["doc_id"], g["head"], g["tail"], g["relation"]
            ))

        tp = pred_set & gold_set
        precision = len(tp) / len(pred_set) if pred_set else 0.0
        recall = len(tp) / len(gold_set) if gold_set else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

        pred_ign = {k for k in pred_set if k[1:] not in self.train_facts}
        gold_ign = {k for k in gold_set if k[1:] not in self.train_facts}
        tp_ign = pred_ign & gold_ign
        ign_prec = len(tp_ign) / len(pred_ign) if pred_ign else 0.0
        ign_rec = len(tp_ign) / len(gold_ign) if gold_ign else 0.0
        ign_f1 = (
            2 * ign_prec * ign_rec / (ign_prec + ign_rec)
            if (ign_prec + ign_rec) > 0 else 0.0
        )

        return {
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "ign_precision": ign_prec,
            "ign_recall": ign_rec,
            "ign_f1": ign_f1,
            "tp": len(tp),
            "pred_count": len(pred_set),
            "gold_count": len(gold_set),
        }

    def compute_evi_f1(
        self,
        predictions: list[dict],
        gold: list[dict],
    ) -> dict:
        """计算 Evidence F1（句子级）。"""
        gold_map = {}
        for g in gold:
            key = _triple_key(g["doc_id"], g["head"], g["tail"], g["relation"])
            gold_map.setdefault(key, set()).update(g.get("evidence", []))

        total_tp = 0
        total_pred = 0
        total_gold = 0
        n_evaluated = 0

        for p in predictions:
            key = _triple_key(p["doc_id"], p["head"], p["tail"], p["relation"])
            if key not in gold_map:
                continue

            pred_evi = set(p.get("evidence", []))
            gold_evi = gold_map[key]

            tp = len(pred_evi & gold_evi)
            total_tp += tp
            total_pred += len(pred_evi)
            total_gold += len(gold_evi)
            n_evaluated += 1

        evi_prec = total_tp / total_pred if total_pred else 0.0
        evi_rec = total_tp / total_gold if total_gold else 0.0
        evi_f1 = (
            2 * evi_prec * evi_rec / (evi_prec + evi_rec)
            if (evi_prec + evi_rec) > 0 else 0.0
        )

        return {
            "evi_precision": evi_prec,
            "evi_recall": evi_rec,
            "evi_f1": evi_f1,
            "n_evaluated": n_evaluated,
        }


    def compute_evi_f1_joint(
        self,
        predictions: list[dict],
        gold: list[dict],
    ) -> dict:
        """Evidence F1 (joint) — DREEAM 协议对齐版本。

        与 compute_evi_f1 的区别：FP triple 的 evidence 计入 precision 分母，
        FN triple 的 evidence 计入 recall 分母，而非仅在 TP triple 上计算。
        """
        gold_map = {}
        for g in gold:
            key = _triple_key(g["doc_id"], g["head"], g["tail"], g["relation"])
            gold_map.setdefault(key, set()).update(g.get("evidence", []))

        pred_map = {}
        for p in predictions:
            key = _triple_key(p["doc_id"], p["head"], p["tail"], p["relation"])
            pred_map.setdefault(key, set()).update(p.get("evidence", []))

        evi_tp = 0
        evi_pred_total = 0

        for key, pred_evi in pred_map.items():
            evi_pred_total += len(pred_evi)
            if key in gold_map:
                evi_tp += len(pred_evi & gold_map[key])

        evi_gold_total = sum(len(evi) for evi in gold_map.values())

        evi_prec = evi_tp / evi_pred_total if evi_pred_total else 0.0
        evi_rec = evi_tp / evi_gold_total if evi_gold_total else 0.0
        evi_f1 = (
            2 * evi_prec * evi_rec / (evi_prec + evi_rec)
            if (evi_prec + evi_rec) > 0 else 0.0
        )

        return {
            "evi_joint_precision": evi_prec,
            "evi_joint_recall": evi_rec,
            "evi_f1_joint": evi_f1,
            "evi_tp": evi_tp,
            "evi_pred_total": evi_pred_total,
            "evi_gold_total": evi_gold_total,
        }

    def compute_edcr(
        self,
        predictions: list[dict],
        gold: list[dict],
    ) -> dict:
        """计算 EDCR（Evidence Distractor Citation Rate）。"""
        gold_map = {}
        for g in gold:
            key = _triple_key(g["doc_id"], g["head"], g["tail"], g["relation"])
            gold_map.setdefault(key, set()).update(g.get("evidence", []))

        n_distractor = 0
        n_total = 0
        n_evaluated = 0

        for p in predictions:
            pred_evi = set(p.get("evidence", []))
            if not pred_evi:
                continue

            key = _triple_key(p["doc_id"], p["head"], p["tail"], p["relation"])
            gold_evi = gold_map.get(key, set())

            distractors = pred_evi - gold_evi
            n_distractor += len(distractors)
            n_total += len(pred_evi)
            n_evaluated += 1

        edcr = n_distractor / n_total if n_total else 0.0

        return {
            "edcr": edcr,
            "n_distractor_citations": n_distractor,
            "n_total_citations": n_total,
            "n_evaluated": n_evaluated,
        }

    def compute_format_compliance(self, raw_outputs: list[dict]) -> dict:
        """计算模型输出的格式合规率。"""
        required_fields = {"head", "relation", "tail", "evidence"}
        n_total = len(raw_outputs)
        n_parseable = 0
        n_field_complete = 0
        n_evidence_valid = 0

        for item in raw_outputs:
            doc_id = item.get("doc_id", "")
            raw_text = item.get("raw_text", "")

            parsed, _ = parse_model_output(raw_text)
            if not parsed and not self._is_parseable_json_list(raw_text):
                continue
            n_parseable += 1

            triples = self._parse_raw_json_list(raw_text)
            if triples is None:
                start = raw_text.find("[")
                if start >= 0:
                    triples = _repair_truncated_json(raw_text[start:])
                    if triples and isinstance(triples[-1], dict) and not required_fields.issubset(triples[-1].keys()):
                        triples = triples[:-1] or None
            if triples is None:
                continue

            all_fields_ok = True
            all_evidence_ok = True
            for t in triples:
                if not isinstance(t, dict) or not required_fields.issubset(t.keys()):
                    all_fields_ok = False
                    all_evidence_ok = False
                    break
                evi = t.get("evidence")
                if not isinstance(evi, list) or not all(
                    isinstance(e, int) and e >= 0 for e in evi
                ):
                    all_evidence_ok = False

            if all_fields_ok:
                n_field_complete += 1
            if all_fields_ok and all_evidence_ok:
                n_evidence_valid += 1

        return {
            "format_compliance_rate": n_parseable / n_total if n_total else 0.0,
            "field_compliance_rate": n_field_complete / n_total if n_total else 0.0,
            "evidence_format_rate": n_evidence_valid / n_total if n_total else 0.0,
            "n_total": n_total,
            "n_parseable": n_parseable,
            "n_field_complete": n_field_complete,
            "n_evidence_valid": n_evidence_valid,
        }

    @staticmethod
    def _is_parseable_json_list(text: str) -> bool:
        try:
            obj = json.loads(text)
            return isinstance(obj, list)
        except json.JSONDecodeError:
            start = text.find("[")
            end = text.rfind("]") + 1
            if start >= 0 and end > start:
                try:
                    obj = json.loads(text[start:end])
                    return isinstance(obj, list)
                except json.JSONDecodeError:
                    return False
            return False

    @staticmethod
    def _parse_raw_json_list(text: str) -> Optional[list]:
        try:
            obj = json.loads(text)
            if isinstance(obj, list):
                return obj
        except json.JSONDecodeError:
            start = text.find("[")
            end = text.rfind("]") + 1
            if start >= 0 and end > start:
                try:
                    obj = json.loads(text[start:end])
                    if isinstance(obj, list):
                        return obj
                except json.JSONDecodeError:
                    pass
        return None

    def evaluate(
        self,
        predictions: list[dict],
        gold: list[dict],
        raw_outputs: Optional[list[dict]] = None,
    ) -> dict:
        """运行所有评测指标。"""
        f1_metrics = self.compute_f1(predictions, gold)
        evi_metrics = self.compute_evi_f1(predictions, gold)
        edcr_metrics = self.compute_edcr(predictions, gold)
        result = {**f1_metrics, **evi_metrics, **edcr_metrics}
        result.update(self.compute_evi_f1_joint(predictions, gold))
        if raw_outputs is not None:
            result.update(self.compute_format_compliance(raw_outputs))
        return result




def _try_parse_json_list(text):
    try:
        obj = json.loads(text)
        if isinstance(obj, list):
            return obj
    except json.JSONDecodeError:
        pass
    return None


def _repair_truncated_json(text):
    stripped = text.rstrip().rstrip(",")
    for suffix in ["]", "}]", '"' + '}' + ']', "null}]"]:
        result = _try_parse_json_list(stripped + suffix)
        if result is not None:
            return result

    last_brace = text.rfind("}")
    if last_brace > 0:
        result = _try_parse_json_list(text[: last_brace + 1] + "]")
        if result is not None:
            return result

    return None


def _get_field(d, *keys):
    for k in keys:
        if k in d:
            return d[k]
    return None


def _normalize_triples(triples):
    results = []
    for t in triples:
        if not isinstance(t, dict):
            continue
        head = _get_field(t, "head", "head_entity")
        tail = _get_field(t, "tail", "tail_entity")
        relation = _get_field(t, "relation", "type", "label")
        if head is None or tail is None or relation is None:
            continue
        evidence = _get_field(t, "evidence", "sentence_ids") or []
        results.append({
            "head": str(head),
            "relation": str(relation).lower().strip(),
            "tail": str(tail),
            "evidence": evidence,
        })
    return results


def parse_model_output(output_text: str) -> tuple[list[dict], bool]:
    text = output_text.strip()

    parsed = _try_parse_json_list(text)
    if parsed is not None:
        return _normalize_triples(parsed), True

    start = text.find("[")
    if start >= 0:
        end = text.rfind("]")
        if end > start:
            parsed = _try_parse_json_list(text[start : end + 1])
            if parsed is not None:
                return _normalize_triples(parsed), True

        repaired = _repair_truncated_json(text[start:])
        if repaired is not None:
            return _normalize_triples(repaired), True

    return [], False

def gold_from_docred(
    docred_data: list[dict],
) -> list[dict]:
    """将 DocRED 原始数据转为评测用 gold 格式。"""
    from freige.data.docred_processor import DOCRED_REL_INFO

    gold = []
    for doc in docred_data:
        doc_id = doc.get("title", "")
        vertex_set = doc["vertexSet"]
        for label in doc.get("labels", []):
            h_name = vertex_set[label["h"]][0]["name"]
            t_name = vertex_set[label["t"]][0]["name"]
            gold.append({
                "doc_id": doc_id,
                "head": h_name,
                "tail": t_name,
                "relation": DOCRED_REL_INFO.get(label["r"], label["r"]),
                "evidence": label.get("evidence", []),
            })
    return gold
