# diag evaluate py version check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_evaluate-py-version-check_20260520T170307_result.json`
- **Structured JSON:** [`aea9b5eccd40ec2ba8fe.json`](../../sessions/ae/aea9b5eccd40ec2ba8fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入。总结：

**MMLU 和 ARC eval 数据可信**。cqa1 与 westd 的 `evaluate_mcq()` 函数（MMLU/ARC 代码路径）经逐段 hash 验证完全一致。+184 bytes 差异全部来自 GSM8K/HumanEval 函数中添加的 `system_prompt="You are a helpful assistant."`（4处×46字节）。

**受影响范围**：
- MMLU: 不受影响
- ARC: 不受影响
- GSM8K: westd 上 5 个 eval（qwen14b_d100_s42, gemma2_d000/d100_s42_fixed, qwen14b_d000/d100_s123）在修改后运行，带了 system_prompt，与 cqa1 产出不一致。如需混用需重跑这 5 个。

**C009 合规问题**：westd eval 脚本中的 EXPECTED_MD5 已被更新为新版本 hash，绕过了版本一致性检查。应恢复为 cqa1 参考值 `001a9bc23f808c47d25ef9eaeecb81f1`。

---
