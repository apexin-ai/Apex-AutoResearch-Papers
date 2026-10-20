# investigate alpha verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_alpha-verify_20260515T151011_result.json`
- **Structured JSON:** [`fa0d344738793c6b0b46.json`](../../sessions/fa/fa0d344738793c6b0b46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 3B SFT Checkpoints（全部 10 个）

| Checkpoint | lora_alpha | 备注 |
|---|---|---|
| `Qwen2.5-3B_d000_s123` | **32** | |
| `Qwen2.5-3B_d000_s42` | **32** | |
| `Qwen2.5-3B_d000_v2_s123` | **16** | v2 重跑版本 |
| `Qwen2.5-3B_d000_v2_s42` | **16** | v2 重跑版本 |
| `Qwen2.5-3B_d005_s123` | **32** | ⚠️ registry 命令写 `--lora-alpha 16`，实际是 32 |
| `Qwen2.5-3B_d005_s42` | **32** | |
| `Qwen2.5-3B_d025_s123` | **32** | |
| `Qwen2.5-3B_d025_s42` | **16** | |
| `Qwen2.5-3B_d100_s123` | **16** | |
| `Qwen2.5-3B_d100_s42` | **16** | |

**分布：5 个 alpha=32，5 个 alpha=16**

### 0.5B / 1.5B 代表性 Checkpoints（各 2 个）

| Checkpoint | lora_alpha |
|---|---|
| `Qwen2.5-0.5B_d005_s123` | **32** |
| `Qwen2.5-0.5B_d025_s42` | **32** |
| `Qwen2.5-1.5B_d005_s123` | **32** |
| `Qwen2.5-1.5B_d025_s42` | **32** |

0.5B 和 1.5B 采样点全部一致为 alpha=32。

### 关键发现

1. **`exp_001_sft_3B_d005_s123` 存在 registry 与实际不一致**：registry 提交命令记录 `--lora-alpha 16`，但 checkpoint 实际保存的是 `lora_alpha=32`。可能原因：脚本有默认值覆盖了命令行参数，或 registry 记录有误。
2. **3B 的 alpha=16 集中在**：v2 重跑版本（d000_v2）和部分后期实验（d025_s42、d100_s123、d100_s42），暗示这些是在某次配置变更后训练的。
3. **0.5B / 1.5B 未受影响**，采样点均为 alpha=32。

---
