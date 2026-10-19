# diagnose check hsweep h5 data

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_check-hsweep-h5-data_20260518T163408_result.json`
- **Structured JSON:** [`23a5e4860b96978f9432.json`](../../sessions/23/23a5e4860b96978f9432.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整诊断结果。

---

## 诊断结果

### 1. hsweep_h5_seed1：不存在

Registry 中**没有名为 `hsweep_h5_seed1` 的实验**。h-sweep 系列只包含：
- `hsweep_h2_seed1` (DONE, success)
- `hsweep_h2_seed2` (DONE, success)
- `hsweep_h10_seed1` (DONE, killed)

最接近 "h=5" 的是 gamma sweep 系列中的 **`gsweep_g095_h5_seed1`**（γ=0.95, h=5），这实际上就是 h=5 的控制条件（registry hypothesis 写明 "control condition matching hsweep_h5"）。

### 2. gsweep_g095_h5_seed1（= h=5 数据点）

| 字段 | 值 |
|---|---|
| Status | DONE, conclusion=**negative** |
| Server | westd-47453, cuda:2,3 |
| W&B run | d3irreww |
| 完成步数 | **仅 ~5 步**（早停） |
| val_success_step5 | **0%** |
| val_success_step10 | **无数据** |
| val_success_step15 | **无数据** |
| Checkpoint | 仅 `global_step_5`（`/root/autodl-tmp/checkpoints/gsweep-g095-h5/`） |

**数据不完整**：只跑到 step 5 就因 collapse 停了，没有 step 10/15 的 val success。

### 3. hsweep_h10_seed1

| 字段 | 值 |
|---|---|
| Status | DONE, conclusion=**killed** |
| Server | bjb1-17606, cuda:0,1 |
| 原因 | 刚启动几分钟就被 kill，为 exp029 reeval 腾 GPU |
| 训练进度 | **零**，无 metrics、无 checkpoint |
| Checkpoint | 无（bjb1 和 westd 上都没有 h10 目录） |

### 4. Checkpoint 全景

**bjb1-17606:**
- `/root/autodl-tmp/checkpoints/hsweep-h2/` → `global_step_10`, `global_step_15`（注意：step_15 被 seed2 覆盖了 seed1）

**westd-47453:**
- `/root/autodl-tmp/checkpoints/gsweep-g095-h5/` → 仅 `global_step_5`
- 无任何 hsweep 目录，无 h10 目录

### 5. 建议

- **h=5 不需要重跑**（如果目标仅是 cliff figure 的数据点）：step 5 val=0% 已足够证明 h=5 collapse。gsweep_g095_h5 本质上就是 hsweep_h5（γ=0.95 是默认值）。如果论文需要完整 15-step trajectory，则需要重跑让它跑满。
- **h=10 必须从零开始跑**：完全没有数据，是 cliff figure 缺失的关键数据点（h=2 collapse, h=5 collapse, h=10=?, h=full=28.1% success）。
- **优先级：h=10 > h=5 重跑**。h=10 是全新数据点，决定 cliff 的形状（是在 h=10 恢复还是只有 h=full 才行）。

---
