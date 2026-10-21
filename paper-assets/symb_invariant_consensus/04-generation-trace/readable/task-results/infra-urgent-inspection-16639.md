# infra urgent inspection 16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-inspection-16639_20260521T212539_result.json`
- **Structured JSON:** [`6e875110017019b8cb8b.json`](../../sessions/6e/6e875110017019b8cb8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-16639 巡检报告

### GPU 状态

| GPU | 显存占用 | 利用率 | 用途 |
|-----|---------|--------|------|
| 0 | 84.2/97.9 GB | 0% | vLLM Mistral (port 8000) - 空闲 |
| 1 | 83.6/97.9 GB | **100%** | vLLM Qwen3 (port 8001) - 活跃 |
| **2** | **0/97.9 GB** | **0%** | **完全空闲** |
| 3 | 89.8/97.9 GB | 0% | vLLM Mistral (port 8004) - 空闲 |

### 实验状态

#### 1. Cross-Model SICA (PID 414515) — 🔄 进行中
- 运行时长：12h45m
- 当前阶段：**extraction_qwen3_same**（Qwen3 same-model extraction）
- 最新日志：05:27 仍在向 port 8001 (Qwen3) 发请求

| 子目录 | 文件数 | 状态 |
|--------|--------|------|
| mistral_traces | 203 | ✅ |
| extraction_mistral_same | 203 | ✅ |
| extraction_mistral_cross_qwen3 | 203 | ✅ |
| extraction_qwen3_cross_mistral | 202 | ✅ (修复后) |
| **extraction_qwen3_same** | **24/203** | **🔄 ~12%** |

#### 2. Qwen3 Fix (PID 473120) — ✅ 已完成
- 修复后 `extraction_qwen3_cross_mistral`: 202 files
- 旧 buggy 版本: 151 files (已备份)

#### 3. Gemini Extraction (PID 480272) — ✅ 已完成
- `cross_model_mistral.json`: 95 items
- `gemini_interim_95_metrics.json` 也已生成

### 空闲资源
- **GPU 2** 完全空闲
- GPU 0 / GPU 3 跑 vLLM Mistral 但无请求，实际空闲（仅占显存）

### 预估
extraction_qwen3_same 当前 24/203 (~12%)，按当前速度（每次请求~15s）估计还需 **数小时** 完成。

---
