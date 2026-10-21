# eval seed300 id diag bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_seed300_id_diag_bjb1_20260522T190836_result.json`
- **Structured JSON:** [`7ed33ca7fa794d93e797.json`](../../sessions/7e/7ed33ca7fa794d93e797.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功，模型正在加载到 cuda:0（当前 559 MiB）。

---

## 汇报

### Part A: Checkpoint / Config 检查

| 检查项 | 结果 |
|--------|------|
| Checkpoint symlink | `qwen_exp029_seed300_step5_hf -> exp029_seed300_step5_hf`，正确 |
| 模型文件完整性 | 1 个 safetensors (4GB) + tokenizer 全套，完整 |
| **enable_response_mask** | **false** — OOD config 设置正确，排除此原因 |
| enable_think | False，与其他 eval 一致 |
| temperature | rollout 1.0, val_kwargs 0.4，正常 |
| val 任务数 | 134 AlfworldSG_OOD tasks，满足 C003（≥16） |

**结论：OOD eval config 没有明显配置错误。0.0% pass@1 更可能是真实的 OOD 泛化失败，而非配置问题。** ID eval 结果将确认 checkpoint 本身是否正常工作。

### Part B: ID Eval 已启动

- **PID**: 448290
- **Config**: `_alfworld_seed300_step5_id_eval_diag.yaml`
- **GPU**: cuda:0，模型加载中
- **Val tasks**: 32 AlfworldSG（in-distribution），group_size=1
- **Log**: `/root/autodl-tmp/logs/seed300_step5_id_eval_diag.log`
- **W&B experiment**: `seed300-step5-id-eval-diag`

---
