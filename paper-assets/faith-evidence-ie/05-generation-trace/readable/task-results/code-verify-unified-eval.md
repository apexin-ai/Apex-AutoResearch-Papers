# code verify unified eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_unified_eval_20260514T145338_result.json`
- **Structured JSON:** [`b76743fe33d4b3a14966.json`](../../sessions/b7/b76743fe33d4b3a14966.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/eval_script_audit.md`。

核心结论：

**eval 脚本不能直接评估 GRPO checkpoint。** 原因：`grpo_trainer.py` 先将 SFT adapter merge 进 base model，再训练新 LoRA。GRPO checkpoint 保存的是相对于 (Qwen3-4B + SFT merged) 的 delta，但 `inference.py` 只支持加载单个 adapter，会直接把 GRPO delta 应用到裸 Qwen3-4B 上，缺失 SFT 贡献。

其他方面没问题：
- Evi-F1、EDCR、Ign-F1 都已实现
- parse_model_output 统一解析逻辑全模型通用
- GRPO checkpoint 格式（LoRA adapter）与 SFT 一致

修复方案：给 `inference.py` 加一个 `--sft_adapter` 参数，加载时先 merge SFT 再叠 GRPO adapter，约 15 行改动。

---
