# ssh plan008 rsa results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan008-rsa-results_20260516T005546_result.json`
- **Structured JSON:** [`0df8ca5ecb28167e00ce.json`](../../sessions/0d/0df8ca5ecb28167e00ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## plan_008 RSA Instruction Control 结果

### 对比表（last_preaction, peak layer = L16）

| Condition | Peak RSA | Peak Layer | Δ vs normal |
|-----------|----------|------------|-------------|
| **normal** | 0.4888 | 16 | — |
| **empty** | 0.4723 | 16 | -0.0165 |
| **random_s0** | 0.4835 | 16 | -0.0053 |
| **shuffled** | 0.4832 | 16 | -0.0056 |

### 参考基线

| Source | RSA |
|--------|-----|
| SigLIP+projector | 0.6153 |
| **VLA normal** | **0.4888** |
| DINO | 0.388 |

### 结论

**success** — Instruction content 不影响 RSA。所有条件（正常/空/随机乱码/打乱词序）均在 L16 达峰，RSA 值在 ±0.017 以内。random_s0 和 shuffled 甚至比 empty 更接近 normal（Δ 仅 -0.005/-0.006 vs empty 的 -0.017）。表征-动作对齐结构对 instruction 内容完全不变。

---
