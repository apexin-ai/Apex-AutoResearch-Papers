# diagnose fewrel 40rel r2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_fewrel_40rel_r2_20260515T170645_result.json`
- **Structured JSON:** [`99de03fa63a45dad3918.json`](../../sessions/99/99de03fa63a45dad3918.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 总结

### exp_fewrel_40rel_r3
- 已结束，EXIT_CODE=0，但**只做了 exp2 预处理**
- **无任何预测结果产出**（exp1/exp2 均无 predictions_*.json）

### r2 OOM 根因
- vLLM 参数与成功的 `run_fewrel_formal.py` **完全一致**
- OOM 发生在模型权重加载阶段（shard 1/7），不是推理阶段
- 最可能原因：**当时有其他 GPU 进程占用显存**

### 已修复
1. `src/run_fewrel_40rel.py` 第 90 行：`gpu_memory_utilization` 从 0.95 降到 **0.85**（增加安全裕量）
2. `scripts/run_fewrel_40rel.sh` 已确认包含 `FLASHINFER_DISABLE_VERSION_CHECK=1`
3. 语法检查通过 (SYNTAX_OK)

---
