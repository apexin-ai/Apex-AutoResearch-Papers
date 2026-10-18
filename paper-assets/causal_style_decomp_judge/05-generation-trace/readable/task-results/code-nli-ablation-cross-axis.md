# code nli ablation cross axis

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nli_ablation_cross_axis_20260521T132507_result.json`
- **Structured JSON:** [`ddc510c95287ab97c3e5.json`](../../sessions/dd/ddc510c95287ab97c3e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验完成。结果验证：

**实验 B — NLI Gate Ablation**

| | Formality | Verbosity |
|---|---|---|
| **NLI-pass** (n=88/86) | BT=66.5%, CI=[58.5, 73.9], p<0.001 | BT=77.3%, CI=[70.3, 84.3], p<0.001 |
| **NLI-fail** (n=12/14) | BT=41.7%, CI=[16.7, 66.6], p=0.69 | BT=75.0%, CI=[53.6, 92.8], p=0.006 |
| **All** (n=100/100) | BT=63.5%, CI=[56.0, 70.5], p<0.001 | BT=77.0%, CI=[70.0, 83.5], p<0.001 |

NLI-pass BT 与 canonical 值一致（formality 66.5%, verbosity 77.3%）。NLI-fail formality 反转到 41.7%（不显著），说明 NLI gate 确实过滤了 content-contaminated pairs。Verbosity NLI-fail 仍然高（75.0%），因为 verbosity manipulation 即使 NLI 未通过，judge 偏好仍强。

**实验 C — Cross-Axis Gradient**

| Axis | NLI Rejection | BT | Likert d | GEE OR |
|---|---|---|---|---|
| Register | 6% | 55.3% | 0.069 | 1.91 |
| Formality | 12% | 66.5% | 0.012 | 4.20 |
| Verbosity | 14% | 77.3% | -0.146 | 13.10 |

输出文件：`data/nli_gate_ablation.json` 和 `data/cross_axis_gradient.json`。

---
