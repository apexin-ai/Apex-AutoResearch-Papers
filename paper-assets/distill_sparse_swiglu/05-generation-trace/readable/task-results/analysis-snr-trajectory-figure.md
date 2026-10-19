# analysis snr trajectory figure

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_snr_trajectory_figure_20260520T054147_result.json`
- **Structured JSON:** [`93d75e3da341f707f00e.json`](../../sessions/93/93d75e3da341f707f00e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表生成完成。

---

## 完整 14-snapshot 数据表

| Step | KL SNR | BCE SNR | BCE/KL Ratio |
|------|--------|---------|--------------|
| 0 | 1.296e-05 | 6.991e-05 | 5.39× |
| 50 | 2.533e-04 | 8.233e-06 | 0.03× |
| 100 | 6.114e-04 | 1.729e-03 | 2.83× |
| 150 | 5.700e-04 | 2.926e-03 | 5.13× |
| 200 | 2.357e-04 | 3.078e-03 | 13.06× |
| 250 | 2.331e-04 | 3.991e-03 | 17.12× |
| 300 | 3.464e-04 | 1.742e-03 | 5.03× |
| 400 | 3.389e-04 | 4.221e-03 | 12.46× |
| 500 | 3.500e-04 | 1.677e-03 | 4.79× |
| 600 | 5.836e-04 | 5.063e-03 | 8.68× |
| 700 | 2.145e-04 | 1.413e-03 | 6.59× |
| 800 | 2.971e-05 | 1.038e-03 | 34.95× |
| 900 | 5.524e-04 | 1.970e-03 | 3.57× |
| 1000 | 8.777e-04 | 2.026e-03 | 2.31× |

**Final summary (step 1000)**: KL SNR = 8.78e-04, BCE SNR = 2.03e-03, ratio = 2.31×

## 输出文件

- 脚本: `figures/paper/gen_snr_trajectory.py`
- PDF: `figures/paper/snr_trajectory.pdf`
- PNG: `figures/paper/snr_trajectory.png`

## 观察

从 step 100 起 BCE SNR 持续高于 KL（2-35×），step 50 是异常点（BCE 初始化阶段 SNR 骤降）。图上标注了核心 narrative: "signal strength ≠ signal quality"——BCE 梯度信噪比更高，但 KL downstream 表现更好。

---
