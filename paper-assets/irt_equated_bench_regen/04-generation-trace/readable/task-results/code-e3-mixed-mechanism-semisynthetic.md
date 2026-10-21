# code e3 mixed mechanism semisynthetic

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e3_mixed_mechanism_semisynthetic_20260523T012835_result.json`
- **Structured JSON:** [`c7384bb4862a33ca6987.json`](../../sessions/c7/c7384bb4862a33ca6987.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部文件已生成。结果总结：

**Scheme D** (base=difficulty-dependent, instruct=uniform) 更接近观测数据（L2=0.246 vs 0.351）：
- ρ_overall = **-0.676** (观测 -0.597，方向正确但偏强)
- ρ_base = **-0.638** (观测 -0.570，接近)
- ρ_instruct = **-0.302** (观测 -0.079，偏强 — 注入推动 instruct ρ 负向太多)
- χ² = **634.4** (观测 562.7，匹配良好)

**关键发现**：
1. 两个 scheme 都能**同时复现** overall ρ≈-0.6 AND direction reversal χ²>100
2. Scheme D 更优，因为它的 instruct ρ 更接近 0（-0.302 vs -0.418），但仍然比观测值 -0.079 强太多
3. 残差主要在 instruct 维度：即使用 uniform injection，instruct 的 ρ 也被 ceiling effect 推向 -0.3，而观测值仅 -0.079 — 说明实际中 instruct models 的"contamination"可能比我们注入的 30% 更稀疏，或者存在其他机制（如 instruction-following 能力提升）抵消了 contamination 信号

---
