# 机制洞察

## Importance Margin Inverted-U 确认 (2026-05-27)

**发现**: Importance margin (L2norm SR - Random SR) 在 keep ratio 上呈 inverted-U 曲线，峰值在 k=0.9。双 seed 验证：
- k=0.95: 25.3pp (86.0%±0.2 - 60.7%±0.1)
- k=0.9: **46.0pp** (80.6%±0.6 - 34.6%±0.4) ← peak
- k=0.85: 32.5pp (78.1%±0.5 - 45.6%±1.6)

**Why inverted-U**: 高 k (0.95) 时压缩太轻，Random 也能保留足够信息，差距小。低 k (0.5) 时压缩太重，L2norm 也救不回来，三方法收敛到 ~50%。中间 k=0.9 是 "sweet spot"——Random 恰好破坏关键 token 引起系统性崩溃 (34.6%)，而 L2norm 的 importance-aware 选择仍能保护性能 (80.6%)，差距最大。

**Paper 意义**: inverted-U 是论文核心 diagnostic metric，远比单点对比更有说服力。peak 位置 (k=0.9) 和 magnitude (46pp) 是 main claim 的数量支撑。

## π0.5 Random Anti-monotonicity: strict vs lenient 反转

**发现**: 在 k=0.9 dip point，strict SR (34.2%) 比 lenient (~32%) 高 2.2pp。这与所有其他 k 值的模式相反（strict 通常比 lenient 低 0.2-2.6pp）。

**机制解释**: 其他 k 值下 strict < lenient 是因为边界案例（任务"差不多"完成但不满足严格标准）。但在 dip point，模型的功能**系统性崩溃**——不是"差一点"完成任务，而是完全无法执行。在这种基础性失败下，评估条件的宽松/严格差异不再有意义，slight variance 导致 strict 反而偶然偏高。

**Paper 意义**: 这支持 anti-monotonicity 是 **architectural vulnerability**（Random pruning 在特定 keep ratio 下破坏了关键计算路径）而非评估噪声。

## Strict 偏差规律 (D256/D257/D260/D261)

已验证的 strict vs lenient 偏差：
- L2norm k=0.95: -0.8pp (87.0→86.2)
- L2norm k=0.85: -0.2pp (77.8→77.6)
- Random k=0.95: -2.6pp (63.2→60.6)
- Random k=0.5: -0.2pp (50.0→49.8)
- **Random k=0.9: +2.2pp (32→34.2) ← 反转**

规律：高性能区偏差小(-0.2~-0.8pp)，中等性能区偏差中等(-2.6pp)，dip point 反转(+2.2pp)。

## 服务器能力备忘

- **cqa1-33015**: 支持 attention pruning mode（已验证）
- **westd-41074**: 支持 attention pruning mode（已验证）
- **westd-27271**: ⚠️ 代码未同步，仅支持 none/random/l2norm（Worker 正在修复）
- **westd-38929**: attention 支持未确认，待 w27 修复后一并验证

## 评估耗时约束 (2026-05-28)

- **π0.5**: LIBERO-10 50eps × 10tasks ≈ 2.5h
- **OpenVLA**: LIBERO-10 50eps × 10tasks ≈ 8.3h (~1.0 eps/min，比 π0.5 慢 ~3.3x)
- OV 评估提交时 timeout_hours 必须 ≥ 9h，否则会被 EXIT_CODE=124 kill

## [失败模式] GPU 冲突 (2026-05-29)

在同一 GPU 上提交新实验时，如果前一个实验仍在运行（进程未退出），两个 4.1B 模型共用一张 GPU 会导致 OOM → SIGTERM (EXIT_CODE=143)。**提交前必须确认目标 GPU 无正在运行的进程。** 案例：eval_pi05_attn_k095_long_seed47_cqa1_v2 在 cuda:0 上启动时 k=0.75 实验仍在同一 GPU 运行。
