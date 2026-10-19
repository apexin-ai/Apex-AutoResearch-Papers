# code mvp A 002

**crosscoder behavioral circuit transplant** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-A-002_20260510T153450_result.json`
- **Structured JSON:** [`6593979c72d7c941bd9f.json`](../../sessions/65/6593979c72d7c941bd9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

mvp-A-002 实验完成（56 秒），结果已保存并注册。

## 结果摘要

| Gate | 结果 | 值 |
|------|------|-----|
| Gate 1 | **FAIL** | L0=515.1（目标 20-100），recon 降 98.9% |
| Gate 2 | PASS | 130 个 exclusive features |
| Gate 3 (Rank-1) | **FAIL** | movement=0.00%（encoder 对 donor-exclusive feature 投影近零） |
| Gate 4 (Rank-1) | PASS | ppl ratio=1.001 |
| Gate 5 (Rank-1) | **FAIL** | DA improvement=-0.01% |
| Part 2 Bias | **ALL FAIL** | 所有 feature×alpha 组合 DA improvement 为负 |

**H1 NOT VERIFIED, H3 NOT VERIFIED**

## 核心问题

**L1 正则化用了 `.mean()` 而非 `.sum()`**，导致 per-feature 惩罚极弱（有效 L1≈0.1/(batch×n_features)≈1e-7）。即使 L1_λ 从 5e-2 提升到 1e-1，L0 只从 582→515，远未达到目标 20-100。要实现真正的高稀疏度，需要：
1. 改用 sum-based L1（`fd.abs().sum(-1).mean()`）
2. 或采用 TopK 激活替代 ReLU+L1

---
