# writing consistency fixes

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_consistency-fixes_20260514T054109_result.json`
- **Structured JSON:** [`09c8fe91e7e7b3fd17de.json`](../../sessions/09/09c8fe91e7e7b3fd17de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All fixes verified. Summary of changes:

| 问题 | 修改前 | 修改后 | 文件 |
|------|--------|--------|------|
| Bootstrap B 值 | `$B = 10,000$` | `$B = 1,000$` (匹配代码 `N_BOOTSTRAP = 1000`) | methodology.tex:78 |
| GPU 型号 | NVIDIA RTX 6000 Ada 96 GB | NVIDIA RTX PRO 6000 Blackwell Server Edition 96 GB | methodology.tex:86 |
| II 公式一致性 | 已经一致 — background.tex 已使用 $r_a$ 下标和匹配 methodology 的 $\text{PPL}_a$ 约定 | 无需修改 | — |

background.tex 中不再提及 bootstrap（统计细节全部集中在 methodology.tex §5.6），且 II 公式已使用 $r_a$（非旧版 $R_h$），与 methodology 一致。

---
