# ops disk cleanup audit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-audit_20260514T055713_result.json`
- **Structured JSON:** [`3f7eb07bb93511c95568.json`](../../sessions/3f/3f7eb07bb93511c95568.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是磁盘审计报告。

---

## 磁盘使用明细

### 分区概览

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/` (根分区) | 30G | 8.1G | 22G | 27% |
| `/root/autodl-tmp` (数据盘) | 250G | 109G | 142G | 44% |

**注意**：相比上次检查（仅剩 6.4G），数据盘已大幅释放，目前有 142G 可用。

### 数据盘 `/root/autodl-tmp` 明细 (109G)

| 路径 | 大小 | 说明 |
|------|------|------|
| `outputs/` | **91G** | 实验输出 |
| `models/` | **16G** | 基础模型 |
| `.hf_cache/` | **2.5G** | HuggingFace 缓存 |
| `gpt2-small` | 0 | 空目录 |

### outputs 明细 (91G)

| 目录 | 大小 | 状态 | 内容 |
|------|------|------|------|
| `grpo_exec_only/` | 15G | **已完成** (step 25, 05-14 05:09) | 最终模型权重 + logs |
| `grpo_exec_sta/` | 15G | **已完成** (step 25, 05-14 05:11) | 最终模型权重 + logs |
| `plan001_exec_only_s42/` | 15G | **已完成** (05-14 07:43) | 最终模型权重 + logs |
| `plan005_sta_low_s42/` | 15G | **已完成** (step 500, 05-13 23:54) | 最终模型权重 + logs |
| `plan002_additive_b01_s42/` | 15G | **运行中** | checkpoint-150 (15G) + reward_log |
| `plan016_extended_1000_s42/` | 15G | **运行中** | checkpoint-100 (15G) + reward_log |

### models 明细 (16G)

| 目录 | 大小 | 说明 |
|------|------|------|
| `Qwen3-4B/` | 7.6G | HuggingFace 版 Qwen3-4B（3 分片） |
| `Qwen3-4B-ms/` | 7.6G | ModelScope 版 Qwen3-4B（**重复**） |

### .hf_cache 明细 (2.5G)

| 目录 | 大小 | 说明 |
|------|------|------|
| `openai-community/gpt2` | 1.1G | GPT-2 模型（项目不需要） |
| `models--openai-community--gpt2/` | 363M | GPT-2 blobs 缓存（同上，重复） |
| `Qwen/` | 954M | Qwen 缓存 |
| `hub/` + `xet/` | ~1.2M | 元数据 |

### 根分区其他大目录

| 目录 | 大小 |
|------|------|
| `miniconda3/` | 13G |
| `min_necessary_circuit_css/` | 56M |
| `runs/` | 33M |
| `solver-trace-ablation/` | 5.3M |

---

## 推荐删除列表

| 优先级 | 目标 | 大小 | 理由 |
|--------|------|------|------|
| **P0** | `outputs/grpo_exec_only/` | **15G** | 早期探索实验（仅 25 step），已被后续 plan001 取代 |
| **P0** | `outputs/grpo_exec_sta/` | **15G** | 同上，早期探索实验 |
| **P1** | `models/Qwen3-4B-ms/` | **7.6G** | ModelScope 下载的副本，与 `Qwen3-4B/` 完全重复 |
| **P2** | `.hf_cache/openai-community/` | **1.1G** | GPT-2 模型，项目不使用 |
| **P2** | `.hf_cache/models--openai-community--gpt2/` | **363M** | GPT-2 blobs 缓存，同上 |
| **P3** | `gpt2-small` | 0 | 空目录，无影响 |

### 需确认后决定

| 目标 | 大小 | 说明 |
|------|------|------|
| `outputs/plan001_exec_only_s42/` | 15G | 如 plan001 系列实验已有统一评估结果，模型权重可删（保留 reward_log/README） |
| `outputs/plan005_sta_low_s42/` | 15G | 同上，如已完成 eval_sta 统一评估则可删权重 |

---

## 空间预估

| 方案 | 释放空间 | 删除后剩余可用 |
|------|---------|---------------|
| 仅 P0 | **30G** | 172G |
| P0 + P1 | **37.6G** | 180G |
| P0 + P1 + P2 | **39G** | 181G |
| 全部含确认项 | **69G** | 211G |

**当前 142G 可用空间对 plan006 Prolog 3-seed 实验（预计 ~45G = 15G × 3 seed）已经足够。** 如果只做保守清理（P0 + P1 = 37.6G），可用空间达 180G，非常充裕。

### 保护名单（不删）
- `outputs/plan002_additive_b01_s42/` — 运行中
- `outputs/plan016_extended_1000_s42/` — 运行中
- `models/Qwen3-4B/` — 基础模型，训练依赖
- `miniconda3/` — 运行环境
- `solver-trace-ablation/` — 项目代码

---
