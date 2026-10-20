# ops check codellama13b nomarker

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_codellama13b_nomarker_20260517T030052_result.json`
- **Structured JSON:** [`6ae2b647004aea431754.json`](../../sessions/6a/6ae2b647004aea431754.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：**已失败**

**原因**：模型路径 `/root/trace-verdict-study/models/CodeLlama-13b-Instruct-hf` 不存在。

服务器上 `/root/trace-verdict-study/models/` 只有：
- `Qwen2.5-Coder-1.5B-Instruct`
- `Qwen2.5-Coder-7B-Instruct`

CodeLlama-13b 模型从未下载到该服务器。训练脚本启动后立即在 tokenizer 加载阶段崩溃（`EXIT_CODE=1`）。

**修复方案**：需要先下载 CodeLlama-13b-Instruct-hf 到 `/root/trace-verdict-study/models/`，然后重新提交训练。是否继续？

---
