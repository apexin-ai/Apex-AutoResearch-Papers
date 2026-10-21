# check olmo d4d5 002 status

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_olmo_d4d5_002_status_20260515T112537_result.json`
- **Structured JSON:** [`304d43cc95dcf80ec1c3.json`](../../sessions/30/304d43cc95dcf80ec1c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告：depth_extension_olmo_d4d5_002

| 检查项 | 结果 |
|--------|------|
| **PID 213793** | 已结束（进程不存在） |
| **tmux session** | 无法通过 read_only 检查（tmux 被拦截），但进程已完成，无影响 |
| **日志最后状态** | **成功完成**，EXIT_CODE=0 |
| **GPU 0** | 55% 利用率，15641/97887 MiB（有其他任务在跑） |
| **GPU 1** | 空闲，0% 利用率，0 MiB |
| **features_6class.jsonl** | 存在，20.6 MB，30000 行 |

### 完成内容

实验已于 **2026-05-15 18:40:50 CST** 成功完成（Step 5-7 全部跑完）。产出：

- `features_6class.jsonl` — 30000 行（6 class × 5000 samples）
- `classification_report.txt`
- `confusion_matrix.png`
- `feature_importance.json`
- `pairwise_auc.json`
- `binary_pairwise/binary_pairwise_results.json`

Binary pairwise sanity check 结果：
- d1v2: AUC=0.9680（vs 4-class 0.8607，Δ=+0.1073）
- d2v3: AUC=0.8429（vs 4-class 0.8005，Δ=+0.0424）

进程已正常退出，无需恢复操作。

---
