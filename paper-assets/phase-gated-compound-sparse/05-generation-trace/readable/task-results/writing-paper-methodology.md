# writing paper methodology

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-methodology_20260514T052759_result.json`
- **Structured JSON:** [`9c1c8ba76a862cce5dd4.json`](../../sessions/9c/9c1c8ba76a862cce5dd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/_project/paper/methodology.tex`。

---

**Word count:** ~962 words (approx. 1 page in double-column ACL format)

**Citations needed (7 placeholders):**
| Placeholder | Target |
|---|---|
| `\cite{deepseek-r1}` | DeepSeek-R1 tech report (2025) |
| `\cite{qwen2.5}` | Qwen2.5 tech report (2024) |
| `\cite{math500}` | MATH-500 / Hendrycks et al. MATH benchmark |
| `\cite{efron1993bootstrap}` | Efron & Tibshirani, *An Introduction to the Bootstrap* (1993) |

**Notes:**
- II 公式使用了代码中的归一化形式 `r_both - r_attn - r_kv + 1`（其中 `r_x = PPL_x / PPL_d`），与 Section 3 的 `II = PPL_b - PPL_a - PPL_k + PPL_d` 等价于 scaling by `1/PPL_d`。如果 Section 3 用的是未归一化形式，需要统一。
- Bootstrap B=10000 按要求写入，但代码 `N_BOOTSTRAP` 默认值为 1000——确认实际运行值。
- Hardware 放在了 footnote（Section 4.5 末尾），GPU 型号写为 RTX 6000 Ada 96GB。如需改为 "RTX 6000 Pro" 请告知。
- `bfloat16` 作为实际实验 dtype 写入，fp16 NaN 问题作为 footnote 说明。

---
