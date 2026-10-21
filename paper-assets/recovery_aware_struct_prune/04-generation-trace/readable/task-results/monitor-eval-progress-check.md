# monitor eval progress check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_eval-progress-check_20260522T000041_result.json`
- **Structured JSON:** [`52bd52886195bd90cbf1.json`](../../sessions/52/52bd52886195bd90cbf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下。注意 westb-23072 上两个实验共享 cuda:1，GPU 竞争导致速度严重下降。

| exp_id | server:gpu | progress | speed | ETA (UTC) |
|--------|-----------|----------|-------|-----------|
| eval_math500_sft_standard_25 | westb:cuda1 | 366/500 (73%) | ~145s/it | ~13:30 (~5h30m) |
| eval_math500_sft_cka_only_20 ¹ | westb:cuda1 | 288/500 (58%) | bimodal: 6~142s/it | ~11:00\~15:00 ² |
| eval_gsm8k_sft_alpha4_20_v4 | westd:cuda0 | 863/1319 (65%) | ~5.9s/it | ~08:47 (~45m) |
| eval_math500_grpo_random_20_v2 | westd:cuda1 | **500/500 (100%)** | — | **DONE, 但保存崩溃** ³ |
| eval_math500_grpo_alpha4_20 | westd:cuda2 | 392/500 (78%) | ~60s/it | ~09:50 (~1h48m) |
| eval_math500_sft_random_20 | westd:cuda3 | 470/500 (94%) | ~75s/it | ~08:40 (~38m) |

**关键问题：**

1. **¹ 实验名不匹配**：PID 118095 实际加载的是 `sft_cka_only_20`（非 v6），log 在 `/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_20/eval.log`

2. **² GPU 竞争**：westb-23072 cuda:1 同时跑两个 eval（PID 104592 + 118095），两者互相拖慢。sft_cka_only_20 的 ETA 不确定性大（速度在 6s/it 和 142s/it 之间剧烈波动）

3. **³ grpo_random_20_v2 已完成但崩溃**：500/500 跑完（Acc=0.1200），但保存结果时报 `IsADirectoryError: [Errno 21] Is a directory: '/root/runs/recovery_aware_struct_prune/eval_math500_grpo_random_20_v2'`——`--output_path` 传了目录而非文件路径，需要修复后重新保存或手工从 log 提取结果

---
