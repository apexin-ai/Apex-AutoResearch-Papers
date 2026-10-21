# eval deepseek cwm repo s42

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_deepseek-cwm-repo-s42_20260517T154619_result.json`
- **Structured JSON:** [`e6c2e70ca9d2fe8f440d.json`](../../sessions/e6/e6c2e70ca9d2fe8f440d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正在稳定运行中。当前状态：

- **模型**: DeepSeek-Coder-6.7B + LoRA (CWM repo-level, seed=42)
- **Test 数据**: `swebench_full/swebench_test.jsonl`, n=9784
- **GPU**: cuda:1 (5090)
- **速度**: ~3.3 秒/样本, 预计总时间 ~9 小时
- **修复内容**:
  1. Prompt 模板对齐（训练用 "## Code" / eval 原来用 "## Patch (git diff)"）
  2. Parser 改进（添加 Traceback 检测、PASSED/FAILED 计数、BPE 解码）
  3. `max_new_tokens` 从 512 降到 128 加速 4x
- **初始 accuracy**: ~71-82% (14 samples), 趋势良好

4.5 分钟后自动检查进度。

---
