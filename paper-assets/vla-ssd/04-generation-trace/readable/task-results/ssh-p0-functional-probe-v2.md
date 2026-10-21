# ssh p0 functional probe v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0-functional-probe-v2_20260515T234809_result.json`
- **Structured JSON:** [`62456c802757296442b0.json`](../../sessions/62/62456c802757296442b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三件事全部完成。结果汇总：

### 1. Bootstrap CI: Projector vs Image_mean_trained_L19 — **PASS**

| | Mean R² |
|---|---|
| Projector (SigLIP+Proj) | 0.7063 |
| LLM image_mean L19 | 0.6832 |
| **Δ** | **+0.0231** |
| 95% CI | [0.0105, 0.0367] |
| p-value | < 0.001 |

CI 下界 > 0，projector 显著优于 LLM image_mean。

### 2. DINO Action Probe

| Source | Mean R² |
|---|---|
| DINO (cls_token) | **0.7116** |
| Projector | 0.7063 |
| LLM image_mean L19 | 0.6832 |

DINO vs Projector: Δ=+0.005, CI [-0.008, 0.019], p=0.22 — 无显著差异。
Action-delta probe: DINO 0.100, Projector 0.118 — 均较低。

**Three-way ordering: DINO ≈ Projector > LLM image_mean**

### 3. Untrained L10/L11 诊断 — **pathological_random_init**

Feature stats 正常（L10 std=5.29, L9 std=5.05，无 NaN/Inf/全零），但 probe R² 从 L9 的 0.632 骤降到 L10 的 0.029。结论：随机初始化 LLM 在 L10/L11 的内部表示虽然数值分布正常，但不包含可线性解码的 action 信息。

结果已保存到 `action_probe_v2.json` 并注册为 artifact `art_20260515_2a55c0`。

---
