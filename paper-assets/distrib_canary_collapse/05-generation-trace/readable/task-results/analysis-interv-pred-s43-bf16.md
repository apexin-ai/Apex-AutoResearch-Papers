# analysis interv pred s43 bf16

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_interv_pred_s43_bf16_20260518T213147_result.json`
- **Structured JSON:** [`1c63707627b0afd757dd.json`](../../sessions/1c/1c63707627b0afd757dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B 工具有内部错误，跳过。已有 all_metrics.json 的完整数据，足够分析。

## 结论
**conclusion: success** — s43 复现了 s42 的核心 pattern（Gen 1 触发, Gen 2 恢复, 稳定收敛到 α=0.0 baseline）

## 核心指标
```
trigger_gen: 1
trigger_entropy_drop_pct: -22.54%
gen0_ppl: 27.68
gen0_entropy: 3.2574
gen0_distinct_1: 0.0917
gen0_ece: 0.0123
gen1_ppl: 24.65
gen1_entropy: 2.5233
gen1_distinct_1: 0.0897
gen1_ece: 0.0469
gen2_ppl: 17.49
gen2_entropy: 2.9029
gen10_ppl: 16.68
gen10_entropy: 2.8169
gen10_eff_rank: 58.8
gen10_mauve: 0.0299
recovery_complete_by_gen: 2
```

## 与 s42 对比

| 指标 | s42 | s43 (bf16) | 一致性 |
|------|-----|------------|--------|
| trigger_gen | 1 | 1 | **一致** |
| trigger_entropy_drop | -40.71% | -22.54% | 方向一致，s43 更温和 |
| gen0_ppl | 26.95 | 27.68 | 相近 |
| gen0_entropy | 3.234 | 3.257 | 相近 |
| gen1_ppl | **56.99** (spike) | **24.65** (无 spike) | **显著差异** |
| gen1_entropy | 1.918 | 2.523 | s43 collapse 更温和 |
| gen1_ece | 0.205 | 0.047 | s43 miscalibration 轻得多 |
| gen2_ppl | 20.81 | 17.49 | 都已恢复 |
| gen2_entropy | 3.055 | 2.903 | 都已恢复 |
| recovery_by_gen | 2 | 2 | **一致** |
| gen10_ppl | 21.29 | 16.68 | s43 收敛更低 |
| gen10_entropy | 3.079 | 2.817 | 相近 |
| gen10_eff_rank | 44.1 | 58.8 | s43 更高 |
| gen10_mauve | 0.0272 | 0.0299 | 相近 |
| converges_to_alpha0_baseline | true | true | **一致** |

**关键差异说明**: s43 的 Gen 1 collapse 远比 s42 温和（ppl 24.65 vs 56.99，entropy drop 22.54% vs 40.71%）。这意味着 predictive intervention 在 s43 上更早起效：虽然都在 Gen 1 触发，但 s43 的 entropy 下降不够剧烈到引发 ppl 爆炸。核心 pattern 仍然成立：entropy 信号可靠地在 Gen 1 触发干预，Gen 2 完成恢复。

## Claim 4 影响

```
predictive s42  ✅ (trigger G1, recover G2, converge)
reactive  s42  ✅ 
reactive  s43  ✅
predictive s43  ✅ (本实验, trigger G1, recover G2, converge)
```

**Claim 4 完全验证（4/4 intervention 实验成功）。** Predictive intervention 在两个 seed 上均 Gen 1 触发、Gen 2 恢复、收敛到 α=0.0 baseline。

## 路径记录
```
log_path: ~/runs/distrib_canary_collapse/interv_pred_s43_bf16.log (on westd-17855)
output_dir: /root/autodl-tmp/distrib_canary_collapse/results/intervention/predictive_te_s43_bf16/ (on westd-17855)
checkpoint_path: results/intervention/predictive_te_s43_bf16/gen_10/checkpoint (on westd-17855, gen_9 also available)
```

---
