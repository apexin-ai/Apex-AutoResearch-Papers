# analysis plan 005 elab

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-005-elab_20260515T060053_result.json`
- **Structured JSON:** [`853280cf721d8a57cd3c.json`](../../sessions/85/853280cf721d8a57cd3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 和项目知识已更新。以下是三种 prompt type 的完整对比：

---

## Plan-005 三种 Prompt Type 对比

### Chain Retention (d4/d0)

| Prompt Type | Records | d0 | d1 | d2 | d3 | d4 | Retention |
|---|---|---|---|---|---|---|---|
| continuation | 4620 | 995 | 992 | 932 | 874 | 827 | **83.1%** |
| elaboration | 4946 | 995 | 995 | 989 | 986 | 981 | **98.6%** |
| inspired_rewriting | 4827 | 995 | 995 | 959 | 944 | 934 | **93.9%** |

### Depth Discriminability (XGBoost 3-class)

| Prompt Type | Within-type CV F1 | LOPTO F1 (cross-type) |
|---|---|---|
| continuation | **0.781** ± 0.012 | 0.762 |
| elaboration | 0.730 ± 0.011 | 0.762 |
| inspired_rewriting | 0.737 ± 0.011 | 0.733 |

### Feature Drift (d0→d4 relative change)

| Feature | continuation | elaboration | rewriting |
|---|---|---|---|
| entropy_mean | **−55.7%** | −47.1% | −47.7% |
| ttr | −60.7% | −64.1% | −61.8% |
| hapax_ratio | −74.0% | **−82.8%** | −80.0% |

### 核心发现

1. **Retention-discriminability tradeoff**: Elaboration 链最稳定 (98.6%) 但 depth signal 最弱 (F1=0.730)；continuation 丢链最多但存活样本的 depth fingerprint 最强 (F1=0.781)。
2. **跨 prompt type 信号可迁移**: LOPTO F1 ≈ 0.75，说明 depth signal 不是 prompt-type-specific 的，classifier 能跨类型迁移。
3. **词汇多样性特征主导**: ttr 和 hapax_ratio 在三种类型中都有 60–83% 的 collapse，是最可靠的 depth indicator。

---
