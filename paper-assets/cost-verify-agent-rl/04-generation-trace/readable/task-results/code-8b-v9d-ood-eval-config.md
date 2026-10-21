# code 8b v9d ood eval config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8b_v9d_ood_eval_config_20260520T092801_result.json`
- **Structured JSON:** [`7a2e508810798be7f50b.json`](../../sessions/7a/7a2e508810798be7f50b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置文件创建完成，YAML 验证通过。

---

**配置文件**: `westd-47453:/root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_v9d_ood_eval.yaml`

**Eval 命令**:
```bash
cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_8b_v9d_ood_eval
```

**Checkpoint 状态**:
- `global_step_15` — 尚未生成（`resume_from_path` 指向此处，训练到 step 15 后可用）
- `global_step_10` — 已存在，但 huggingface 目录仅有 tokenizer，无权重文件。如需用 step 10，改 `resume_from_path` 为 `.../global_step_10`

**关键配置差异 vs 训练**:
- `val_only: True`，`resume_mode: resume_path`
- 134 OOD tasks (`AlfworldSG_OOD`)，T=0.4 do_sample
- `gpu_memory_utilization: 0.45`（eval-only 可给更多显存给 vLLM）
- `use_ref: False`, `use_kl_loss: False`（eval 不需要）
- **保留 4 GPU**：checkpoint 以 `world_size_4` 保存，2 GPU 加载可能需要 resharding，4 GPU 更稳妥

---
