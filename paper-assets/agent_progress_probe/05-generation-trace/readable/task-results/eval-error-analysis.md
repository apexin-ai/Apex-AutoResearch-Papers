# eval error analysis

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_error_analysis_20260514T084032_result.json`
- **Structured JSON:** [`aaaf316b2abe962a38c1.json`](../../sessions/aa/aaaf316b2abe962a38c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整了。以下是结构化的错误分析报告。

---

## probe_001 FP/FN 错误分析报告

### Confusion Matrix

| | Pred=Progress | Pred=Stagnation |
|---|---|---|
| **Actual=Progress** | TP=1293 (70.9%) | FN=46 (2.5%) |
| **Actual=Stagnation** | FP=85 (4.7%) | TN=400 (21.9%) |

总错误 131/1824 = 7.2%，其中 FP 占 65%，FN 占 35%。

---

### FP 分析（85 例，predicted=progress, actual=stagnation）

**1. 极度集中于单一 trajectory**
- `palantir__python-language-server-220` 贡献了 **29/85 = 34%** 的全部 FP
- 前 2 个 instance 占了 33/85 = 39% 的 FP
- FP 在 instance 层面高度集中，不是均匀分散的

**2. Probe 对 FP 非常自信**
- 73% 的 FP 概率在 [0.9, 1.0)，模型以极高置信度犯错
- 仅 1.2% 在边界附近 [0.5, 0.6)
- 说明这些不是"侥幸过线"的案例，而是模型系统性地误判了某种模式

**3. LF 投票特征：outcome_backpropagation 主导判定**
- `file_diff_delta`: 44.7% 投 progress，42.4% abstain，12.9% 投 stagnation
  - 即 FP 窗口中接近一半有文件变更（LF 也觉得是 progress）
- `command_repetition`: 92.9% abstain（没有重复命令）
- `outcome_backpropagation`: 67.1% abstain, **32.9% 投 stagnation**
  - 最终 majority label 被 outcome_backpropagation 的 stagnation 票翻转

**核心模式**：FP 主要发生在"agent 在做事（有文件变更、没有重复命令）但最终 outcome 失败"的窗口。Probe 学到了表面活跃的信号，但无法捕捉 outcome_backpropagation 的回溯惩罚。

**4. 几乎全是 confidence=2**（97.6%），说明 LF 投票本身就有分歧（2/3 LF 投了同一方向）。

---

### FN 分析（46 例，predicted=stagnation, actual=progress）

**1. LF 投票特征：file_diff + command_repetition 一致投 progress**
- `file_diff_delta`: **91.3%** 投 progress
- `command_repetition`: **91.3%** 投 progress
- `outcome_backpropagation`: **58.7%** 投 stagnation

**核心模式**：FN 是"两个正向 LF 压倒一个 outcome_backpropagation"的窗口，但 probe 的 embedding 似乎更多学到了类似 stagnation 的表征。可能是这些窗口虽有进展但 embedding 层面的特征（如重复浏览、试错）与 stagnation 相似。

**2. Probe 对 FN 也较自信**
- 34.8% 概率 < 0.1，总共 54.4% < 0.2
- 模型不是在边界犯错，而是"确信这是 stagnation"

**3. 分布相对分散**
- 最多的 trajectory 只有 3 个 FN，没有像 FP 那样的极端集中

---

### 整体模式

**1. Probe vs Repeat-3 错误重叠**

| | 数量 |
|---|---|
| Probe 错误 | 131 |
| Repeat-3 错误 | 192 |
| 两者都错 | 39 (29.8% of probe errors) |
| 仅 Probe 错 | 92 |
| 仅 R3 错 | 153 |

- Probe 的 85 个 FP 中有 **39 个** Repeat-3 也判错（46%）
- Probe 的 46 个 FN 中 **0 个** Repeat-3 也判错
- 说明 FN 是 probe 特有的错误模式（R3 在这些窗口上全判对了——因为没有重复命令，R3 默认 predict=progress）

**2. 错误率 vs Confidence**

| Confidence | Error Rate |
|---|---|
| 2 | 7.1% (126/1780) |
| 3 | 11.4% (5/44) |

意外发现：**confidence=3（全票一致）的错误率反而更高**。样本量小（44），但值得注意。

**3. 错误率 vs 窗口长度**

| Length | Error Rate |
|---|---|
| 7 (短窗口) | **16.8%** (22/131) |
| 9 | 7.5% (12/161) |
| 10 (标准) | 6.3% (97/1532) |

**短窗口（length=7）错误率是标准窗口的 2.7 倍。**

**4. 错误集中在决策边界附近？不完全**
- |prob-0.5| < 0.1 区间错误率 33%，但只有 9 个样本
- |prob-0.5| ∈ [0.3, 0.5) 区间错误率仅 5.7%（1727 个样本）
- 但 FP 的 73% 和 FN 的 54% 都在远离边界处犯错
- **错误不是"犹豫不决"造成的，而是"自信地判错"**

**5. LF 一致性：错误窗口的 LF 反而更一致**
- 错误窗口：mean LF agreement = **0.827**
- 正确窗口：mean LF agreement = **0.592**

这说明 probe 犯错的地方恰恰是 LF 投票很一致的地方——probe 和 LF 对同一窗口的判断系统性地相反。

---

### 关键结论

1. **FP 的根因是 outcome_backpropagation**：probe 无法从 embedding 中获取"最终是否解决了问题"的回溯信号，导致把"活跃但最终失败"的窗口误判为 progress。单一 instance (`palantir__python-language-server-220`) 贡献了 34% FP。

2. **FN 的根因是 embedding 与行为表征的不匹配**：这些窗口有真实进展（file_diff + no repetition），但 embedding 空间中的表征可能被 outcome_backpropagation 的 stagnation 信号（出现在训练集其他样本中）污染。

3. **短窗口是高风险区**：length=7 的错误率是 length=10 的 2.7 倍。

4. **Probe 犯错时很自信**：不是边界决策问题，而是模型对某些模式的系统性误判。

---
