# code mf1 worked examples v2

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mf1_worked_examples_v2_20260522T035218_result.json`
- **Structured JSON:** [`21ff5d2c615eeef5282d.json`](../../sessions/21/21ff5d2c615eeef5282d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件在 `artifacts/mf1_worked_examples/`:

**全局 flip 统计**: τ=0.9594, flip_rate=2.03%, 约 276,980 对模型发生排名翻转。

**5 个推荐 worked example pairs**（均为跨 family、大幅翻转）:
1. **Phi-3 vs Mistral** — full 差 803 位，cleaned 后反转 544 位
2. **Llama-3 vs Mistral** — full 差 759 位，cleaned 后反转 581 位
3. **Qwen-1.5 vs Mistral-0.1** — 含官方 Qwen 发布模型
4. **Llama-3 vs Mixtral** — 跨 dense/MoE 架构
5. **Phi-3 vs Zephyr** — 不同架构族

**论文数字核实**:
- Llama-3 "+53" → ✅ 确认是 **median**（mean=+121）
- Mistral "−35" → ✅ 来源是 `mistral` + `mistral-0.1` **合并后的 median**（mistral 单独 median=−32，mistral-0.1 单独 median=−47.5）。建议论文注明合并口径。

---
