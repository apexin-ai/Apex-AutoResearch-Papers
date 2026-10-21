# ops fix tokenizer cka only 30

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_tokenizer_cka_only_30_20260517T215823_result.json`
- **Structured JSON:** [`ba3fccca5a2cbee798d9.json`](../../sessions/ba/ba3fccca5a2cbee798d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载，没有 tokenizer 报错。

## 产出

1. **Tokenizer 来源**: base model (`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/`)，复制了 `tokenizer.json` 和 `tokenizer_config.json`。`special_tokens_map.json` 在 base model 中本身不存在（Qwen 系正常）。
2. **新 PID**: 59403
3. **GPU 确认**: cuda:2，进程已启动，模型加载中（日志显示正常检测到 Non-uniform MLP）。

---
