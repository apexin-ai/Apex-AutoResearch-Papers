# code smoke test and eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_smoke-test-and-eval_20260514T045135_result.json`
- **Structured JSON:** [`27778e4fc1b5afca5dd9.json`](../../sessions/27/27778e4fc1b5afca5dd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件编译通过。

**创建/修改的文件：**

1. **`training/smoke_test.py`** — 自包含 smoke test 脚本
   - 20 个合成样本（5 个文档模板循环 + 随机采样 triples）
   - Qwen3-4B + QLoRA 4-bit (nf4, double quant, bf16 compute)
   - LoRA r=64, 7 个 target modules
   - GRPOTrainer: num_generations=4, max_completion_length=256
   - DeepSpeed ZeRO-3 内联配置（CPU offload optimizer+param）
   - 仅用 `format_reward_fn`，无 NLI 模型依赖
   - 10 步训练后打印：每步 loss、梯度范数、4 卡峰值显存、总用时、PASS/FAIL 判定
   - enable_thinking=False
   - 零 freige import

2. **`eval/evaluator.py`** — 新增 `compute_format_compliance` 方法
   - `format_compliance_rate`: JSON list 可解析比例
   - `field_compliance_rate`: 每个 triple 含 head/relation/tail/evidence 的比例
   - `evidence_format_rate`: evidence 为 `list[int]`（非负）的比例
   - `evaluate()` 新增可选参数 `raw_outputs`，传入时自动包含格式合规指标

---
