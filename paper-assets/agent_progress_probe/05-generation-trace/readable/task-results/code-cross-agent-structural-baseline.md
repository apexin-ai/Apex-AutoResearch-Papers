# code cross agent structural baseline

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross-agent-structural-baseline_20260514T170555_result.json`
- **Structured JSON:** [`b974823cfecb701d31e2.json`](../../sessions/b9/b974823cfecb701d31e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

## Cross-Agent Structural Baseline 结果

| 设置 | Model | Macro F1 | F1_stag | F1_prog |
|------|-------|----------|---------|---------|
| **In-domain (SWE-Agent test)** | LR | 0.9874 | 0.9815 | 0.9933 |
| | RF | 0.9951 | 0.9928 | 0.9974 |
| | GB | 0.9951 | 0.9928 | 0.9974 |
| **Cross-agent OH (all, N=150652)** | LR | 0.7801 | 0.6842 | 0.8760 |
| | RF | 0.9123 | 0.8658 | 0.9587 |
| | GB | **0.9674** | 0.9479 | 0.9869 |
| **Cross-agent OH (conf≥2, N=43376)** | LR | 0.9671 | 0.9477 | 0.9865 |
| | RF | **0.9959** | 0.9935 | 0.9984 |
| | GB | 0.9919 | 0.9869 | 0.9968 |

### 对比 Probe

| Method | In-domain | Cross-agent (zero-shot) |
|--------|-----------|------------------------|
| GRU Probe | 0.9055 | 0.5320 |
| Probe (full-finetune) | - | 0.7510 |
| **Struct+GB** | **0.9951** | **0.9674** (all) |
| **Struct+RF** | **0.9951** | **0.9959** (conf≥2) |

### 关键结论

结构特征的跨域迁移**远优于** probe：
- Struct+GB 在 OH 全量数据上 macro_f1=0.9674，比 probe full-finetune (0.751) 高 **+0.216**
- Struct+RF 在 OH conf≥2 上 macro_f1=0.9959，几乎完美
- 这说明**停滞检测任务的大部分信号存在于结构特征中**（命令重复、相似度、类型分布），而非语义内容
- In-domain 数字完全匹配 `non_nlp_baseline_results.json`（LR=0.9874, RF/GB=0.9951）

JSON 已保存到 `/root/autodl-tmp/agent_progress_probe/data/cross_agent_structural_results.json`

---
