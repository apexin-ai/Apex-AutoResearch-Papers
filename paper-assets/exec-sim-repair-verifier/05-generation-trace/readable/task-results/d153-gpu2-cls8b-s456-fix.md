# d153 gpu2 cls8b s456 fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_d153-gpu2-cls8b-s456-fix_20260519T121836_result.json`
- **Structured JSON:** [`d05f5bf4a0f6ff65ac27.json`](../../sessions/d0/d05f5bf4a0f6ff65ac27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### 完成的步骤
- **Step 1 (诊断)**: 完成
- **Step 2 (清理)**: 完成 - 空目录已删除
- **Step 3 (GPU 2)**: 确认空闲（0MiB, 0%）
- **Step 6 (Registry)**: `cls8b-repo-s456-train` 已标记为 DONE(failed)

### 阻塞：Step 4-5 无法执行

**根因**：训练数据在 May 19 11:14 被损坏。`swebench_full/swebench_pilot_data.jsonl`（原 89,867 行）被覆盖为 `swebench_pilot/` 的 10-instance 版本（7,349 行），MD5 完全相同。这导致 split 后 train=5,869（应为 70,748），val=0（应为 ~9,335）。

**验证**：s42 和 s123 的 trainer_state 均显示 step=6633, epoch=3.0 → 2211 steps/epoch × 32 = 70,752 samples，确认原始数据量。

**无法恢复的原因**：
1. 全磁盘搜索无备份（`find / -name "swebench_pilot_data.jsonl" -size +50M` 仅找到 swebench_fix_test 的小版本）
2. 无 Docker/swebench-harness 重新生成
3. 无 `logs/run_evaluation/` 评估日志
4. 非 git 仓库，无版本历史
5. `swebench_test.jsonl`（9,784 行，May 12）虽完好，但仅是 test split，无法逆推 train/val

### 需要你操作

恢复 `data/swebench_full/swebench_pilot_data.jsonl`（89,867 行），然后重新运行 `python split_swebench_data.py` 重建 train/val/test split。数据最初在一台有 Docker + swebench-harness 的机器上通过 `build_swebench_data.py --mode full --num_instances 500` 生成。恢复数据后我可以立即在 GPU 2 重启训练。

---
