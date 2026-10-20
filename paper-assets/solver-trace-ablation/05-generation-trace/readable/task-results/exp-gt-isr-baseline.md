# exp gt isr baseline

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gt-isr-baseline_20260513T181022_result.json`
- **Structured JSON:** [`18db1734c401c03055d9.json`](../../sessions/18/18db1734c401c03055d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。Registry 和 artifact 均已更新。

## 结果总结

| 指标 | Model (Qwen3-4B) | Ground-Truth FOL |
|------|:-:|:-:|
| Prove rate | 12% | **18%** |
| Mean ISR | 0.064 | **0.5588** |
| ISR median | — | 0.6125 |
| ISR range | — | [0.14, 1.00] |

**核心发现**：

1. **GT ISR = 0.5588 > 0.5**，假设成立——好的 formalization 的 ISR 显著高于模型生成的 0.064。
2. **Prove rate 只有 18%**，主要因为 Prover9 是定理证明器，只能证 entailment：
   - `true` 类型：50% 可证，mean ISR = 0.5833
   - `false` 类型：4% 可证（仅 1 条）
   - `unknown` 类型：0% 可证——符合预期，这些本来就不可判定
3. **XOR 处理正常**：34 条含 ⊕ 的样本中 6 条可证，ISR = 0.5456，与整体一致。
4. **ISR 分布偏右**：60% 的已证样本 ISR ≥ 0.4，33% 在 [0.6, 0.8) 区间。
5. **最佳案例** folio_711 达到 ISR=1.0（3/3 必要组件）；**最差** folio_1086/folio_167 仅 0.143。

---
