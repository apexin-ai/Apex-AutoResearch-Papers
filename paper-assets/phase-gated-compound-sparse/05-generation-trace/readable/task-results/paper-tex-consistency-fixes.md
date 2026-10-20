# paper tex consistency fixes

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_tex_consistency_fixes_20260516T224936_result.json`
- **Structured JSON:** [`93b6e2805620c04b9864.json`](../../sessions/93/93b6e2805620c04b9864.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，共 5 处：

| # | 文件 | 修改 | 原因 |
|---|------|------|------|
| 1a | `results.tex:88` | `$2.7$--$20{\times}$` → `$2.7$--$3.5{\times}$` | Qwen-specific，数据验证 0.39/1.07=2.7×, 0.91/3.16=3.5× |
| 1b | `appendix_disc_analysis.tex:53` | `$2.7$--$20{\times}$` → `$2.7$--$17{\times}$` | "both models" 语境，与 conclusion.tex 一致（DeepSeek 15–17×, Qwen 2.7–3.5×） |
| 2 | `conclusion.tex:4` | `$n{=}500$` → `$n{=}496$` | 与 results.tex table caption 一致 |
| 3a | `discussion.tex:8` | `GSM8K (${\sim}3{\times}$)` → `GSM8K (${\sim}2{\times}$ point-estimate ratio; random non-significant at $n{=}50$)` | 实际点估计 1.6–2.6×，且 random 全部 NS |
| 3b | `results.tex:129` | `ratio ${\sim}3{\times}$` → `ratio ${\sim}2{\times}$ from point estimates` | 同上，保持一致 |

---
