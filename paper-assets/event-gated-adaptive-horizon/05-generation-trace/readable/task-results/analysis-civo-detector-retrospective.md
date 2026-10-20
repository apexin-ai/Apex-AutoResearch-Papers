# analysis civo detector retrospective

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_civo-detector-retrospective_20260517T020739_result.json`
- **Structured JSON:** [`d48285bc8640e2d43b18.json`](../../sessions/d4/d48285bc8640e2d43b18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `artifacts/civo_detector_retrospective.json`。

**关键发现：**

| 指标 | 结果 |
|------|------|
| CIVO 检测率 | 2/2 (100%) |
| 平均提前步数 | 10K (008d: 15K, 010b: 5K) |
| 健康组误报率 | 2/3 (67%) |

**CIVO 组（真阳性）：**
- **008d**: Level 2 在 45K 触发，collapse 在 60K，提前 15K 步预警。VE ratio 从 0.15→0.41→0.69→1.67 持续加速上升。
- **010b**: Level 2 在 65K 触发，collapse 在 70K，提前 5K 步。VE 在 55K-65K 从 1.02 飙到 3.18。

**健康组（假阳性问题）：**
- **008f**: 早期训练波动（eval 206→194→173）触发了 Level 2，但实验后来恢复到 503。
- **baseline**: 收敛后微小波动（eval ~930±20，VE ~0.70±0.02）触发了 Level 2。
- **008a**: 无误报（正确）。

**边界组：**
- **009b** (自纠正): 无 Level 2 触发，检测器正确忽略。
- **008e_v3_s2** (非 CIVO collapse): Level 2 仅在 collapse 后才触发（105K > 95K collapse）。VE ratio 在 collapse 前一直健康（<0.51），因为这不是 value overestimation 导致的崩溃。

**规则弱点**：当前规则对正常 eval 方差过于敏感。改进方向：加入 delta_ve 最小幅度门槛（如 >0.1）、要求 ve_ratio 已超过 0.5 后才启用检测、或用 eval_return 下降百分比替代绝对下降。

---
