# infra fix path bug urgent

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_path_bug_urgent_20260521T234337_result.json`
- **Structured JSON:** [`63a894fee91c8be85945.json`](../../sessions/63/63a894fee91c8be85945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**Bug 修复**
- 创建了双重路径目录 `data/{model}/data/{model}/`，防止 Llama 结果丢失
- 修复了 `train_probe.py` 中的 `output_filename` 逻辑：`--output_file` 传入完整路径时只取 basename，避免与 `--output_dir` 重复拼接
- Llama 结果已从错误路径复制到正确路径

**Qwen 结果从 log 恢复完成**

**两模型 n=100 Bootstrap 最终结果**

| 方向 | Llama-3.1 bal_acc | Qwen-3 bal_acc |
|------|-------------------|----------------|
| EN→EN | 0.7710±0.0119 | 0.7528±0.0168 |
| ZH→ZH | 0.7124±0.0127 | 0.7162±0.0179 |
| EN→ZH | 0.6405±0.0245 | 0.6496±0.0273 |
| ZH→EN | 0.7127±0.0270 | 0.7215±0.0256 |

两模型跨语言迁移格局一致：同语言 > 跨语言，ZH→EN 迁移优于 EN→ZH。

---
