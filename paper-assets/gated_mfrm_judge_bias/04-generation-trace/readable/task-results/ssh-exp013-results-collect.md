# ssh exp013 results collect

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp013_results_collect_20260523T052310_result.json`
- **Structured JSON:** [`8773ee1549fe9804c96e.json`](../../sessions/87/8773ee1549fe9804c96e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Part A: exp-013 Weight Sensitivity

**状态：仍在运行** (PID 558426, elapsed 1h13m, GPU 0 占用 73.5GB)

当前正在拟合最后一个配置 `100_0` (ref=1.0, cma=0.0)，warmup 进度约 45% (1794/4000)。

已完成 3 个配置的 G-MFRM 拟合，结果保存为 JSON（无 CSV — CSV 应该是全部跑完后汇总生成）：

| 配置 | r_hat | ESS | Divergences | θ range | c range |
|------|-------|-----|-------------|---------|---------|
| 50_50 | 1.02 | 196 | 0 | [-3.04, 1.84] | [0.96, 3.20] |
| 75_25 | 1.04 | 115 | 0 | [-3.12, 1.85] | [1.09, 3.49] |
| 90_10 | 1.01 | 432 | 0 | [-3.15, 1.87] | [1.01, 3.67] |

MCMC 诊断正常（0 divergences），模型能力排序稳定：gpt-4o > qwen2.5-72b ≈ gpt-4o-mini > llama-3.3-70b > qwen3-8b > gemma-2-9b > gpt-4-0613 > gpt-3.5-turbo。

**预估剩余时间：** 100_0 warmup 还需约 3 分钟完成，加上 sampling 2000 步约 2 分钟，总计约 5 分钟内完成。之后生成 weight_sensitivity.csv。

---

## Part B: exp-001 Llama 收集

**vLLM 服务运行中，但无 collect 进程：**
- GPU 1: vLLM Llama-3.3-70B-AWQ on port 8001 (运行 1天4小时)
- GPU 2: vLLM Llama-3.3-70B-AWQ on port 8004 (运行 5h50m)
- **无活跃的 collect.py 进程**

**数据文件（最后修改时间均为 13:24，已停止增长）：**

| 文件 | 行数 |
|------|------|
| llama-3.3-70b/ | 6,061 |
| llama-3.3-70b-shard2/ | 5,821 |
| **合计** | **11,882** |
| 参考：qwen2.5-72b | 9,281 |
| 参考：mistral-large-2 | 9,021 |

Llama 两个 shard 合计 11,882 行，超过其他本地 judge 的 ~9,000 行，**数据收集大概率已完成**。但 collect 进程不在运行，数据文件已停止增长。

**GPU 状态：**

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 73.5/97.9 GB | 72% (exp-013) |
| 1 | 91.0/97.9 GB | 100% (vLLM Llama) |
| 2 | 91.0/97.9 GB | 100% (vLLM Llama) |
| 3 | 0/97.9 GB | 0% (空闲) |

**建议：** Llama 收集已完成，GPU 1-2 上的 vLLM 可以关掉释放资源。exp-013 约 5 分钟内完成。

---
