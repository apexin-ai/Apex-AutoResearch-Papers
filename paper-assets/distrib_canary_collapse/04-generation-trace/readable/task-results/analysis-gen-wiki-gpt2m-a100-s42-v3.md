# analysis gen wiki gpt2m a100 s42 v3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gen_wiki_gpt2m_a100_s42_v3_20260515T221636_result.json`
- **Structured JSON:** [`51d7566bb502e68aa239.json`](../../sessions/51/51d7566bb502e68aa239.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析完成

### 结论：**SUCCESS** — collapse pattern 跨架构一致

### Drift 对比 (GPT-2m vs Pythia-410m, α=1.0)

| 指标 | GPT-2m | Pythia-410m | 方向 |
|------|--------|-------------|------|
| entropy | **-86.5%** | -60.5% | ✓ 更严重 |
| ece | **+4544%** | +3762% | ✓ 更严重 |
| perplexity | **+44693%** | +3624% | ✓ 12x 更严重 |
| distinct_1 | -12.4% | **-28.3%** | ✓ 更温和 |
| distinct_2 | -14.7% | **-35.2%** | ✓ 更温和 |
| distinct_3 | -12.7% | **-31.6%** | ✓ 更温和 |

### 方法论陷阱验证
- **Cross-correlation lag-0 dominance**：14/16 pairs 峰值在 lag=0，与 Pythia 一致 — 朴素方法会高估因果性
- **Granger 选择性**：entropy/ece → diversity 显著（p<0.003），但 → perplexity 全部不显著；self_bleu 完全无 Granger 信号（p>0.88）
- 这与 Pythia 上观察到的 pattern 一致：方法选择（哪对 metric pair、是否做差分）决定性地影响因果推断结论

### 额外发现
GPT-2m 表现出"更极端的校准崩溃 + 更温和的多样性损失"模式 — 更大的模型在 collapse 过程中保留了更多词汇多样性，但 perplexity 爆炸更剧烈（447x vs 36x）。这可能因为 355M 参数模型在 iterative finetuning 中过拟合合成数据更彻底。

---
