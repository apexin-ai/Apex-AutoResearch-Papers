# ssh search collapsed seed late checkpoints

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_search_collapsed_seed_late_checkpoints_20260522T215853_result.json`
- **Structured JSON:** [`e7f730e2b89347e91f64.json`](../../sessions/e7/e7f730e2b89347e91f64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完毕。结果如下：

---

**seed2048:**
- step5: 存在 — `qwen_seed2048_step5_hf`（HF）+ `seed2048_step5_ood_eval`（eval 输出）
- step10: **不存在**
- step15: **不存在**

**seed42:**
- step5: 存在 — `exp029_seed42_step5_hf` + `qwen_exp029_seed42_step5_hf`（HF）
- step10: **不存在**
- step15: **不存在**

**seed8:**
- step5: 存在 — `qwen_exp029_seed8_step5_hf`（HF）+ `exp029_seed8_ood_precollapse`
- step10: **不存在**
- step15: **不存在**

**结论：三个 collapsed seeds 的训练在 step5 之后没有保存任何 checkpoint。** 服务器上完全没有 step10/15 的 FSDP 或 HF checkpoint。训练大概率在 collapse 检测后被提前终止了。

作为对比，非 collapsed 的 seed（seed5）保存了 step10 checkpoint（`exp029-seed5/global_step_10` + `global_step_10_hf`），其他健康 seed 也有 step15（seed2, seed4, seed6 均有 `step15_hf`）。

**如果 Reviewer 需要 "collapsed seeds 不会在后期恢复" 的证据，需要重新训练这三个 seed 并让它们跑到 step10-15 保存 checkpoint，或者用训练日志中的 reward/accuracy 曲线来替代 OOD eval 作为间接证据。**

---
