# analysis cheetah nve consistency

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cheetah-nve-consistency_20260520T004048_result.json`
- **Structured JSON:** [`88b54050b1a15205f6db.json`](../../sessions/88/88b54050b1a15205f6db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：decisions.yaml 记录 `baseline avg V/E@65K=0.385`，用的是 023a/023b 2-seed baseline，不是 5-seed mean。验证: 3.1829 / 0.385 = 8.27×。

现在汇总结果。

## #1 Cheetah NVE Consistency

**exp_010b (seed1)** peak ve_ratio = **3.1829** @ step 65K (value_mean=72.15, eval_return=22.67)

| baseline source | baseline_ve@65K | NVE | match? |
|---|---|---|---|
| 023a/023b 2-seed (decisions.yaml 记录) | 0.385 | **8.27×** | 论文值 |
| 5-seed mean CSV (interpolated) | 0.378 | 8.42× | +1.8% 偏差 |

**结论**: 8.27× 是 **normalized**（非 raw）。公式 = raw_ve_ratio / baseline_ve_ratio = 3.1829 / 0.385 = 8.27×。使用的 baseline 是 023a/023b 两个 Cheetah baseline seed 在 step 65K 的平均 VE ratio。

**exp_010b_s0** 数据有问题：peak ve_ratio = 70.64 @ step 105K，eval_return 已崩溃到 0.83，NVE 因分母极小而爆炸，不具参考意义。

对比表：

```
experiment   | peak_step | raw_ve | bl_ve@step | NVE      | 论文值  | 备注
-------------|-----------|--------|------------|----------|---------|---
010b seed1   | 65K       | 3.18   | 0.385      | 8.27×    | 8.27×   | ✓ 023a/023b baseline
010b seed0   | 105K      | 70.64  | ~0.584     | ~120.9×  | N/A     | eval崩溃致分母极小
026_s0       | 65K       | 8.56   | 0.3918     | 21.85×   | N/A     | 进行中
026_s1       | 65K       | 10.84  | 0.3918     | 27.67×   | N/A     | 进行中
```

**注意**: 如果后续统一用 5-seed mean baseline 重算 NVE，010b 的值会从 8.27× 变为 8.42×（+1.8%）。需要确认论文最终用哪套 baseline。

---

## #2 Progress Snapshot

| 实验 | 当前 step | 目标 | 进度 |
|---|---|---|---|
| exp_025_s1 (Walker) | 176K | 210K | 83.8% |
| exp_025_s2 (Walker) | 175K | 210K | 83.3% |
| exp_025_s3 (Walker) | 216K | 210K | **完成** |
| exp_025_s4 (Walker) | 180K | 210K | 85.7% |
| exp_026_s0 (Cheetah) | 96K | 105K | 91.4% |
| exp_026_s1 (Cheetah) | 96K | 105K | 91.4% |

exp_025_s3 已超过目标步数。exp_026 两个 seed 还差 ~9K steps，预计很快完成。exp_025 剩余三个 seed 还需 30-35K steps。

---
