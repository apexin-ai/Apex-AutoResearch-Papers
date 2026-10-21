# ops westd cleanup restart ood eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-cleanup-restart-ood-eval_20260519T024512_result.json`
- **Structured JSON:** [`050749d5ad85f65f5354.json`](../../sessions/05/050749d5ad85f65f5354.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OOD eval 已启动，正在评估 **134 个 AlfworldSG_OOD tasks (eval_out_of_distribution)**。

汇总：

| 项目 | 状态 |
|------|------|
| GPU 清理 | 4 张 GPU 全部释放（182 个 Ray 进程已清理） |
| hsweep_h10_seed1 | 已终止（PID 34193 + 所有 Ray worker） |
| 旧 OOD eval | 已终止（PID 691244） |
| 新 OOD eval PID | **719394**（bash wrapper），实际 train.py PID **725711** |
| W&B run | **l0zohzt5** — `exp029-seed2-ood-reeval` |
| GPU 使用 | cuda:0 (11102MiB) + cuda:1 (11102MiB)，cuda:2,3 空闲 |
| Checkpoint | global_step_30 加载成功（world_size=2 需要 2 卡） |
| Config | `_alfworld_exp029_seed2_reeval_ood`（原始 2GPU config） |

注意：因 checkpoint 是 world_size=2 保存的，必须用 2 卡加载，无法单卡运行。已通过 `CUDA_VISIBLE_DEVICES=0,1` 限制只用 cuda:0,1，cuda:2,3 保持空闲。

---
