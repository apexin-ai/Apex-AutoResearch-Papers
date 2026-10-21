# analysis bootstrap dual benchmark

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-dual-benchmark_20260520T182818_result.json`
- **Structured JSON:** [`b73c7d68c8acfd807752.json`](../../sessions/b7/b73c7d68c8acfd807752.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是双 benchmark bootstrap CI 汇总：

## MMLU Δ(d100)

| Family | n | Δ(d100) | 95% CI | Pattern | Dir-Con |
|--------|---|---------|--------|---------|---------|
| Phi-4 | 3 | +0.72pp | [-0.17, +1.39] | Immune† | ✗ |
| Qwen-14B | 2 | -11.05pp | [-32.41, +10.30]ᵗ | Collapse | ✓ |
| Qwen-7B | 2 | -0.89pp | [-12.16, +10.37]ᵗ | V-recovery | ✗ |
| Gemma-2 | 2 | +2.62pp | [-11.81, +17.06]ᵗ | Benefit-sat† | ✓ |
| OLMo-2 | 3 | +1.35pp | [-0.55, +2.60] | Benefit-sat† | ✗ |

## ARC Δ(d100)

| Family | n | Δ(d100) | 95% CI | Pattern | Dir-Con |
|--------|---|---------|--------|---------|---------|
| Phi-4 | 3 | +0.65pp | **[+0.51, +0.77]** | Immune | ✓ |
| Qwen-14B | 2 | -2.86pp | [-6.65, +0.94]ᵗ | Collapse | ✓ |
| Qwen-7B | 2 | -2.65pp | [-5.90, +0.61]ᵗ | V-recovery† | ✓ |
| Gemma-2 | 1 | +2.73pp | [pt] | Benefit | ✓ |
| OLMo-2 | 3 | +3.44pp | **[+2.90, +3.78]** | Benefit-sat | ✓ |

关键发现：
- **ARC Dir-Con 全 ✓ (5/5)**，MMLU 仅 2/5 — ARC 的 contamination direction 跨 seed 更稳定
- **OLMo-2 两 benchmark 最强 Benefit**，ARC CI 完全 >0
- **n=2 families CI 极宽**（t-dist df=1），增加 seed 是收窄 CI 的唯一路径

脚本已添加 `--benchmark arc/mmlu` 参数。4 个 artifacts 已注册，memory.md 已更新。

---
