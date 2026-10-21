# infra plan003 402 triage

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan003-402-triage_20260520T225505_result.json`
- **Structured JSON:** [`0c934be111edfd513be8.json`](../../sessions/0c/0c934be111edfd513be8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据采集完毕。以下是完整报告。

---

## 产出报告

### 1. 进程终止确认
- **PID 438843 (qwen3)**: 已终止 (SIGTERM)
- **PID 439116 (deepseek)**: 已终止 (SIGTERM)

### 2. API 端点与 402 来源
- **端点**: `http://47.94.22.126/v1/chat/completions`
- **认证**: `OPENROUTER_API_KEY` 环境变量 (Bearer token)
- **错误**: `HTTP 402: 402 Client Error: Payment Required` — API 余额耗尽

### 3. 27 组合完成矩阵

文件在 `results/` 目录（不是 `data/`）。

**humaid** (全部 1500 行):

| 组合 | valid/1500 | 状态 |
|------|-----------|------|
| llama4_zero-shot | 1500 | ✅ 完整 |
| llama4_few-shot-3 | 1498 | ✅ (2个transient错误) |
| llama4_few-shot-5 | 1471 | ⚠️ 29个402 |
| qwen3_zero-shot | 1500 | ✅ 完整 |
| qwen3_few-shot-3 | 1423 | ⚠️ 77个402 |
| qwen3_few-shot-5 | 0 | ❌ 全部402 |
| deepseek_zero-shot | 1500 | ✅ 完整 |
| deepseek_few-shot-3 | 1345 | ⚠️ 155个402 |
| deepseek_few-shot-5 | 1237 | ⚠️ 263个402 |

**vast** (全部 1500 行):

| 组合 | valid/1500 | 状态 |
|------|-----------|------|
| llama4_zero-shot | 1496 | ✅ (4个transient) |
| llama4_few-shot-3 | 1500 | ✅ 完整 |
| llama4_few-shot-5 | 346 | ❌ 1154个402 |
| qwen3_zero-shot | 0 | ❌ 全部402 |
| qwen3_few-shot-3 | 0 | ❌ 全部402 |
| qwen3_few-shot-5 | 0 | ❌ 全部402 |
| deepseek_zero-shot | 1000 | ⚠️ 500个402 |
| deepseek_few-shot-3 | 0 | ❌ 全部402 |
| deepseek_few-shot-5 | 0 | ❌ 全部402 |

**civil_comments** (全部 402，零有效数据):

| 组合 | 行数 | 状态 |
|------|------|------|
| llama4_zero-shot | 1500 | ❌ 全402 |
| llama4_few-shot-3 | 1500 | ❌ 全402 |
| llama4_few-shot-5 | 1500 | ❌ 全402 |
| qwen3_zero-shot | 420 | ❌ 全402 (进程被kill) |
| qwen3_few-shot-3 | — | ❌ 文件不存在 |
| qwen3_few-shot-5 | — | ❌ 文件不存在 |
| deepseek_zero-shot | 1500 | ❌ 全402 |
| deepseek_few-shot-3 | 1498 | ❌ 全402 (进程被kill) |
| deepseek_few-shot-5 | — | ❌ 文件不存在 |

### 4. Confusion matrix NPZ 文件

27 个 NPZ 文件存在（humaid 9个 + vast 9个 + civil_comments 6个），但 402 污染的 NPZ 全是零矩阵，无用。civil_comments 有 3 个组合连 NPZ 都没生成。

### 5. 汇总

| 类别 | 数量 | 详情 |
|------|------|------|
| ✅ 完整可用 (≥1496/1500) | **6** | humaid: llama4×2, qwen3×1, deepseek×1; vast: llama4×2 |
| ⚠️ 部分可用 (需补跑缺失) | **5** | humaid: llama4-fs5, qwen3-fs3, deepseek-fs3/fs5; vast: deepseek-zs |
| ❌ 全废 (需完全重跑) | **16** | humaid: qwen3-fs5; vast: 6个; civil_comments: 全部9个 |

402 从 humaid 跑到中途开始出现，三个进程并发消耗同一 API 余额，llama4 最快跑完了 humaid 全部 + vast 大部分才撞墙。

---
