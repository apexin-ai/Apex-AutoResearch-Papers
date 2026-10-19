# monitor m2 m1 status check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_m2-m1-status-check_20260513T025149_result.json`
- **Structured JSON:** [`18aeb3eca84319651363.json`](../../sessions/18/18aeb3eca84319651363.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，汇总如下。

---

```
=== M2 Early Pilot ===
PID 795791: 存活（运行 ~57 分钟）
GPU 4: 9342 MiB / 24564 MiB, 83% 利用率
状态: 运行中 — 策略 random, Epoch 2 刚开始（Epoch 1 完成 1300 steps）

训练顺序: random → embedding_distance → dataflow_aware（各 3 epochs）
当前在第 1 个策略的 Epoch 2。

Eval 指标 (random 策略):
  eval@500:  val_loss=0.5391  recall@1=0.5134  recall@5=0.5134  recall@10=0.5134  ← best
  eval@1000: val_loss=0.5492  recall@1=0.5281  recall@5=0.5281  recall@10=0.5281

Checkpoints:
  m2_pilot_random_s42/best/ — model.pt + tokenizer（best val_loss=0.5391 时保存）

注意: recall@1/5/10 值相同，可能候选集太小或评估逻辑有问题。

=== M1 提取 ===
PID 577864: 存活（运行 6h04m）
131 unique (repo, commit) groups，50869 instances 总量
已启动: 26/131 repos（含 1 个 clone 失败: pdfminer）
预估总时间: ~54h (8 workers)，当前约 11% 进度

最新进度（各 repo 最后汇报）:
  oauthlib/oauthlib:              850/940   接近完成
  Cog-Creators/Red-DiscordBot:    450/460   接近完成
  mahmoud/boltons:                600/737
  pygments/pygments:              550/1430
  cantools/cantools:              500/1440
  pyupio/safety:                  450/759
  marshmallow-code/webargs:       250/321
  joke2k/faker:                   200/360
  google/textfsm:                  50/79
  小 repo (seatgeek/thefuzz 32, madzak/python-json-logger 38, Knio/dominate 42 等) 已完成或接近完成

跳过(clone 失败): pdfminer/pdfminer 660 instances
skip_log: 660 条

磁盘: 53G free / 169G total (70% used)

=== 数据盘总览（迁移用）===
M1 数据:   2.5G   /root/autodl-tmp/structfuse/m1_extraction/
M2 数据:   879M   /root/autodl-tmp/structfuse/m2_pilot_data/
Checkpoints: 5.8G   /root/autodl-tmp/structfuse/checkpoints/
模型:      5.8G   /root/autodl-tmp/structfuse/models/
HF cache:  22G    /root/autodl-tmp/.hf_cache/
代码:      31G    /root/structfuse/（含 data/.git 等，实际代码远小于此）
```

**关键问题**: recall@1 = recall@5 = recall@10 完全相同（0.513/0.528），建议训练完成后检查 eval 逻辑——可能是候选池大小 ≤ 1 或 ranking 没有真正区分。

---
