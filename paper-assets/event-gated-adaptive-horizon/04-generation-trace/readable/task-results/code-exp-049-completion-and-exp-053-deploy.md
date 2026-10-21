# code exp 049 completion and exp 053 deploy

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_049_completion_and_exp_053_deploy_20260523T034532_result.json`
- **Structured JSON:** [`f8865c662e6e6a18db99.json`](../../sessions/f8/f8865c662e6e6a18db99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两步任务均完成。汇报如下：

---

## exp_049 最终指标（DONE, success）

| 指标 | 值 | Step |
|------|-----|------|
| eval_final | **34.88** | 212,500 |
| eval_peak | **35.89** | 182,500 |
| ve_ratio_final | **0.186** | 212,500 |
| ve_ratio_peak | **3.27** | 32,500 |
| total_steps | 222,500 (实际运行，因 dreamer loop 多跑 eval_every) | — |

结论：CIVO 在 StackCube manipulation 上触发（32.5K ve_ratio=3.27），随后自修复到 0.186。eval_return 最终 34.88 接近峰值 35.89，训练未崩溃。

备注：dreamer 训练循环实际跑到 `steps + eval_every`（222.5K），不是 210K。后续实验需注意。

---

## exp_053 部署结果

| 项目 | 值 |
|------|-----|
| PID | **123495** |
| GPU | GPU 1（2754 MiB） |
| 状态 | 正常训练中，已过 prefill（2500 步） |
| dt_emb_freeze | 确认 True（gate_dt_mean=2.0 固定） |
| 日志 | `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_053_peginsertion_frozen_s0.log` |

---
