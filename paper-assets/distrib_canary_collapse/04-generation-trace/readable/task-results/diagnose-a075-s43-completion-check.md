# diagnose a075 s43 completion check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_a075_s43_completion_check_20260516T141554_result.json`
- **Structured JSON:** [`adab4a19c4a370c43079.json`](../../sessions/ad/adab4a19c4a370c43079.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### a075_s43：未完成，仍在运行
- PID 184026 存活，运行 4h18m
- 训练已完成：gen_0 ~ gen_10 全部 checkpoint 完成
- 当前阶段：正在计算 post-training metrics（Featurizing q ~41%）
- 预计还需若干分钟完成 metrics 计算

### a075_s44：已完成，完整 metrics

| 指标 | gen_0 | gen_10 | 变化 |
|------|-------|--------|------|
| perplexity | 26.95 | 76.35 | +183% |
| token_entropy | 3.234 | 2.336 | -27.8% |
| ece | 0.0108 | 0.206 | +1807% |
| effective_rank | 46.61 | 77.84 | +67.0% |
| distinct_1 | 0.0981 | 0.0669 | -31.8% |
| distinct_2 | 0.513 | 0.309 | -39.9% |
| distinct_3 | 0.806 | 0.508 | -37.0% |
| self_bleu | 0.0110 | 0.0143 | +30.0% |
| mauve | 0.0295 | 0.0291 | -1.4% |

a075_s43 的 gen_0 baseline 已出（ppl=26.95, entropy=3.234, eff_rank=46.6），与 s44 一致（同模型不同 seed）。等 metrics 计算完即可更新 registry。

---
