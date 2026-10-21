# gpu2 cls8b s456 retry

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu2-cls8b-s456-retry_20260519T124913_result.json`
- **Structured JSON:** [`54b8562bfb0f65cb6811.json`](../../sessions/54/54b8562bfb0f65cb6811.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。总结如下：

**失败原因**：`val=0` 导致 `KeyError: eval_loss`。`swebench_train.jsonl` 和 `swebench_val.jsonl` 今天被覆盖：
- 原始（s42/s123 训练用）：train=70748, val=9335（来自 89,867 条的完整 pilot_data）
- 当前（已损坏）：train=5504, val=1023（来自仅 7349 条的 pilot_data）

**数据丢失情况**：
- 完整的 `swebench_pilot_data.jsonl`（89,867 条）已被 7349 条的 pilot 版本覆盖
- `swebench_test.jsonl`（9784 条）未受影响（仍为 May 12 原始版本）
- 服务器无 `.git` 目录，无法从 git 恢复
- `swebench_full_s123_snapshot` 也是今天创建的（已是损坏后的数据）
- 全盘搜索未找到 >200MB 的原始训练文件

**根因**：今天 (May 19) 有人/某进程将 `data/swebench_pilot/swebench_pilot_data.jsonl`（7349 条 pilot 小数据集）复制到了 `data/swebench_full/swebench_pilot_data.jsonl`，然后运行了 `split_swebench_data.py` 重新切分，覆盖了原始的 train/val 文件。

**无法直接重试训练**——需要先恢复 70748/9335 的原始训练数据。重建需要 SWE-bench Docker 执行环境（`build_swebench_data.py --mode full`），该环境不在此服务器上。

需要确认：
1. 原始完整 pilot_data（89,867 条）是否在其他机器上有备份？
2. 是否有其他方式恢复（如从另一台服务器拷贝）？
3. 或者是否接受用当前数据（5504 train / 1023 val）重新训练所有 3 个 seed？

---
