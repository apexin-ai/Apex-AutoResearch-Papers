# code virology lz diagnostic

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_virology-lz-diagnostic_20260520T132643_result.json`
- **Structured JSON:** [`b34df072fb4488255c7a.json`](../../sessions/b3/b34df072fb4488255c7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心发现：

**双重根因，而非单一 θ 错配：**

1. **θ 错配**（已知）：global θ=0.78 vs MMLU θ\_MLE=4.0。在 θ=0.78 下 68/166 virology items P<0.5，导致 lz\*=-8.21。

2. **d\_feasibility 病态**（新发现，更深层）：virology **全部 166 个 items 的 d<1.0**（mean=0.71, min=0.19）。4PL 中 d 是 P(correct) 的上限——即使 θ→∞，P(correct)→d。因此 58/166 items 在 θ=4.0 下仍 P<0.5。**即使用"正确"的 θ=4.0，virology lz\* 仍为 -3.27（负值）。** 这不是 person-fit 异常，而是 PSN-IRT calibration artifact。

**对论文的影响：**
- Overall MMLU lz\*=34.75 **不受影响**（θ=0.78→34.75, θ=4.0→31.81）
- Per-subject 分析需加 caveat：global θ 下的分解是近似的，且 d 参数普遍低于 1 的科目（如 virology）不适用
- 仅 2/57 subjects 在 θ=0.78 下 lz\*<0，1/57 在 θ=4.0 下仍 <0

产出已注册：`virology_diagnostic_report.md` + `virology_diagnostic.py`。

---
