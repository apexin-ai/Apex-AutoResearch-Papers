# ssh gpu audit and fix 20260521T0430

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_audit_and_fix_20260521T0430_20260521T043852_result.json`
- **Structured JSON:** [`e8dc30cb43e382945d10.json`](../../sessions/e8/e8dc30cb43e382945d10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 已成功启动，正在加载模型。

---

## GPU 对账表

| 服务器 | GPU | 进程 | PID | 状态 | 备注 |
|--------|-----|------|-----|------|------|
| **westd-29022** | cuda:0 | grpo_random_20 | 317332 | **死（训练完成，保存失败）** | 100/100 steps 完成，final reward=**0.189**，save_model 磁盘满失败。`checkpoint-100/` 有完整模型（12G），已删除截断的 root model.safetensors + optimizer.pt，释放 21G |
| westd-29022 | cuda:1 | — | — | 空闲 | — |
| westd-29022 | cuda:2 | eval_gsm8k_grpo_cka_only_25_v2 | **320735（新）** | **已重交** | 原 PID 318738 因路径错误崩溃（`/checkpoint-100` 不存在），已修正为 `/grpo_cka_only_25` 重交 |
| westd-29022 | cuda:3 | grpo_rasp_20_seed456 | — | **不存在** | 无 log 文件、无进程，从未启动 |
| **westb-23072** | cuda:0 | eval_math500_sft_standard_25 | 62714 | **运行中** | 106/500 (21%), ~85s/it |
| westb-23072 | cuda:1 | grpo_standard_25_westb | 64194 | **运行中** | 51/100 (51%), ~108s/it |

## 已执行的操作

1. **清理磁盘**：删除 `grpo_random_20/model.safetensors`（5.9G 截断废文件）+ `checkpoint-100/optimizer.pt`（15G），数据盘从 100% → 97%（21G 可用）
2. **重交 eval**：`eval_gsm8k_grpo_cka_only_25_v2` 已用修正路径重交，PID=320735

## grpo_random_20 最终训练指标（step 100）

| 指标 | 值 |
|------|----|
| reward | 0.189 |
| kl | 0.0049 |
| entropy | 0.169 |
| grad_norm | 5.53 |
| loss | -0.00013 |

## 需要关注

- **RASP seed456（cuda:3）从未启动**——需确认是否还要跑
- **grpo_random_20 的可用模型**在 `checkpoint-100/model.safetensors`（12G），后续 eval 需指向 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100`
- westd-29022 数据盘仍 97%，空间紧张

---
