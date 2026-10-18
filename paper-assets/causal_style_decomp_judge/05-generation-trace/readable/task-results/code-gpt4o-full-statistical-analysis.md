# code gpt4o full statistical analysis

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpt4o_full_statistical_analysis_20260521T052945_result.json`
- **Structured JSON:** [`f18ebfe9a21fa4034a40.json`](../../sessions/f1/f18ebfe9a21fa4034a40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 项分析成功完成。结果：

```
=== GPT-4o Statistical Analysis Summary ===

LIKERT ATE:
| Axis       | ATE     | p (Wilcoxon)  | Cohen d  | Tie Rate  |
|------------|---------|---------------|----------|-----------|
| verbosity  | +0.1163 | 0.4033        | +0.0780  | 0.5814    |
| register   | +0.0000 | 0.7849        | +0.0000  | 0.6489    |

BRADLEY-TERRY:
| Axis       | P(style)  | CI [lo, hi]        | p-value    |
|------------|-----------|--------------------|------------|
| verbosity  | 0.7602    | [0.6881, 0.8283]   | 0.0001     |
| register   | 0.5699    | [0.5000, 0.6398]   | 0.0400     |

GEE DECOMPOSITION:
| Axis       | Style OR  | Style p    | Orig OR  | Orig p     |
|------------|-----------|------------|----------|------------|
| verbosity  | 10.9719   | < 0.0001   | 0.4373   | 0.0514     |
| register   | 1.8759    | 0.0285     | 2.2098   | 0.0058     |
```

脚本已写入 `csd_pipeline/gpt4o_analysis.py`。

**关键发现**：
- **Likert ATE**：两轴均不显著（verbosity ATE=+0.12, p=0.40; register ATE=0, p=0.78），高 tie rate (~58-65%)
- **BT pairwise**：GPT-4o 强烈偏好 verbose（P=0.76, p=0.0001）；轻微偏好 academic（P=0.57, p=0.04）
- **GEE**：verbosity style effect 极强（OR=10.97, p<0.0001），originality 边际不显著（OR=0.44, p=0.051）；register style 显著（OR=1.88, p=0.03），但 originality 效应更强（OR=2.21, p=0.006）

---
