# check exp003s2 health

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp003s2-health_20260520T001915_result.json`
- **Structured JSON:** [`77f519fea3bca5adc193.json`](../../sessions/77/77f519fea3bca5adc193.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-003-s2 健康报告：**

| 项目 | 状态 |
|------|------|
| **进程** | 存活，已运行 1h51m |
| **当前 step** | 5 / 8000（刚启动，~39.6s/step） |
| **entropy/reward** | 日志中尚未输出指标（仅 5 步，太早），暂无 collapse 迹象 |
| **GPU 0** | 100% 利用率，76064 MiB 显存占用 |

补充：
- 反复出现的 `d_syc not loaded; returning R3-only rewards` 是预期行为（脚本为 `run_exp003s2_r3only.py`）。
- NLI 模型 `cross-encoder/nli-deberta-v3-base` 已成功加载。
- GPU 1 也有 97%/38161 MiB 占用，可能是其他任务。

**结论：运行正常，建议 30-60 分钟后再查一次日志确认 reward 指标趋势。**

---
