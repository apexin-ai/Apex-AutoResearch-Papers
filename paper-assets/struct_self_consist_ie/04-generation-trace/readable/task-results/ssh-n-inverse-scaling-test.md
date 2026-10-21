# ssh n inverse scaling test

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n-inverse-scaling-test_20260520T105455_result.json`
- **Structured JSON:** [`ab0311e713969af57297.json`](../../sessions/ab/ab0311e713969af57297.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

**Inverse scaling 确实存在，且广泛、显著。** 这是 structured self-consistency 中首次系统报告的 inverse scaling 现象。

### 核心数据
- 6 configs (2 models × 3 datasets), 6 methods, N∈{2,4,6,8,16}
- **58 个 inverse scaling transitions, 其中 40 个统计显著** (paired bootstrap, 95% CI 完全 < 0)

### 按 method 分布

| Method | Inverse cases | Significant |
|--------|:---:|:---:|
| majority_vote (θ=0.5) | 1 | **0** |
| lp_weighted (θ=2/N) | 12 | 10 |
| vc_weighted (θ=2/N) | 8 | 5 |
| sj_weighted (θ=2/N) | 9 | 5 |
| theta2n (θ=2/N) | **16** | **11** |
| uniform (θ=0.25) | 12 | 9 |

### 关键机制

1. **theta=2/N 是祸首**: 随 N 增大，θ 变得过于宽松 (N=16 时 θ=0.125，任何出现在 2/16 个 sample 中的 entity 都被纳入)，导致大量噪声 entity 进入 constructed set，precision 崩塌。CoNLL Qwen: theta2n 从 N=8→16 下降 **3.45pp** (CI=[-3.87,-3.04])。

2. **majority_vote (θ=0.5) 免疫**: 固定比例阈值保证 entity 必须在 >50% sample 中出现，自然过滤噪声。全 6 configs 中仅 1 个 borderline case (not significant)。

3. **Weighted methods 减轻但不消除**: LP/VC/SJ weighting 部分补偿了 threshold 问题，但不足以阻止 inverse scaling。

### 产出文件 (artifacts/n_inverse_scaling/)
- `f1_by_n.json` — 完整 F1(N) 数据表
- `inverse_scaling_summary.json` — 每个 case 的判定 + bootstrap CI + p-value
- `analysis.md` — 结论与机制分析
- `f1_vs_n_all_configs.png` — 6 config 总览图
- `inverse_scaling_detail.png` — 逐 config 详细图

---
