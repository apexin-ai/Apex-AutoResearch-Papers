# check westd disk and pending

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_disk_and_pending_20260520T113007_result.json`
- **Structured JSON:** [`615ef0364f678362a429.json`](../../sessions/61/615ef0364f678362a429.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 磁盘状态 — P0 blocker 已解除

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 数据盘 `/root/autodl-tmp/` | 619G | 435G | **185G** | 71% |
| 根分区 `/root/` | 30G | 5.4G | 25G | 18% |

项目占 421G。磁盘不再是 blocker，ROADMAP 中 "westd 磁盘清理 ≥100GB" 可标记完成。

### GPU 状态 — 4 卡全占，cuda:0/1 并非空闲

| GPU | 任务 | 已运行 | 显存 | 利用率 |
|-----|------|--------|------|--------|
| cuda:0 | `eval_gsm8k` **pruned_cka_only_30** | 6h37m | 11.5G/98G | 85% |
| cuda:1 | `eval_gsm8k` **pruned_standard_30** | 6h37m | 11.5G/98G | 85% |
| cuda:2 | `eval_gsm8k` **grpo_standard_20_seed123** (n=1319) | 1h04m | 29.1G/98G | 91% |
| cuda:3 | `eval_gsm8k` **grpo_standard_20_seed456** (n=1319) | 1h04m | 29.1G/98G | 99% |

- cuda:0/1 跑的是 ROADMAP 中的 **"30% eval"**，已跑 6.5h，应该接近完成
- cuda:2/3 跑的是 **多种子 GRPO Standard×2 seed eval**（W-C4），1h in

### 释放后优先提交建议

cuda:0/1 完成后（预计很快），按优先级：

1. **CKA-only 多种子 GRPO seed eval**（W-C4 剩余 1 run）— 补齐 3-seed 实验，审稿硬需求
2. **15% GRPO 重启**（W-C6）— 之前被磁盘满阻塞，现在可以跑了
3. **v5 step-100 eval**（W-C2）— Table 2 修复

另外 **Bootstrap CI + McNemar's test**（W-S4）是纯 CPU 任务，可以立即提交不占 GPU。

---
