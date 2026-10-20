# draw fig counterfactual bar

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_draw_fig_counterfactual_bar_20260523T170127_result.json`
- **Structured JSON:** [`6fa3e9fb5ff973b5dc6b.json`](../../sessions/6f/6fa3e9fb5ff973b5dc6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成完毕。

**输出文件：**
- `/root/vla-ssd/paper_figures/fig_counterfactual_bar.pdf` (27 KB)
- `/root/vla-ssd/paper_figures/fig_counterfactual_bar.png` (137 KB, 300 dpi)

**数据汇总：**

**上面板 — Cohen's d（trained VLAs）：**

| Arch-Suite | empty | wrong | shuffled | paraphrased | empty最高? |
|---|---|---|---|---|---|
| OpenVLA-Goal | 1.17 | **1.18** | 1.10 | 1.00 | ✗ (wrong最高) |
| OpenVLA-Spatial | **1.17** | 0.88 | 0.98 | 0.81 | ★ |
| TracVLA-Goal | **1.52** | 1.40 | 1.34 | 1.21 | ★ |
| TracVLA-Spatial | **1.33** | 1.17 | 1.29 | 1.18 | ★ |
| TracVLA-Object | **1.21** | 1.06 | 1.16 | 0.97 | ★ |
| TracVLA-Long | **1.47** | 1.42 | 1.39 | 1.16 | ★ |

**下面板 — Cosine distance（untrained base VLMs）：**

| Arch-Suite | empty | wrong | shuffled | paraphrased |
|---|---|---|---|---|
| TracVLA-Goal | **0.153** | 0.016 | 0.084 | 0.004 |
| TracVLA-Spatial | **0.181** | 0.005 | 0.140 | 0.004 |
| TracVLA-Object | **0.185** | 0.004 | 0.098 | 0.005 |
| TracVLA-Long | **0.173** | 0.022 | 0.120 | 0.007 |
| NORA-Goal | **0.081** | 0.014 | 0.033 | 0.004 |
| NORA-Spatial | **0.081** | 0.002 | 0.031 | 0.005 |

所有下面板 + 5/6 上面板组中 empty 条件排名第一（已标 ★）。唯一例外是 OpenVLA-Goal 的 wrong 略高于 empty（1.1821 vs 1.1696）。无 NORA 值 ≥ 0.95，故未使用 "sat." 标注。

---
