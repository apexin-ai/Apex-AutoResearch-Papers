# gpu 14b conll check and retry

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_14b_conll_check_and_retry_20260521T111624_result.json`
- **Structured JSON:** [`73594efbb3a5f060d619.json`](../../sessions/73/73594efbb3a5f060d619.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B CoNLL v2 推理结果

**状态：完成** — samples.jsonl 行数 = 3453（完整）

### 核心指标

| 指标 | 值 |
|------|-----|
| Greedy F1 | 0.0462 |
| Oracle F1 | 0.1549 |
| Oracle headroom | +0.1087 |
| Fleiss' κ (mean) | 0.3712 |
| Soft Jaccard (mean) | 0.6580 |
| Sample F1 (mean) | 0.0397 |
| Sample F1=0 (%) | **95.2%** |

### 相关性分析

| | Full (n=2756) | Conditional (n=161) |
|---|---|---|
| ρ(κ, F1) | -0.099 (p=1.7e-7) | **-0.339** (p=1.1e-5) |
| ρ(SJ, F1) | -0.270 (p=2.0e-47) | -0.231 (p=3.2e-3) |
| Structural > Surface | **NO** (delta=-0.171) | |

### Logprob baseline

| | ρ | τ | AUROC |
|---|---|---|---|
| Full | -0.187 | -0.152 | 0.272 |
| Conditional | -0.307 | -0.241 | 0.286 |

### Verdict: **FAIL**
- 95.2% samples F1=0，模型基础 NER 能力极差
- 所有相关性为**负**，consistency 指标与质量反相关
- 建议：re-run at T=0.7（但根本问题是 14B finetuned on FewNERD 在 CoNLL 上 zero-shot 表现极差）

### GPU 状态 (5090-c)

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 空闲 |
| 1 | 0% | 空闲 |
| 2 | 0% | **空闲**（14B 已退出） |
| 3 | 75% | 30295/32607 MiB（有任务运行中） |

GPU 0/1/2 全部空闲。GPU 3 仍有进程占用。

---
