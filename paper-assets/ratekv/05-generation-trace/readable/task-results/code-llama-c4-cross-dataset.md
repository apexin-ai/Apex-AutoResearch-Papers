# code llama c4 cross dataset

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_c4_cross_dataset_20260514T121428_result.json`
- **Structured JSON:** [`546d42eea366c2991665.json`](../../sessions/54/546d42eea366c2991665.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常运行中。模型加载完成，Phase 1 C4 profiling 已开始。

**已完成**：
- 脚本 `run_llama_c4_cross_dataset.py` 已创建并上传到服务器
- 实验 `llama_c4_cross_dataset` 已通过 `submit_training_job` 在 westd-37397 cuda:0 上启动
- Registry 已更新为 RUNNING

**脚本流程**（6 个 phase）：
1. C4 profiling（16×512，标准分辨率）
2. C4-calibrated MCKP 求解（budget=0.25, max_2bit=2）
3. 加载 WT2 hires profiles，用相同约束重新求解 MCKP
4. 计算 C4 vs WT2 allocation agreement rate
5. WT2 test eval（BF16 / C4-cal MCKP / WT2-cal MCKP / uniform 4-bit）
6. C4 cross-domain eval（BF16 / WT2-cal MCKP / C4-cal MCKP / uniform 4-bit）

结果输出到 `llama_c4_cross_dataset_results.json`，日志到 `llama_c4_cross_dataset.log`。预计 profiling ~45min + eval ~10min。

---
