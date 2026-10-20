# research qwen3 8b leaderboard

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_qwen3_8b_leaderboard_20260523T140130_result.json`
- **Structured JSON:** [`69d0cb8864abc6f38eae.json`](../../sessions/69/69d0cb8864abc6f38eae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调研结果

### 1. Qwen3-8B 在各 Leaderboard 上的状态

| Leaderboard | 状态 | 说明 |
|---|---|---|
| **Chatbot Arena (arena.ai)** | **无官方 ELO** | Arena 上有 Qwen3-235B-A22B、Qwen3.6-Max、Qwen3.7-Max (ELO 1475)，但 8B 级别模型未被提交/评测 |
| **Arena-Hard-Auto (GitHub)** | **官方排行榜无** | 官方 README 仅列 Qwen3-32B (53.3%)、Qwen3-235B-A22B (73.5%)，无 8B |
| **Arena-Hard (Qwen 自报)** | 79.6 | 出自 Qwen3 Technical Report，**自报数据**，评测设置可能与官方排行榜不同 |
| **AlpacaEval 2.0** | **无** | 未出现在官方排行榜 |
| **Open LLM Leaderboard v2** | **未确认** | 搜索未找到具体条目 |
| **Artificial Analysis** | Intelligence Index = 11 | 自有评测体系，非 ELO，无法直接对比 |

**结论：方案 C 不可行。** 没有任何可信的公开排名能作为 Chatbot Arena ELO 的替代。自报的 Arena-Hard 79.6 不是 ELO，评测设置不透明，无法用于 Kendall τ 计算。

### 2. 三方案对比

| 维度 | 方案 A (替换为 mixtral-8x7b) | 方案 B (保留但 τ 排除) | 方案 C (找替代排名) |
|---|---|---|---|
| **可行性** | 可行但代价高 | 直接可行 | **不可行** |
| **实验影响** | N=8 结果全部失效，需重跑 exp-003b | 无需重跑任何实验 | — |
| **时间成本** | ~12-16h (评测+MCMC) | 0 | — |
| **统计影响** | τ 分辨率 1/136 | τ 分辨率 1/120 (差异 <0.001) | — |
| **论文叙述** | 干净，所有模型都有官方 ELO | 需一句解释，完全合理 | — |
| **MCMC fitting** | 17 模型全参与 | 17 模型全参与（更多数据=更好估计） | — |
| **风险** | 新增 mixtral-8x7b 数据可能引入新问题 | 无 | — |

### 3. 推荐：方案 B

理由：
1. **零成本**——不需要重跑任何实验
2. **统计 power 损失可忽略**——N=16 vs N=17，τ 分辨率差 0.0009
3. **MCMC 不受影响**——qwen3-8b 的 judge 评测数据仍参与 fitting，17 个模型的数据量 > 16 个，参数估计更稳健
4. **论文表述自然**——"We evaluate on 17 target models; Kendall τ is computed over the 16 models with official Chatbot Arena Elo ratings" 是完全标准的做法
5. **方案 A 的 12-16h 时间成本和重跑风险不值得**——仅为换回 1 个 τ 数据点

Sources:
- [Qwen3: Think Deeper, Act Faster](https://qwenlm.github.io/blog/qwen3/)
- [Qwen3 8B - Artificial Analysis](https://artificialanalysis.ai/models/qwen3-8b-instruct)
- [Arena-Hard-Auto GitHub](https://github.com/lmarena/arena-hard-auto)
- [Arena Leaderboard](https://arena.ai/leaderboard)
- [AlpacaEval Leaderboard](https://tatsu-lab.github.io/alpaca_eval/)
- [Arena-Hard v2 Leaderboard](https://llm-stats.com/benchmarks/arena-hard-v2)

---
