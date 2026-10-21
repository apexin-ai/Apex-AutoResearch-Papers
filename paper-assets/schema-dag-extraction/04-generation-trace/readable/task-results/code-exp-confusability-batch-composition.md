# code exp confusability batch composition

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_confusability_batch_composition_20260516T061306_result.json`
- **Structured JSON:** [`db4e4b199d04e6316c93.json`](../../sessions/db/db4e4b199d04e6316c93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-018 已提交运行。

**摘要**：
- 脚本：`src/run_confusability_batch_composition.py` — 统一运行所有 3 个条件，vLLM 只加载一次
- **17 个条件**：1 confusability_aware + 15 random seeds (CI) + 1 single_pass
- **16,320 次推理**，预计 ~218 分钟
- Graph coloring 分组成功降低了 intra-batch BCS（0.5524 vs random 均值 ~0.558）
- PID=373174，日志：`logs/exp018_confusability_batch.log`
- Registry: `exp_confusability_batch_composition` → RUNNING
- 支持 `--resume` 断点续传（按 condition 粒度记录进度）
- 分析阶段自动计算 random batch 的 95% CI、per-type accuracy delta（confusability vs random mean）

---
