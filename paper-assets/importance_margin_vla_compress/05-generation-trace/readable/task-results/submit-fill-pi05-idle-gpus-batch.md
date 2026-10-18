# submit fill pi05 idle gpus batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_fill_pi05_idle_gpus_batch_20260526T152152_result.json`
- **Structured JSON:** [`df6123dfbffec03c04e3.json`](../../sessions/df/df6123dfbffec03c04e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**发现：4 张卡全满，没有空闲 GPU。**

实际 GPU 占用：

| GPU | tmux session | PID | 任务 | 状态 |
|-----|-------------|-----|------|------|
| cuda:0 | eval_pi05_random_k085_long_seed42 | 384775 | random k=0.85 | 🏃 |
| cuda:1 | eval_pi05_l2norm_k085_long_seed42_v3 | 416018 | **l2norm k=0.85** | 🏃 |
| cuda:2 | eval_pi05_random_k07_long_seed42 | 467731 | random k=0.7 | 🏃 (刚启动 23:05) |
| cuda:3 | eval_pi05_attention_k085_long_seed42_v2 | 337369 | attention k=0.85 | 🏃 |

关键发现：

1. **实验 2 (l2norm k=0.85) 已经在 cuda:1 上跑了**，无需重复提交
2. **cuda:2 被 random k=0.7 占了**（不在 cliff curve 表里，k=0.7 不是必需数据点）
3. **attn k=0.5 v3 死因**：日志仅 31 行，跑到 T0 ep=20 (85%) 后进程静默死亡，无错误信息，tmux session 已不存在。可能是 OOM 或被误杀

**建议**：random k=0.7 不在 cliff curve 所需的 k 值列表中(0.95/0.9/0.85/0.75/0.5)，而 attn k=0.5 是 cliff curve 三方法收敛图的最后缺失点。是否 kill cuda:2 的 random k=0.7，腾出 GPU 给 attn k=0.5 v4？

---
