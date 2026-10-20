# paper w2 d059 results abstract

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_w2-d059-results-abstract_20260514T232126_result.json`
- **Structured JSON:** [`71d6afe866615a29321d.json`](../../sessions/71/71d6afe866615a29321d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

1. **results.tex §5.5** — 第二段已替换，使用实际数值（0.002, 0.043, 0.219, 0.029, 0.020, 0.356），无 `\placeholder`。
2. **abstract.tex D1**（line 8）— `$d_z{=}{-}0.04$` 已替换为 `negligible median difference ($\widetilde{\Delta} = \placeholder{}$)`。
3. **abstract.tex D2+W2**（line 10）— LLaMA 部分已替换，使用 `$\widetilde{\Delta}$: $0.020 \to 0.356$`，无残留的 imp-vs-rand `d_z`。

检查 abstract.tex 中剩余的 `d_z` 出现：line 7 的 `$d_z$ growing from $0.44$ to $0.80$` 和 line 10 的 `$d_z \geq 0.55$` 均为 within-importance d_z，合规保留。

---
