# ops check unmonitored exps

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-unmonitored-exps_20260524T132454_result.json`
- **Structured JSON:** [`41f7cb7d44b02adca7fd.json`](../../sessions/41/41f7cb7d44b02adca7fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**实验 1: eval_pi05_l2norm_k095_long_seed42_postfix** (westd-38929)
- 状态：**运行中**，PID 401837，已运行 ~1h16m
- 进度：T0-T5 完成，正在跑 T6 (ep=30, 50% SR)
- 累计 SR：T0=96%, T1=100%, T2=98%, T3=98%, T4=100%, T5=96%，总计 292/300=97.3%
- 预计剩余 ~40min（还有 T6-T9 共 4.5 个 task）

**实验 2: eval_pi05_l2norm_k09_long_seed42_postfix** (cqa1-33015)
- 状态：**运行中**，PID 392492，已运行 ~26min
- 进度：T0 完成 (SR=96.0%)，10 个 task 中完成 1 个
- 已更新 registry：log_path → `eval_l2norm_k09_long_postfix.log`，pid → 392492
- 预计剩余 ~3h

已为两个实验创建 12 分钟间隔的 cron 监控（job 552a9e70 / 4ba7f5f4），进程结束后会自动更新 registry 为 DONE 并提取 metrics。

---
