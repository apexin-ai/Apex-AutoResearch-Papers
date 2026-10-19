# diagnose verify hsweep models

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_verify-hsweep-models_20260518T182922_result.json`
- **Structured JSON:** [`3e45bcda9ba29fd116eb.json`](../../sessions/3e/3e45bcda9ba29fd116eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。结果汇总：

## Part 1: Kill h=20
h=20 进程树（71822/71823/71827/71828）已通过 `kill -9` 全部终止，ps 确认无残留。

## Part 2-5: 模型对照表

**所有 h-sweep 和 g-sweep config 的 `model_path` 完全一致：**

| 实验 | Config 文件 | model_path | 实际模型 | 服务器 |
|------|-----------|------------|---------|--------|
| h=2 | `_alfworld_hsweep_h2.yaml` | `qwen3_exp021_ragen_sft_v4` | **Qwen3-1.7B** (SFT) | bjb1 + westd |
| h=5 | `_alfworld_hsweep_h5.yaml` | `qwen3_exp021_ragen_sft_v4` | **Qwen3-1.7B** (SFT) | bjb1 + westd |
| h=10 | `_alfworld_hsweep_h10.yaml` | `qwen3_exp021_ragen_sft_v4` | **Qwen3-1.7B** (SFT) | bjb1 + westd |
| h=20 | `_alfworld_hsweep_h20.yaml` | `qwen3_exp021_ragen_sft_v4` | **Qwen3-1.7B** (SFT) | bjb1 + westd |
| h=full | `_alfworld_hsweep_full.yaml` | `qwen3_exp021_ragen_sft_v4` | **Qwen3-1.7B** (SFT) | bjb1 + westd |
| g=0.50,h=5 | `_alfworld_gamma_sweep_g050_h5.yaml` | `qwen3_exp021_ragen_sft_v4` | **Qwen3-1.7B** (SFT) | westd |
| g=0.80,h=5 | `_alfworld_gamma_sweep_g080_h5.yaml` | `qwen3_exp021_ragen_sft_v4` | **Qwen3-1.7B** (SFT) | westd |
| g=0.95,h=5 | `_alfworld_gamma_sweep_g095_h5.yaml` | `qwen3_exp021_ragen_sft_v4` | **Qwen3-1.7B** (SFT) | westd |
| g=1.00,h=5 | `_alfworld_gamma_sweep_g100_h5.yaml` | `qwen3_exp021_ragen_sft_v4` | **Qwen3-1.7B** (SFT) | westd |

**模型身份确认（bjb1 上的 config.json）：**
- `model_type`: qwen3
- `hidden_size`: 2048
- `num_hidden_layers`: 28
- 这对应 **Qwen3-1.7B**，不是 Qwen2.5-3B

**结论：所有 h-sweep 和 g-sweep 实验统一使用 Qwen3-1.7B SFT checkpoint（exp021），不存在混用 Qwen2.5-3B 的情况。** 如果 registry 记录了 Qwen2.5-3B，那是 registry 记录错误。

**注意：** westd 上 `qwen3_exp021_ragen_sft_v4` 是一个断链 symlink（指向 `exp021_ragen_sft_v4/final/`，目标不存在）。westd 上的实验如果现在启动会因找不到模型而失败。

---
