# ssh kill and restart math500 westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_and_restart_math500_westd_20260521T132826_result.json`
- **Structured JSON:** [`d44ffab565c67f3012eb.json`](../../sessions/d4/d44ffab565c67f3012eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 显存已加载确认：

| GPU | 显存占用 | 状态 |
|-----|---------|------|
| cuda:0 | 11825 MiB | eval_math500_grpo_cka_only_25_v2 ✓ |
| cuda:1 | 0 MiB | 空闲（按要求留空） |
| cuda:2 | 11825 MiB | eval_math500_sft_cka_only_25_v2 ✓ |
| cuda:3 | 28911 MiB | eval_gsm8k_sft_standard_25 (PID 335301) 未动 ✓ |

---

**D097 执行汇报：**

| 项目 | 结果 |
|------|------|
| Kill 3 进程 | PID 336961/359173/338876 全部已杀，确认 ALL_DEAD |
| eval_gsm8k_sft_standard_25 | PID 335301 仍在运行，进度 1111/1319 (84%)，acc=0.5082, eos_rate=95.64%, avg_len=320 |
| eval_math500_grpo_cka_only_25_v2 | PID **379999**，cuda:0，11825 MiB，正在加载 MATH dataset |
| eval_math500_sft_cka_only_25_v2 | PID **380074**，cuda:2，11825 MiB，正在加载 MATH dataset |

注：D097 指令中的参数名有误（`--output_dir`→`--output_path`，`--n_samples`→`--max_samples`，`--temperature` 不存在），已自动修正。

---
