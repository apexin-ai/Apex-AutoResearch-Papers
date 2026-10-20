# eval 70b lora scierc inference

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_70b_lora_scierc_inference_20260522T021201_result.json`
- **Structured JSON:** [`aaf578223c059a25f6ca.json`](../../sessions/aa/aaf578223c059a25f6ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6/551 样本完成，推理正常进行中。

当前状态总结：

1. **已完成**：修复了 PEFT AWQ LoRA dispatch 兼容性问题（`peft/tuners/lora/awq.py` 中 `AwqGEMMQuantLinear` 改为 `AWQuantLinear` 以匹配 AwqMarlinLinear kernel），并给 `run_constrained_extraction.py` 添加了 `--lora_path` 参数

2. **正在运行**：unconstrained 推理 (PID 879994, cuda:0)
   - 551 samples × ~17s/sample ≈ 2.6 小时
   - 输出：`/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl`

3. **待执行**：unconstrained 完成后，需要启动 constrained S1 推理（同样路径，`--mode full_s1`），然后用 `check_violations.py` 提取指标

需要我定期检查进度还是等 unconstrained 完成后再通知你启动 S1？

---
