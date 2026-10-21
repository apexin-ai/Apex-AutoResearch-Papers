# diagnose evaluator ignf1 root bug

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_evaluator_ignf1_root_bug_20260516T035045_result.json`
- **Structured JSON:** [`159a60ea1ed950849873.json`](../../sessions/15/159a60ea1ed950849873.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结论

### 根因

**原始 bug**：Ign-F1 过滤使用了包含 `doc_id` 的 `train_triples`。由于 dev 集文档的 doc_id 与 train 集不同，`k not in self.train_triples` 永远为 True，**没有任何三元组被过滤**，导致 ign_f1 == f1。

recompute_ign_f1.py 的 `_note` 字段直接确认了这一点：`"Recomputed with fixed Ign-F1 (doc_id-free train_facts)"`

### 当前状态：已修复

`evaluator.py` 当前代码正确：

- **`from_train_file()`**（~L47-55）：构建了两个集合——`train_triples`（含 doc_id）和 `train_facts`（不含 doc_id，仅 `(head, tail, relation)`）
- **`compute_f1()`**（~L76-77）：Ign-F1 过滤使用 `k[1:] not in self.train_facts`，其中 `k[1:]` 去掉了 doc_id，与 `train_facts` 的格式匹配

`inference.py` 的 `evaluate()` 函数（L240-247）正确调用了 `DocREDEvaluator.from_train_file(train_path)`，且 `/root/autodl-tmp/data/docred/train_annotated.json` 存在。

### 当前 RUNNING 实验

**4 个 RUNNING 实验完成后会产出正确的 ign_f1**。evaluator.py 的根源 bug 已修复，不再需要 recompute_ign_f1.py 作为 workaround。

---
