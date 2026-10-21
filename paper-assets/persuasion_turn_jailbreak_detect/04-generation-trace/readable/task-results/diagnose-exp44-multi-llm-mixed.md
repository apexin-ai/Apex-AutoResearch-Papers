# diagnose exp44 multi llm mixed

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp44_multi_llm_mixed_20260522T055445_result.json`
- **Structured JSON:** [`ff7b694382a422e55213.json`](../../sessions/ff/ff7b694382a422e55213.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**exp44 没有崩溃，是监控误报。** 进程 PID 31463 当前仍在正常运行。

核心发现：
- 3 个 seed 的训练**全部完成**，当前处于**评估阶段**（Seed 42 评估完毕，Seed 123 正在推理中）
- Seed 42 评估结果极好：IID F1=1.0, WildChat FPR=0, 所有 OOD recall=1.0, 所有 Llama cross-LLM recall=1.0
- 日志中**无任何错误**（无 Traceback、OOM、Killed）
- GPU 状态正常（2.2GB / 97.8GB, 76% util），磁盘充足

**误报原因**：脚本不使用 W&B（仅在完成后写 JSON），监控系统检测不到心跳，加上可能跟踪了已结束的 FITD generation 进程 PID 而非当前训练 PID。

报告已保存到 `artifacts/exp44_multi_llm_mixed/diagnosis_report.md`。

---
