## exp_066 时序 RSSM Fidelity 分析结果

### 核心结论
Fidelity gap LEADS VE ratio by 5K-15K steps → 支持 "RSSM fidelity gap → value overestimation" 时序因果链

### 数据

| Step | SS ratio (dt2/dt1) | OL ratio (H=8) | CumRew Err (dt2) | State Div Gap | VE ratio |
|------|-------------------|-----------------|-------------------|---------------|----------|
| 10K  | 1.058x | 0.942x | 1.24 | 0.093 | 0.005 |
| 15K  | 1.049x | 1.022x | 1.28 | 0.131 | 0.022 |
| 20K  | 1.113x | 1.072x | 1.35 | 0.149 | 0.156 |
| 25K  | 1.069x | 1.287x | 1.60 | 0.153 | 0.163 |
| 30K  | 1.250x | 1.371x | 1.82 | 0.151 | 0.215 |
| 35K  | 1.302x | 1.491x | 1.99 | 0.157 | 0.229 |
| 40K  | 1.295x | 1.407x | 1.76 | 0.155 | 1.591 |
| 45K  | 1.407x | 1.339x | 1.74 | 0.149 | 0.360 |
| 50K  | 1.430x | 1.519x | 1.90 | 0.146 | 0.616 |
| 55K  | 1.278x | 1.448x | 1.87 | 0.151 | 0.621 |
| 60K  | 1.623x | 1.417x | 1.79 | 0.142 | 1.399 |
| 65K  | 1.835x | 1.328x | 1.68 | 0.134 | 1.399 |

### 关键时序节点
- Fidelity gap 加速点: 25K-30K (OL ratio 突破 1.25x)
- VE ratio 首次 spike: 40K (1.591)
- 时间差: ~5K-15K steps

### 机制
dt=1 MAE 随训练持续下降 (0.093→0.047)，而 dt=2 MAE 基本不变 (~0.08)。Gap 来自差异化改善。

### 数据文件
- 服务器: bjb1-40020:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_066_timeseries_rssm_fidelity_s0/timeseries_analysis_v2.json
- 脚本: scripts/exp_066_timeseries_analysis_v2.py