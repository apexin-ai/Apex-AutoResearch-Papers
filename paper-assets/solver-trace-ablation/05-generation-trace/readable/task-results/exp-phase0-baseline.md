# exp phase0 baseline

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phase0-baseline_20260513T175225_result.json`
- **Structured JSON:** [`3213dc8c792e3d8369f7.json`](../../sessions/32/3213dc8c792e3d8369f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 0 完成。结果汇总：

| 指标 | 值 |
|------|-----|
| **Mean ISR** | 0.0641 ± 0.1983 |
| **Median ISR** | 0.0 |
| **ISR Range** | [0.0, 0.889] |
| **Prove Rate** | 12/100 (12.0%) |
| **Runtime** | 336s (3.4s/sample) |

**按 answer type 分组：**
- **true**: n=34, proved=9 (26.5%), ISR=0.1345
- **false**: n=25, proved=1 (4.0%), ISR=0.0240  
- **unknown**: n=41, proved=2 (4.9%), ISR=0.0302

**关键发现：**
1. Base Qwen3-4B 能生成格式正确的 FOL（Premises/Conclusion 结构），但大部分 (88%) 无法被 Prover9 证明
2. "true" 类问题 prove rate 最高 (26.5%)，符合预期（solver 本来就是尝试证明结论成立）
3. ISR 有区分度：proved 的样本中 ISR 从 0.125 到 0.889，说明 STA 能区分 tight vs. redundant 的 formalization
4. 3 条 false/unknown 被错误 proved，说明存在 formalization 语义错误（但比例很低）

这为后续 GRPO 训练提供了清晰的 baseline anchor：训练后如果 prove rate 上升但 ISR 下降，就是 reward hacking 信号。

---
