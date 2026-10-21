# analysis cross family pooled irt llama v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_family_pooled_irt_llama_v2_20260517T030258_result.json`
- **Structured JSON:** [`f4c1fe01b4b322cab444.json`](../../sessions/f4/f4c1fe01b4b322cab444.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### Step 1: Llama Signals 完整性 ✓

所有 4 个 dosage × 3 benchmarks × 3 signals + merged 文件齐全，位于 `/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d{000,005,025,100}_s42/`。

已知问题：
- **Llama d000 MMLU**: aligned eval 中无 MMLU 数据（raw eval 有 45.4% accuracy 但 item_responses 未对齐）
- **Llama d100 MMLU**: 退化（全部预测 A）

### Step 2-3: Cross-Family Pooled IRT v4 结果

| Benchmark | N | γ | 95% CI | Significant? | PPP |
|-----------|---|---|--------|-------------|-----|
| MMLU | 18 | 0.41 | [-0.60, 1.41] | **NO** | 0.596 |
| GSM8K | 28 | -0.11 | [-0.52, 0.28] | **NO** | 0.832 |
| ARC | 20 | 0.00 | [-0.57, 0.60] | **NO** | 0.449 |

### 对比 Qwen-only (N=24)

| | Qwen-only γ | Cross-family γ | 变化 |
|---|---|---|---|
| MMLU | 0.66 | 0.41 | ↓ 信号减弱 |
| GSM8K | 0.06 | -0.11 | → 翻号 |
| ARC | **0.73 [0.02, 1.44] 显著** | 0.00 | ↓↓ **失去显著性** |

### 核心结论

**Gamma 在 cross-family pooled 中不显著** (p>0.05 for all benchmarks)。添加 Llama 不但未增强信号，反而稀释了 Qwen-only 中 ARC 的边际显著性。

N 达标情况：GSM8K N=28 ✓, ARC N=20 ✓, MMLU N=18 (因排除退化模型略低于 20)。

**解读**：Llama 与 Qwen 的 contamination-exposure 关系可能根本不同，单一 pooled gamma 不适合跨模型族。建议方向：family-stratified IRT（每个模型族单独估计 gamma）。

---
