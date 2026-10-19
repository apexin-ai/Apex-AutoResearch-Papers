# analysis factorial seed task comparison

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_factorial-seed-task-comparison_20260519T003751_result.json`
- **Structured JSON:** [`8ac1629f69525416fd02.json`](../../sessions/8a/8ac1629f69525416fd02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是我的调查结论：

## 结果

**无法从现有数据确定具体解了哪个 task。** 原因如下：

### 已检查的数据源

1. **日志文件** (`factorial_h2_episodeadv_seed1.log`, `factorial_seed2_v4.log`): 只有聚合指标，无 per-task breakdown。只能确认两个 seed 在 step 15 的 OOD success 都是 `0.007462686567164179` (1/134)。

2. **W&B 表格** (seed1 `val/generations_14`): 每步只采样 20/134 个 task。Step 15 采样的 20 个 task 全部 score=0，成功的那个 task 不在采样中。

3. **W&B 历史**: step 15 数据未同步到 W&B 服务器（seed1 只同步了 step 0/5/10，seed2 无 val 数据同步）。

4. **Checkpoints**: 无 factorial 实验 checkpoints 保存（`/root/autodl-tmp/checkpoints/` 下没有 factorial 目录）。

5. **validation_data_dir**: 配置为 `None`，未 dump per-task eval 结果。

### 可用信息对比

| 指标 | Seed1 (step 15) | Seed2 (step 15) |
|------|-----------------|-----------------|
| OOD success | 1/134 (0.75%) | 1/134 (0.75%) |
| avg num_actions | 7.60 | 48.37 |
| action_is_valid | 0.110 | 0.173 |
| action_is_effective | 0.157 | 0.969 |

两个 seed 的行为模式截然不同（seed1 平均 7.6 步就放弃，seed2 几乎用满 50 步），因此**很可能解的是不同的 task**，但无法从聚合指标确认。

### 建议方案

要确定具体 task，需要**重跑 eval 并开启 per-task 日志**：

1. 在 config 中设置 `validation_data_dir` 指向一个输出目录
2. 用 step 15 checkpoint 跑一次 eval-only
3. 从 dump 的 per-task 结果中找到 success=1 的 task

但 step 15 checkpoints 已不存在，因此需要**重新训练**或**从 W&B 上恢复 checkpoint**（如果有上传的话）才能得到答案。

---
