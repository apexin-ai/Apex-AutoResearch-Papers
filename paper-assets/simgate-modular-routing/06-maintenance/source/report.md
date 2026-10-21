# Handover — 2026-05-24

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
| exp_id | 假设 | 状态 | 关键指标 | W&B |
|--------|------|------|---------|-----|
| alfworld-llama-cross-model | Llama-3.1-8B on ALFWorld will show information asymmetry (not death) as the dominant routing mechanism, consistent with Qwen2.5-7B findings (25.9% det-preferred, DAF=0%), confirming the framework diagnoses environment-specific mechanisms regardless of model family. | — | — | — |
| gemma-scienceworld-cross-model | Gemma-2-9B-it on ScienceWorld will show death dominance (DAF > 80%) consistent with Qwen2.5-7B (90.4%) and Llama-3.1-8B (88.2%), extending the cross-model-family evidence from 2 to 3 independent model families and strengthening the claim that death avoidance dominates routing signal regardless of model architecture. | — | — | — |

## 待处理
- llama-70b-cross-model: Llama-3.1-70B-Instruct on ScienceWorld will show death dominance (DAF>80%) consistent with Qwen2.5-72B (DAF=92.4%), extending the cross-model scaling evidence from 1 to 2 independent 70B-class model families and upgrading C3 (scaling) from single-model probe to cross-model-at-scale validation.（准备中）

## 近期结论
- **llama-70b-episodes** (success): Llama-3.1-70B-Instruct-AWQ on ScienceWorld will show death dominance (DAF > 80%) consistent with 7-9B models, confirming the pattern scales to 70B ← 基于 llama-70b-cross-model
  [llama70b_episodes_launch](/api/workspace-files/projects/simgate-modular-routing/artifacts/llama-70b-episodes/report/llama70b_episodes_launch.md) | [llama70b_episodes_diagnosis](/api/workspace-files/projects/simgate-modular-routing/artifacts/llama-70b-episodes/report/llama70b_episodes_diagnosis.md)
- **backbone-scaling-70b** (success): 72B model 的 death rate 显著低于 7B (42.9%)，但 DAF 可能仍 dominant 因为 deterministic modality 的 death rate 也会降低 ← 基于 backbone-scaling-death-rate-0.5b
  [72B DAF Decomposition Analysis](/api/workspace-files/projects/simgate-modular-routing/artifacts/backbone-scaling-70b/report/72b_daf_decomposition.md)
- **gemma-scienceworld-v4** (success): Gemma-2-9B-it on ScienceWorld will replicate the death-avoidance dominance pattern (DAF>80%) observed with Qwen2.5-7B (DAF=90.4%) and Llama-3.1-8B (DAF=88.2%), confirming the diagnostic finding is model-agnostic across 3 model families.

## 趋势
成功 54 / 负向 30 / 失败 17 / 共 120

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-18266: 无 GPU 信息

## 告警
- gpu0-v6-lifespan: 已被终止 — unknown
- llama-cross-model-expanded: 已被终止 — unknown
- math-200-fixed: 训练失败 — unknown
- mvp-p1-gpu0: 已被终止 — unknown
- mvp-p1-gpu1: 已被终止 — unknown
- mvp-p1-gpu1-v2: 已被终止 — unknown
- mvp-p1-gpu1-vllm: 已被终止 — unknown
- mvp-p1-signal: 已被终止 — unknown
- plan-001b-gpu0: 训练失败 — unknown
- plan-001b-gpu0-v2: 训练失败 — unknown
- plan-001b-gpu0-v3: 训练失败 — unknown
- plan-001b-gpu0-v4: 已被终止 — unknown
- plan-001b-gpu0-v5: 已被终止 — unknown
- plan-001b-gpu1-extra: 训练失败 — unknown
- plan-001b-gpu1-rebalance: 已被终止 — unknown
- plan-002-formal: 训练失败 — unknown
- plan-002-formal-v2: 训练失败 — unknown
- plan-002-formal-v3: 训练失败 — unknown
- plan-002-generative-v1-ga1: 已被终止 — unknown
- plan-003-e2e-ablation-b: 训练失败 — unknown
- plan-004-v2: 训练失败 — unknown
- plan-008-router-size: 训练失败 — unknown
- plan-008-router-size-v2: 训练失败 — unknown
- plan-008-router-size-v3: 已被终止 — unknown
- plan-010-cross-task-transfer: 已被终止 — unknown
- research-cf-pilot-gpu1: 已被终止 — unknown
- research-prescreening-gpu0: 已被终止 — unknown
- seed-robustness-ext: 已被终止 — unknown
- seed-robustness-ext-gpu0: 已被终止 — unknown
- seed-robustness-ext-gpu1: 已被终止 — unknown
- r7n2-data-size-ablation: 训练失败 — unknown
- r7n2-data-size-ablation-v2: 训练失败 — unknown
- reflexion-dose-response: 已被终止 — unknown
- grounding-prompt-ablation: 训练失败 — unknown
- alfworld-llama-counterfactual: 训练失败 — unknown
- gemma-scienceworld-counterfactual: 训练失败 — unknown
