# analysis 8b scaling results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_8b-scaling-results_20260512T092218_result.json`
- **Structured JSON:** [`e1fe07164e66e9cab016.json`](../../sessions/e1/e1fe07164e66e9cab016.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。汇总：

## 8B Model-Size-Scaling 结果

### Classification 8B (cls8b) — **SUCCESS**

| 指标 | 4B baseline | 8B | Δ |
|------|------------|-----|-----|
| accuracy | 88.41 | **90.48** | +2.07 |
| pass_f1 | 88.41 | **90.86** | +2.45 |
| fail_f1 | 88.40 | **90.06** | +1.66 |

### CWM 8B (cwm8b) — 几乎无提升

| 指标 | 4B baseline | 8B | Δ |
|------|------------|-----|-----|
| accuracy | 87.51 | 87.67 | +0.16 |
| pass_f1 | 87.31 | 87.57 | +0.26 |
| fail_f1 | 87.71 | 87.77 | +0.06 |
| exact_match | 84.02 | 84.39 | +0.37 |

### 核心发现：cls-cwm gap 随模型增大显著扩大

| 指标 gap (cls-cwm) | 4B | 8B | 扩大倍数 |
|----------|------|------|------|
| accuracy | 0.90pp | **2.81pp** | 3.1× |
| pass_f1 | 1.10pp | **3.29pp** | 3.0× |
| fail_f1 | 0.69pp | **2.29pp** | 3.3× |

**结论**：Classification 的 scaling 效率远优于 CWM generation。4B 时两者几乎无差距，8B 时 gap 扩大 ~3 倍。强烈支持 complexity hypothesis —— CWM 的瓶颈不在模型容量，而在生成精确错误信息的任务复杂度本身。

---
