# eval bjb1 cuda1 seed5 mask check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bjb1_cuda1_seed5_mask_check_20260522T190128_result.json`
- **Structured JSON:** [`ee103b7b0f6842f0f60e.json`](../../sessions/ee/ee103b7b0f6842f0f60e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 正常运行中，正在处理数据（进度条显示 14%）。

**汇报：**

| 项目 | 详情 |
|------|------|
| **实验** | seed7-step5-response-mask-check（替代 seed5，因 seed5 checkpoint 仅在 westd、无法 SCP） |
| **Checkpoint** | `qwen_exp029_seed7_high_kl_step5_hf`（seed7 step5 pre-collapse） |
| **关键参数** | `enable_response_mask=true`, 134 OOD tasks, temp=0.4, val_only=True |
| **GPU** | cuda:1（8605 MiB），cuda:0 空闲未干扰 |
| **PID** | 446280（shell）→ 447671（TaskRunner） |
| **日志** | `/root/autodl-tmp/logs/seed7_response_mask_check.log` |
| **W&B** | `seed7-step5-response-mask-check` |

**额外发现：seed300 step5 OOD eval（v2）已完成，结果 0% success rate**（134 tasks 全部失败）。该 eval 的 config 显示 `enable_response_mask: True`。与 baseline 25.37%（mask=false）形成鲜明对比——response mask 可能导致严重性能下降，seed7 结果值得关注。

---
