# analysis paired bootstrap

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paired-bootstrap_20260514T212555_result.json`
- **Structured JSON:** [`8cb7904c5cccfd35ee3a.json`](../../sessions/8c/8cb7904c5cccfd35ee3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 对比 | Method A | Method B | Δ macro_f1 | 95% CI | p-value |
|------|----------|----------|-----------|--------|---------|
| 1 | Structural RF (0.9944) | Probe (0.9055) | +8.89pp | [7.37, 10.49] | < 0.001 |
| 2 | Probe (0.9055) | LLM-as-Judge (0.6625) | +24.30pp | [21.74, 26.83] | < 0.001 |
| 3 | Probe (0.9055) | Cosine Sim (0.5606) | +34.49pp | [31.78, 37.14] | < 0.001 |
| 4 | Struct GB vs Probe (OH) | — | **跳过** | — | — |

**备注**：
- 所有 3 个 in-domain 比较均 p < 0.001（10000 次 bootstrap 中没有一次翻转符号），差异显著
- RF 重跑 macro_f1=0.9944（vs 论文报告 0.9951），微小差异来自 sklearn 版本/随机性
- 对比 4（cross-agent OH）跳过：Structural GB 评估集为全部 150,652 OH windows，而 Probe 在 20,807 OH test windows 上评估，两者不可直接 pair。需重跑 GB 在 OH test split 上的 inference

脚本和结果 JSON 均已保存在服务器 `/root/autodl-tmp/agent_progress_probe/` 下。

---
