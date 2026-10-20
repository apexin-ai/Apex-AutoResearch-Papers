# analysis nve threshold sensitivity

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve-threshold-sensitivity_20260524T175333_result.json`
- **Structured JSON:** [`9f65bab75c0ea526c0fe.json`](../../sessions/9f/9f65bab75c0ea526c0fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。分析结果已存在且已注册 (art_20260524_b831db)。

核心结论：
- **AUROC = 0.961** (n=32, Walker+Cheetah)
- **最优阈值 1.5x**: F1=0.880, Recall=1.000, Precision=0.786
- Cheetah 环境完美分离 (AUROC=1.0, 1.5x 以上零 FP)
- 不可消除的 FP 来源：exp_008e_v3_s2 (NVE=3.78, IRD 非 CIVO 坍缩) 和 frozen dt_emb 的瞬态尖峰 (047/057)
- 建议：alert 用 1.5x，confirm 用 2.0x 或 1.5x 持续 >10K steps

---
