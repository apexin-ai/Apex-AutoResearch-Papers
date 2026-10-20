# ops llama70b scale validation

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama70b_scale_validation_20260523T090310_result.json`
- **Structured JSON:** [`68cf8fc8ecc21d13cadc.json`](../../sessions/68/68cf8fc8ecc21d13cadc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**磁盘占用明细：**

| 路径 | 大小 | 备注 |
|------|------|------|
| `.hf_cache/Qwen/` | 171GB | Qwen2.5-72B-Instruct（当前实验在用） |
| `.hf_cache/LLM-Research/` | 61GB | ModelScope 下载 |
| `.hf_cache/01ai/` | 17GB | Yi 系列 |
| `.hf_cache/Shanghai_AI_Laboratory/` | 15GB | InternLM 系列 |
| `.hf_cache/allenai/` + OLMo blobs | 28GB | OLMo-2-7B |
| `.hf_cache/deepseek-ai/` | 13GB | DeepSeek |
| `pip-cache/` + `pip-tmp/` | 7.7GB | pip 缓存 |
| **总已用** | **321GB / 350GB** | |

**结论：无法继续。** 下载 Llama-3.1-70B-Instruct 需要 ~140GB，当前仅剩 30GB。即使清理 pip 缓存（7.7GB）也远远不够。

**需要 Director 决策的清理候选项：**
1. `LLM-Research/`（61GB）— 可能是 ModelScope 镜像的冗余副本
2. `01ai/`（17GB）+ `Shanghai_AI_Laboratory/`（15GB）+ `deepseek-ai/`（13GB）— 如无后续实验需要可清理
3. `allenai/` + OLMo blobs（28GB）— OLMo-2-7B 相关

清理 2+3+pip 可释放 ~81GB，加上 1 可达 ~142GB，勉强够下载 70B 模型。但 **Qwen 171GB 不可删**（当前 G-study baseline）。

等待 Director 批准清理方案或提供替代指令。

---
