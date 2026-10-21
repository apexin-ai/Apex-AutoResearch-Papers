# check matrix completeness

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_matrix_completeness_20260523T154503_result.json`
- **Structured JSON:** [`1089506339718f6acc35.json`](../../sessions/10/1089506339718f6acc35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 数据完整度报告

### 1. 文件清单（4 个核心探针 + RSA 可选）

| arch×suite | condition | R² | L1 Attn | Cross-Instr | Counterfactual | RSA |
|---|---|---|---|---|---|---|
| **openvla_goal** | trained | ✅ | ✅ | ✅ | ✅ | ✅ |
| | untrained | ✅ | ✅ | ✅ | ✅ | ✅ |
| **openvla_spatial** | trained | ✅ | ✅ | ✅ | ✅ | ✅ |
| | untrained | ✅ | ✅ | ✅ | ✅ | ✅ |
| **openvla_object** | trained | ✅ | ✅ | ✅ | ✅ | ✅ |
| | untrained | ✅ | ✅ | ✅ | ✅ | ✅ |
| **openvla_long** | trained | ✅ | ✅ | ✅ | ✅ | ✅ |
| | untrained | ✅ | ✅ | ✅ | ✅ | ✅ |
| **tracvla_goal** | trained | ✅ | ✅ | ✅ | ✅ | — |
| | untrained | ✅ | ✅ | ✅ | ✅ | — |
| **tracvla_spatial** | trained | ✅ | ✅ | ✅ | ✅ | — |
| | untrained | ✅ | ✅ | ✅ | ✅ | — |
| **tracvla_object** | trained | ✅ | ✅ | ✅ | ✅ | — |
| | untrained | ✅ | ✅ | ✅ | ✅ | — |
| **tracvla_long** | trained | ✅ | ✅ | ✅ | ✅ | — |
| | untrained | ✅ | ✅ | ✅ | ✅ | — |
| **nora_goal** | trained | ✅ | ✅ | ✅ | ✅ | — |
| | untrained | ✅ | ✅ | ✅ | ✅ | — |
| **nora_spatial** | trained | ✅ | ✅ | ✅ | ✅ | — |
| | untrained | ✅ | ✅ | ✅ | ❌ | — |

### 2. 缺口汇总

**唯一缺口：`nora_spatial/untrained/counterfactual_combined.json`**

### 3. 补跑状态

`nora_spatial_untrained_counterfactual.py` **正在运行**，有两个实例：
- PID 748325：`timeout 180` 包裹，CPU 765%，已运行 ~12 分钟
- PID 748707：tmux session `nora_spatial_cf` 中，CPU 636%，已运行 ~4 分钟

两个实例同时跑同一个脚本，可能会冲突（竞争写同一个输出文件）。建议 kill 其中一个（PID 748325 的 timeout 版本会先超时自杀，留 tmux 里的即可）。

### 4. Bootstrap v3

10 个 arch×suite × 2 conditions = 20 个文件，**全部完整**。

---
