# analysis folio 2x2 cross extractor mcnemar

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_folio-2x2-cross-extractor-mcnemar_20260522T053530_result.json`
- **Structured JSON:** [`099a76734361a6861794.json`](../../sessions/09/099a76734361a6861794.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
Cross-extractor McNemar (FOLIO 2×2):

Pair 1: Mistral gen | A(Mistral ext) vs B(Qwen3 ext)
  Acc: A=56.86%, B=59.80%, Δ=+2.94pp
  Contingency: both=108, A_only=8, B_only=14, neither=74
  McNemar χ²=1.136, p=0.143, odds_ratio(B/A)=1.75

Pair 2: Qwen3 gen | C(Mistral ext) vs D(Qwen3 ext)
  Acc: C=81.86%, D=84.80%, Δ=+2.94pp
  Contingency: both=167, C_only=0, D_only=6, neither=31
  McNemar χ²=4.167, p=0.021, odds_ratio(D/C)=∞
```

**解读：**

同样是 +2.94pp 的 Δ，但两个 generator 条件下的统计显著性完全不同：

- **Mistral gen**：不显著（p=0.143）。22 个 discordant pairs（8+14）中差异方向虽偏向 Qwen3 ext，但样本不够说明 extractor 有真实差异。
- **Qwen3 gen**：显著（p=0.021）。6 个 discordant pairs 全部是 Qwen3 ext 对而 Mistral ext 错（C_only=0），odds ratio 为 ∞。Qwen3 generator 产出的 FOL 表达对 Mistral extractor 造成了 6 个系统性失败，换 Qwen3 ext 全部修复。

这说明 extractor 差异并非均匀的——Qwen3 生成的符号表示有某些模式让 Mistral extractor 一致性地出错，而 Mistral 生成的符号表示两个 extractor 的错误更接近随机分布。

---
