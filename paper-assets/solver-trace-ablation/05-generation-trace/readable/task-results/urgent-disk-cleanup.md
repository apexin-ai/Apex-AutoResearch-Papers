# urgent disk cleanup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_disk-cleanup_20260514T114152_result.json`
- **Structured JSON:** [`ed2c7ce247432592d2b8.json`](../../sessions/ed/ed2c7ce247432592d2b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**1. 磁盘清理：释放 90G**（142G → 52G used, 21%）
- 清理了 plan001_exec_only_s42, plan002_additive_b01_s42, plan016_extended_1000_s42, plan018_additive_random_b01_s42 的模型文件
- eval JSON 已备份到 `/root/autodl-tmp/eval_backups/`
- plan006_prolog_exec_s42 未动（需要 eval）

**2. plan018-s44 存活状态**
- PID 564900 存活，step 25/500，GPU 0 正常训练

**3. plan006-prolog-exec-s42 eval 结果**

| 指标 | exec-only | sta-only (对比) |
|---|---|---|
| prove_rate | 83% | 50% |
| mean_isr | 0.031 | 0.5 |
| proved_only_isr | 0.037 | 1.0 |
| H7 rate | 0% | 100% |
| H1 rate | 0% | 0% |

核心发现：exec-only 和 STA 产生截然不同的失败模式。exec-only 生成 "creative shortcut proofs"（可执行但不走 gold-standard 步骤），STA 生成 "trivial copy"（H7 hacking）。

**4. Registry 已更新** — plan006-prolog-exec-s42 状态 → DONE, conclusion → success

**注意：** GPU 1 上同时有 plan009-sft-baseline-s42-r4 训练在运行（PID 572609），另一个 worker 提交的。

---
