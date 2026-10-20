# diagnose clustered bootstrap reanalysis v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_clustered_bootstrap_reanalysis_v1_20260523T004605_result.json`
- **Structured JSON:** [`7aa0175d0a3ee1bd2d72.json`](../../sessions/7a/7aa0175d0a3ee1bd2d72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据到手。整理结果。

# Bootstrap Reanalysis Status

## Process Status
- **cuda:0**: COMPLETE (finished 08:26:35 CST)
- **cuda:1**: RUNNING — 当前: `tracvla_object untrained` bootstrap 阶段 (100 workers × 1000 iter, 自 08:44:41 CST 起)

cuda:1 脚本剩余队列: `tracvla_long trained` → `tracvla_long untrained`。预估剩余 ~1.5–2h。

## Completed Results (17/20)

### OpenVLA (exit layer = L31)

| Suite | Cond | Peak R² | @Layer | Exit R² | Δ | CI95(Δ) | Sig? |
|-------|------|---------|--------|---------|------|---------|------|
| goal | trained | 0.4164 | L1 | 0.2826 | 0.1339 | [0.0000, 0.0742] | **No** |
| goal | untrained | 0.4026 | L10 | 0.3039 | 0.0988 | [0.0000, 0.0484] | **No** |
| spatial | trained | 0.5452 | L24 | 0.4963 | 0.0489 | [0.0000, 0.0444] | **No** |
| spatial | untrained | 0.5339 | L4 | 0.5180 | 0.0160 | [0.0000, 0.0362] | **No** |
| object | trained | 0.5752 | L21 | 0.5509 | 0.0242 | [0.0000, 0.0269] | **No** |
| object | untrained | 0.5932 | L14 | 0.5407 | 0.0525 | [0.0000, 0.0575] | **No** |
| long | trained | 0.5121 | L25 | 0.4691 | 0.0430 | [0.0000, 0.0591] | **No** |
| long | untrained | 0.5341 | L24 | 0.5080 | 0.0261 | [0.0000, 0.0692] | **No** |

### TracVLA (exit layer = L31)

| Suite | Cond | Peak R² | @Layer | Exit R² | Δ | CI95(Δ) | Sig? |
|-------|------|---------|--------|---------|------|---------|------|
| goal | trained | 0.5399 | L13 | 0.2065 | 0.3334 | [0.0924, 0.3545] | **Yes** |
| goal | untrained | 0.5048 | L11 | 0.4403 | 0.0645 | [0.0000, 0.0776] | **No** |
| spatial | trained | 0.6871 | L13 | 0.5315 | 0.1557 | [0.0487, 0.1619] | **Yes** |
| spatial | untrained | 0.6120 | L4 | 0.5643 | 0.0477 | [0.0000, 0.0464] | **No** |
| object | trained | 0.6315 | L13 | 0.2692 | 0.3623 | [0.0735, 0.3719] | **Yes** |

### NoRA (exit layer = L35)

| Suite | Cond | Peak R² | @Layer | Exit R² | Δ | CI95(Δ) | Sig? |
|-------|------|---------|--------|---------|------|---------|------|
| goal | trained | 0.4489 | L8 | -0.0062 | 0.4551 | [1.0253, 1.8867] | **Yes** |
| goal | untrained | 0.4203 | L5 | 0.3397 | 0.0806 | [0.0046, 0.1076] | **Yes** |
| spatial | trained | 0.5763 | L20 | 0.2683 | 0.3080 | [0.1097, 0.4715] | **Yes** |
| spatial | untrained | 0.5125 | L4 | 0.4240 | 0.0885 | [0.0002, 0.0873] | **Yes** |

## Missing Conditions (3)
- `tracvla_object/untrained` — **正在运行**
- `tracvla_long/trained` — 排队中
- `tracvla_long/untrained` — 排队中

## Summary

17/20 conditions 完成，3 个剩余（均为 cuda:1 队列中的 tracvla）。

显著性分布:
- **OpenVLA**: 0/8 significant — 所有 CI 下界为 0.0000，delta 均不显著
- **TracVLA**: 3/5 significant (全部是 trained) — trained 的 goal/spatial/object 均显著，untrained 不显著
- **NoRA**: 4/4 significant — trained 和 untrained 均显著，但 trained Δ 远大于 untrained

关键观察: OpenVLA 的 CI 下界全部精确为 0.0000，这可能表明 bootstrap 实现中对 CI 做了 `max(0, ...)` clamp，值得检查是否属于 artifact。

---
