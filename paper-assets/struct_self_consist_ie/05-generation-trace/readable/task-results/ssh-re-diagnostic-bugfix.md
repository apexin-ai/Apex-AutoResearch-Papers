# ssh re diagnostic bugfix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_re_diagnostic_bugfix_20260522T075425_result.json`
- **Structured JSON:** [`e0f96bccc9f915401284.json`](../../sessions/e0/e0f96bccc9f915401284.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 三个 Bug

| Bug | 描述 |
|-----|------|
| 1. 错误数据源 | Worker 在 autodl-5090-c 的 `re_sc/re_samples.jsonl` 上运行，该文件来自一个极弱的模型（greedy micro F1 仅 0.069），而非 autodl-5090 上的正规数据 `exp_012_rerun_1024/samples_with_logprobs.jsonl`（micro F1 = 0.44） |
| 2. 错误匹配方式 | 用 text-based `(head_text, type, tail_text)` 匹配，而非标准的 span-based `(head_start, head_end, tail_start, tail_end, type)` |
| 3. 错误 zero-F1 定义 | 计算"所有 8 个 sample 的 F1 = 0"的 instance 比例，而非"greedy F1 = 0"的 instance 比例 |

### 修正对比

| Metric | 原值 (错误) | 修正值 | 变化 |
|--------|-----------|--------|------|
| **Zero-F1%** | **71.8%** | **40.1%** (159/397) | **大幅修正** |
| Degeneracy | 0.8% | 10.1% | ↑ |
| Greedy F1 | 0.0752 | 0.4042 | ↑ 大幅 |
| MV F1 | 0.0390 | 0.3452 | ↑ 大幅 |
| MV Δ | −3.62pp | −5.90pp | MV 损害更大 |
| LP-best F1 | 0.0760 | 0.3948 | ↑ 大幅 |
| LP-best Δ | +0.08pp | −0.94pp | 从微正变负 |
| Oracle F1 | 0.1541 | 0.5850 | ↑ 大幅 |
| Oracle headroom | +7.89pp | +18.08pp | ↑ 大幅 |
| LP-F1 ρ (pooled) | 0.1622 | 0.3501 | ↑ 显著增强 |
| LP-F1 ρ (within) | 0.2243 | 0.1573 | ↓ |

已完成：
- 修正脚本保存至 autodl-5090: `code/re_diagnostic_cascade.py`
- 更新 artifact: `re_diagnostic_cascade_pilot.md` 和 `complete_diagnostic_cascade_table.md`
- 更新 `mistakes.yaml` M060 状态为 fixed

---
