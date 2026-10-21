# code gradient flow v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient_flow_v2_20260519T143619_result.json`
- **Structured JSON:** [`202df76f62bc388f8bc3.json`](../../sessions/20/202df76f62bc388f8bc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**实验结果 — Gradient Flow Analysis (gradient_flow_analysis)**

| 指标 | CKA-only | Standard | 比值 |
|------|----------|----------|------|
| Attn 梯度均值 | 0.3135 | 0.1316 | **2.38x** |
| MLP 梯度均值 | 0.2850 | 0.1222 | **2.33x** |
| Attn cross-layer CV | 1.2231 | 1.1363 | ~1.08x |
| MLP cross-layer CV | 1.2424 | 1.1489 | ~1.08x |

**核心发现**：CKA-only 剪枝模型的梯度幅度是 Standard 的 **~2.4 倍**，两种剪枝的 cross-layer CV（梯度平滑度）相近。这说明 CKA-only 的 GRPO 恢复优势来自**更强的梯度信号**（更大的学习信号），而非梯度分布更均匀。

**产出文件**（westb-23072 上）：
- `gradient_flow_stats.json` — 28 层 x 2 模型的完整统计
- `gradient_flow_comparison.{pdf,png}` — per-layer gradient norm bar chart
- `gradient_stability_comparison.{pdf,png}` — cross-layer CV 线图
- 脚本：`/root/recovery_aware_struct_prune/src/gradient_flow_analysis.py`

---
