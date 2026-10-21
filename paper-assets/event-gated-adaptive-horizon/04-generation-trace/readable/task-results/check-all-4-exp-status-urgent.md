# check all 4 exp status urgent

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_4_exp_status_urgent_20260522T121853_result.json`
- **Structured JSON:** [`e7260e584fde0042f486.json`](../../sessions/e7/e7260e584fde0042f486.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| exp_id | server | GPU | PID | alive? | step | target | eval_return | ve_ratio | 备注 |
|--------|--------|-----|-----|--------|------|--------|-------------|----------|------|
| exp_044_gradient_stop_walker | bjb1-45299 | cuda:1 (2744 MiB) | 68371→68376 | **RUNNING** | 105K | 210K (50%) | 87.8 | 4.45→**1.94** | 95K CIVO alert 已消退，105K alert=0，ve_ratio 下降中 |
| exp_045_treatment_extension_008d_s3 | bjb1-45299 | cuda:0 (3361 MiB) | 70945 | **RUNNING** | 196K | 300K (65%) | 699.5 (@192K) | 0.129 | 健康运行，train_return 600-740 区间稳定 |
| exp_046_frozen_dt_emb_cheetah | bjb1-40020 | cuda:0 (3025 MiB) | 281513 | **RUNNING** | 48K | 210K (23%) | 77.1 (@45K) | 0.175 | 正常早期阶段，train_return ~130-165 |
| exp_047_frozen_dt_emb_walker_s1 | bjb1-40020 | cuda:1 (3025 MiB) | 282452 | **RUNNING** | 40K | 210K (19%) | 206.6 (@35K) | 0.187 | 正常早期阶段，train_return ~125-257 |

### 关键发现

**exp_044**: 95K 处触发 CIVO alert（ve_ratio=4.45），但到 105K 已自行回落至 1.94（alert=0）。eval_return 从 44.3 恢复到 87.8，走势向好但绝对值仍偏低。继续观察 115K eval 是否持续恢复。

**exp_045**: 从上次 176K 推进到 196K，eval_return 699.5 表现优秀，ve_ratio 0.13 极低且稳定，无异常。

**exp_046/047**: 两个 frozen_dt_emb 实验刚跑 1-1.5 小时，均在早期阶段，指标正常，无异常信号。

---
