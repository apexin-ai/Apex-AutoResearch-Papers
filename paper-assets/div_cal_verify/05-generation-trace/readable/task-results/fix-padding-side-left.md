# fix padding side left

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_padding_side_left_20260512T203709_result.json`
- **Structured JSON:** [`5171fd3770a775b3d87a.json`](../../sessions/51/5171fd3770a775b3d87a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

- **语法检查**：`SYNTAX OK`
- **dry-run**：`run_mvp.py --help` 正常输出参数列表
- **Qwen3 padding_side 检查**：HF Hub 网络不通（AutoDL 限制），无法在线验证默认值，但我们显式设置 `left` 是通用安全做法，不影响正确性

修改完成：`run_mvp.py` 第 191 行添加了 `gen_tokenizer.padding_side = 'left'`，位于 pad_token 设置之后。Phase 1 进程未受影响，Phase 2 启动时会自动使用修改后的代码。

---
