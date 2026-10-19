# analysis paper data audit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_data_audit_20260525T194736_result.json`
- **Structured JSON:** [`084f215c41dcae86ddbc.json`](../../sessions/08/084f215c41dcae86ddbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/data_audit_report.md`。

**核心结论：~280 个数字中 96% 精确匹配 registry。** 主表 (Table 1)、C1 表 (Table 2)、Ablation 表 (Table 3) 全部通过。

**3 个需要修复的问题：**

1. **Qwen-14B KL uniform 行（附录 Table 7）**— ARC-c 差 1.03pp，GSM8K s123 差 1.68pp，HS/PIQA 的 std 也不对。根因是该行数据拼凑自不同版本实验（pre/post D075 sigmoid fix、不同服务器）。建议用统一代码版本重跑 s42+s123 并注册。

2. **C1 PPL gap "0.65pp" 应为 "0.63pp"**— 出现在 abstract、conclusion、experiments footnote 三处。9.4463−8.8157=0.6306，四舍五入是 0.63 不是 0.65。

3. **Lagrangian 50% actual sparsity**— 论文写 0.504，registry 里对应实验是 0.4979。final_λ=8 来自另一个实验。

**4 个小问题：** MSE 30% std 1.68→1.67、"≤29%" MMLU 但 TEAL=29.26%、C4 30% PPL 16.03→16.04、conclusion "14.5% across three architectures" 措辞不准。

---
