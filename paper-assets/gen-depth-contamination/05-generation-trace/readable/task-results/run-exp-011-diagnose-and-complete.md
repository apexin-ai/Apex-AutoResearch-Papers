# run exp 011 diagnose and complete

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp_011_diagnose_and_complete_20260513T105759_result.json`
- **Structured JSON:** [`2c6fc58649085055f597.json`](../../sessions/2c/2c6fc58649085055f597.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-011 全部完成。以下是完整产出。

---

## 产出总结

### 1. Claude 诊断结果

| Model ID | 结果 |
|---|---|
| `anthropic/claude-opus-4-6` | **FAIL** — 503 model_not_found: "No available channel for model anthropic/claude-opus-4-6 under group default (distributor)" |
| `claude-opus-4-6` | **SUCCESS** |
| `anthropic/claude-opus-4.6` | **SUCCESS** |

已修复脚本 MODEL_MAP 从 `anthropic/claude-opus-4-6` → `claude-opus-4-6`。

### 2. GPT-5.5 诊断结果
单条测试 **SUCCESS**。

### 3. GPT-5.5 最终状态
- **行数**: 500（已去重，原始 504 行有 4 个重复）
- **解析失败**: 0

### 4. Claude 最终状态
- **行数**: 500
- **解析失败**: 1

### 5. 分析结果 (`exp011_analysis.json`)

| Model | Acc(5-class) | MAE | Spearman ρ | Binary Acc |
|---|---|---|---|---|
| OBD-LightGBM (baseline) | 0.3856 | 1.1072 | τ_b=0.4745 | N/A |
| Claude Opus 4.6 | 0.3307 | 1.1503 | 0.4162 | 0.8818 |
| GPT-5.5 | 0.3320 | 1.1020 | 0.3834 | 0.8780 |

**Per-depth accuracy:**

| Depth | Claude | GPT-5.5 |
|---|---|---|
| 0 (human) | 0.690 | 0.770 |
| 1 | 0.210 | 0.190 |
| 2 | 0.280 | 0.380 |
| 3 | 0.101 | 0.240 |
| 4 | 0.370 | 0.080 |

两个 LLM 的 5-class accuracy 均略低于 OBD-LightGBM baseline（~33% vs 38.6%），但 binary detection（人/AI）准确率都很高（~88%）。Claude 在高 depth (4) 上表现更好，GPT-5.5 在中间 depth (2-3) 上更好。

---
