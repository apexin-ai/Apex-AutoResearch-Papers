# code hidden state divergence

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hidden-state-divergence_20260519T201201_result.json`
- **Structured JSON:** [`91dc520e52f02980102e.json`](../../sessions/91/91dc520e52f02980102e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成，24.5s，GPU峰值 14.4 GB。结果：

### Layer-18 Hidden State Divergence (20 tasks, 100 pairs)

| 指标 | Scope | Mean | Std | Min | Max |
|------|-------|------|-----|-----|-----|
| **Cosine distance** | all tokens | 0.0284 | 0.0100 | 0.0079 | 0.0514 |
| **Cosine distance** | image tokens | 0.000023 | 0.000009 | 0.000000 | 0.000029 |
| **Normalized L2** | all tokens | 1.886 | 0.790 | 0.142 | 2.434 |
| **Normalized L2** | image tokens | 0.00596 | 0.00232 | 0.000 | 0.00723 |
| **Per-position variance** | image tokens | 2.26e-05 | 2.91e-06 | 1.61e-05 | 2.74e-05 |

**按 Tier 分组** (image token cosine distance):
- Tier-1 (trivial): mean=0.000025, n=38
- Tier-2 (moderate): mean=0.000025, n=17
- Tier-3 (deep): mean=0.000021, n=45

### 判定

**Image token hidden states 几乎完全不变** — cosine distance 仅 2.3e-05 (sim > 0.99997)，远低于信号存在阈值 0.05。各 tier 之间也无差异。

**All-token hidden states 有明显 divergence** — cosine distance 0.028 (sim ≈ 0.972)，说明 text token 位置的 hidden states 确实因指令变化而不同，但这个差异没有传播到 image token 位置。L_consist 的梯度通过 image token hidden states → decoder → heatmap 传播，而 image token 在 layer-18 已经对语义等价的指令完全稳定。

结果文件: `/root/afford_invar/results/phase0/hidden_state_divergence.json`

---
