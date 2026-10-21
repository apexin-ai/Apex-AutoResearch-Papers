# ops harvest and deploy s47 batch2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_and_deploy_s47_batch2_20260529T040515_result.json`
- **Structured JSON:** [`20c0a1cf3326cc605e5d.json`](../../sessions/20/20c0a1cf3326cc605e5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 张 GPU 均被占用，无法立即部署新实验。汇报当前状态。

## 收割结果

3 个目标实验**均未完成**，全部仍在运行。

| exp_id | 服务器 | 当前进度 | 预计完成 (UTC) |
|--------|--------|----------|---------------|
| eval_pi05_random_k095_long_seed47_cqa1 | cqa1 cuda:0 | 刚启动 ~7min，初始化中 | ~15:30 |
| eval_pi05_attention_k050_long_seed47_w41 | w41 cuda:0 | T5 ep=40/50 (~55%) | ~13:20 |
| eval_pi05_attention_k085_long_seed47_w38 | w38 cuda:0 | T6 ep=20/50 (~62%) | ~13:00 |

## GPU 状态

| 服务器 | GPU | 当前实验 | 进度 | 预计释放 |
|--------|-----|---------|------|---------|
| cqa1 cuda:0 | Random k=0.95 s47 | 刚启动 | ~15:30 |
| cqa1 cuda:1 | Attn k=0.9 s47 | T2 ep=40 (~24%) | ~15:10 |
| cqa1 cuda:2 | Random k=0.9 s47 | T2 ep=10 (~22%) | ~15:55 |
| cqa1 cuda:3 | Random k=0.85 s47 | T2 ep=20 (~24%) | ~15:55 |
| w41 cuda:0 | Attn k=0.5 s47 | T5 ep=40 (~55%) | ~13:20 |
| w38 cuda:0 | Attn k=0.85 s47 | T6 ep=20 (~62%) | ~13:00 |

**6/6 GPU 全部占满，无空卡可部署。**

## 待部署（按释放顺序排队）

| 优先级 | exp_id | prune_mode | keep_ratio | 目标服务器 | 预计可部署 |
|--------|--------|-----------|------------|-----------|-----------|
| 1 | eval_pi05_l2norm_k085_long_seed47_w38 | l2norm | 0.85 | w38（最先释放） | ~13:00 UTC |
| 2 | eval_pi05_l2norm_k09_long_seed47_w41 | l2norm | 0.9 | w41 | ~13:20 UTC |
| 3 | eval_pi05_l2norm_k095_long_seed47_cqa1 | l2norm | 0.95 | cqa1 首个空卡 | ~15:10 UTC |
| 4 | eval_pi05_random_k05_long_seed47_cqa1 | random | 0.5 | cqa1 第二个空卡 | ~15:30 UTC |

需要约 1 小时后回来收割 w38/w41 的结果并部署前两个 L2norm 实验。要设置 cron 监控还是稍后手动回来检查？

---
