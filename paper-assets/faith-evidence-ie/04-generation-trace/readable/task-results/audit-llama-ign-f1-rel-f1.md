# audit llama ign f1 rel f1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_llama-ign-f1-rel-f1_20260520T043357_result.json`
- **Structured JSON:** [`0fec3acc0967ea216340.json`](../../sessions/0f/0fec3acc0967ea216340.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 12 个目录的 metrics.json 已读取完毕，registry 也已检查。下面是完整审计结果。

## 源文件验证结果

| # | 实验 | ign_f1 | rel_f1 | invariant | 来源文件 |
|---|------|--------|--------|-----------|---------|
| 1 | LLaMA SFT s42 (with-evi) | 0.5384 | 0.5514 | ✓ | `llama_3_1_8b_sft_eval/metrics.json` |
| 2 | LLaMA SFT s42 (no-evi) | 0.5452 | 0.5624 | ✓ | `llama_3_1_8b_no_evidence_eval/metrics.json` |
| 3 | LLaMA RSFT k1 s42 (with-evi) | **0.5714** | **0.5839** | ✓ | `d102_llama_k1_s42/metrics.json` |
| 4 | LLaMA RSFT k1 s42 (no-evi) | 0.5526 | 0.5666 | ✓ | `eval_llama_rsft_s42_no_evidence/metrics.json` |
| 5 | LLaMA RSFT k1 s43 (with-evi) | 0.5662 | 0.5780 | ✓ | `d102_llama_k1_s43/metrics.json` (=`eval_llama_rsft_k1_s43`，完全一致) |
| 6 | LLaMA RSFT k1 s43 (no-evi) | 0.5546 | 0.5670 | ✓ | `eval_llama_rsft_s43_no_evidence/metrics.json` |
| 7 | LLaMA RSFT k1 s44 (with-evi) | 0.5587 | 0.5706 | ✓ | `rsft_llama_k1_s44_eval/metrics.json` |

**所有 7 个实验 invariant (ign_f1 ≤ rel_f1) 全部通过。**

---

## Registry 与源文件对比

| Registry 条目 | 存储的 ign_f1 | 存储的 f1/rel_f1 | 源文件 ign_f1 | 源文件 f1 | 一致？ |
|---------------|-------------|-----------------|-------------|----------|-------|
| `plan_016_llama_3_1_8b_sft_eval` | 0.5384 | 0.5514 | 0.5384 | 0.5514 | ✓ |
| `plan_016_llama_3_1_8b_no_evidence_eval` | 0.5452 | 0.5624 | 0.5452 | 0.5624 | ✓ |
| `eval_llama_rsft_s42_no_evidence` | 0.5526 | 0.5666 (f1) | 0.5526 | 0.5666 | ✓ |
| `seed_llama_rsft_k1_s43_eval` | 0.5662 | 0.578 (f1) | 0.5662 | 0.5780 | ✓ |
| `eval_llama_rsft_k1_s43` | 0.5662 | 0.578 (f1) | 0.5662 | 0.5780 | ✓ |
| `eval_llama_rsft_s43_no_evidence` | 0.5546 | 0.567 (f1) | 0.5546 | 0.5670 | ✓ |
| `llama_rsft_s44_pipeline` | 0.5587 | 0.5706 (f1) | 0.5587 | 0.5706 | ✓ |
| `plan_006_llama_rsft_r3_eval` (旧 r3) | 0.5563 | 0.5674 (f1) | 0.5563 | 0.5674 | ✓ |
| `plan_006_llama_rsft_seed43_eval_r2` (旧 s43) | 0.5619 | 0.5727 | 0.5619 | 0.5727 | ✓ |

**所有 registry 存储的 metrics 数值与源文件一致。**

---

## 问题发现

**RSFT k1 s42 eval 没有独立的 registry 条目。** `d102_llama_k1_s42` 目录的 eval metrics (ign_f1=0.5714, f1=0.5839) 未记录在任何 registry eval 条目中。训练条目 `d102_llama_rsft_k1_s42` 只记录了 training metrics。

**Hypothesis 文本中的 ign_f1/rel_f1 混淆**（非 metrics 字段，仅文字描述）：

1. **`eval_llama_rsft_k1_s43`** (L10873): hypothesis 写 `s42 ign_f1=0.5839, SFT ign_f1=0.5514` — **两个值都是 rel_f1 而非 ign_f1**（实际 s42 ign_f1=0.5714, SFT ign_f1=0.5384）

2. **`llama_rsft_s44_pipeline`** (L11068): hypothesis 写 `s42 ign_f1=0.5839` — **应为 0.5714**（s43 ign_f1=0.5662 是正确的）

**RSFT variance std=0.0052 是正确的**：使用 ign_f1 值 (0.5714, 0.5662, 0.5587) 的总体标准差 = 0.00521，与记录一致。混淆仅在 hypothesis 文本中，未影响实际计算。

---

## 额外发现的 eval 目录

| 目录 | 说明 | ign_f1 | f1 |
|------|------|--------|-----|
| `plan_006_llama_rsft_r3_eval` | 旧版 RSFT r3 checkpoint-3312 (非 k=1) | 0.5563 | 0.5674 |
| `plan_006_llama_rsft_seed43_eval_r2` | 旧版 RSFT s43 checkpoint-3312 (非 k=1) | 0.5619 | 0.5727 |
| `plan_006_llama_rsft_test` | test split（无 metrics，需 CodaLab 提交） | — | — |

---
