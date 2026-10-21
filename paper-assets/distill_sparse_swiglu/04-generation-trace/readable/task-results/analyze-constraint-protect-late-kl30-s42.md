# analyze constraint protect late kl30 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_constraint_protect_late_kl30_s42_20260522T142651_result.json`
- **Structured JSON:** [`52b313253f2bfdb5f6d5.json`](../../sessions/52/52b313253f2bfdb5f6d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：`constraint_protect_late_kl30_s42`

### 评估指标

| Metric | Protect-Late | E2E KL (baseline) | Per-layer KL (baseline) | Δ vs E2E | Δ vs Per-layer |
|--------|-------------|-------------------|------------------------|----------|----------------|
| **PPL** | **9.26** | 8.81 | 9.05 | +0.45 ↑ | +0.21 ↑ |
| **ARC-c (acc_norm)** | **42.41** | 43.7 | 39.9 | -1.29 | +2.51 |
| **ARC-c (acc)** | **37.88** | — | — | — | — |
| **MMLU** | **40.66** | 40.7 | 38.6 | -0.04 | +2.06 |
| **GSM8K** | **6.52** | 7.5 | 5.8 | -0.98 | +0.72 |

### 每层 Sparsity 分布

**Uncapped（原始 predictor 输出）→ Capped（约束后）：**

| Layer | Uncapped | Constrained | Note |
|-------|----------|-------------|------|
| 0 | 0.276 | 0.301 | |
| 1 | 0.182 | 0.219 | 最低 |
| 2 | 0.258 | 0.293 | |
| 3 | 0.235 | 0.277 | |
| 4 | 0.227 | 0.270 | |
| 5 | 0.266 | 0.297 | |
| 6 | 0.276 | 0.305 | |
| 7 | 0.277 | 0.309 | |
| 8 | 0.267 | 0.309 | |
| 9 | 0.288 | 0.320 | |
| 10 | 0.270 | 0.312 | |
| 11 | 0.286 | 0.320 | |
| 12 | 0.289 | 0.320 | |
| 13 | 0.305 | 0.328 | |
| 14 | 0.287 | 0.316 | |
| 15 | 0.246 | 0.270 | |
| 16 | 0.216 | 0.250 | |
| 17 | 0.221 | 0.246 | |
| 18 | 0.208 | 0.238 | |
| 19 | 0.244 | 0.277 | |
| 20 | 0.268 | 0.305 | |
| 21 | 0.279 | 0.312 | |
| **22** | **0.309** | **0.297** | capped ↓ |
| **23** | **0.326** | **0.293** | capped ↓ |
| **24** | **0.358** | **0.293** | capped ↓ |
| **25** | **0.387** | **0.297** | capped ↓ |
| **26** | **0.439** | **0.301** | capped ↓ |
| **27** | **0.490** | **0.297** | capped ↓ |
| **28** | **0.524** | **0.297** | capped ↓ |
| 29 | 0.485 | **0.502** | 未被保护，吸收了溢出 ↑ |
| 30 | 0.316 | 0.328 | |
| 31 | 0.289 | 0.301 | |

- **Model-level sparsity**: 0.300（精确命中目标）
- **Capped 释放的 zeros**: 29,763 / 137,626 total（21.6% 的预算被重新分配）

### 异常检查

- `torch_dtype` deprecation warning — 无害
- `fatal: not a git repository` — lm-eval 内部 git 调用，无害
- **无实质性 error/warning**，EXIT_CODE=0

### Conclusion: **Negative**

保护晚期层（L22-L28 cap 0.30）没有带来质量提升，反而略有下降：

1. **PPL 恶化**：9.26 vs 9.05（per-layer baseline），+0.21。比 E2E baseline 8.81 更差 +0.45。
2. **下游任务**：ARC-c 和 MMLU 介于两个 baseline 之间（接近 per-layer），GSM8K 也处于中间位置。没有一个指标超过 E2E baseline。
3. **水床效应（waterbed effect）**：从 L22-L28 释放的 21.6% sparsity 预算被重新分配到其他层，L29 从 0.485→0.502 成为新瓶颈。早期层（L0-L14）普遍增加了 2-4 个百分点的 sparsity，抵消了保护晚期层的收益。
4. **核心问题**：约束只是把 sparsity 从一组"重要"层搬到了另一组层，总预算不变，质量没有 free lunch。

等 `constraint_remove_valley_kl30_s42` 结果出来后可做交叉对比，但 protect-late 本身不支持"晚期层保护能改善质量"的假设。

---
