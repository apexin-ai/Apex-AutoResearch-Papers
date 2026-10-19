# research pi05 a1 sdf integration feasibility

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pi05_a1_sdf_integration_feasibility_20260522T212707_result.json`
- **Structured JSON:** [`b6bb30c49471fe8817f5.json`](../../sessions/b6/b6bb30c49471fe8817f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/pi05_a1_sdf_feasibility_report.md`。

**核心结论：Go。集成工作量极小（~6-9 worker-hours）。**

关键发现：
- Pi0 和 Pi0.5 **共用同一个 `PI0Pytorch` 类**，仅通过 `pi05=True` 切换
- Action Expert 完全一致（gemma_300m, width=1024）→ `action_out_proj` hook 挂载点相同 → SDFDecoder/EEExtractor 无需改动
- `TrainHooks` 接口已被 A1 使用，pi0.5 训练流程完全兼容
- LoRA 注入 (`inject_lora_pi0`) 目标层不受 AdaRMSNorm 影响
- 核心修改仅 3 行 config 代码：`Pi0Config(pi05=True, action_horizon=10, discrete_state_input=False)` + 权重路径
- Pi0.5 LIBERO 权重已在 westd-45947 上可用

唯一需要关注的点：action_horizon 从 50 降到 10 后 mean pooling 信息密度变化（可能需微调 lambda_sdf），以及显存可能增加（max_token_len 200 vs 48）。

---
