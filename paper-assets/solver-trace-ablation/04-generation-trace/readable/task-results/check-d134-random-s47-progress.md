# check d134 random s47 progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d134-random-s47-progress_20260518T162052_result.json`
- **Structured JSON:** [`17f93bd0cf0965a80876.json`](../../sessions/17/17f93bd0cf0965a80876.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline log 中没有 COMPLETE/STARTING 标记（grep 无匹配），说明 pipeline 脚本不使用这些关键字。但从实际文件状态可以确认：

## 报告

| 项目 | 状态 |
|------|------|
| **s51 ISR** | **COMPLETE** — 目录含完整模型文件 + eval_results.json。prove_rate=0.98, mean_ISR=0.6992, proved_only_mean_ISR=0.7134 |
| **Random s47** | **训练中** — step 222/500 (44%), 已运行 ~47 min, 预计剩余 ~1h18m (~14s/step) |
| **GPU** | 90% 利用率, 85453 MiB 显存占用（正常，s47 在跑） |
| **磁盘** | 223G/250G (89%) — **剩余 28G，偏紧**。Random s47 训练完成后 checkpoint 会额外占用 ~16G，需关注是否触发 C003 |

磁盘 28G 余量需要注意：如果 save_total_limit=1 已配置则勉强够用，但后续还有 s51/s53 两个 Random seed 要训练，建议 s47 完成 eval 后及时清理旧 checkpoint。

---
