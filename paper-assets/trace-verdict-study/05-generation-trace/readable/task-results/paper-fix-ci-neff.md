# paper fix ci neff

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_ci_neff_20260515T195655_result.json`
- **Structured JSON:** [`53fcdfadbd5638bb778b.json`](../../sessions/53/53fcdfadbd5638bb778b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，0 errors，0 实际 warnings。

---

**修改汇总：**

| 文件 | 位置 | 旧值 | 新值 |
|---|---|---|---|
| `experiments.tex:30` | Table 1 caption | `[99.58, 100.00]` | `[98.81, 99.91]$^*$` + 脚注说明 |
| `experiments.tex:58` | Table 2 body | `[99.58, 100.00]` | `[98.81, 99.91]$^*$` |
| `experiments.tex:66` | Table 2 caption | — | 添加 `$^*$CI computed with $N_\text{eff}{=}607$` 脚注 |
| `method.tex:20` | dedup 段落 | — | 添加 N_eff=607 CI 说明句 |

**Wilson CI (N_eff=607, k=605):** [99.58, 100.00] → **[98.81, 99.91]**

编译结果：12 pages，0 errors，0 warnings。

---
