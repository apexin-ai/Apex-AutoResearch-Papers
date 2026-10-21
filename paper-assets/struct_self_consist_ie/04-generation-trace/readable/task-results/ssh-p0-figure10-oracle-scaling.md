# ssh p0 figure10 oracle scaling

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0-figure10-oracle-scaling_20260520T132907_result.json`
- **Structured JSON:** [`43b415fcca50c4be131f.json`](../../sessions/43/43b415fcca50c4be131f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 10 已生成，保存在 `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/artifacts/f1_scaling/fig_oracle_scaling.{pdf,png}`（PDF 30KB）。

内容摘要：
- **6 条曲线**：Qwen2.5-7B（实线）+ LLaMA-3.1-8B（虚线）× SciERC/CoNLL/FewNERD
- 拟合公式 $F_1(N) = a - b \cdot N^{-c}$，所有 R² > 0.999
- 标注：SciERC c=0.39/0.30，FewNERD c=0.61，CoNLL 只标 a/b（c_se 过大）
- LLaMA FewNERD 标注 "(4-pt)"（仅 N∈{1,2,4,8}）
- N=1 处 "×" 标记 greedy F1（低于 oracle 是 T=1 采样噪声所致）

---
