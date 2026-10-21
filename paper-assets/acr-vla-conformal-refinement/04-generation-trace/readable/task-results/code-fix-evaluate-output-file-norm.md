# code fix evaluate output file norm

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-evaluate-output-file-norm_20260515T181246_result.json`
- **Structured JSON:** [`0be45221a70a9a94622f.json`](../../sessions/0b/0be45221a70a9a94622f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。4 台服务器修复结果：

| 服务器 | 代码修改 | `--help` 验证 |
|--------|---------|--------------|
| bjb1-32546 | ✓ | ✓ |
| bjb1-18228 | ✓ | ✓ |
| bjb2-28827 | ✓ | ✓ |
| bjb2-40593 | ✓ | ✓ |

`output_file` 模板现在为 `logs/eval_{benchmark}_{mode}{norm_tag}_seed{seed}.json`，其中 `norm_tag` 在指定 `--max_correction_norm` 时为 `_norm{value}`，未指定时为空字符串，不影响现有无 norm 参数的实验路径。

---
