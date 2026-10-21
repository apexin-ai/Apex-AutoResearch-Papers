# code plan 030 rssm analysis

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_030_rssm_analysis_20260526T024153_result.json`
- **Structured JSON:** [`2e272d423a9dcd1379c3.json`](../../sessions/2e/2e272d423a9dcd1379c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

bjb1-45299 SSH 连接失败（端口不通）。AutoDL 实例可能已重启，端口已变。

但从已读取的服务器数据中，**已有两份覆盖 Walker RSSM fidelity 的分析结果**：

## 已有数据汇总

### analysis_rssm_walker_fidelity.json（Walker 专项）

| Model | Experiment | dt1 obs_mse | dt2 obs_mse | dt2/dt1 ratio | dt1 reward_mae | dt2 reward_mae | reward ratio |
|-------|-----------|-------------|-------------|---------------|----------------|----------------|--------------|
| baseline_walker | exp_009d_baseline_walker_s1 | 16.07 | 23.49 | **1.46x** | 0.0453 | 0.0587 | 1.30x |
| collapsed_civo_walker | exp_008d_civo_trigger_s4 | 9.96 | 13.20 | **1.33x** | 0.0392 | 0.1219 | **3.11x** |
| healthy_frozen_walker | exp_057_frozen_dt_emb_walker_s2 | 11.14 | 14.95 | **1.34x** | 0.0678 | 0.1330 | 1.96x |

### analysis_rssm_prediction_quality.json（原始分析）

| Model | dt2/dt1 obs_mse ratio | dt2/dt1 reward ratio |
|-------|----------------------|---------------------|
| baseline_s1 | 2.04x | 1.56x |
| exp_008d (dt_emb) | 1.30x | 1.04x |
| exp_008f (no dt_emb) | 2.75x | 1.01x |

## 关键发现

1. **RSSM obs prediction 在 dt=2 上确实更差**（所有模型 dt2/dt1 ratio > 1.3x），但 dt_emb 模型（1.30-1.33x）比 baseline（1.46-2.04x）和 no_emb（2.75x）的 fidelity gap 更小。

2. **collapsed CIVO 模型的 reward prediction gap 异常大**：dt2/dt1 reward_mae ratio = **3.11x**，远高于 frozen（1.96x）和 baseline（1.30x）。这表明 CIVO collapse 与 **reward prediction 在 dt>1 上的严重退化** 强相关。

3. **obs fidelity gap 不是 CIVO collapse 的主因**：collapsed 和 healthy 的 obs_mse ratio 几乎相同（1.33x vs 1.34x），说明 world model 的 observation prediction 质量类似，区别在 reward head。

## 待完成

脚本已写好但未能上传执行（服务器断连）。需要：
- 去 AutoDL 控制台查看 bjb1-45299 的新 SSH 端口并更新 `~/.ssh/config`
- 然后重新运行分析，覆盖 exp_009e_008d_walker_s1 和 exp_084_frozen_dt_emb_walker_s0 这两个具体 checkpoint

现有数据已经提供了强有力的分析基础——CIVO 的 root cause 更可能与 **reward prediction 在 dt>1 的退化** 相关，而非 observation reconstruction 质量。

---
