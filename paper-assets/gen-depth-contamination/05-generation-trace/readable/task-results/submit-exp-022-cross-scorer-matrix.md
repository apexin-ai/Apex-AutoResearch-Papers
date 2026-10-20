# submit exp 022 cross scorer matrix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_022_cross_scorer_matrix_20260516T150341_result.json`
- **Structured JSON:** [`91af5c0f04479d97c0aa.json`](../../sessions/91/91af5c0f04479d97c0aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 确认活跃：**71% 利用率，4783MiB 显存，PID 49787**。

汇总：

| 项 | 值 |
|---|---|
| tmux session | `exp022` |
| PID | 49787 |
| GPU | cuda:1 (RTX 4090 D) |
| 显存占用 | 4783 MiB / 24564 MiB |
| GPU 利用率 | 71% |
| 日志 | `/root/autodl-tmp/gen-depth-contamination/logs/exp022.log` |

**当前运行的是 2×2 子矩阵**（2 generators × 2 scorers = 4 组合）：
- Generators: Qwen2.5-1.5B (continuation), Pythia-1.4B
- Scorers: Qwen2.5-1.5B (base), Pythia-1.4B

**缺失项**（无法运行完整 4×4 矩阵）：
- **Scorer 模型未缓存**: Qwen2.5-1.5B-Instruct, OLMo-1B
- **Generator depth chain 数据缺失**: Qwen2.5-1.5B (rewrite), OLMo-1B

如需完整 4×4 矩阵，需要先 `source /etc/network_turbo` 下载缺失模型，并生成 Qwen-rewrite 和 OLMo 的 depth chain 数据。预计当前 2×2 矩阵约 40-50 分钟完成。

---
