# analysis rho02 adaptive tau09 r2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rho02_adaptive_tau09_r2_20260517T111817_result.json`
- **Structured JSON:** [`e19fb279472768658e5b.json`](../../sessions/e1/e19fb279472768658e5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## rho02_adaptive_tau09_r2 分析

**Status**: FAILED — 初始化阶段崩溃，零训练产出。

**错误**: `TypeError: Trainer.__init__() got an unexpected keyword argument 'tokenizer'`
- `pretrain_weighted.py:101` 中 `WeightedTrainer.__init__` 传入了 `tokenizer=` 关键字
- westd-30476 上的 transformers 版本已将该参数重命名为 `processing_class`
- 同一 bug 导致 `rho02_adaptive_tau09_seed42`、`bs8_auto_nmin_r2`、`batch_adaptive_tau_rho06_r2` 等多个实验全部失败

**对 Claim 3 的影响**:
- ρ=0.2 adaptive 无数据，Claim 3 (proportion-robustness) **无法验证**
- 已有 baseline: `rho02_uniform_seed42` PPL=**17.336**
- 对比参考: ρ=0.4 adaptive PPL=17.644 vs ρ=0.4 uniform PPL≈17.69

**Registry 已更新**: log_path、metrics（含错误信息）、conclusion=failed。

**修复方案**: `pretrain_weighted.py` 第~101行将 `tokenizer=` 替换为 `processing_class=`，然后重提交实验。这个 fix 同时会解决其他因相同 bug 失败的实验。

---
