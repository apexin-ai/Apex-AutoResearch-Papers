# analyze test eval 8b rsft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_test_eval_8b_rsft_s42_20260521T145621_result.json`
- **Structured JSON:** [`d677b32198c4e5f01ddf.json`](../../sessions/d6/d677b32198c4e5f01ddf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Metrics

| Metric | Value |
|--------|-------|
| **F1 / Ign-F1** | **0.3353** |
| Precision | 0.5149 |
| Recall | 0.2486 |
| Evi-F1 (DREEAM) | 0.2526 |
| Evi-F1 (TP) | 0.6037 |
| EDCR | 0.7993 |
| format_ok | 499/500 (99.8%) |
| field_compliance | 74/500 (**14.8%**) |
| Truncated | 9/500 |

### Dev→Test Gap

- Dev ign_f1 = 0.5376 → Test F1 = 0.3353 → **gap = -20.2pp**

### 异常

1. **field_compliance_rate 仅 14.8%** — 85% 文档的 evidence 字段格式不合规。JSON 解析正常 (99.8%)，问题出在 evidence 字段的具体格式。这是 recall 极低 (0.2486) 的主因。

2. **train_annotated.json 缺失** — log 有 WARNING: `train_annotated.json not found, Ign-F1 = F1`。本地计算的 ign_f1 就是 f1，**非官方分数**。需要将 `codalab_submission.json` 提交 CodaLab 获取权威 test ign_f1。

3. **CodaLab submission 已生成** — 8049 triples converted，315 skipped (rel)，301 skipped (entity)。文件路径：`/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42/codalab_submission.json`。

### 已完成操作
- Registry: status→DONE, conclusion→success, metrics 和 checkpoint_path 已写入
- memory.md: 添加了 test eval 结果和异常分析
- Artifact: 已注册

---
