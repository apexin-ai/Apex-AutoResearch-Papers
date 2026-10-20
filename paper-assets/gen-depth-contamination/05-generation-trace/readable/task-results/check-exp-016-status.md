# check exp 016 status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_016_status_20260516T031858_result.json`
- **Structured JSON:** [`06d29301aed796cbfc67.json`](../../sessions/06/06d29301aed796cbfc67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_016 实验状态：**中断**

**发生了什么：**
- 实例在 ~11:07-11:08 UTC 重启（tensorboard/jupyter 在 11:08 重新启动），tmux session `exp016` 被杀，实验进程消失。

**已完成：**
- depth_0: 5000 samples ✓ (09:13)
- depth_1: 5000 samples ✓ (09:46)
- depth_2: 5000 samples ✓ (10:18)
- depth_3: 5000 samples ✓ (10:51)

**中断点：**
- depth_4: 51% (160/313 batches) 时被杀，未生成 depth_4.jsonl
- depth_5: 未开始
- 分类/AUC 分析阶段: 未执行（`results_exp016_qwen_base/` 为空）

**时间线估算：**
- 每个 depth ≈ 32 分钟（313 batches × ~6.2s/it）
- 需补跑 depth_4 (完整) + depth_5 ≈ 64 分钟
- 加上分类分析 ≈ 总计 ~70-80 分钟

**文件位置：**
- 日志: `/tmp/exp016.log`
- 数据: `/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/`
- 结果目录: `/root/autodl-tmp/gen-depth-contamination/results_exp016_qwen_base/` (空)

**原因：** AutoDL 实例重启（可能是空闲超时或平台维护）。

**需要操作：** 重新提交实验，需支持从 depth_4 断点续跑（跳过已有的 depth_0-3），否则需全量重跑。是否要我检查脚本是否支持断点续跑并重新启动？

---
