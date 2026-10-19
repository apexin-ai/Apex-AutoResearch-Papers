# ops kill duplicate eval cuda1

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-duplicate-eval-cuda1_20260516T031104_result.json`
- **Structured JSON:** [`bf1a8e6e897fdb642467.json`](../../sessions/bf/bf1a8e6e897fdb642467.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况与预期不同。报告：

### PID 708166 & 738549
两个进程**都已经死掉了**，不需要 kill。

### baseline_std_v3/libero_10 eval 进度
输出目录只有一个空的 `videos/` 子目录，无 `eval_info.json`。eval 似乎没有产出有效结果就终止了。

### GPU 占用 (当前)

| GPU | PID | 显存 | 进程 |
|-----|-----|------|------|
| GPU 0 (b869) | 675231 | 5910 MiB | lerobot-eval baseline_plus_v2/libero_10 |
| GPU 0 (b869) | 682233 | 16214 MiB | train_acib.py acib_v5_div_reg |
| GPU 1 (5c82) | 733616 | 6601 MiB | 未知（进程列表中未匹配到） |
| GPU 1 (5c82) | 736291 | 16216 MiB | train_acib.py acib_v5_div_reg_seed2 |

### 新问题：seed2 重复进程
GPU 1 上有**多个** train_acib.py 进程都指向同一 output_dir `acib_v5_div_reg_seed2`：
- PID 736291（运行 11m28s）
- PID 738721, 738722, 738723, 738725（运行 ~9m55s）

这些可能是 DataLoader worker 子进程（正常），但也可能是重复启动。需要确认是否要处理？

---
