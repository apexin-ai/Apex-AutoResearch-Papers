# code exp65 svd ablation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp65_svd_ablation_20260522T233142_result.json`
- **Structured JSON:** [`cfb7dcb360ebc24abb1d.json`](../../sessions/cf/cfb7dcb360ebc24abb1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果如下：

## 结果表格（mean±std，3 seeds）

| Condition | DD F1 | FITD F1 | AA F1 |
|---|---|---|---|
| Original 768-dim | **1.0000±0.0000** | **1.0000±0.0000** | **0.9936±0.0045** |
| Remove top-3 SVD | 0.8308±0.0642 | 1.0000±0.0000 | 0.9380±0.0112 |
| Remove random-3 | 1.0000±0.0000 | 1.0000±0.0000 | 0.9936±0.0045 |

SVD info: top-3 方向解释了训练 turn embeddings 89.81% 的方差。

## 分析

1. **DD**: 移除 top-3 SVD 导致 F1 从 1.0 暴跌至 0.83（**Δ=-0.17**），而移除 random-3 零影响。**强因果证据**——3/768 维度的移除造成 17 点下降。

2. **AA**: 移除 top-3 SVD 导致 F1 从 0.994 降至 0.938（**Δ=-0.056**），random-3 零影响。效果显著但比 DD 弱，说明 AA 的判别信息在更多维度上有冗余。

3. **FITD**: 两种 ablation 均无影响（F1=1.0）。FITD 的判别信息更分散，不集中在 top-3 方向。

4. **因果证据成立**：random-3 对照组完美复现 original 结果（数值完全一致），排除了"移除任意 3 个维度都会降低性能"的混淆解释。

5. **与 exp54 的互补**：exp54 证明 3 维足够（sufficiency），exp65 证明 3 维必要（necessity，至少对 DD）。Top-3 SVD 方向对 DD 检测既充分又必要，对 AA 充分但部分冗余，对 FITD 充分但非必要。

---
