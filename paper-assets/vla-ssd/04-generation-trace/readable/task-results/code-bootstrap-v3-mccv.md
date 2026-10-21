# code bootstrap v3 mccv

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap_v3_mccv_20260523T064112_result.json`
- **Structured JSON:** [`cdb07ec5ed89f76ceb67.json`](../../sessions/cd/cdb07ec5ed89f76ceb67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

## 1. v3 代码改动摘要

| 位置 | v2 | v3 |
|------|----|----|
| 全局变量 | `_MP_RESAMPLES` | `_MP_SEEDS`（per-iteration 随机种子数组） |
| `_bootstrap_single(b)` | `resampled = _MP_RESAMPLES[b]` 然后按位置切 `[:n_train]` / `[n_train:]` | `rng_b = np.random.default_rng(_MP_SEEDS[b])` → `rng_b.permutation()` 无放回切分 + `assert` 验证不重叠 |
| 种子生成 | `rng2.choice(unique_demos, size=n_total, replace=True)` ×B | `rng2.integers(0, 2**63, size=n_bootstrap)` |
| 输出目录 | `results/clustered_bootstrap/` | `results/bootstrap_v3/` |
| docstring | 标注 v3 Monte Carlo CV 修复说明 |

## 2. Dry-run 结果

- tracvla/goal/trained, n_bootstrap=10, dry_run (4 demos, 20 samples)
- Peak R²=-1.4703 @ L23, Exit R²=-2.0955 @ L31
- Delta=0.6252, CI95=[-0.2945, 1.2055]
- **无 assertion 错误**（train/test demo 完全不重叠）
- R²为负是因为 dry-run 样本极少，正常

## 3. 双卡启动确认

| 卡 | tmux session | PID | 当前任务 | 条件数 |
|----|-------------|-----|---------|-------|
| cuda:0 | `bootstrap_v3_cuda0` | 724283 | openvla/goal/trained | 12（openvla×8 + nora×4） |
| cuda:1 | `bootstrap_v3_cuda1` | 724305 | tracvla/goal/trained | 8（tracvla×8） |

## 4. 预计完成时间

v2 单条件（1000 bootstrap）约 20-30 分钟（特征提取 ~15min + bootstrap ~5-10min）。
- cuda:0（12 条件）：~5-6 小时
- cuda:1（8 条件）：~3-4 小时

---
