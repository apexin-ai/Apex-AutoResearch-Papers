# writing paper background

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-background_20260514T052741_result.json`
- **Structured JSON:** [`e691e9f4dc91a6b06e25.json`](../../sessions/e6/e691e9f4dc91a6b06e25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Word count:** ~834 words (approximately 1 page in double-column EMNLP format).

**Citations needed** (6 placeholders to resolve):
| Placeholder | Target |
|---|---|
| `\cite{placeholder_thinkv}` (×2) | ThinKV, ICLR 2026 Oral |
| `\cite{placeholder_math500}` | MATH-500 dataset |
| `\cite{placeholder_thinking_tokens_mi}` | "Thinking Tokens are Information Peaks", NeurIPS 2025 |

**Notes:**
- II 定义使用了代码中实际的 ratio-based 公式 `R_b - R_h - R_k + 1`，与 prompt 中的 PPL 差值定义不同。代码实现是 ratio-based（除以 dense PPL），论文中已统一为此版本，因为它 scale-invariant。如果需要改回 PPL 差值版本请告知。
- KV importance 的 position normalization `1/(T-j)` 已写入公式，对应 memory.md 记录的 commit 20182ec 修复。
- Phase segmentation 描述的是实际使用的 quantile-based 方法（`alt_segmentation.py`），而非 KDE 方法（KDE 在 82% 样本上 fallback）。
- 需要 `\usepackage{enumitem}` 支持 `[nosep,leftmargin=*]` 选项。

---
