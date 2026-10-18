# check simplerenv westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_simplerenv_westd27271_20260524T193031_result.json`
- **Structured JSON:** [`7c6abb667ccf4bc0a6c4.json`](../../sessions/7c/7c6abb667ccf4bc0a6c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成并更新 registry → DONE (negative)。

## 结果汇总

| Task | Baseline SR | L2norm k=0.9 SR |
|------|:-----------:|:---------------:|
| PutCarrotOnPlate | 0.0% (0/50) | 0.0% (0/50) |
| PutSpoonOnTableCloth | 0.0% (0/50) | 0.0% (0/50) |
| StackGreenCubeOnYellowCube | 0.0% (0/50) | 0.0% (0/50) |
| PutEggplantInBasket | 0.0% (0/50) | 0.0% (0/50) |
| **平均** | **0.0%** | **0.0%** |

**关键发现**：Baseline 本身就是 0%，说明问题不在 pruning，而在 OpenVLA-7B + ManiSkill3 的 sim 评估流程。可能的原因：
1. **transformers 版本不匹配** — 日志警告 expected 4.40.1 但实际 5.5.4，可能导致 inference 退化
2. **action 接口 / unnormalization 问题** — ManiSkill3 的 action space 与 OpenVLA 输出可能不兼容
3. **Sim-to-real gap** — OpenVLA Bridge 模型在 ManiSkill3 仿真器中表现可能本身就很差

这两个实验的比较结论无效（baseline 为零时无法评估 pruning 影响）。需要先修复 baseline 才能继续 SimplerEnv 方向的实验。

---
