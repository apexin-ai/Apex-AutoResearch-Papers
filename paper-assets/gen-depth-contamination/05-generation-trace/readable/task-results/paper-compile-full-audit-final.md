# paper compile full audit final

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile_full_audit_final_20260523T115555_result.json`
- **Structured JSON:** [`9cd8bce1948ca107d441.json`](../../sessions/9c/9cd8bce1948ca107d441.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译与验证结果：

| 项目 | 结果 |
|------|------|
| **编译** | 0 errors, PDF 生成成功 (554KB, 18页) |
| **页数** | Main text 8页 (正文至 Conclusion 结束在 p8), Limitations+Ethics 在 p9, References p10, Appendix p11-18 — **符合 EMNLP 8页限制** |
| **Table 10 (Mistral-7B)** | .9209 / .5695 / .5335 / .5140 / .5184 — **全部匹配** |
| **Table 17 (Pythia)** | 0v1 = .972（无CI）, 2v3 = .544 — **匹配** |
| **Table 19 (Pythia decoding)** | T=0.7 2v3 = .594, T=1.2 2v3 = .523 — **匹配** |
| **PDF 已复制** | `artifacts/paper_final_audit_20260523.pdf` |

---
