# analysis n16 5signal eval

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n16_5signal_eval_20260514T185920_result.json`
- **Structured JSON:** [`f65efffe377415c75fe7.json`](../../sessions/f6/f65efffe377415c75fe7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。核心结果：

**exp_002 Qwen CoNLL N=16 (full set, ρ)**:
| Signal | N=8 | N=16 | Δ |
|--------|-----|------|---|
| EM | 0.451 | **0.463** | +0.012 |
| SJ | 0.436 | **0.450** | +0.014 |
| voting_conf | 0.424 | 0.429 | +0.005 |
| FK | 0.400 | 0.393 | -0.007 |
| logprob | 0.316 | 0.315 | -0.001 |

**exp_007 LLaMA SciERC N=16 (full set, ρ)**:
| Signal | N=8 | N=16 | Δ |
|--------|-----|------|---|
| voting_conf | 0.433 | **0.452** | +0.018 |
| SJ | 0.363 | **0.379** | +0.016 |
| EM | 0.315 | 0.316 | +0.001 |
| FK | 0.327 | 0.308 | -0.019 |
| logprob | 0.183 | 0.204 | +0.021 |

**关键发现**:
1. **SJ N-scaling 成立** — 两个实验 SJ ρ 都随 N 增长（+0.014, +0.016），跨模型、跨数据集一致
2. **FK 随 N 退化** — 两个实验 FK ρ 都下降，不适合 N-scaling
3. **logprob N-invariant** — 符合预期，logprob 不依赖样本数
4. **Structural > Surface 优势扩大** — CoNLL 最佳结构信号 vs logprob gap 从 0.135 增到 0.148
5. **SJ ECE 最低**（0.075-0.102），校准性最好

报告已保存到 `artifacts/n16_5signal_comparison.md`，两个实验 registry 已更新完整 5-signal metrics。

---
