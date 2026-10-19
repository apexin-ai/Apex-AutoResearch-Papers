# diagnose eval random selection object k5 seed43 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-random-selection-object-k5-seed43-r2_20260519T162712_result.json`
- **Structured JSON:** [`f5400ae4eff9f37c1c42.json`](../../sessions/f5/f5400ae4eff9f37c1c42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断报告

### 失败根因

**这些实验并没有真正失败。** 所有在 bjb2-28827 上能查到日志的实验都**正常运行完毕**，结果已保存为 JSON 文件：

| 实验 | 状态 | 结果 |
|------|------|------|
| random_selection_k5_seed43 | 正常完成 | 11/100 (11.0%), JSON 已保存 |
| obs_only_spatial_norm02_k5_seed44 | 正常完成 | 37/100 (37.0%), JSON 已保存 |
| obs_only_spatial_norm02_k5_seed45 | 正常完成 | 34/100 (34.0%), JSON 已保存 |

日志中无 Traceback、Error、OOM 或任何异常。

### 误报原因

评估脚本 (`src/evaluate.py`) **既不写 sentinel 文件，也不集成 W&B**。监控系统的判定逻辑是 "process dead 5× with no sentinel/W&B → auto-resolved as failed"，但实际上进程是正常退出（exit code 0），只是不符合监控系统的完成信号约定。

`logs/sentinels/` 目录为空，从未写入过任何 sentinel 文件。

### 系统性问题

不是系统性问题。服务器状态健康：
- **磁盘**：根分区 32% (21GB free)，数据盘 7% (235GB free)
- **GPU**：6×RTX 4090 均正常，当前有 3 个 GPU 在跑其他任务
- **无 OOM/CUDA 错误**

### 对当前运行实验的影响

**无影响。** seed46 的 random_selection 评估目前仍在正常运行中（日志显示正在执行 rollout）。

### 建议修复

1. **这些实验无需重跑**——结果已完整保存在 JSON 文件中，直接使用即可
2. **修复监控误报**：在评估脚本完成后写一个 sentinel 文件（如 `touch logs/sentinels/&lt;experiment_name>.done`），或调整监控系统使其检查 JSON 输出文件的存在作为完成信号
3. seed44、seed45 的 random_selection_k5 日志不在 bjb2-28827 上（只有 seed43），如果需要确认它们也已完成，需要到对应服务器上检查

---
