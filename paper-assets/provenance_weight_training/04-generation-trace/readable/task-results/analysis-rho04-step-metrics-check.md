# analysis rho04 step metrics check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rho04-step-metrics-check_20260518T211041_result.json`
- **Structured JSON:** [`5201a09ecfb51ab91aec.json`](../../sessions/52/5201a09ecfb51ab91aec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

---

## 结果汇总

**westd-30476**: 无任何 adaptive 实验目录（autodl-tmp 和项目根目录均无）。

**westd-41312** 上所有 adaptive 实验（全部 ρ=0.4，除 contamination_60）：

| 实验 | 模型 | ρ | 行数 | 最大 step | max_steps 目标 | 状态 |
|---|---|---|---|---|---|---|
| `adaptive_fix_seed42` | Qwen3-0.6B | 0.4 | 100 | 24 | 6103 | **极度不完整**（SIGTERM） |
| `ngram_adaptive_seed42` | Qwen3-0.6B | 0.4 | 24,412 | 6102 | 6103 | **完整** |
| `gpt2_adaptive_seed42` | Qwen3-0.6B | 0.4 | 10,820 | 2717 | 6103 | 不完整（~44%） |
| `adaptive_1_7b_seed42` | Qwen3-1.7B | 0.4 | 26,412 | 6102 | 6103 | **完整** |
| `adaptive_1_7b_seed123` | Qwen3-1.7B | 0.4 | 6,050 | 1522 | 6103 | 不完整（~25%） |
| `contamination_60_adaptive_seed456` | (未检查) | 0.6 | 24,712 | 6102 | 6103 | 完整（当前用于 figure） |

**用户要找的 `adaptive_fix_seed123` 和 `adaptive_fix_seed456` 在两台服务器上均不存在。**

## 可用于补充 ρ=0.4 训练动态分析的数据

有两个完整的 ρ=0.4 实验：

1. **`ngram_adaptive_seed42`** — Qwen3-0.6B，24,412 行，step 0→6102，完整训练。但注意这是 **ngram-based** 评分方法的 adaptive，不是标准 adaptive。
2. **`adaptive_1_7b_seed42`** — Qwen3-1.7B，26,412 行，step 0→6102，完整训练。但这是 **1.7B 模型**，不是主实验的 0.6B。

**结论**：没有与主实验（Qwen3-0.6B + 标准 adaptive + ρ=0.4）配置完全一致的完整 step_metrics。最接近的替代是 `ngram_adaptive_seed42`（同模型同 ρ，但评分方法不同）或 `adaptive_1_7b_seed42`（同方法同 ρ，但模型不同）。如果要做 ρ=0.4 的训练动态图，需要决定是否接受这些差异，或者重跑 `adaptive_fix_seed42`。

---
