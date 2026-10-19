# code qwen14b kl30 s456 eval 41718

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen14b_kl30_s456_eval_41718_20260519T153305_result.json`
- **Structured JSON:** [`83a737c568f119a63dd2.json`](../../sessions/83/83a737c568f119a63dd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

- **进程已启动**：westd-41718 cuda:0，PID 156016，`qwen14b_kl30_s456_eval_v2` 命令
- **D075 sigmoid 修复**：已确认 (`torch.sigmoid(logits)`)
- **Checkpoint**：从 westd-34887 scp 到 westd-41718，224M，校验一致
- **Per-layer sparsity**：~0.29-0.30，符合 0.3 目标
- **6 tasks**：wikitext2, arc_challenge, winogrande, hellaswag, piqa, mmlu
- **Registry**：`qwen14b_kl30_s456_eval_v3`（v2 已被之前的 westd-34887 运行占用，status=DONE），当前 status=RUNNING
- **Cron 监控**：每 2 分钟检查，job ID `8154f724`

注意：`qwen14b_kl30_s456_eval_v2` 在 registry 中已有之前在 westd-34887 完成的结果（PPL=7.69, ARC=0.53, WG=0.72, HS=0.71, PIQA=0.76, MMLU=0.64）。本次在 westd-41718 的重跑注册为 v3。

---
