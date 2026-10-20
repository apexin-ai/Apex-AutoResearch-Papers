# ssh exp 016 017 progress 3

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp_016_017_progress_3_20260522T175850_result.json`
- **Structured JSON:** [`999650f158c1bfa016af.json`](../../sessions/99/999650f158c1bfa016af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### exp_016
- **配置**: Phase 1, fixed_mix, pythia-410m, seed=44, r03, 35000 samples/gen
- **当前**: Generation **10/10**，生成阶段 — 32960/35000 samples（~94%）
- **状态**: 运行中，未完成
- **Gen 9 metrics**: eff_rank=517.18, ppl=12.98, distinct4=0.4268

### exp_017
- **配置**: Phase 1, fixed_mix, pythia-410m, seed=43, r02, 40000 samples/gen
- **当前**: Generation **6/10**，生成阶段 — 18880/40000 samples（~47%）
- **状态**: 运行中，未完成
- **Gen 5 metrics**: eff_rank=492.09, ppl=11.83, distinct4=0.4435

exp_016 即将完成最后一个 generation 的样本生成，之后还有训练+评估就结束。exp_017 还需跑完 Gen 6-10，预计还需较长时间。

---
