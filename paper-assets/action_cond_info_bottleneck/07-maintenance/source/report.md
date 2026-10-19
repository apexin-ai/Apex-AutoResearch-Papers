# Handover — 2026-05-18

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
| exp_id | 假设 | 状态 | 关键指标 | W&B |
|--------|------|------|---------|-----|
| acib_v73_eval_alpha00_spatial | v7.3 LoRA 结构性保证验证：α=0.0 时 lora_scale=0 精确恢复 baseline connector weights，spatial suite SR 必须 = baseline 66.0% ±1pp。这是 LoRA 方案的核心 claim——如果 α=0.0 不能恢复 baseline，则 LoRA isolation 实现有 bug。 | — | — | — |
| acib_v73_connector_only_eval | Connector-only eval α=0.0: connector drift 13.7%（无 reg）对 4-suite 性能的影响。预计损伤远大于 v7.2 的 0.4% drift (-4.85pp)。论文 ablation table 数据：connector-only vs v7.2 vs v7.3 对比。 | — | — | — |
| acib_v73_connector_lora | v7.3 connector LoRA (rank=8) + scorer training: LoRA 冻结原始 connector weights，α=0.0 时 lora_scale=0 精确恢复 baseline（消除 connector drift 根因），α=1.0 时 LoRA adapter 提供 task-discriminative features 给 scorer。结构性解决 v7.2 的 Goldilocks 困境。Pass: α=0.0=baseline±1pp, Probe A cos<0.8, α=1.0 4-suite avg≥64.1%。 | — | — | — |

## 待处理
- acib_deploy_westb13953（排队等待 GPU）
- acib_v7_alpha0.0_eval: Alpha=0.0 passthrough 诊断：scoring weight 为 0 时 ACIB 无干预，模型应等同 base model。如果回退仍存在，说明训练本身损伤了 base policy（而非 scoring 过激）。如果恢复到 baseline 水平，确认回退根因是 scoring 强度。（准备中）
- acib_v7_seed1_resume: v7 log-barrier contrastive seed1 完整重跑：原 run 在 step ~6700/20000 被 SIGHUP 杀 (EXIT_CODE=129)。Step 5000 Probe A cos [0.476, 0.894] 已验证方法有效。需要完整 20000 步训练以获得最终 checkpoint 供 eval。（准备中）
- acib_v8_film: FiLM conditioning 替代 concat+MLP：用 gamma*visual+beta 乘性调制使 language 信号无法被 shortcut 学习绕过。scorer 输入从 [vis,cond] concat 改为 modulated_vis，维度 1920→960。不加 contrastive loss。预期 Probe A cos < 0.95。（准备中）

## 近期结论
- **acib_v73_connector_only_ablation** (success): Connector-only ablation (无 scorer/contrastive/IB loss): 仅 task loss 训练 connector (freeze_mode=connector_only)，判定 v7.2 的 spatial conditioning 是 scorer-driven contrastive learning 的产物还是 connector tuning 的自然结果。Pass: 如果 Probe A cos≈1.0（无语言依赖）→ 证明 scorer contrastive 是 spatial conditioning 的必要组件。 ← 基于 acib_v72_connector_scorer_seed1
- **acib_v72_eval_alpha10** (negative): v7.2 alpha=1.0 full scoring eval: ACIB scoring 全开时应 ≥ baseline - 2pp (64.1%)。核心测试：language-conditioned token importance 是否提升或保持 policy 性能。Pass: avg SR ≥ 64.1%。 ← 基于 acib_v72_connector_scorer_seed1
- **acib_v72_eval_alpha00** (negative): v7.2 alpha=0.0 passthrough eval: scoring 关闭时 v7.2 checkpoint 应恢复到 baseline 水平 (~66.1%)，验证 connector+scorer 训练未损伤 action expert（connector drift reg 有效）。Pass: avg SR ≥ 64%。 ← 基于 acib_v72_connector_scorer_seed1

## 趋势
成功 9 / 负向 12 / 失败 4 / 共 28
training_steps: 20000 →（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westb-13953: 无 GPU 信息

## 告警
- mvp1_baseline_std: 已被终止 — unknown
- mvp1_baseline_std_remaining: 训练失败 — unknown
- acib_v5_div_reg: 训练失败 — unknown
- acib_v5_div_reg_seed2: 训练失败 — unknown
- acib_v5_div_reg_eval_ckpt10000: 训练失败 — unknown
- acib_v7_contrastive_r2: 已被终止 — unknown
- acib_v7_alpha03_eval: 已被终止 — unknown
