# code lora load fix

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lora-load-fix_20260514T051705_result.json`
- **Structured JSON:** [`c82b9560e74061981db3.json`](../../sessions/c8/c82b9560e74061981db3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。

**改动摘要：**

1. **第 19 行** — import 增加 `PeftModel`
2. **第 96-121 行** — 替换原来的直接加载逻辑为 adapter 检测分支：
   - 检查 `sft_path / "adapter_config.json"` 是否存在
   - **LoRA adapter 路径**：用 `args.model_name` 加载 base model → `PeftModel.from_pretrained` 加载 adapter → `merge_and_unload()` 合并
   - **完整模型路径**：直接 `from_pretrained(sft_path)`
   - `pad_token` 设置移到分支之后统一处理

---
