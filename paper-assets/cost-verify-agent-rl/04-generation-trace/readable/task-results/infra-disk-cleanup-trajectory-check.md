# infra disk cleanup trajectory check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-cleanup-trajectory-check_20260514T145454_result.json`
- **Structured JSON:** [`7bbbebf6f10dd1db368a.json`](../../sessions/7b/7bbbebf6f10dd1db368a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都已完成检查。

---

## 任务 1: Expert Trajectory 收集进度

**状态**: 进行中（PID 340587, 100% CPU）

| 指标 | 值 |
|---|---|
| 当前进度 | **2234 / 3553** (62.9%) |
| 目标 | max-games=3553（比之前的 1759 翻倍） |
| 数据大小 | 16MB |
| 平均 messages/trajectory | 30.2 (min=7, max=201) |
| test 子目录 | 5 条 |

**数据格式**: 正确的 messages JSONL，包含 system prompt（带 self-guidance 要求）+ user/assistant 多轮对话。Assistant 回复使用 `&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>` 格式。

**任务类型覆盖**:
- pick_and_place: 788 (35.3%)
- pick_clean_then_place: 645 (28.9%)
- pick_cool_then_place: 499 (22.3%)
- look_at_obj_in_light: 153 (6.8%)
- other: 149 (6.7%)
- pick_heat_then_place: **0** — 尚未收集到（可能在后续 batch 中）

---

## 任务 2: 磁盘清理

**不需要清理。** 磁盘状况已大幅改善：

| 指标 | 值 |
|---|---|
| 总容量 | 250G |
| 已用 | 92G (37%) |
| 可用 | **159G** |

Checkpoint 目录只剩 3 个：
- `exp008_sft/` — 3.3G (保留，SFT 基础)
- `exp015/` — 21G (保留，exp016 恢复点)
- `exp016/` — 21G (保留，当前活跃实验)

**exp013b/c/d/e 的 checkpoint 不存在**——已被之前清理过，或从未写入此路径。

---

## 异常发现

1. 磁盘从 "95% 满" 变为 37%，可能之前已有人做过大规模清理
2. Expert trajectory 收集的 max-games 从 1759 增加到 3553，是一次新的收集任务
3. `pick_heat_then_place` 类型目前 0 条收集，需关注后续是否覆盖
4. exp016 训练正在 tmux session 中运行

---
