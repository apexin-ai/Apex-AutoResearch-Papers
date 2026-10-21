# research benchmark survey beyond libero

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_benchmark-survey-beyond-libero_20260519T163045_result.json`
- **Structured JSON:** [`6764b9f6726a59f49d7b.json`](../../sessions/67/6764b9f6726a59f49d7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/benchmark_survey.md`。核心结论：

**P0 必做 — LIBERO-Goal + LIBERO-Long**: 零代码改动，只改配置即可扩展到完整 4-suite 评估（社区标准协议）。LIBERO-Long 上 SmolVLA 仅 71%，CRM 改进空间最大，且长 horizon 的 error compounding 天然适合 correction 方法的叙事。

**P1 强烈建议 — CALVIN**: 7D action space 直接兼容，~23K demo trajectories 充足，5-subtask chain 评估适合展示 correction 方法。瓶颈是需要 fine-tune SmolVLA-CALVIN checkpoint（~4h A100 + 1-2 周工程）。

**P2 可选 — SimplerEnv/Bridge V2**: 7D action space 兼容，有 real-to-sim 叙事价值，但需要 SmolVLA-Bridge checkpoint 且任务较简单。

**不推荐**: RLBench（keyframe action space 不兼容）、MetaWorld（4D 无旋转，CRM 退化）。

---
