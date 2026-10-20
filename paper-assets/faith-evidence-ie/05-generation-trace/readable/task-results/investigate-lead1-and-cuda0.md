# investigate lead1 and cuda0

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_lead1_and_cuda0_20260517T125405_result.json`
- **Structured JSON:** [`f41d8e7d7493fbb8e82c.json`](../../sessions/f4/f41d8e7d7493fbb8e82c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Part 1: lead1_ced_evidence_filter — 已完成，结论 negative

PID 441954 已退出。输出目录 `/root/autodl-tmp/lead1_ced_filter_results/` 有完整结果。

**关键指标对比：**

| 指标 | Baseline | tau=0.3 | tau=0.5 | tau=0.7 |
|------|----------|---------|---------|---------|
| Evi Precision | 0.802 | 0.902 | 0.904 | 0.908 |
| Evi Recall | 0.810 | 0.613 | 0.612 | 0.608 |
| **Evi F1** | **0.806** | 0.730 | 0.730 | 0.729 |
| EDCR | 0.654 | 0.580 | 0.578 | 0.578 |
| Joint Evi F1 | 0.361 | 0.335 | 0.334 | 0.334 |
| RE F1 | 0.460 | 0.460 | 0.460 | 0.460 |

**结论：** NLI filter 提升 precision (+10pt) 但 recall 损失过大 (-20pt)，所有 tau 下 evi_f1、EDCR、joint_f1 均劣于 baseline。D090 判断正确。Registry 已更新为 DONE/negative。

---

### Part 2: CodaLab test 提交文件 — 已就绪

两个模型的 test predictions 均已生成且包含 `codalab_submission.json`：

| 文件 | 模型 | Predictions | Format OK |
|------|------|-------------|-----------|
| `/root/autodl-tmp/eval_results/plan_002_test_rsft_s44/codalab_submission.json` (2.3MB) | Qwen3-4B rsft_s44/ckpt-510 | 26,925 | 99.6% |
| `/root/autodl-tmp/eval_results/plan_002_test_rsft_s43/codalab_submission.json` (2.3MB) | Qwen3-4B rsft_ced_s43/ckpt-510 | 27,119 | 99.8% |

**格式：** 标准 DocRED 提交格式 `[{title, h_idx, t_idx, r, evidence}, ...]`，可直接上传 CodaLab。两个文件均已就绪，无需额外转换。

---
