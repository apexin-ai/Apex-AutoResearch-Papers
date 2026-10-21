# diag cwm8b shard3 failure

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cwm8b-shard3-failure_20260516T054405_result.json`
- **Structured JSON:** [`32c035dfa6941b09d775.json`](../../sessions/32/32c035dfa6941b09d775.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根因：实验已完成，非真正失败

实验**实际上已成功完成全部 1480 个样本的评估**。监控系统误判为失败。

**证据：**
- `results_incremental.jsonl` = 1480 行（覆盖 index 6200→7679，恰好 = test[6200:7680]）
- `eval_repo_cwm.json` 包含完整的 metrics 摘要（accuracy 64.26%, F1_macro 52.81%）
- 进程完成全部推理后正常退出，但未写入 sentinel 文件或上报 W&B，导致监控认为它是异常死亡

### 已回收数据

| 指标 | 值 |
|------|-----|
| 完成样本数 | 1480/1480 (100%) |
| Accuracy | 64.26% |
| F1 macro | 52.81% |
| Unparseable | 1076/1480 (72.7%) |
| Truncated | 75/1480 (5.07%) |

### 修复方案

无需重跑。数据已完整产出，只需：
1. 将该实验状态从 `failed` 标记为 `completed`
2. 如果需要合并到其他 shard 结果，直接使用 `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard3/` 下的文件即可

### GPU 状态
- GPU 0-2 空闲（0MiB），GPU 3 有其他任务在跑（21GB/32GB, 88% util）
- 无 OOM 迹象

---
