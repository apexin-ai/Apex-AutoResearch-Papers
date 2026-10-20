# ops verify s42 checkpoint alpha

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-s42-checkpoint-alpha_20260515T185157_result.json`
- **Structured JSON:** [`53b288f2f8a5afb14ae9.json`](../../sessions/53/53b288f2f8a5afb14ae9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 原始 s42 checkpoint（3B）

| Checkpoint | lora_alpha | 状态 |
|---|---|---|
| `Qwen2.5-3B_d000_s42` | **32** | 受 bug 影响（DEFAULT_LORA_CONFIG 覆盖） |
| `Qwen2.5-3B_d005_s42` | **32** | 受 bug 影响 |
| `Qwen2.5-3B_d025_s42` | **16** | 正确 |
| `Qwen2.5-3B_d100_s42` | **16** | 正确 |

### v2 修复版

| Checkpoint | lora_alpha |
|---|---|
| `Qwen2.5-3B_d000_v2_s42` | **16** | 已修复重训 |

### 当前重训 checkpoint（a32/v3 命名）

| Checkpoint | 状态 |
|---|---|
| `d000_a32_s42` | lora_adapter 空（未写出模型） |
| `d100_a32_s42` | lora_adapter 空（未写出模型） |
| `d025_v3_s42` | 训练中 66%（2229/3384 steps） |
| `d025_a32_s42` | 训练中 2%（68/3384 steps） |
| `d100_a32_s123` | lora_adapter 空（未写出模型） |

### 结论

**s42 原始 checkpoint 不全是 alpha=32。** 情况是混合的：
- **d000、d005**：alpha=32（与 s123 一样受 bug 影响）
- **d025、d100**：alpha=16（正确值，未受 bug 影响）

因此：
- `d000_a32_s42` 重训**冗余**——原始 d000_s42 已经是 alpha=32
- `d025_a32_s42` / `d025_v3_s42` 重训**不冗余**（如果目标是统一到 alpha=32）——原始是 alpha=16
- `d100_a32_s42` 重训**不冗余**——原始是 alpha=16
- d005_s42 没有对应的 a32 重训目录，因为原始已经是 alpha=32

---
