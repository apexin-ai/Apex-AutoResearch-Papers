# code e1a download 1p5b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e1a_download_1p5b_20260518T100931_result.json`
- **Structured JSON:** [`8aa4639efe872549fa7c.json`](../../sessions/8a/8aa4639efe872549fa7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 1. 1.5B 架构参数

| 参数 | 1.5B |
|---|---|
| model_type | qwen2 |
| num_hidden_layers | 28 |
| hidden_size | 1536 |
| intermediate_size | 8960 |
| num_attention_heads | 12 |
| num_key_value_heads | 2 |
| vocab_size | 151936 |
| 参数量 | **1.78B** |
| 磁盘占用 | **3.4GB** (safetensors) |

## 2. 7B vs 1.5B 架构对比

| 参数 | 7B | 1.5B | 变化 |
|---|---|---|---|
| num_hidden_layers | 28 | **28** | 相同 |
| hidden_size | 3584 | **1536** | 缩小 57% |
| intermediate_size | 18944 | **8960** | 缩小 53% |
| num_attention_heads | 28 | **12** | 缩小 57% |
| num_key_value_heads | 4 | **2** | 缩小 50% |
| vocab_size | 152064 | **151936** | 略小 (差128) |
| GQA ratio (heads/kv) | 7:1 | **6:1** | 不同 |

## 3. Forward pass

**成功。** 输出正确回答 "2+2=4"，生成流畅。

## 4. 代码兼容性问题

核心 pruning 代码**大部分兼容**，关键参数从 `model.config` 动态读取。但存在以下需注意项：

| 文件 | 行号 | 问题 |
|---|---|---|
| `src/prune.py` | L105 | `prune_mlp_channels` 默认参数 `n_mlp_groups=28`（仅默认值，实际调用时传入动态值 `n_heads`，**不影响运行**） |
| `src/cka_overlap.py` | L120 | `collect_mlp_activations` 默认参数 `n_groups=28`（同上，CLI 调用时通过 `--mlp_groups` 传入） |
| `src/cka_overlap.py` | L204 | `--mlp_groups` 默认值 `default=28`（**需改为动态获取或改为 12**） |
| `src/extract_pruning_pattern.py` | L5-8 | 多个 hardcoded 常量：`ORIGINAL_INTERMEDIATE_SIZE=18944`, `GROUP_SIZE=676`, `NUM_LAYERS=28`, `GROUPS_PER_LAYER=28`（**全部需要适配**，此文件是分析脚本，非核心） |
| `src/run_mvp.sh` 等 shell 脚本 | 多处 | `--n_mlp_groups 28` 和 7B 模型路径 hardcoded（**需要创建新的 1.5B 专用脚本**） |

**关键发现**：`n_mlp_groups` 在 pruning 中等于 `num_attention_heads`。7B 为 28，1.5B 为 **12**。这意味着 1.5B 每层只有 12 个 MLP channel group 和 2 个 GQA group，pruning 粒度更粗。另外 GQA ratio 从 7:1 变为 6:1，attention group pruning 的最小单元也不同。

核心代码（`prune.py` 的 pruning 逻辑、`model_utils.py` 的模型加载、`train_grpo_v5.py`/`sft_recovery.py` 的训练）均从 config 动态读取参数，**无需修改即可运行**。

---
