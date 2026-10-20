# eval dr q05 ckpt5500 cuda0

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_dr_q05_ckpt5500_cuda0_20260525T032625_result.json`
- **Structured JSON:** [`e02143c78d4b1022f2e7.json`](../../sessions/e0/e02143c78d4b1022f2e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇报：**

| 项目 | 状态 |
|------|------|
| Checkpoint | `/root/autodl-tmp/.../detect_remove_q05_seed42/checkpoint-5500/` ✓ |
| GPU | cuda:0 (RTX PRO 6000 Blackwell, 98GB), PID 5867 运行中 |
| Eval 顺序 | holdout → openwebtext → wikipedia（串行，各 5000 docs） |
| 输出文件 | `eval_results_dr_q05_ckpt5500_{holdout,owt,wiki}.json` |
| 日志 | `/tmp/eval_dr_q05_ckpt5500.log` |
| Registry | `eval_dr_q05_ckpt5500` → RUNNING, parent=detect_remove_q05_seed42 |
| 父进程 PID | 5861 (nohup bash) |

当前正在评估 holdout 数据集（模型已加载完毕）。预计三项 eval 总计 30-60 分钟完成。可用 `tail /tmp/eval_dr_q05_ckpt5500.log` 查进度。

---
