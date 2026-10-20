# Handover — 2026-05-21

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
（无）

## 近期结论
- **exp_062_decoding_strategy_shape** (success): DDR shape stability (entropy_max, entropy_min, tail_decay near-stationary with d<0.15) holds under greedy (temperature=0) and top-k (k=50, τ=0.7) decoding, not just nucleus sampling — verifying the DDR decomposition is decoding-strategy-agnostic
- **decoding_strategy_shape** (killed): DDR shape stability (entropy_max, entropy_min, tail_decay d<0.15) holds under greedy and top-k decoding, not just nucleus sampling — verifying the claim is decoding-strategy-agnostic
- **plan-004-prep** (success): Downstream utility 准备：depth-stratified 数据集 + OLMo-1B fine-tuning 脚本（不开跑，等 Director 确认）

## 趋势
成功 48 / 负向 2 / 失败 12 / 共 68

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
bjb2-18868: 无 GPU 信息

## 告警
- mvp-001-gen-s0: 已被终止 — unknown
- mvp-001-gen-s1: 训练失败 — unknown
- mvp-001-gen-s2: 训练失败 — unknown
- mvp-001-gen-s3: 训练失败 — unknown
- plan-001-restore: 已被终止 — unknown
- plan-002-qwen3-1_7b-s0: 训练失败 — unknown
- plan-002-qwen3-1_7b-s1: 已被终止 — unknown
- plan-002-qwen17b-s0: 训练失败 — unknown
- plan-002-qwen17b-s1: 训练失败 — unknown
- plan-002-qwen17b-retry-s0: 训练失败 — unknown
- plan-002-qwen17b-retry-s1: 训练失败 — unknown
- plan-002-qwen06b-s0: 训练失败 — unknown
- plan-002-qwen06b-s1: 训练失败 — unknown
- plan-004: 训练失败 — unknown
- review-exp-a-baseline-ensemble: 已被终止 — unknown
- multi_domain_t07: 已被终止 — unknown
- exp_050_temp_curve_t09: 训练失败 — unknown
- decoding_strategy_shape: 已被终止 — unknown
