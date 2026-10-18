# analysis kv separation

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kv_separation_20260514T083637_result.json`
- **Structured JSON:** [`a89a9c4374e94892ce22.json`](../../sessions/a8/a89a9c4374e94892ce22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## kv_separation 实验分析 — 结论：**NEGATIVE**

### PPL 对比（Qwen2.5-7B, budget=25%）

| Method | PPL | Memory | Δ vs Baseline |
|---|---|---|---|
| Baseline (bf16) | 9.8106 | 100% | — |
| Uniform 4-bit | 15.4454 | 25.0% | +5.635 |
| **Joint K=V MCKP** | **10.9131** | **25.0%** | **+1.103** |
| K/V Separated MCKP | 11.2162 | 24.9% | +1.406 |

**K/V Sep vs Joint: +0.303 PPL（更差）**

### Bit-width 分布

| | 2-bit | 4-bit | 8-bit | 16-bit |
|---|---|---|---|---|
| **Sep-K** | 16 | 91 | 4 | 1 |
| **Sep-V** | 0 | **112** | 0 | 0 |
| **Joint K=V** | 8 | 100 | 4 | 0 |

21/112 heads 出现 K≠V 不对称，全部是 K 低于 V（K=2bit/8bit/16bit, V=4bit）。

### 原因分析

1. **V 量化几乎无损**：所有 112 个 V head 的 distortion profile 在各 bit-width 下都接近 0，MCKP 一律分配 4-bit。V 方向没有可利用的优化空间。
2. **分离后 2-bit 配额翻倍反而有害**：separated 允许 max_2bit=16（joint 只有 8），solver 将 16 个 K head 降到 2-bit，但省出的 budget 给 V 没有收益（V 已经在 4-bit 饱和）。
3. **K 更敏感但被过度压缩**：Layer 0 的 K 需要 8-16 bit（RoPE 首层敏感），但中间层大量 K 被推到 2-bit 来腾空间，导致整体 PPL 上升。

### 结论

K/V 分离在当前 MCKP 框架下没有改善。根本原因是 V quantization distortion 极低（per-token 量化天然更鲁棒），自由度翻倍后 solver 只会更激进地压缩 K，适得其反。Joint K=V 优化仍是更优方案。

---
