# analysis exp qwen25 72b fewshot

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_qwen25_72b_fewshot_20260520T004942_result.json`
- **Structured JSON:** [`3b6a8d69868223c3fe91.json`](../../sessions/3b/3b6a8d69868223c3fe91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验分析完成。完整结果：

## ZS vs FS 对比表（Qwen2.5-72B, N=8）

| Dataset  | Regime | Degen% | LP ρ   | SJ ρ  | VC ρ  | Greedy F1 | Oracle F1 | LP-wt Δ (pp) | p       |
|----------|--------|--------|--------|-------|-------|-----------|-----------|-------------|---------|
| SciERC   | ZS     | 21.0%  | 0.081  | 0.217 | 0.277 | 0.399     | 0.549     | **+1.53**   | **0.008** |
| SciERC   | FS     | 16.6%  | 0.060  | 0.293 | 0.258 | 0.461     | 0.604     | -0.08       | 0.544   |
| CoNLL    | ZS     | 67.7%  | -0.002 | 0.304 | 0.297 | 0.712     | 0.765     | -0.37       | —       |
| CoNLL    | FS     | 70.0%  | 0.106  | 0.442 | 0.426 | 0.745     | 0.796     | +0.03       | 0.417   |
| FewNERD  | ZS     | 46.2%  | 0.119  | 0.345 | 0.416 | 0.628     | 0.707     | -0.20       | —       |
| **FewNERD** | **FS** | **45.2%** | **0.161** | 0.345 | 0.410 | 0.619 | 0.702 | **+0.02** | **0.401** |

## 关键发现

**FewNERD FS construction 无效**：Δ=+0.02pp, p=0.401, Cohen's d=0.001, 84.3% tied instances。

**Dual-gating 不成立**：FewNERD FS 拥有全局最高 LP ρ (0.161) + 中等 degen (45.2%)，两个 gate 都通过，但 construction 仍然 flat。6 个条件中仅 SciERC ZS 一个显著。

**根因**：LP 信号量级太弱（ρ_max=0.161），无法在实例级别可靠区分样本质量。Dual-gating 是必要条件但非充分条件。

Registry 已更新为 DONE/negative，memory.md 和 artifact 已保存。

---
