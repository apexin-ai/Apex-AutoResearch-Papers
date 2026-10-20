# analysis d112 mf3 random vs single

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d112_mf3_random_vs_single_20260516T090329_result.json`
- **Structured JSON:** [`7d9a0dbe44639bba114b.json`](../../sessions/7d/7d9a0dbe44639bba114b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three artifacts registered. Here's the summary:

---

## 根因：Table 2 "Single" 行标注错误

**Paper 声称** "Single: one T=1.0 draw"，但**代码实际使用 T=0 greedy decode**。

### 证据链

1. `table2_selection_f1.py:131` — `greedy = inst.get("greedy", samples[0])`
2. `sampling.py` — `greedy` 字段来自 `sampler.sample(prompts, n_samples=1, temperature=0.0)`
3. 这个 T=0 greedy F1 被论文标为 "Single (one T=1.0 draw)"

### 数值映射

| Paper 标签 | 值 | 实际来源 |
|---|---|---|
| Greedy (T=0) | 0.663 | micro F1, T=0, 551 inst |
| Single‡ | 0.645 | **macro F1, T=0** (标注为 T=1.0) |
| Random | 0.610 | macro F1, T=1.0 samples 均值 |

### 3.5pp 差距解释

- 完全是 T=0 argmax vs T=1.0 stochastic 的解码策略差异
- 如果 Single 正确实现为 T=1.0 单次采样：E[Single] = E[Random] ≈ 0.610（审稿人直觉正确）
- 信号 vs 真正的 single-sample baseline (0.610)：LP +3.7pp, SJ/FK +3.6pp

### 输出文件

服务器 `output/d112_mf3_random_single/`:
- `investigation.md` — 完整调查报告（含代码行号）
- `clarification.txt` — 英文澄清文本（可直接用于 rebuttal）
- `raw_values.json` — 原始数值验证

---
