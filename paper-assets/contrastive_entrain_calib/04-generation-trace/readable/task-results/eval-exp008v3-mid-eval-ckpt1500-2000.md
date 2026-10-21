# eval exp008v3 mid eval ckpt1500 2000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp008v3-mid-eval-ckpt1500-2000_20260519T213822_result.json`
- **Structured JSON:** [`9870050f41208040d870.json`](../../sessions/98/9870050f41208040d870.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ckpt-2000 也完成了。两个结果都出来了。

---

## exp-008v3 Mid-Eval 结果

| Checkpoint | ToF | NoF | SYCONScore | Samples |
|---|---|---|---|---|
| **ckpt-1500** | 0.0000 | 0.9945 | **0.0000** | 362 |
| **ckpt-2000** | 0.0000 | 1.0000 | **0.0000** | 362 |
| Vanilla baseline | — | — | **0.134** | — |
| ACT (exp-004) | — | — | **0.301** | — |

## 对比分析

- ckpt-1500/2000 的 SYCONScore = 0.000，远低于 vanilla baseline (0.134)
- 模型 NoF 接近/等于 1.0：binary probe GRPO 训练让模型**完全拒绝修改答案**，无论用户纠正是否合理
- 从 ckpt-1500 到 ckpt-2000，NoF 从 0.9945 升到 1.0000，说明训练越久模型越顽固
- 这是一个典型的 reward hacking / mode collapse：模型学到了"永远不改答案"就能获得高 reward

## 结论：Story B is **dead**

Binary probe R1 (GRPO) 完全失败。模型没有学会区分 warranted vs sycophantic revision，而是直接坍缩到"永远不修改"的策略。

## 结果文件路径

- ckpt-1500: `/root/autodl-tmp/results/exp008v3_ckpt1500_eval/default_preset_eval.json`
- ckpt-2000: `/root/autodl-tmp/results/exp008v3_ckpt2000_eval/default_preset_eval.json`
- 摘要: 同目录下 `default_preset_summary.txt`

---
