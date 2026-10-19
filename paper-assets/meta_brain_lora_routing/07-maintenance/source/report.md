# Handover — 2026-05-17

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- phase1_physical_demo_collection（已分配 ? GPU:?，等待提交）
- phase1_spatial_demo_collection（已分配 ? GPU:?，等待提交）
- phase1_lora_spatial（已分配 westd-34142 GPU:['cuda:0']，等待提交）
- phase_b5_activation_collection（准备中）
- eval_variance_p0: Eval 存在未控制的非确定性源（torch/numpy/env/LIBERO simulator random state），导致 same-seed 结果方差 >15pp，需定位并修复后才能做可靠对比（准备中）
- p1_universal_r16_full: Universal LoRA r16 是否能在某些扰动类型上改善 baseline——若无改善则证明 specialized routing 的必要性（universal 不够，需要 per-perturbation expert）（准备中）
- p1_baseline_full_coverage: Frozen pi0_libero 在不同扰动类型下性能下降程度不同，robot_initial_states 和 language 预期降幅最大（>30pp），background_textures 预期降幅小（<10pp），建立完整 baseline 量化各类扰动影响（准备中）
- eval_data_confirm_r48_sensor: 确认 universal r16 eval 数据完整性（3-seed×20eps=60eps），补全 r48 sensor_noise 评估，并追溯 physical expert 数据不一致（26.4% vs 28.3%）的来源（准备中）
- v3_r48_early_stop_ablation: r48 训练过程中存在过拟合拐点：中间 checkpoint (step 3000-5000) 在 nominal 和 light_conditions 上应优于最终 step 10000，直接证明 r48 性能退化源自过拟合而非容量本身有害（准备中）
- eval_no_routing: Frozen PI0 baseline (no LoRA) for comparison — measures perturbation robustness without any adaptation（准备中）

## 近期结论
- **v3_lora_universal_r32** (failed): Rank-32 universal LoRA (~7.4M params) 是否比 r16 过拟合（类似 r48 pattern），用于精确定位 rank scaling 拐点——若 r32 已开始退化则拐点在 r16-r32 之间，若仍有提升则 r16 并非最优 ← 基于 v3_lora_universal_r16
- **v3_lora_universal_r8** (failed): Rank-8 universal LoRA (~1.8M params) 在有限增强数据下是否与 r16 表现相当，用于确定 rank scaling 下界——若 r8 接近 r16 则说明 r16 已有冗余容量，若 r8 明显更差则 r16 是容量下限 ← 基于 v3_lora_universal_r16
- **v3_lora_universal_r48** (success): Universal LoRA r48 (11M params) 比 r16 (3.7M) 有更强的扰动适应能力，因为更高 rank 提供更大的表征容量来建模多类扰动的联合分布

## 趋势
成功 12 / 负向 0 / 失败 2 / 共 21
final_train_loss: 0.4302 ↓（近 3 次 success）
initial_train_loss: 1.6695 ↓（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-34142: 无 GPU 信息

## 告警
- eval_visual_r16: 已被终止 — unknown
- eval_physical_r16: 已被终止 — unknown
- eval_par_v1: 已被终止 — unknown
- eval_univ_r16: 已被终止 — unknown
- eval_univ_r48: 已被终止 — unknown
- v2_lora_spatial_r16: 已被终止 — unknown
- v2_lora_universal_r16: 已被终止 — unknown
- v3_lora_universal_r8: 训练失败 — unknown
- v3_lora_universal_r32: 训练失败 — unknown
