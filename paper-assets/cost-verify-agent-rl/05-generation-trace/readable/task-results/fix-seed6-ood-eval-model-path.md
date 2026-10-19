# fix seed6 ood eval model path

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_seed6_ood_eval_model_path_20260521T133730_result.json`
- **Structured JSON:** [`2b2c69b8f49902639e62.json`](../../sessions/2b/2b2c69b8f49902639e62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修复**：`ctx_manager.py:28` 的 `get_special_tokens()` 通过 `"qwen" in tokenizer.name_or_path.lower()` 识别模型类型。创建符号链接 `qwen_exp029_seed6_step15_hf` → 原 checkpoint 路径，更新 eval config 的 `model_path`。

**Eval 状态**：
- PID: 342378（westd-47453, cuda:2）
- Qwen3ForCausalLM 1.72B 已加载，vLLM 初始化中
- GPU 2 已占用 ~11 GB，正在启动
- 日志：`/tmp/exp029_seed6_ood_eval_v2.log`
- 134 OOD tasks, val_only 模式

---
