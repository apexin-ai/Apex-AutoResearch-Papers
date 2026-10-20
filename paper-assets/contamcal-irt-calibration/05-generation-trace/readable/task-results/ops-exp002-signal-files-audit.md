# ops exp002 signal files audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp002-signal-files-audit_20260514T112513_result.json`
- **Structured JSON:** [`976697bd5bc509e63cac.json`](../../sessions/97/976697bd5bc509e63cac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## 审查结果

### 1. 已产出文件清单

| 目录 | 文件 | 大小 | 时间 |
|------|------|------|------|
| `Qwen2.5-0.5B_d000_s42/` | `signal_embedding_mmlu_Qwen2.5-0.5B_d000_s42.json` | 2KB | 16:00 |
| | `signal_embedding_gsm8k.json` | 568KB | 18:38 |
| | `signal_embedding_arc_challenge.json` | 515KB | 18:41 |
| | `signal_embedding_mmlu.json` | 6.1MB | 18:50 |
| | `signal_minkpp_mmlu.json` | 2.1MB | 18:55 |
| `Qwen2.5-0.5B_d005_s42/` | `signal_embedding_mmlu.json` | 6.1MB | 18:45 |
| d100 目录 | 不存在 | — | — |
| 根目录 | `batch_report_Qwen2.5-0.5B.json` | dry-run 报告，1 task FAIL(SIGTERM) | 18:15 |

**无任何 `signals_merged_*.json` 文件**，说明没有任何 (dosage, benchmark) 组合跑完全部信号。

### 2. 残留文件

`signal_embedding_mmlu_Qwen2.5-0.5B_d000_s42.json` (2KB) 是旧版命名格式的遗留产物，当前 `_save_signal()` 输出格式为 `signal_{signal_name}_{benchmark}.json`（不含 model_id）。这个文件应该清理掉，否则可能造成混淆。

### 3. Task 列表 (9 tasks)

执行顺序（外层 dosage，内层 benchmark）：

| # | dosage | benchmark |
|---|--------|-----------|
| 1 | d000 | mmlu |
| 2 | d000 | gsm8k |
| 3 | d000 | arc_challenge |
| 4 | d005 | mmlu |
| 5 | d005 | gsm8k |
| 6 | d005 | arc_challenge |
| 7 | d100 | mmlu |
| 8 | d100 | gsm8k |
| 9 | d100 | arc_challenge |

前提：checkpoint 必须存在，否则整个 dosage 被跳过。

### 4. skip-completed 逻辑分析

**命名匹配：无 bug。** `run_batch.py` 的 `merged_output_exists()` 检查路径为 `{OUTPUT_ROOT}/{model}_{dosage}_{SEED}/signals_merged_{benchmark}.json`，与 `compute_signals.py` 写出的 merged 文件路径完全一致。

**但存在一个设计缺陷：**

- `compute_signals.py` 仅在单次运行产出 ≥2 个信号时才写 merged 文件
- `compute_signals.py` 内部**没有任何 per-signal skip 逻辑**（grep 确认无 `exists`/`skip` 关键词）
- 后果：如果一个 task 跑完 embedding 后崩溃（如当前 d000/mmlu 的情况——embedding 完成、minkpp 完成、但 selfcritique/constat 未开始），merged 文件不存在 → 重跑时**所有信号从头算**，已算的 embedding 和 minkpp 被浪费

**当前状态**：因为没有任何 merged 文件，`skip_completed=True` 不会跳过任何 task，下次 run_batch 会全量重跑所有 9 个 task，包括 d000 已完成的那些个别信号。

---
