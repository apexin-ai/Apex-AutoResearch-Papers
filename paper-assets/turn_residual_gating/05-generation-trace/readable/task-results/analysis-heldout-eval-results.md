# analysis heldout eval results

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_heldout_eval_results_20260519T143259_result.json`
- **Structured JSON:** [`1ead762b449a987da072.json`](../../sessions/1e/1ead762b449a987da072.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 8 个 eval 数据已收集。汇总如下：

## Held-out 四路 Eval 结果

| Model | GAR-ours (mid) | recovery (pp) | GAR-Dongre (mid) | recovery (pp) | PPL | NTP Loss |
|-------|:-:|:-:|:-:|:-:|:-:|:-:|
| **Base** | 0.0128 | +0.06 | 0.0031 | -0.91 | 4.34 | 1.4045 |
| **TG v7** | 0.5035 | +49.13 | 0.0152 | +0.30 | 2.78 | 0.9771 |
| **UG** | 0.5053 | +49.31 | 0.0124 | +0.02 | 2.78 | 0.9752 |
| **LoRA-only** | 0.4978 | +48.56 | 0.0132 | +0.10 | 2.78 | 0.9771 |

## 与 Overlap 数据对比

| Model | GAR-ours: overlap→held-out | PPL: overlap→held-out |
|-------|:-:|:-:|
| Base | 0.0107 → 0.0128 (+0.2pp) | 4.23 → 4.34 (+0.11) |
| TG v7 | 0.4866 → 0.5035 (+1.7pp) | 2.63 → 2.78 (+0.15) |
| UG | 0.4923 → 0.5053 (+1.3pp) | 2.62 → 2.78 (+0.16) |
| LoRA-only | 0.4860 → 0.4978 (+1.2pp) | 2.63 → 2.78 (+0.15) |

## 分析

1. **三路趋同在 held-out 数据上完全复现**：TG/UG/LO 的 GAR-ours 分别为 0.5035/0.5053/0.4978，spread 仅 0.75pp；PPL 三者均为 2.78。

2. **绝对值略有上升但趋势一致**：GAR-ours 各路在 held-out 上比 overlap 高 ~1-2pp，PPL 高 ~0.15，属于 held-out 数据的正常泛化偏移。

3. **GAR-Dongre 仍然低且无区分力**（TG 0.015, UG 0.012, LO 0.013），与 overlap 一致。

4. **无意外发现**。

## Conclusion: **SUCCESS**

三路趋同（TG≈UG≈LO）在 held-out 数据上鲁棒复现，进一步确认 gating mechanism 未提供超越 LoRA-only baseline 的独立贡献。

---
