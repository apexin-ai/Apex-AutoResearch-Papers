# analysis exp 004 eval ckpt5500 ckpt4500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-004-eval-ckpt5500-ckpt4500_20260520T160646_result.json`
- **Structured JSON:** [`e9834fdf02a943a5e3f1.json`](../../sessions/e9/e9834fdf02a943a5e3f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## exp-004 ACT Trajectory Eval 结果

| Checkpoint | ToF | NoF | SYCONScore |
|------------|-----|-----|------------|
| D027 Vanilla | 0.072 | 0.945 | 0.134 |
| ckpt-4000 | 0.1215 | 0.8950 | **0.2140** |
| **ckpt-4500** | 0.1050 | 0.8785 | **0.1875** |
| ckpt-5000 | 0.1547 | 0.8785 | **0.2631** |
| **ckpt-5500** | 0.1381 | 0.8674 | **0.2383** |
| ckpt-6000 | 0.1547 | 0.8508 | **0.2618** |

两个新 checkpoint 均 > vanilla 0.134 → conclusion = **success**。

**轨迹趋势**：整体上升但非单调。ckpt-4000~4500 出现明显低谷（SYCONScore 从 ckpt-2000 的 0.255 降至 0.188），ckpt-5000 起回升，后半程 (5000-6000) plateau ~0.24-0.26，ckpt-8000 再突破至 0.301。

**已完成**：
- memory.md 已更新（含完整 8-checkpoint 轨迹表 + 新增分析段落）
- Registry 两个实验均已设为 DONE(success)，metrics/spec/conclusion 已写入
- 无 W&B URL（日志中未出现）

---
