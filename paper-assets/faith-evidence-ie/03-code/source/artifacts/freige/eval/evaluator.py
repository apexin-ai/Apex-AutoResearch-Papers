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
    return (doc_id, head.lower().strip(), tail.lower().strip(), relation)


class DocREDEvaluator:
    """DocRED 评测器。

    Args:
        train_triples: 训练集中的三元组集合，用于计算 Ign-F1。
                       每个元素为 (doc_title, head_name, tail_name, relation)。
                       为 None 时 Ign-F1 = F1。
    """

    def __init__(self, train_triples: Optional[set[tuple]] = None):
        self.train_triples = train_triples or set()

    @classmethod
    def from_train_file(cls, train_path: str) -> "DocREDEvaluator":
        """从训练集 JSON 文件构建 evaluator，自动提取训练集三元组。"""
        from freige.data.docred_processor import DOCRED_REL_INFO

        with open(train_path) as f:
            train_data = json.load(f)

        train_triples = set()
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

        logger.info("Loaded %d training triples for Ign-F1", len(train_triples))
        return cls(train_triples=train_triples)

    def compute_f1(
        self,
        predictions: list[dict],
        gold: list[dict],
    ) -> dict:
        """计算 F1 和 Ign-F1。

        Args:
            predictions: [{"doc_id": str, "head": str, "tail": str,
                           "relation": str, ...}, ...]
            gold: 同上格式

        Returns:
            {"precision", "recall", "f1", "ign_precision", "ign_recall", "ign_f1"}
        """
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

        pred_ign = pred_set - self.train_triples
        gold_ign = gold_set - self.train_triples
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
        """计算 Evidence F1（句子级）。

        仅对正确预测的三元组计算 evidence 匹配。

        Args:
            predictions: [{"doc_id", "head", "tail", "relation",
                           "evidence": [int, ...]}, ...]
            gold: 同上格式

        Returns:
            {"evi_precision", "evi_recall", "evi_f1", "n_evaluated"}
        """
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

    def compute_edcr(
        self,
        predictions: list[dict],
        gold: list[dict],
    ) -> dict:
        """计算 EDCR（Evidence Distractor Citation Rate）。

        对所有预测的三元组（不限于正确预测），统计其 evidence 中
        不在 gold evidence 集合里的句子占比。

        EDCR = |pred_evi - gold_evi| / |pred_evi|，越低越好。

        Args:
            predictions: [{"doc_id", "head", "tail", "relation",
                           "evidence": [int, ...]}, ...]
            gold: 同上格式

        Returns:
            {"edcr", "n_distractor_citations", "n_total_citations", "n_evaluated"}
        """
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
        """计算模型输出的格式合规率。

        Args:
            raw_outputs: [{"doc_id": str, "raw_text": str}, ...]

        Returns:
            dict with format_compliance_rate, field_compliance_rate,
            evidence_format_rate, and counts.
        """
        required_fields = {"head", "relation", "tail", "evidence"}
        n_total = len(raw_outputs)
        n_parseable = 0
        n_field_complete = 0
        n_evidence_valid = 0

        for item in raw_outputs:
            doc_id = item.get("doc_id", "")
            raw_text = item.get("raw_text", "")

            parsed = parse_model_output(doc_id, raw_text)
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
        if raw_outputs is not None:
            result.update(self.compute_format_compliance(raw_outputs))
        return result


def parse_model_output(doc_id: str, output_text: str) -> list[dict]:
    """解析模型输出的 JSON 文本为标准预测格式。

    模型输出格式:
    [{"head": "...", "relation": "...", "tail": "...", "evidence": [0, 3]}, ...]

    Returns:
        标准预测列表，每个元素包含 doc_id
    """
    try:
        triples = json.loads(output_text)
    except json.JSONDecodeError:
        start = output_text.find("[")
        end = output_text.rfind("]") + 1
        if start >= 0 and end > start:
            try:
                triples = json.loads(output_text[start:end])
            except json.JSONDecodeError:
                logger.warning("Failed to parse output for doc %s", doc_id)
                return []
        else:
            return []

    results = []
    for t in triples:
        if not isinstance(t, dict):
            continue
        if "head" not in t or "tail" not in t or "relation" not in t:
            continue
        results.append({
            "doc_id": doc_id,
            "head": str(t["head"]),
            "tail": str(t["tail"]),
            "relation": str(t["relation"]),
            "evidence": t.get("evidence", []),
        })
    return results


def gold_from_docred(
    docred_data: list[dict],
) -> list[dict]:
    """将 DocRED 原始数据转为评测用 gold 格式。

    将 Wikidata property ID (如 "P17") 映射为 relation name (如 "country")，
    与模型训练输出格式对齐。
    """
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
