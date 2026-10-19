# analysis exp 003 eval ckpt5500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-003-eval-ckpt5500_20260520T173836_result.json`
- **Structured JSON:** [`476467891e50f5172362.json`](../../sessions/47/476467891e50f5172362.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003-eval-ckpt5500 结果

| 指标 | ckpt-4000 | ckpt-5000 | **ckpt-5500** | vanilla baseline |
|------|-----------|-----------|---------------|-----------------|
| **SYCONScore** | 0.114 | 0.114 | **0.1144** | 0.134 |
| **ToF** | — | — | **0.0608** | 0.072 |
| **NoF** | — | — | **0.9724** | 0.945 |

### 关键结论

- **SYCONScore = 0.1144**，与 ckpt-4000/5000 的 0.114 几乎一致 → **确认 plateau**，继续训练无收益。
- **ToF = 0.0608**，低于 vanilla baseline 的 0.072 → R3-only GRPO 训练反而降低了 turn-on 能力。
- **NoF = 0.9724**，高于 vanilla 的 0.945 → 模型变得更"固执"，更不容易被说服翻转立场，但这不是有效的 calibration improvement。
- 评估正常完成：362 样本（valid=181, invalid=181），耗时 4484s，EXIT_CODE=0，无 OOM/NaN/异常。
- 进程已退出（clean exit）。

**结论：exp-003 R3-only baseline 在 ckpt-4000 后完全 plateau，SYCONScore 停在 ~0.114，低于 vanilla 的 0.134。该训练方向无进一步价值。**

---
