# ssh exp020 v4 mfrm only 317

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp020-v4-mfrm-only-317_20260525T155812_result.json`
- **Structured JSON:** [`95e77c0309eefa070a03.json`](../../sessions/95/95e77c0309eefa070a03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

**v4 MFRM-only τ = 0.824** vs v3 G-MFRM τ = 0.809 → **contamination gating 轻微有害**

关键发现：
- MFRM-only 与 raw_average 产生 **完全相同的排名**（互相关 τ=1.000）
- v4 去掉 c_n·e_i 项后 τ 反而提高了 0.015
- 收敛良好：R̂=1.006, ESS=1118, div=0
- 受 contamination gating 影响最大的模型：gpt-4-turbo（c=4.015，v3 排名被压到第 4，v4 恢复到第 2）、gpt-4-0613（c=4.263，θ 偏移 +0.539）

结论：在 317 items 子集上，contamination gating 不仅没有提升 Arena 对齐度，反而引入了少量噪声。结果已保存到 `/root/gated_mfrm_judge_bias/v4_results.txt`。

---
