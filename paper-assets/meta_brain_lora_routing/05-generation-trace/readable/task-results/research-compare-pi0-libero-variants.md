# research compare pi0 libero variants

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_compare_pi0_libero_variants_20260516T143630_result.json`
- **Structured JSON:** [`3ad7a31f5c2f74848a00.json`](../../sessions/3a/3ad7a31f5c2f74848a00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the comparison:

---

## pi0_libero vs pi0_libero_finetuned 对比

### 来源

| | pi0_libero | pi0_libero_finetuned |
|---|---|---|
| HF repo | `lerobot/pi0_libero` (base model) | `pepijn223/pi0_libero_finetuned_extra2` |
| base_model | — | `lerobot/pi0_libero_base` |
| pretrained_path | — | `pepijn223/pi0_libero_finetuned_extra` |
| 训练数据 | 未指定 | `HuggingFaceVLA/libero` |
| 定位 | "Base model to fine tune" | 在 LIBERO 上微调过的版本 |

### Config 关键差异

| 字段 | pi0_libero | pi0_libero_finetuned |
|---|---|---|
| **dtype** | float32 | **bfloat16** |
| **n_action_steps** | 10 | **50** |
| **gradient_checkpointing** | false | **true** |
| **compile_model** | false | **true** |
| scheduler_decay_steps | 30000 | 10000 |
| normalization_mapping | 缺失 | 显式定义 (VISUAL→IDENTITY, STATE→MEAN_STD, ACTION→MEAN_STD) |
| input_features | 3 个 (image, image2, state) | **4 个** (+empty_camera_0 [3,224,224]) |
| time_sampling_scale/offset | 缺失 | 0.999 / 0.001 |

### Norm Stats 差异

| | pi0_libero | pi0_libero_finetuned |
|---|---|---|
| state mean[:4] | [-0.047, 0.034, 0.765, 2.972] | [-0.047, 0.034, 0.765, 2.972] (几乎一致) |
| **action mean[:4]** | [0.067, 0.064, **-0.805, -2.972**] | [0.063, 0.087, **-0.090, 0.001**] |
| action std[:4] | [0.329, 0.420, 0.617, 0.351] | [0.336, 0.378, 0.445, **0.039**] |
| state std padding (dim 8-31) | 全 0 | 全 **1.0** |
| q01/q99 | 有真实值 | **全 0**（未计算或不同 norm 方式） |

action 统计差异巨大：pi0_libero 是绝对关节位置的统计，finetuned 更像是 delta action 或在不同数据分布上计算的。

### 文件结构差异

| | pi0_libero | pi0_libero_finetuned |
|---|---|---|
| model.safetensors | 7,011,549,448 B ✅ 完整 | 7,011,548,640 B ⚠️ **有 .aria2 文件，下载未完成** |
| train_config.json | ❌ 无 | ✅ 有（batch_size=32, steps=10000, wandb run=wdhhngzb） |
| preprocessor state | 无 safetensors | ✅ `policy_preprocessor_step_5_normalizer_processor.safetensors` |
| postprocessor state | 无 safetensors | ✅ `policy_postprocessor_step_0_unnormalizer_processor.safetensors` |
| preprocessor features | 空 {} | 完整定义所有 features |

### ModelScope 下载状态

- `.ms_cache/lerobot/pi0_libero/` 只有 28K 元数据文件（config/README/policy JSON），**无 model.safetensors**
- `.ms_cache/lerobot/pi0_base/` 有完整 model.safetensors
- 没有活跃的 modelscope 下载进程在运行

### 结论

1. **pi0_libero** = 官方 base checkpoint（float32），已完整下载，用于微调起点
2. **pi0_libero_finetuned** = 社区用户 pepijn223 在 LIBERO 数据上微调的版本（bfloat16），是"更新的"版本，但 **model.safetensors 下载不完整**（有 .aria2 残留，且文件比 base 小 808 bytes）
3. finetuned 版本的 preprocessor/postprocessor 配置更完整，有独立的 normalizer state 文件
4. **ModelScope 的 pi0_libero 下载基本未开始**（只拉了元数据），也没有下载进程在跑

---
