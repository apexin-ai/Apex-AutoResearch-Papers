# research swebench pipeline design

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_swebench-pipeline-design_20260511T235646_result.json`
- **Structured JSON:** [`8c94c0f1be9f28e8526d.json`](../../sessions/8c/8c94c0f1be9f28e8526d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案已写入 `artifacts/swebench_pipeline_design.md`。

核心要点：
- **~75K 样本**：500 instances × 15 patches × 10 tests/instance
- **推荐方案 C（混合变异）**：gold + 合成变异 + LLM patches + 部分修复，兼顾数据量保底和真实错误分布
- **执行耗时 32-62h**（4 并行 Docker），纯 CPU，不占 GPU
- **数据格式与现有 train.jsonl 向后兼容**，code 字段改为 patch diff + modified files，test 字段为单个测试函数
- **5 个待确认决策点**列在文末（变异策略、context 粒度、split 策略、是否混合函数级数据、Docker 环境确认）

---
