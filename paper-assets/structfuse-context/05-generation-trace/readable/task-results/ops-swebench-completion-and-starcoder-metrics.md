# ops swebench completion and starcoder metrics

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_swebench-completion-and-starcoder-metrics_20260516T025336_result.json`
- **Structured JSON:** [`bcca897ca8b71e672f2b.json`](../../sessions/bc/bcca897ca8b71e672f2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 任务 1: SWE-bench random_s42 eval

**PID 61328: DONE**（进程已结束）

**异常**: eval 并未完成。

- `summary.json` **不存在**
- `per_instance_results.jsonl` 只有 **4 行**（不是预期的 99 或 100）
- 日志显示：加载了 300 个 SWE-bench Lite 实例，仅处理到 **4/300 就被 Terminated**

日志末尾关键行：
```
Evaluating:   1%|▏         | 4/300 [08:05<9:34:07, 116.38s/it] Terminated
```

eval 被外部 kill 了，未正常完成。

---

## 任务 2: StarCoder embedding_distance_s42

训练完成，early stopping 触发于 step 1500（patience=2，best val_loss 在 step 500）。

| Step | val_loss | R@1 | R@5 | R@10 |
|------|----------|------|------|------|
| 500 | **0.6154** | 0.4372 | 0.9094 | 1.0 |
| 1000 | 0.6466 | **0.4567** | 0.9128 | 1.0 |
| 1500 | 0.6835 | 0.4473 | 0.8973 | 1.0 |
| Final | 0.6927 | 0.4376 | 0.8977 | 1.0 |

- **Best val_loss** = 0.6154 @ step 500 → `best_by_val_loss/`
- **Best R@1** = 0.4567 @ step 1000 → `best_by_recall_at_1/`
- Final model → `final/`

Checkpoints 路径: `/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/embedding_distance_s42/`

---

## 任务 3: Watcher PID 验证

**PID 966920: 存活**

```
PID     CMD                          ELAPSED
966920  bash /root/structfuse/watch  1-11:20:23
```

已运行 1 天 11 小时 20 分钟，正常。

---
