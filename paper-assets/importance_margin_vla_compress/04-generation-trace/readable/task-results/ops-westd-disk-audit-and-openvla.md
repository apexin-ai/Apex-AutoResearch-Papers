# ops westd disk audit and openvla

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_disk_audit_and_openvla_20260517T140429_result.json`
- **Structured JSON:** [`66d5c0948ee630e46989.json`](../../sessions/66/66d5c0948ee630e46989.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。以下是汇总报告。

---

## Part 1: 磁盘审计

**总览**: 250GB 总容量，已用 226GB，剩余 25GB (91%)

### 一级空间分布

| 目录 | 大小 | 说明 |
|------|------|------|
| `importance_margin_vla_compress/checkpoints/` | **153 GB** | 实验 checkpoints |
| `.hf_cache/` (隐藏) | **72 GB** | HuggingFace 缓存 |
| `.ms_cache/` | 2.1 GB | ModelScope 缓存 |
| 其他 (logs, tar.gz, 代码) | <1 GB | — |

### Checkpoints 详情 (153 GB)

| Checkpoint | 大小 | 步数 | 每步大小 | 删除建议 |
|---|---|---|---|---|
| `libero_imm_twostage_fullft/` | 21 GB | stage1(4步)+stage2(9步)+final+stage1_done | 1.2-1.6G | **可清中间步**：仅保留 final (879M)，释放 ~20GB |
| `imm_anchor_v8b_twostage/` | 19 GB | stage1+stage2+final+stage1_done | 1.2G | **可清中间步**：仅保留 final (1.2G)，释放 ~18GB |
| `imm_anchor_v8c_annealing/` | 18 GB | 15 步 | 1.2G | **旧实验？** 可只保留 latest，释放 ~17GB |
| `imm_anchor_v8_1/` | 18 GB | 15 步 | 1.2G | **旧实验？** 可只保留 latest，释放 ~17GB |
| `imm_anchor_v8/` | 18 GB | 16 步 | 1.2G | **旧实验？** 可只保留 latest，释放 ~17GB |
| `imm_anchor_v7_1/` | 18 GB | 15 步 | 1.2G | **旧迭代**，v8 系列已替代？释放 ~17GB |
| `imm_anchor/` | 18 GB | 16 步 | 1.2G | **最早版本**，可能已过时？释放 ~17GB |
| `baseline_v6_alpha16/` | 6.8 GB | 7 步 | 1.2G | 可只保留 latest，释放 ~5.6GB |
| `baseline/` | 6.8 GB | 6 步 | 1.2G | 可只保留 latest，释放 ~5.6GB |
| 11 个小 checkpoints | ~12 GB | 各 1 步 | 0.9-1.6G | 逐个确认是否需要 |

### HF Cache 详情 (72 GB)

| 路径 | 大小 | 删除建议 |
|---|---|---|
| `.hf_cache/lerobot/hub/datasets--HuggingFaceVLA--libero/` | 33 GB | **与下条疑似重复**，确认后可删一份 |
| `.hf_cache/datasets/parquet/default-9082...` | 33 GB | 同上，两个 cache backend 缓存了同一数据集 |
| `.hf_cache/lerobot/hub/models--SmolVLM2-500M` | 1.5 GB | 如不再需要可删 |
| `.hf_cache/datasets/parquet/` 其他 hash | ~1.8 GB | 旧缓存 |
| `.hf_cache/lerobot/smolvla_base/` | 873 MB | 如不再需要可删 |
| `.ms_cache/` | 2.1 GB | ModelScope 缓存，确认后可清 |

### 释放空间估算

| 策略 | 预估释放 |
|---|---|
| 清 HF cache 重复数据 (33GB 二选一) | **~33 GB** |
| 旧版 checkpoints 只保留 latest (imm_anchor, v7_1, v8, v8_1) | **~67 GB** |
| twostage 实验只保留 final | **~38 GB** |
| 清全部 HF cache | **~72 GB** |
| **合计潜力** | **~140+ GB** |

轻松满足 ≥40GB 目标。最保守方案：清 HF cache 重复 (33GB) + 清 imm_anchor 和 v7_1 中间步 (34GB) = **67GB**。

---

## Part 2: OpenVLA Checkpoint 类型

**`openvla/openvla-7b-finetuned-libero-object` 是 full model，不是 LoRA adapter。**

虽然模型描述说 "fine-tuned via LoRA (r=32)"，但仓库中存储的是 **LoRA 合并后的完整权重**：

| 文件 | 大小 |
|---|---|
| model-00001-of-00004.safetensors | 4.93 GB |
| model-00002-of-00004.safetensors | 4.95 GB |
| model-00003-of-00004.safetensors | 4.95 GB |
| model-00004-of-00004.safetensors | 0.26 GB |
| tokenizer + config 等 | ~2 MB |
| **总计** | **~15.1 GB** |

**结论**：
- 下载大小：**~15.1 GB**
- 类型：Full merged model (LoRA 已合并进 base model)
- **不需要**额外下载 base model `openvla/openvla-7b`
- 当前磁盘需先释放至少 15GB 才能放下（现在只剩 25GB 可用）

---

**等 Director 确认哪些可以删除。**

---
