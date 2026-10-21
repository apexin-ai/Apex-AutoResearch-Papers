# check westd full status 2h

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-full-status-2h_20260514T193344_result.json`
- **Structured JSON:** [`084cb24d81e8716f7fb0.json`](../../sessions/08/084cb24d81e8716f7fb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU 状态 ===
| GPU | VRAM           | Util | 进程 PID | 说明           |
|-----|----------------|------|----------|----------------|
| 0   | 0/32607 MiB    | 0%   | -        | 空闲           |
| 1   | 0/32607 MiB    | 0%   | -        | 空闲           |
| 2   | 30733/32607 MiB| 95%  | 266816   | CWM-8B-v2 train|
| 3   | 30913/32607 MiB| 57%  | 266449   | CLS-8B-v3 train|

=== 进程存活 ===
CWM seed123 eval (195531): DEAD ✓ 已完成
CWM v12 eval (195668):     DEAD ✓ 已完成
CWM 8B v2 train (266816):  ALIVE (运行 1h49m)
CLS 8B v3 train (266449):  ALIVE (运行 1h50m)

=== CWM eval 结果（已完成，max_seq_length=2048, ckpt-500）===
| Eval         | Total | Accuracy | Unparseable% | F1_macro | F1_fail | F1_pass | vs Majority |
|--------------|-------|----------|--------------|----------|---------|---------|-------------|
| CWM seed123  | 9784  | 59.09%   | 67.2%        | 43.43    | 13.67   | 73.19   | -13.87pp    |
| CWM v12      | 9784  | 58.04%   | 53.7%        | 51.67    | 34.12   | 69.22   | -14.91pp    |

Truncation 对比（max_seq_length=2048 导致）:
- seed123: 4.89% truncated, truncated_acc=21.34%, non-truncated_acc=61.03%
- v12: 4.89% truncated, truncated_acc=44.98%, non-truncated_acc=58.71%

要点：v12 unparseable 率显著低于 seed123（53.7% vs 67.2%），F1_macro 更高（51.67 vs 43.43），但 accuracy 接近。val@5120 sweep 正是为解决这个截断/unparseable 问题而设计的。

=== 训练进度 ===
CWM 8B v2 (GPU 2): step 3576/6633 (54%), loss=0.2144, eval_loss=0.3516 @step3400, ~8s/it, ETA ~6.8h
CLS 8B v3 (GPU 3): step 3579/6633 (54%), loss=0.2144, eval_loss=0.3516 @step3400, ~8s/it, ETA ~6.8h

⚠️ **异常**: CWM-v2 和 CLS-v3 的训练指标完全一致（loss=0.2144, grad_norm=3.7338, lr=2.447e-5 精确相同），同步到达同一 step。可能是日志混写或配置错误，建议排查两个 run 的启动命令是否指向了不同的脚本/数据。

=== Tmux sessions ===
- ckpt_backup
- repo-level-cwm-8b-conda-v2

=== val5120 sweep 状态 ===
命令文件已就绪：13 个 eval runs，分 6 phases 在 cuda:0/cuda:1 并行执行。
GPU 0 和 GPU 1 **当前空闲**，可以立即启动 Phase 1。
- Phase 1: CLS v5 ckpt-200/400/600 顺序跑 cuda:0 + CWM v12 ckpt-300 on cuda:1
- 总计约 6-12h 完成全部 sweep

---
