# analysis exp003 bootstrap review

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp003_bootstrap_review_20260516T032051_result.json`
- **Structured JSON:** [`e83d9651a247b5c4d35a.json`](../../sessions/e8/e83d9651a247b5c4d35a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The artifacts copy is an older draft version — the authoritative copy is `docs/paper/`, which is what I edited.

## 结果

### 已完成的修改

**1. `docs/paper/experiments_c1.tex` 第65行** — 添加了 1v2 bootstrap CI 下界信息：
- 新增 "bootstrap CI lower bounds ≥ 0.677, all > θ"，确认4种解码策略的 1v2 CI 下界均远超 θ=0.60

**2. `docs/paper/appendix.tex` Table S2** — 完整添加了 bootstrap CIs：
- 更新 caption 注明 bootstrap 95% CIs（10,000 resamples）
- 所有5个 depth pair 行均添加了 CI（格式与 Table S8 一致）
- 脚注 † 标注 nucleus p=0.9 的 2v3 CI upper=0.601 marginally exceeds θ
- 脚注 ‡ 标注 nucleus p=0.9 的 4v5 permutation p=0.12（不显著）

### 数字一致性验证

| 检查项 | 论文值 | 原始数据 | 状态 |
|--------|--------|----------|------|
| nuc09 2v3 CI [0.582, 0.601] (主文第66行) | [0.582, 0.601] | [0.5824, 0.6010] | ✓ |
| greedy 1v2 CI | [.680, .698] | [0.6802, 0.6982] | ✓ |
| T=1.2 1v2 CI | [.695, .713] | [0.6945, 0.7126] | ✓ |
| "3/4 decoding variants below θ" | 3/4 | greedy/T07/T12 below, nuc09 above | ✓ |

### Appendix per-pair CI 表格覆盖
- Table S8: 4 model-mode configs 完整 per-pair CI（已有）
- Table S2: 4 decoding configs 完整 per-pair CI（刚添加）

---
