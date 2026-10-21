# check autodl tmp dirs

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_autodl_tmp_dirs_20260514T165950_result.json`
- **Structured JSON:** [`7b92890cb6564b10d8a1.json`](../../sessions/7b/7b92890cb6564b10d8a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

**`/root/autodl-tmp/output/`** — 不存在
**`/root/autodl-tmp/schema-conform-ie-training/`** — 不存在

以下是 `autodl-tmp` 下实际存在的目录：

| 目录 | 大小 | 内容 | 归属 |
|------|------|------|------|
| `models/Qwen/Qwen3___5-9B` | **19G** | Qwen3.5-9B 完整模型权重 (safetensors) | **recovery_aware_struct_prune** — 剪枝基座模型 |
| `DeepSeek-R1-Distill-Qwen-7B/` | **15G** | DeepSeek-R1-Distill-Qwen-7B 完整模型权重 (2 个 safetensors 分片) | **recovery_aware_struct_prune** — 另一个实验基座模型 (ModelScope 下载) |
| `pruned_rasp_20/` | **12G** | Qwen2ForCausalLM 剪枝输出，`per_layer_intermediate_size` 非均匀，含 `pruning_metadata.pt` | **recovery_aware_struct_prune** — RASP 方法 20% 剪枝结果 |
| `pruned_rasp_25/` | **11G** | 同上结构 | **recovery_aware_struct_prune** — RASP 方法 25% 剪枝结果 |
| `pruned_standard_20/` | **12G** | 同上结构，`per_layer_intermediate_size` 分布不同 | **recovery_aware_struct_prune** — 标准方法 20% 剪枝结果 |
| `pruned_standard_25/` | **11G** | 同上结构 | **recovery_aware_struct_prune** — 标准方法 25% 剪枝结果 |
| `data/` | **1.5G** | crossner、scierc 数据集 | **recovery_aware_struct_prune** — 评估数据集 |
| `logs/` | **64M** | train_A/B/D1/D2、eval_A/B/C/D 等训练和评估日志 | **recovery_aware_struct_prune** — 实验日志 |
| `recovery_aware_struct_prune/` | **56K** | 项目子目录 | **recovery_aware_struct_prune** — 项目文件 |
| `.hf_cache/` | **7.2M** | HuggingFace 缓存 | 通用缓存 |
| `.ms_cache/` | **0** | ModelScope 缓存（空） | — |
| `tmp_build/` | **0** | 空目录 | 可清理 |

**总结**：`autodl-tmp` 下所有目录均属于 **recovery_aware_struct_prune** 项目。总占用约 **81G**，其中基座模型 34G（Qwen3.5-9B + DeepSeek-R1-Distill-Qwen-7B），剪枝产物 46G（4 个 pruned_* 目录）。`output/` 和 `schema-conform-ie-training/` 不存在于该服务器。

---
