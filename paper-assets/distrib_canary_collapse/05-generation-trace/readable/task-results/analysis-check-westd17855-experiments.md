# analysis check westd17855 experiments

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_westd17855_experiments_20260519T051151_result.json`
- **Structured JSON:** [`70287b847a3e65527d82.json`](../../sessions/70/70287b847a3e65527d82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/westd17855_status_check.md`。

**摘要：**

| 实验 | 状态 |
|------|------|
| interv_pred_a075_s42_fp32_v4 | 已完成 (exit 0, 11/11 gen) |
| alpha_sweep_a060_s42_fp32_v3 | 已完成 (exit 0, 11/11 gen) |
| alpha_sweep_a005_s42_v3 | 已完成 (exit 0, 11/11 gen) |
| qwen35_08b_wiki_a100_s42_v2 | 运行中 (GPU 1, gen_5 训练 23%, 预计 ~4-5h 后完成) |
| smollm3_3b_wiki_a100_s42_v3 | **未找到** — 服务器上无任何痕迹（无进程/tmux/exit file/输出目录/log），可能从未成功提交 |

GPU 2-5 空闲，可用于重新提交 smollm3。GPU 0 另有 `scale_69b_a100_s42` 在跑。

---
