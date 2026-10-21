# code scoring ablation magnitude sft

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scoring_ablation_magnitude_sft_20260517T072457_result.json`
- **Structured JSON:** [`2eedbd4e3cc5c0ef71d8.json`](../../sessions/2e/2eedbd4e3cc5c0ef71d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SFT 已成功启动并在运行。

**报告：**

| 项目 | 详情 |
|------|------|
| Kill 的进程 | PID 681896 — `eval_gsm8k.py --model_path pruned_magnitude_20`（60/200 samples, acc=0%） |
| SFT 进程 PID | 689115 — `sft_recovery.py` on cuda:0 |
| Pruned model 路径 | `/root/autodl-tmp/recovery_aware_struct_prune/pruned_magnitude_20/` |
| SFT 输出路径 | `/root/autodl-tmp/recovery_aware_struct_prune/sft_magnitude_20/` |
| GPU 利用 | cuda:0 96%, 29GB used（SFT）; cuda:1 90%, 17GB（其他 eval 进程） |
| tmux session | `scoring_ablation_v2`（已重建） |

**后续方法执行方式：** 原 script 因 `set -e` 在 kill 时退出。已创建续跑脚本 `run_scoring_ablation_continue.sh`，在 magnitude SFT+eval 完成后会自动依次执行 gradient → random → cka_only 全流程（prune+eval+SFT+eval），无需手动干预。

---
