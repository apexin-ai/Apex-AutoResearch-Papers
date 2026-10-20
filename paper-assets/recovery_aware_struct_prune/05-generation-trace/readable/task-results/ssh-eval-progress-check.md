# ssh eval progress check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_progress_check_20260523T205045_result.json`
- **Structured JSON:** [`f41fcbeb42e671200bc5.json`](../../sessions/f4/f41fcbeb42e671200bc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 个进程均存活，GPU 负载正常。

| # | Eval | 服务器 | GPU | 进度 | 速率 | 预估剩余 |
|---|------|--------|-----|------|------|----------|
| 1 | sft_standard_25_fixed | westd | cuda:0 | **83/500** (17%) | ~81s/it | ~9h20m |
| 2 | grpo_rasp_alpha1p0_20_fixed | westd | cuda:1 | **462/500** (92%) | ~34s/it | **~22min** |
| 3 | grpo_standard_20_fixed | westd | cuda:2 | **416/500** (83%) | ~60s/it | ~1h24m |
| 4 | sft_standard_20_fixed_v2 | westd | cuda:3 | **21/500** (4%) | ~98s/it | ~13h |
| 5 | grpo_cka_only_20_fixed | westb | cuda:0 | **140/500** (28%) | ~48s/it | ~4h47m |
| 6 | sft_random_20_fixed | westb | cuda:1 | **61/500** (12%) | ~54s/it | ~6h35m |

**GPU 状态**：
- westd: 4 卡全部 94-99% 利用率，温度 73-80°C，显存 16.8-36.0 GB
- westb: 2 卡 92-99% 利用率，温度 71-80°C，显存 15.4-16.8 GB

**关键观察**：
- `grpo_rasp_alpha1p0_20_fixed` 约 22 分钟内完成，最快出结果
- `grpo_standard_20_fixed` 约 1.5h 后完成
- `sft_standard_25_fixed` 和 `sft_standard_20_fixed_v2` 速率最慢（SFT 25% 剪枝和 v2），预计还需 9-13h
- cuda:3 上的 `sft_standard_20_fixed_v2` 显存占用 36GB，显著高于其他任务（可能是更大模型或 batch size 差异）

---
