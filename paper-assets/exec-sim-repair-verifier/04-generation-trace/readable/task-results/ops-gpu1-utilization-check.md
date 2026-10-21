# ops gpu1 utilization check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu1-utilization-check_20260523T205114_result.json`
- **Structured JSON:** [`b777682ad7f4d6e63184.json`](../../sessions/b7/b777682ad7f4d6e63184.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查结果：

### CWM s42 ckpt300 reeval — **需要跑，可以上 GPU 1**

- **Checkpoint 存在**：`/root/autodl-tmp/checkpoints_backup_cwm_8b/checkpoint-300`（这是 s42 模型的 backup 目录）
- **无已完成结果**：eval_results 下没有任何 `*s42*300*` 的 reeval 目录
- **对称性**：GPU 0 正跑 s456 ckpt300 reeval，GPU 2 正跑 s123 ckpt300 reeval，缺的正好是 s42 ckpt300 reeval

### 当前 reeval 进度

| GPU | 任务 | 已完成行数 |
|-----|------|-----------|
| 0 | s456 ckpt300 reeval | 1,632 |
| 2 | s123 ckpt300 reeval | 1,480 |
| 3 | ckpt6100 eval | 6,416 |

### 结论

**GPU 1 应跑 CWM s42 ckpt300 reeval**，补齐三个 seed 的 ckpt300 reeval 对比。Checkpoint 路径是 `checkpoints_backup_cwm_8b/checkpoint-300`（注意不是 `checkpoints_repo_cwm_8b_conda`，后者没有 checkpoint-300）。

---
