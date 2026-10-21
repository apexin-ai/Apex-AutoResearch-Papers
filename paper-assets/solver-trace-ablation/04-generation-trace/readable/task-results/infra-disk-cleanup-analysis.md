# infra disk cleanup analysis

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-cleanup-analysis_20260514T061159_result.json`
- **Structured JSON:** [`af349cdf762a557c16ad.json`](../../sessions/af/af349cdf762a557c16ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整的磁盘分析和清理建议。

---

## 磁盘总览

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/root/autodl-tmp/` | 250G | 109G | 142G | 44% |
| `/root/` (根) | 30G | 8.1G | 22G | 27% |

上次报告的 plan001_s43_r4 (~46G) 和 plan001_s44 (~31G) 已被清理，磁盘从 ~6.4G 恢复到 142G 可用。

---

## `/root/autodl-tmp/` 空间明细

### outputs/ 目录 (~91G)

| 目录路径 | 大小 | 实验 | Registry 状态 | Eval 已完成 | 可否删除 | 原因 |
|----------|------|------|--------------|-------------|----------|------|
| `outputs/grpo_exec_only/` | 15G | sta-phase1-exec-only-r5 | DONE (success) | 是 (plan003-eval) | **可删** | R5 旧实验，已被 plan001 系列取代，eval metrics 已在 registry |
| `outputs/grpo_exec_sta/` | 15G | sta-phase1-exec-sta-r5 | DONE (negative) | 否 | **可删** | Negative 结论，已被 plan005 取代，无需再 eval |
| `outputs/plan001_exec_only_s42/` | 15G | plan001-exec-only-s42-r2 | DONE (success) | 是 (eval_sta) | **谨慎** | 主实验 s42 baseline，eval 已完成。如确认不再需要模型权重做进一步分析，可删 |
| `outputs/plan005_sta_low_s42/` | 15G | plan005-sta-low-s42 | DONE (negative) | 否（仅训练日志 metrics） | **可删** | Negative 结论，如需 eval 先跑 eval_sta.py 再删 checkpoint |
| `outputs/plan002_additive_b01_s42/` | 16G | plan002-additive-b01-s42 | **RUNNING** | — | **不可删** | 正在训练 (cuda:0, PID 262266) |
| `outputs/plan016_extended_1000_s42/` | 15G | plan016-extended-1000-s42 | **RUNNING** | — | **不可删** | 正在训练 (cuda:1, PID 263273) |

### models/ 目录 (~15.2G)

| 目录路径 | 大小 | 说明 | 可否删除 | 原因 |
|----------|------|------|----------|------|
| `models/Qwen3-4B/` | 7.6G | HuggingFace 下载的 base model | **不可删** | 所有实验的 base model |
| `models/Qwen3-4B-ms/` | 7.6G | ModelScope 下载的同一模型 | **可删** | 与 Qwen3-4B/ 重复（`Qwen3-4B-ms/Qwen/Qwen3-4B`），需确认无 config 引用此路径 |

### 缓存目录 (~3.7G)

| 目录路径 | 大小 | 可否删除 | 原因 |
|----------|------|----------|------|
| `.hf_cache/` | 2.5G | **可删部分** | 含 openai-community/gpt2 (1.1G+363M) 和 Qwen cache (954M)。gpt2 用于 tokenizer fallback，若不再需要可删 |
| `.ms_cache/` | 1.2G | **可删** | ModelScope 缓存，模型已在 models/ 目录，此为下载中间文件 |

---

## 清理优先级建议（按释放空间排序）

| 优先级 | 操作 | 释放空间 | 风险 |
|--------|------|----------|------|
| 1 | 删 `outputs/grpo_exec_only/` | ~15G | 极低 — eval 已完成，metrics 在 registry，被 plan001 取代 |
| 2 | 删 `outputs/grpo_exec_sta/` | ~15G | 极低 — negative 结论，被 plan005 取代 |
| 3 | 删 `outputs/plan005_sta_low_s42/` | ~15G | 低 — negative 结论。若计划补跑 eval_sta.py 则先 eval 再删 |
| 4 | 删 `models/Qwen3-4B-ms/` | ~7.6G | 低 — 与 Qwen3-4B/ 重复，先 grep config 确认无引用 |
| 5 | 删 `.ms_cache/` | ~1.2G | 极低 — 纯下载缓存 |
| 6 | 删 `.hf_cache/openai-community/` + `models--openai-community--gpt2/` | ~1.5G | 低 — 确认当前代码不 import gpt2 tokenizer |
| 7 | 删 `outputs/plan001_exec_only_s42/` | ~15G | **中** — 主实验 checkpoint，eval 已跑完，但若需做 error analysis / 进一步推理则需保留 |

**优先级 1-3 可立即释放 ~45G，无实验价值损失。**

加上优先级 4-6 共可释放 **~55G**。

加上优先级 7 共可释放 **~70G**。

当前 142G 可用空间已经比较充裕。如果 plan006 Prolog 实验需要 ~16G 空间，现有空间足够，无需立即清理。但如果计划运行更多并行实验或需要下载额外模型，建议先清理优先级 1-3。

---
