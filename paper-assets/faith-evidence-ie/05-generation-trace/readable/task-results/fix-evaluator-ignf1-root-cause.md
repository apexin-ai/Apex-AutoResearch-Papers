# fix evaluator ignf1 root cause

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_evaluator_ignf1_root_cause_20260516T034949_result.json`
- **Structured JSON:** [`52bbae74a78c91199641.json`](../../sessions/52/52bbae74a78c91199641.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析结论：

**当前 evaluator.py 已经是修复后的版本**（07:53 修改）。我的端到端验证确认 `from_train_file` 加载 34610 个 train_facts，`compute_f1` 产出 ign_f1=0.4435 != f1=0.4523。

**旧版 bug**：old `from_train_file` 只构建了 `train_triples` 而没有 `train_facts`，且 return 时没传 `train_facts` 参数（日志证据：旧 eval 输出 "Loaded 37785 training triples for Ign-F1" 而非 "(34610 unique facts)"）。

**运行中 eval 状态**：
- `eval_rsft_ced_s45` (09:30 启动) — 在 07:53 修复之后，新代码 ✓
- `eval_plan_014_no_evidence_r2` (10:27 启动) — 新代码 ✓
- `reeval_flat_nli_s43_r2` (11:05 启动) — 新代码 ✓
- `mvp2_eval_rsft_s43_r2` (May 15 启动) — **旧代码**，完成后需 recompute

不过你的验证步骤 `DocREDEvaluator('/root/autodl-tmp/data/docred')` 是错的 — 这把路径字符串传给了 `train_triples` 参数，不会加载数据。应该用 `DocREDEvaluator.from_train_file(...)` 或者我改一下 `__init__` 让它支持接收 `data_dir`。

要不要我给 `__init__` 加一个 `data_dir` 参数支持，让 `DocREDEvaluator('/root/autodl-tmp/data/docred')` 也能正确加载 train_facts？这样以后不容易误用。

---
