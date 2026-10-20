# paper method section

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_method-section_20260516T041831_result.json`
- **Structured JSON:** [`1a77fe039fd38940de57.json`](../../sessions/1a/1a77fe039fd38940de57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section 草稿已写入 `paper/sections/method.md`，1136 words（含数学标记）。

关键设计决策与代码验证结果：

1. **公式与代码一致**：Stan 实现中 γ·e 在 logit scale 上与 a_i(θ_j - b_i) **相加**，不在 a_i 乘法内部。写作计划中的 `a_i(θ_j - b_i + γ_k·e_{ij})` 与代码不符，已修正为 `a_i(θ_j - b_i) + γ_k·e_{ij}`。这使 γ_k 的解释更清晰：对最大暴露项的 uniform logit shift，不依赖 item discrimination。

2. **先验与 MCMC 设置**：全部从 Stan 代码核实——θ~N(0,1), a~LogNormal(0,0.5), b~N(0,1), c~Beta(5,20), d~Beta(20,5), γ~N(0,1)；4 chains, 1000+1000, adapt_delta=0.95。

3. **RRF**：k=60, equal weights, min-max normalized，代码核实一致。

4. **Signals**：s1+s2+s4 三信号（s3 排除），与代码 `SIGNAL_KEYS` 一致。

5. **符号体系**：i=item, j=model, k=benchmark，贯穿一致。

---
