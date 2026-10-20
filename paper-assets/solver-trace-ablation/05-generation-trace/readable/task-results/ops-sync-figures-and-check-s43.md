# ops sync figures and check s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync-figures-and-check-s43_20260515T040801_result.json`
- **Structured JSON:** [`267030e03d53154c7873.json`](../../sessions/26/267030e03d53154c7873.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 任务 1：图表同步 — 已是最新

远程和本地文件大小完全一致，无需重新同步：

| 文件 | 远程大小 | 本地大小 | 状态 |
|------|---------|---------|------|
| fig2_isr_collapse.pdf | 18,118 | 18,118 | 一致 |
| fig2_isr_collapse.png | 103,274 | 103,274 | 一致 |
| fig3_hacking_composition.pdf | 25,166 | 25,166 | 一致 |
| fig3_hacking_composition.png | 115,990 | 115,990 | 一致 |
| fig4 (remote: cross_logic / local: comparison) .pdf | 22,762 | 22,762 | 一致 |
| fig4 (remote: cross_logic / local: comparison) .png | 117,128 | 117,128 | 一致 |

本地 fig4 已正确命名为 `fig4_prolog_comparison`，匹配 `experiments.tex` 引用。

---

## 任务 2：exp1-random-b03-s43-r4 训练进度

**状态：训练中，尚未完成**

| 指标 | 值 |
|------|-----|
| 当前 step | 393 / 500 (79%) |
| 已运行 | ~1h 26m |
| 最新 checkpoint | checkpoint-350 |
| 平均 step 时间 | ~8.7s/step |
| 预计剩余 | ~15 min（107 steps × 8.7s） |
| GPU 0 | 83,123 / 97,887 MiB, 85% util |
| GPU 1 | 空闲 |

**最近 reward 趋势（step 389-393）：**
- prove_rate 多数 1.000，偶尔回落到 0.375
- ISR 在 0.076 ~ 0.330 之间波动
- reward 均值 ~1.0-1.15

训练预计约 15 分钟后完成。完成后需要手动触发 eval + classify_h7。

---
