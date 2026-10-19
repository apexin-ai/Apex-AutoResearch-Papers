# pipeline seed4 fsdp hf scp ood eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_seed4_fsdp_hf_scp_ood_eval_20260521T204214_result.json`
- **Structured JSON:** [`e2cf7213b4a834fd9799.json`](../../sessions/e2/e2cf7213b4a834fd9799.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

```
FSDP→HF 转换: 成功 | 3.8GB bf16 | 15.7s | bjb1:/root/autodl-tmp/checkpoints/exp029-seed4/global_step_15_hf/
SCP: 成功 | bjb1→westd 直连 | ~5min
Symlink: /root/autodl-tmp/checkpoints/qwen_exp029_seed4_step15_hf → exp029-seed4/global_step_15_hf
Config: /root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_seed4_ood_eval.yaml
  - model_path: qwen_exp029_seed4_step15_hf
  - CUDA_VISIBLE_DEVICES: "0"
  - enable_response_mask: False
  - val_only: True
  - AlfworldSG_OOD 134 tasks, τ=0.4
Eval PID: 762273 | tmux session: exp029_seed4_ood_eval
Log: ~/runs/cost-verify-agent-rl/exp029_seed4_ood_eval.log
```

---
