# eval seed4 ood eval v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_seed4_ood_eval_v2_20260521T210824_result.json`
- **Structured JSON:** [`7f52331d0b5b214e360a.json`](../../sessions/7f/7f52331d0b5b214e360a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 项目 | 结果 |
|------|------|
| **Checkpoint** | `/root/autodl-tmp/checkpoints/qwen_exp029_seed4_step15_hf/` 验证通过，config.json + model.safetensors (3.8GB) + tokenizer 齐全，路径含 "qwen" 可通过 token 检测 |
| **Config** | 复用已有 `_alfworld_exp029_seed4_ood_eval.yaml`，仅将 CUDA_VISIBLE_DEVICES 从 "0" 改为 "2"。val_only=True, enable_response_mask=False, OOD 134 tasks |
| **Dry-run** | Config 加载成功 |
| **Job 提交** | PID 779407, westd-47453, cuda:2, tmux session `exp029_seed4_ood_eval_v2`, log: `~/runs/cost-verify-agent-rl/exp029_seed4_ood_eval_v2.log` |
| **Registry** | `exp029_seed4_ood_eval_v2` 已创建，parent=exp029_seed4_v2, status=RUNNING |

---
