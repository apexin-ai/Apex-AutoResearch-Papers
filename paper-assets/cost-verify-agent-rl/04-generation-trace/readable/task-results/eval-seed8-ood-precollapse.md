# eval seed8 ood precollapse

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_seed8_ood_precollapse_20260521T211413_result.json`
- **Structured JSON:** [`7362535c70d22899ce18.json`](../../sessions/73/7362535c70d22899ce18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 已正常启动，模型加载成功，wandb 连接就绪，正在处理 validation 数据。

**执行总结：**

| 项目 | 详情 |
|------|------|
| exp_id | `exp029_seed8_ood_precollapse` |
| 服务器 | westd-47453 cuda:3（原计划 bjb1 cuda:1，因跨服务器 SSH 不通，走备选方案） |
| checkpoint | `/root/autodl-tmp/checkpoints/exp029-seed8/global_step_5/actor/` → FSDP→HF 转换至 `/root/autodl-tmp/checkpoints/qwen_exp029_seed8_step5_hf` (3.8G) |
| PID | 801623 |
| wandb run | `bpmk7i8r` |
| config | `_alfworld_exp029_seed8_ood_precollapse.yaml`（134 OOD tasks, enable_response_mask: False, CUDA_VISIBLE_DEVICES=3） |
| registry | RUNNING，spec 已写入 |

---
