# analysis h7 subtype random s43r3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_h7-subtype-random-s43r3_20260515T185050_result.json`
- **Structured JSON:** [`3bc661d271f617ee6694.json`](../../sessions/3b/3bc661d271f617ee6694.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

### 任务 A：Random s43-r3 H7 子类别
| 指标 | 值 |
|------|-----|
| H7a (text-match tautology) | **36** (100% of H7) |
| H7b (obfuscated tautology) | **0** |
| H7 total | 36/94 = 38.3% |
| H1 (conclusion embedding) | 56/94 = 59.6% |
| H8 (conjunction collapse) | 1/94 = 1.1% |
| Genuine | 1/94 = 1.1% |

所有 36 个 H7 全是 H7a，零 H7b。且 single_premise_count=0——Random 的 H7a 是多前提证明中嵌入一个与结论完全匹配的前提，而非单前提 tautology。

### 任务 B：Exec-only s43 核实
- **确认 exec-only**：reward_log 中 random_mean=null, beta_t=null；training_args beta=0.0, reward_weights=None；reward 恰好等于 prove_rate
- **D089 "100% H7" 确认**：90/90 proved 全是 H7a，零 H7b，全部 single-premise
- **D088 需修正**："H7 由 additive reward 驱动" 对 H7a 不成立——exec-only（无 additive bonus）产出 100% H7a

### Framing 影响
- **H7b (vacuous quantifier obfuscated tautology) 确认为 ISR-specific**——Random 和 exec-only 都是 0
- **H7a 是通用 reward hacking**——出现在所有训练模式中，不能作为 ISR-specific 证据
- **结构差异**：exec-only 的 H7a 全是单前提最小 tautology；Random 的 H7a 是多前提中嵌入 tautology

文件已保存到 `/root/solver-trace-ablation/analysis/d093_h7_subtype_analysis.json`。

---
