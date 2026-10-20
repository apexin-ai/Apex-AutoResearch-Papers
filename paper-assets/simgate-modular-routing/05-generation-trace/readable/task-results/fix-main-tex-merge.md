# fix main tex merge

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_main-tex-merge_20260514T132822_result.json`
- **Structured JSON:** [`00c15acc99baaca4c165.json`](../../sessions/00/00c15acc99baaca4c165.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，5 页 PDF，无错误。

合并完成。本地和远程已同步一致（编辑在本地完成后上传到远程）。

### 合并结果摘要

| 检查项 | 状态 |
|--------|------|
| `representation-to-generation gap` 不存在 | PASS |
| `logit-to-generation gap` 不存在 | PASS |
| `96.2` 不存在 | PASS |
| `98.2` 不存在 | PASS |
| `65.4%` (GA=8) 在正确位置 | PASS |
| `96.3%` 在 experiments/conclusion/introduction | PASS |
| `97.4%` tie rate 在 abstract/intro/method | PASS |
| `95% Bootstrap CIs` 在 Table 1 caption | PASS |
| Limitations + Ethics Statement 独立 section | PASS |
| Related Work 含 ARES 52.7%, Dyna-Think 685B 细节 | PASS |
| `logit--generation gap` (em-dash) 在 Limitations | PASS |
| 编译通过 | PASS |

### 具体变更

- **main.tex**: `logit-to-generation` → `logit--generation`
- **experiments.tex**: `Bootstrap CIs` → `95% Bootstrap CIs`, `96.2%` → `96.3%` (×2)
- **introduction.tex**: `96.2%` → `96.3%`
- **conclusion.tex**: `96.2%` → `96.3%`
- **related_work.tex**: ARES 加 `reduces token cost by 52.7%`, Dyna-Think 加 `matching 685B performance with 32B at half the token cost`
- **abstract.tex / method.tex**: 无变更（本地已正确）

---
