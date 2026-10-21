# ssh westd 14b eval verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-14b-eval-verify_20260519T015834_result.json`
- **Structured JSON:** [`ad0391425240e4e987df.json`](../../sessions/ad/ad0391425240e4e987df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B Eval Batch 状态（westd cuda:0）

**服务器确认**：westd-29999，4× NVIDIA RTX PRO 6000 Black (~97887 MiB)

**进程状态**：eval 仍在运行（PID 95424，tmux session `eval_14b_batch`），cron 报告进程退出是误报。

**已完成结果**：

| Adapter | MMLU | ARC Challenge |
|---------|------|---------------|
| d000_s42 | 0.7459 (10474/14042) | 0.9352 (1096/1172) |
| d005_s42 | 进行中 (34%, ~4851/14042 MMLU) | 待评 |
| d025_s42 | 待评 | 待评 |
| d050_s42 | 待评 | 待评 |
| d100_s42 | 待评 | 待评 |

**Checkpoints**：5 个 adapter 全部存在且有 adapter_config.json（d050/d100 有 .done 标记，d000/d005/d025 无 .done 但 lora_adapter 目录完整）。

**cuda:0 状态**：占用中（32.7GB / 97.9GB，94% 利用率），d005 MMLU 评估以 ~17 it/s 推进。按 14042 items 估算 MMLU 约 14 分钟完成，加上 ARC 约 1 分钟，每个 adapter 约 15-16 分钟。剩余 4 个 adapter 预计约 1 小时完成全部 eval。

---
