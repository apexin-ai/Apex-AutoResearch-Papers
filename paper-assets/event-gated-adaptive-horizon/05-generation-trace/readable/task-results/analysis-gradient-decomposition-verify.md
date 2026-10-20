# analysis gradient decomposition verify

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient-decomposition-verify_20260517T165831_result.json`
- **Structured JSON:** [`50a1a8c7257c85caf343.json`](../../sessions/50/50a1a8c7257c85caf343.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 独立验证结果

### dt_emb.weight 梯度分解 (008d checkpoint @55K)

**正确配置** (gate_fixed_dt=2, gate_subsample_max_dt=2)：

| Component | L2 norm | % | std |
|-----------|---------|---|-----|
| obs | 0.0527 | **15.84%** | 0.0169 |
| reward | 0.1762 | **53.01%** | 0.0678 |
| kl | 0.1036 | **31.15%** | 0.0287 |
| cont | ~0 | 0% | ~0 |

**错误配置** (gate_fixed_dt=0, gate_subsample_max_dt=8)：

| Component | L2 norm | % |
|-----------|---------|---|
| obs | 0.5751 | 25.79% |
| reward | 0.4910 | 22.02% |
| kl | 1.1640 | 52.19% |

### 对比判定

| 数据源 | obs% | reward% | kl% | 状态 |
|--------|------|---------|-----|------|
| **Paper Table 8** | 16.3 | 49.0 | 34.7 | **正确** |
| **独立验证 (本次)** | 15.84 | 53.01 | 31.15 | 一致（20 vs 50 batch 差异） |
| **D061** | 93 | 0 | 7 | **错误，不可复现** |

### 关键发现

1. **Paper Table 8 数据正确** — 独立验证高度一致，reward 梯度主导 (~50-53%)，其次 KL (~31-35%)，obs 最小 (~16%)
2. **D061 数据 (reward=0%, obs=93%, KL=7%) 完全错误** — 没有任何配置或方法能复现，与所有实际测量相差 >10 倍
3. **配置极度敏感** — 正确配置 (fixed_dt=2) 得到 reward 主导；错误配置 (fixed_dt=0) 得到 KL 主导；总梯度范数差 ~7 倍
4. 服务器上找到 3 个脚本版本：`compute_gradient_decomposition.py`、`grad_decomp_008d.py`（均用错误配置）、`grad_decomp_008d_corrected.py`（正确配置，其结果即 Table 8 来源）

---
