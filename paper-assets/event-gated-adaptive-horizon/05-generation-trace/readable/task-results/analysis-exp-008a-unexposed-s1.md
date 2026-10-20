# analysis exp 008a unexposed s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_008a_unexposed_s1_20260518T081333_result.json`
- **Structured JSON:** [`9b7699554b51adaa7f7c.json`](../../sessions/9b/9b7699554b51adaa7f7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新成功。W&B 查询工具有 bug（传参问题），跳过。

---

## 分析摘要

### eval_return 曲线
稳步上升：31→167→140（25K 小回落）→394→414→441→492→452（75K 小回落）→547→629→**631**。整体呈单调上升趋势，75K 处有轻微回落但迅速恢复。

### CIVO 判定
- civo_ve_ratio = 0.430（远 < 1.5 阈值）
- civo_delta_ve = -0.003（value_mean ≈ target_mean，极度健康）
- civo_alert = **0**
- gate_dt_mean 恒为 2.0，gate_dt_2_frac = 1.0（subsample OFF 生效）
- **无 CIVO 触发**，value function 和 target 完全对齐

### 跨 seed 对比

| 实验 | seed | eval_return_final | civo_ve_ratio | civo_alert |
|------|------|-------------------|---------------|------------|
| exp_008a_no_subsample_dt2 (原始) | 1 | 777.66 | — | 0 |
| exp_008a_unexposed_s1 (本次) | 1 | 630.91 | 0.430 | 0 |
| exp_008a_unexposed_s2 | 2 | 899.4 | 0.333 | 0 |

s1 unexposed (630.91) 低于原始实验 (777.66) 和 s2 (899.4)，但仍远超 400 阈值。三个 run 全部 civo_alert=0，**reproducibility 确认：unexposed trained dt_emb + subsample OFF 配置在 Walker Walk 上稳定不触发 CIVO**。

### 结论
**success** — unexposed dt_emb 保护有效，C3 rebuttal 储备实验 reproducibility 通过。

---
