# eval collect vanilla baseline results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-vanilla-baseline-results_20260519T094150_result.json`
- **Structured JSON:** [`028ba0f4a92df190a682.json`](../../sessions/02/028ba0f4a92df190a682.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已获取。以下是 westd-28034 vanilla baseline eval 的完整指标：

## Eval 结果（westd-28034，Qwen3-8B vanilla baseline）

| 指标 | 值 |
|------|-----|
| **ToF** (True-of-Flip) | **0.1105** |
| **NoF** (No-Flip rate) | **0.9227** |
| **sycon_score** | **0.1974** |
| 样本数 | 362（valid_correction: 181, invalid_pressure: 181） |
| avg_flip_turn_valid | 1.0 |
| avg_flip_count_invalid | 0.08 |
| 耗时 | ~5697 秒（约 95 分钟） |

### 与 westd-29046 结果对比

westd-29046 的 eval_vanilla_baseline.py 报告 WRR=0.558。这里没有直接输出 WRR，但可以推算：

- **WRR = 1 - NoF（invalid_pressure 场景）= 1 - 0.9227 = 0.0773**（7.7%）

这与 westd-29046 的 WRR=0.558（55.8%）差距巨大（**48pp**），远超之前预估的 28.7pp。

可能的差异来源：
- **WRR 定义不同**：westd-29046 可能将 WRR 定义为 valid_correction 场景下未 flip 的比率（即 1 - ToF = 1 - 0.1105 = 0.8895），或两个脚本的 WRR 计算逻辑根本不同
- **评估脚本不同**：两台服务器使用的 eval 脚本版本/参数可能不一致
- **数据集差异**：样本集或 split 可能不同

需要对比两边的 eval 脚本源码和数据集来定位差异根因。

---
