# ssh full status westd check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full_status_westd_check_20260522T150425_result.json`
- **Structured JSON:** [`74482bd0c1642aed6bf3.json`](../../sessions/74/74482bd0c1642aed6bf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-32935 全量状态

| GPU | 任务 | PID | 状态 | 进度 | 中间结果 | 备注 |
|-----|------|-----|------|------|----------|------|
| **0** | seed123 v2 GRPO eval | 56283 | **Running** | 62/1319 (5%) | acc=52.0%@50 | ~2.3s/it，稳定，预计再~50min |
| **1** | (seed123 v2 GRPO train) | 53822 | **Idle** | — | — | PID 已退出，训练已完成 |
| **2** | depth-first SFT eval | 54882 | **Running** | 62/1319 (5%) | acc=10.0%@50 | 有周期性卡顿（~5min/次），实际进度慢 |
| **3** | depth-first GRPO eval | 51986 | **Running** | 88/1319 (7%) | acc=8.0%@50 | 同样有周期性卡顿，eos_rate=92% |

**GPU 显存**: 0=17GB/98GB, 1=0/98GB, 2=29GB/98GB, 3=29GB/98GB

**磁盘**: /root/autodl-tmp/ 使用 588G/650G (91%)

### 注意事项

1. **GPU:2 和 GPU:3 的 eval 有严重卡顿**：每跑 ~15 个样本就停顿 5-6 分钟（进度条从 ~2s/it 跳到 ~100s/it）。GPU:0 的 eval 没有这个问题。按当前速度，GPU:2/3 的 eval 预计还需 **3-5 小时**。
2. **depth-first 两个模型的 acc 都极低**（SFT 10%, GRPO 8%），远低于 seed123 v2 的 52%。
3. **磁盘 91%**，还剩 63GB，暂时不紧急但需要关注。

---
