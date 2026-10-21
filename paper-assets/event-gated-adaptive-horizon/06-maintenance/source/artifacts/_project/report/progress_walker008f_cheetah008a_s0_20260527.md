# 实验进度报告: Walker 008f s0 + Cheetah 008a s0
**日期**: 2026-05-27  **服务器**: westd-51268

## 状态汇总

| exp_id | PID | 状态 | 当前step | GPU | 显存 | FPS | 预估完成 |
|--------|-----|------|----------|-----|------|-----|----------|
| exp_walker_008f_s0 | 637987 | 运行中 | 80K/105K | GPU 0 | 3257 MiB | 10.5 | ~40 min |
| exp_cheetah_008a_s0 | 637656 | 运行中 | 88K/105K | GPU 1 | 4671 MiB | 11.4 | ~25 min |

## Walker 008f s0

### Eval Return 轨迹
| Step | eval_return | ve_ratio | delta_ve | alert |
|------|------------|----------|----------|-------|
| 5K   | 34.9  | —     | —      | — |
| 15K  | 133.7 | 0.019 | 0.000  | 0 |
| 25K  | 175.8 | 0.102 | +0.083 | 0 |
| 35K  | 219.0 | 0.173 | +0.072 | 0 |
| 45K  | 233.8 | 0.234 | +0.060 | 0 |
| 55K  | 154.8 | 0.477 | +0.243 | 0 |
| 65K  | 126.4 | 0.728 | +0.251 | **1** |
| 75K  | 183.0 | 0.586 | -0.142 | 0 |

- **Peak eval_return: 233.8 @ 45K**，55-65K 大幅回落，75K 部分恢复
- Walker baseline (seed 0): eval_return ≈ 916 → 当前峰值仅 25.5%
- 同配置历史: exp_008f (s0, 完成) eval=503, NVE=0.30; exp_walker_no_dt_emb_s1 (s1) eval=469, NVE_peak=0.88
- ve_ratio 在 65K 达到 0.728 并触发 CIVO alert，但 eval 在该点反而最低（126.4）
- **CIVO 判定**: NVE_peak 未达 2.0 阈值，不满足 CIVO 条件

### Gate 行为
- **所有 checkpoint**: gate_dt_mean=2.0, gate_dt_2_frac=1.0, gate_empirical_entropy=0.0
- Gate 完全锁死在 dt=2，自适应机制未激活

## Cheetah 008a s0

### Eval Return 轨迹
| Step | eval_return | ve_ratio | delta_ve | alert |
|------|------------|----------|----------|-------|
| 5K   | 8.3   | —     | —      | — |
| 15K  | 24.3  | 0.106 | 0.000  | 0 |
| 25K  | 343.9 | 0.055 | -0.052 | 0 |
| 35K  | 306.9 | 0.150 | +0.095 | 0 |
| 45K  | 391.8 | 0.197 | +0.048 | 0 |
| 55K  | 325.1 | 0.325 | +0.128 | 0 |
| 65K  | 344.3 | 0.369 | +0.044 | 0 |
| 75K  | 433.5 | 0.326 | -0.043 | 0 |
| 85K  | **483.0** | 0.312 | -0.014 | 0 |

- **Peak eval_return: 483.0 @ 85K，仍在上升趋势**
- Cheetah baseline (seed 1): eval_return ≈ 444 → **已超越 baseline (108.8%)**
- 同配置历史: exp_cheetah_008a_s1 (s1, 完成) eval=281, NVE=0.584 → s0 大幅领先 (+71.9%)
- ve_ratio 在 65K 峰值 0.369 后趋稳于 ~0.31
- **CIVO 判定**: NVE_peak 未达 2.0，无 alert 触发

### Gate 行为
- **所有 checkpoint**: gate_dt_mean=2.0, gate_dt_2_frac=1.0, gate_empirical_entropy=0.0
- 与 Walker 相同，Gate 完全锁死在 dt=2

## 关键发现

1. **Gate 机制失效**: 两个实验的 gate 在全部训练过程中始终输出 dt=2（最小值），empirical entropy=0，entropy_ratio=0。自适应 horizon 选择功能实际未启用，实验等效于固定 dt=2 baseline。

2. **Cheetah s0 表现亮眼**: eval_return=483 已超越 baseline (444)，且仍在上升。与 s1 (eval=281) 形成巨大 seed variance。

3. **Walker s0 表现平庸**: Peak 233.8 远低于 baseline (916) 和已完成 seeds (503/469)。45K 后出现明显性能退化，75K 部分恢复但仍低。
