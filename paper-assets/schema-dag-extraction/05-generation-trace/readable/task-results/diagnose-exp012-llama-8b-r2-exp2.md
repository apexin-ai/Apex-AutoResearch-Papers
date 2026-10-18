# diagnose exp012 llama 8b r2 exp2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp012_llama_8b_r2_exp2_20260515T200434_result.json`
- **Structured JSON:** [`6bf7d4c90863659ba857.json`](../../sessions/6b/6bf7d4c90863659ba857.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：进程正常运行中。**

关键信息：
- **PID 321037 存活**，子进程 321407 (VLLM::EngineCore) 占用 ~78GB GPU 显存
- **进度 ~48%**：总 44 batches，已完成 21 个，当前在 count_6/random/19，预计再 10-15 分钟完成
- **日志持续产出**，vLLM 推理速度正常（~400K toks/s input）
- **磁盘 85%**，暂无风险

异常点：etime 仅 9 分钟，与"2 小时前提交"不符——可能是脚本前置阶段耗时或实际启动延迟。Registry 状态应从 PREPARING 更新为 RUNNING。

报告已写入 `artifacts/exp012_exp2_diagnosis.md`。

---
