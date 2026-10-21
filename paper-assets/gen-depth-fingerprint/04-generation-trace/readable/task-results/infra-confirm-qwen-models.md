# infra confirm qwen models

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_confirm-qwen-models_20260514T191415_result.json`
- **Structured JSON:** [`9880961bd573e174e76c.json`](../../sessions/98/9880961bd573e174e76c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

网络超时（AutoDL 代理问题）。基于已知信息即可判断：

---

## 汇总报告

### 实验计划 vs 实际模型

实验计划（experiment_plan.yaml）中 plan_002 写的是 **Qwen3.5-2B** 和 **Qwen3.5-0.8B**，但 **Qwen3.5 系列不存在**。Qwen 截至目前发布的小模型是 Qwen3 系列。服务器上实际下载的是正确的替代：

- 计划中 "Qwen3.5-2B" → 实际为 **Qwen/Qwen3-1.7B-Base**（1.72B 参数）
- 计划中 "Qwen3.5-0.8B" → 实际为 **Qwen/Qwen3-0.6B-Base**（0.60B 参数）

### 全部可用生成器清单

| # | 显示名 | HF repo ID | 实际参数量 | 本地路径 | 验证状态 |
|---|--------|-----------|-----------|---------|---------|
| 1 | pythia-2.8b | EleutherAI/pythia-2.8b | **2.77B** | `/root/autodl-tmp/models/pythia-2.8b/models--EleutherAI--pythia-2.8b/snapshots/2a259c.../` | MVP 已验证 |
| 2 | pythia-1b | EleutherAI/pythia-1b | **1.01B** | `/root/autodl-tmp/models/pythia-1b/EleutherAI/pythia-1b/` | config 已验证 |
| 3 | olmo-2-1b | allenai/OLMo-2-0425-1B | **1.48B** | `/root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B/` | config 已验证 |
| 4 | qwen-1.7b | **Qwen/Qwen3-1.7B-Base** | **1.72B** | `/root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base/` | config 已验证 |
| 5 | qwen-0.6b | **Qwen/Qwen3-0.6B-Base** | **0.60B** | `/root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base/` | config 已验证 |

### 额外发现的模型（非实验计划内）

| 模型 | 本地路径 | 备注 |
|------|---------|------|
| EleutherAI/pythia-410m | `/root/autodl-tmp/models/pythia-410m/...` | MVP 参考模型 |
| Qwen/Qwen2.5-14B-Instruct | `/root/autodl-tmp/models/Qwen/Qwen2___5-14B-Instruct/` | 非实验用 |
| deepseek-ai/DeepSeek-R1-Distill-Qwen-14B | `/root/autodl-tmp/models/deepseek-ai/...` | 非实验用 |

### 关键差异说明

1. **Qwen 参数量与计划不匹配**：计划写 "2B" 和 "0.8B"，实际为 **1.7B** 和 **0.6B**。差异不大，对实验设计无实质影响——仍覆盖了 "中等规模" 和 "小规模" 两个档位。
2. **experiment_plan.yaml 需更新**：应将 "Qwen3.5-2B" → "Qwen3-1.7B-Base"，"Qwen3.5-0.8B" → "Qwen3-0.6B-Base"。
3. **OLMo 实际 repo 名**：计划写 "OLMo-2-1B"，本地是 `allenai/OLMo-2-0425-1B`（同一模型的日期版本号），参数量 1.48B。

---
