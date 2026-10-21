# analysis verbosity bt split

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verbosity-bt-split_20260522T041523_result.json`
- **Structured JSON:** [`566402c32123b40bd51d.json`](../../sessions/56/566402c32123b40bd51d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### Verbosity Direction-Aware Gate BT Split（Qwen3-32B Judge）

| Group | n | BT P(verbose) | 95% CI | p |
|-------|---|---------------|--------|---|
| Strict Bidirectional | 65 | 0.7845 | [0.7076, 0.8537] | <0.0001 |
| Direction-Aware (all) | 86 | 0.7732 | [0.7034, 0.8429] | <0.0001 |
| **Extra (DA-only)** | **21** | **0.7379** | **[0.5714, 0.8806]** | **0.0040** |

**Delta test**: DA - Strict = -1.1pp, CI [-5.6, +3.0], contains 0 → no significant difference.

**Extra group 构成**: 17 expansion + 4 compression。几乎全部 opposite-direction NLI 极低（0.001–0.096），即内容增减幅度大但单方向语义保持良好的 pairs。

**结论**: Direction-aware gate 额外放入的 21 pairs 展现与 strict 组**同方向**的 verbosity bias（0.7379 vs 0.7845），且独立显著（p=0.004）。DA gate 不引入异常 bias pattern，支持使用 DA gate 而非 strict bidirectional。

数据存档于 `data/verbosity_bidir_nli.jsonl`。

---
