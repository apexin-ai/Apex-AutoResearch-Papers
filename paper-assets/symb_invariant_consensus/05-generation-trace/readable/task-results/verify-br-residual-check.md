# verify br residual check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_br-residual-check_20260522T224205_result.json`
- **Structured JSON:** [`9035d9c1b95c93d2b058.json`](../../sessions/90/9035d9c1b95c93d2b058.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### 3.93 残留
| 文件 | 行号 | 说明 |
|------|------|------|
| `docs/paper/r8_response_drafts.md` | 31 | rebuttal 草稿中写了 `$3.93\times$ (Qwen-14B)` |

仅 1 处，在 `.md` 草稿文件中，**不在任何 `.tex` 文件中**。

### 3.85 出现位置（已更新值）
| 文件 | 行号 | 说明 |
|------|------|------|
| `analysis.tex` | 31 | Table 行：Qwen-14B BR = 3.85 |
| `appendix.tex` | 415 | alpha-ablation 表 caption |
| `appendix.tex` | 602 | cross-model bias 讨论段落 |
| `diagnosis.tex` | 55, 138 | 正文引用 |

### 结论

**tex 文件无残留**——所有 `.tex` 中 Qwen-14B 的 BR 已统一为 3.85。唯一的 3.93 残留在 `r8_response_drafts.md`（rebuttal 草稿），需要更新该处为 3.85。是否修改？

---
