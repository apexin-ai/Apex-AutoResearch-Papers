# Handover — 2026-05-25

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- phase1a_multiseed_8runs（准备中）
- phase1b_llama_complement: Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.（准备中）
- p0_ss_steering_eval: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.（准备中）
- d048_queue_runner（准备中）
- d048_ss_s42_resume（准备中）
- llama_tg_training（准备中）

## 近期结论
- **phase2_tf_ar_switching** (negative): TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift.
  [switching_analysis](/api/workspace-files/projects/turn_residual_gating/artifacts/phase2_tf_ar_switching/report/switching_analysis.md)
- **p1_llama_ss_eval** (success): Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.
- **phase1a_multiseed_qwen** (killed): Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.

## 趋势
成功 40 / 负向 6 / 失败 4 / 共 54

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-20861: 无 GPU 信息

## 告警
- phase2_tg_s42_v2: 已被终止 — unknown
- phase2_tg_s42_v4: 训练失败 — unknown
- phase2_tg_s42_v8_schedsampling: 训练失败 — unknown
- phase2_tg_s42_v8b_ss_fixed: 训练失败 — unknown
- d048_split_softmax_eval: 训练失败 — unknown
- phase1a_multiseed_qwen: 已被终止 — unknown
- phase2_switching: 已被终止 — unknown
- p1_ss_lora_only: 已被终止 — unknown
