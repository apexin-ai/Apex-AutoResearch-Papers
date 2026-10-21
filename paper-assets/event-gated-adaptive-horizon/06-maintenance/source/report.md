# Handover — 2026-05-29

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
| exp_id | 假设 | 状态 | 关键指标 | W&B |
|--------|------|------|---------|-----|
| exp_walker_no_dt_emb_s0_r2 | dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 0 will NOT show CIVO (NVE<1.5), replicating 008f causal control. This confirms removing dt_embedding prevents CIVO, strengthening C2 (trained dt_emb is necessary condition). Retry of exp_walker_no_dt_emb_s0 (killed: resource reallocation). Source: D164 Walker priority. | — | — | — |

## 待处理
（无）

## 近期结论
- **exp_quadruped_baseline_s0_r2** (negative): Quadruped Walk baseline (dt=1, no gate) establishes reference performance for 12-DoF four-legged environment CIVO verification. Expect stable training without value overestimation (NVE < 2.0×). Retry of exp_quadruped_baseline_s0 (failed: EGL device 1 not available). Source: post-D171 scope expansion. ← 基于 exp_quadruped_baseline_s0
- **exp_quadruped_008d_s0** (killed): Quadruped Walk trained dt_emb + gate + subsample ON (008d config: gate_fixed_dt=2, gate_subsample_max_dt=2, H=8), seed=0 — tests whether CIVO onset generalizes to 12-DoF four-legged morphology distinct from Walker/Cheetah single-spine. Expect NVE > 2.0× if CIVO is morphology-independent. Source: post-D171 scope expansion.
- **exp_walker_no_dt_emb_s0** (killed): dt_embed_dim=0 + gate+subsample ON in Walker Walk seed 0 will NOT show CIVO (NVE<1.5), replicating 008f causal control. This confirms removing dt_embedding prevents CIVO, strengthening C2 (trained dt_emb is necessary condition). Source: D164 Walker priority, replaces killed exp_009f.

## 趋势
成功 103 / 负向 45 / 失败 22 / 共 213
NVE_105K: 0.88 ↓（近 3 次 success）
civo_alert: 0 →（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-51268: 空闲 cuda:0, cuda:1

## 告警
- 016e: 已被终止 — unknown
- exp_002_event_gated: 训练失败 — unknown
- exp_006: 已被终止 — unknown
- exp_008a: 已被终止 — unknown
- exp_008a_untrained_s1: 已被终止 — unknown
- exp_008a_untrained_s2: 已被终止 — unknown
- exp_008c: 已被终止 — unknown
- exp_008d: 已被终止 — unknown
- exp_008d_civo_trigger_s2: 已被终止 — unknown
- exp_008e_subsample_on_dt1_h15: 已被终止 — unknown
- exp_008e_subsample_on_fixed_dt1: 已被终止 — unknown
- exp_008e_v2_subsample_on_dt1_h15: 已被终止 — unknown
- exp_008f_s2: 已被终止 — unknown
- exp_009c_s2: 已被终止 — unknown
- exp_009d_baseline_walker_s1: 已被终止 — unknown
- exp_009f_008f_walker_s1: 已被终止 — unknown
- exp_009g_008f_walker_s0: 已被终止 — unknown
- exp_009h_008f_walker_s0: 训练失败 — unknown
- exp_016_sgs_walker_s1: 训练失败 — unknown
- exp_016b_sgs_walker_s1: 训练失败 — unknown
- exp_016c_sgs_walker_s1: 训练失败 — unknown
- exp_016d_sgs_walker_s1: 训练失败 — unknown
- exp_017_subsample_off_trained_dt_emb: 已被终止 — unknown
- exp_018_full_sgs_walker_s1: 已被终止 — unknown
- exp_019a_pickcube_baseline: 已被终止 — unknown
- exp_022_untrained_dt_emb_learned_gate: 已被终止 — unknown
- exp_024_cheetah_no_dt_emb_s0: 已被终止 — unknown
- exp_025_obs_sgs_walker_s1: 训练失败 — unknown
- exp_025_obs_sgs_walker_s3: 训练失败 — unknown
- exp_025_obs_sgs_walker_s4: 训练失败 — unknown
- exp_026_obs_sgs_cheetah_s0: 训练失败 — unknown
- exp_026_obs_sgs_cheetah_s1: 训练失败 — unknown
- exp_075_cheetah_civo_trigger_s2: 已被终止 — unknown
- exp_076_cheetah_civo_trigger_s3: 已被终止 — unknown
- exp_079_frozen_dt_emb_walker_s0: 已被终止 — unknown
- exp_089_cheetah_no_dt_emb_s1: 训练失败 — unknown
- exp_090_cheetah_no_dt_emb_s2: 训练失败 — unknown
- exp_088: 已被终止 — unknown
- exp_094_cheetah_008d_s3: 训练失败 — unknown
- exp_095_cheetah_no_dt_emb_s3: 训练失败 — unknown
- exp_095_cheetah_008a_s0: 已被终止 — unknown
- exp_093: 已被终止 — unknown
- exp_094: 已被终止 — unknown
- exp_096_cheetah_008a_s0: 训练失败 — unknown
- exp_098_cheetah_008a_s0: 已被终止 — unknown
- exp_099_cheetah_008a_s1: 已被终止 — unknown
- exp_101_rssm_prediction_quality: 已被终止 — unknown
- exp_102_cheetah_008a_s0: 已被终止 — unknown
- exp_103_cheetah_008a_s1: 已被终止 — unknown
- exp_hopper_trained_s1: 已被终止 — unknown
- exp_hopper_frozen_s1: 已被终止 — unknown
- exp_104_hopper_baseline_s0: 已被终止 — unknown
- exp_105_hopper_trained_s0: 已被终止 — unknown
- exp_106_hopper_trained_s1: 已被终止 — unknown
- exp_107_hopper_frozen_s0: 已被终止 — unknown
- exp_108_hopper_frozen_s1: 已被终止 — unknown
- exp_walker_no_dt_emb_s0: 已被终止 — unknown
- exp_cheetah_008a_s3: 训练失败 — unknown
- exp_walker_008d_s6: 训练失败 — unknown
- exp_walker_008d_s7: 训练失败 — unknown
- exp_walker_008d_s6_r2: 训练失败 — unknown
- exp_walker_008d_s7_r2: 训练失败 — unknown
- exp_humanoid_008d_s0: 已被终止 — unknown
- exp_quadruped_baseline_s0: 训练失败 — unknown
- exp_quadruped_008d_s0: 已被终止 — unknown
