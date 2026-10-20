# Handover — 2026-05-26

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- tracvla_spatial_full_v2: TraceVLA (Phi-3-mini) on LIBERO-Spatial shows the convergent entry-exit routing pattern when fine-tuned, and the untrained base model (Phi-3-Vision) lacks this pattern. Cross-suite validation for second architecture.（已分配 ? GPU:?，等待提交）
- l1_head_ablation_control8（准备中）
- fulllayer_action_probe（准备中）
- behavioral_pilot: Ablating L1 instruction-dominant heads during VLA inference will measurably change task success rate, providing behavioral evidence that these heads serve a functional role beyond representational reorganization measured by probes.（准备中）
- behavioral_pilot_v2: Ablating L1 instruction-dominant heads (24/32) during VLA inference on LIBERO-Goal fine-tuned OpenVLA reduces task success rate, providing behavioral evidence that attention head specialization has functional consequences for task execution.（准备中）
- behavioral_smoketest_diag（准备中）
- libero_finetuned_probe（准备中）
- tracvla_spatial_trained（准备中）
- bootstrap_v3_cuda1（准备中）
- bootstrap_v3_cuda0（准备中）
- …另有 1 项

## 近期结论
- **action_head_decoding_openvla_goal_untrained** (negative): Untrained OpenVLA (OXE-pretrained, no LIBERO fine-tuning) should NOT show exit-peaking action-head R² because the LM head has not been specialized for LIBERO action decoding. If trained model shows exit-peak and untrained does not, this dissociation confirms format specialization is a training-induced effect, not an architectural artifact.
  [openvla_goal_untrained_50demos_action_head_r2](/api/workspace-files/projects/vla-ssd/artifacts/action_head_decoding_openvla_goal_untrained/data/openvla_goal_untrained_50demos_action_head_r2.json) | [untrained_v2_action_head_r2](/api/workspace-files/projects/vla-ssd/artifacts/action_head_decoding_openvla_goal_untrained/data/untrained_v2_action_head_r2.txt)
- **action_head_decoding_openvla_goal** (negative): Exit-layer ΔR² drop in VLM→VLA models reflects format specialization (exit representations are optimized for the action head's specific decoding format) rather than genuine information loss. If true, applying the frozen action head to each layer's hidden state should show monotonically increasing or exit-peaking R², while independent probes show mid-layer peak + exit drop — the dissociation between the two curves is direct evidence of format specialization.
  [action_head_v2_trained_r2](/api/workspace-files/projects/vla-ssd/artifacts/action_head_decoding_openvla_goal/data/trained_action_head_r2.json)
- **qwen_nlp_control** (success): NLP instruction-tuning of Qwen2.5-3B backbone (Qwen2.5-3B-Instruct) produces flat R² action-probe profile with ΔR²≈0, confirming exit collapse is specific to VLA action training — extending NLP controls to the third backbone family (Qwen, shared with NORA), closing the stated limitation in discussion.tex:23

## 趋势
成功 108 / 负向 18 / 失败 7 / 共 145
n_samples: 5000 →（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-19183: 无 GPU 信息

## 告警
- mvp2_action_probe: 已被终止 — unknown
- lg_extract_trained_r2: 已被终止 — unknown
- lg_extract_untrained_r2: 已被终止 — unknown
- lg_extract_trained_r1: 已被终止 — unknown
- lg_extract_untrained_r1: 已被终止 — unknown
- lg_shuffled_token_control: 已被终止 — unknown
- lg_instruction_ablation: 已被终止 — unknown
- lg_output_head_analysis: 已被终止 — unknown
- threecond_multiseed_r2: 已被终止 — unknown
- behavioral_pilot_w4: 已被终止 — unknown
- libero_object_full_pipeline: 已被终止 — unknown
- tracvla_spatial_pipeline: 训练失败 — unknown
- nora_goal_full_pipeline: 训练失败 — unknown
- nora_goal_pipeline_v2: 已被终止 — unknown
- object_pipeline_ridge: 训练失败 — unknown
- nora_spatial_pipeline_v1: 训练失败 — unknown
- openvla_long_pipeline_v1: 训练失败 — unknown
- clustered_bootstrap_reanalysis_v1: 训练失败 — unknown
- clustered_bootstrap_reanalysis_v2: 训练失败 — unknown
