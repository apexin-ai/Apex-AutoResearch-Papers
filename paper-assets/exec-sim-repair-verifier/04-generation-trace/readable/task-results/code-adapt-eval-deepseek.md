# code adapt eval deepseek

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_adapt-eval-deepseek_20260516T052154_result.json`
- **Structured JSON:** [`68f979949bfcdac9a3aa.json`](../../sessions/68/68f979949bfcdac9a3aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。三个 eval 脚本已适配 DeepSeek-Coder-6.7B-Instruct：

**修改内容：**
1. 新增 `detect_model_family()` — 根据模型名自动识别 `qwen`/`deepseek`/`auto`
2. 将 `detect_thinking_support()` 替换为 `get_chat_template_kwargs(family, tokenizer)` — Qwen 传 `enable_thinking=False`，DeepSeek 无特殊参数
3. 新增 `get_stop_token_ids(family, tokenizer)` — Qwen 用 `<|im_end|>`/`<|endoftext|>`，DeepSeek 用 `<|EOT|>`/`<｜end▁of▁sentence｜>`
4. 新增 `_apply_chat_template_safe()` — 若 system role 不被支持（部分 DeepSeek 模型），自动合并 system 到 user message
5. `model.generate()` 加上 `eos_token_id=eos_ids` 确保正确停止

**向后兼容：**
- `--model_name` 默认仍为 `Qwen/Qwen3-4B`，现有命令行不变
- DeepSeek 只需传 `--model_name deepseek-ai/deepseek-coder-6.7b-instruct`

---
