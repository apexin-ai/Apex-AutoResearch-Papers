# ssh eval math500 grpo cka25 cuda0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_math500_grpo_cka25_cuda0_20260521T081928_result.json`
- **Structured JSON:** [`435f910baef330e2c5b8.json`](../../sessions/43/435f910baef330e2c5b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MATH-500 eval 正常运行中。

**产出汇总：**

| 项目 | 详情 |
|------|------|
| 模型路径 | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25/model.safetensors` (11G) |
| 脚本 | `src/eval_math500.py` |
| 服务器/GPU | westd-29022 cuda:0 |
| PID | 336961 (python), 336956 (bash wrapper) |
| GPU 占用 | cuda:0, ~11.8 GiB |
| 进度 | 1/500, ~3.68s/it，预计 ~30 分钟完成 |
| 日志 | `/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25.log` |

首次启动因未启用 `network_turbo` 导致 HF 数据集下载卡住，已杀掉重启并修复。

---
