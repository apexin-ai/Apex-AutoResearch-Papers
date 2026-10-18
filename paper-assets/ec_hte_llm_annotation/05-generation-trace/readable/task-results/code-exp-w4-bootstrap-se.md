# code exp w4 bootstrap se

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-w4-bootstrap-se_20260522T095508_result.json`
- **Structured JSON:** [`95e77480abfb04f06841.json`](../../sessions/95/95e77480abfb04f06841.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。总结：

**W4 结果（6秒完成，远低于预估的2-4小时）**

| n_expert | Plug-in Cov | Bootstrap Cov | Combined Cov | Plug-in SE | Boot SE |
|----------|------------|---------------|-------------|-----------|---------|
| 50       | 0.970      | 0.790         | 0.980       | 0.0808    | 0.1703  |
| 100      | 0.960      | 0.680         | 0.970       | 0.0685    | 0.0805  |
| 250      | 0.970      | 0.380         | 0.970       | 0.0626    | 0.0167  |
| 500      | 0.970      | 0.280         | 0.970       | 0.0612    | 0.0100  |

**核心发现（与预期相反）**：Plug-in SE 在所有 expert budget 下都达到 95-97% 覆盖率，**不存在覆盖率缺口**。原因：noisy M̂⁻¹ 同时放大了校正误差和传播的 SE，形成自校准效应。

CM-only bootstrap SE 单独使用反而严重 under-cover（28-79%），因为它只捕获 CM 不确定性而遗漏了主导的 outcome 方差。Combined SE（√(plugin² + boot²)）在所有 budget 下保持 97-98% 覆盖率。

**Rebuttal R5-N3 要点**：Plug-in SE 在 n_expert=50 的极端条件下仍然充分，reviewer 的担忧不成立。LaTeX 段落已生成，代码和结果已注册到 artifacts。

---
