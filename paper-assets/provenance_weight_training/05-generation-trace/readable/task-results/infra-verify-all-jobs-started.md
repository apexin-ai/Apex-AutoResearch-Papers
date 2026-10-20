# infra verify all jobs started

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_all_jobs_started_20260520T033200_result.json`
- **Structured JSON:** [`cfbeacbcf010752a25d4.json`](../../sessions/cf/cfbeacbcf010752a25d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 任务 | GPU | PID | 显存 | GPU利用率 | 状态 |
|------|-----|-----|------|-----------|------|
| adaptive_rho06_tau07_seed42 | GPU 0 | 383864 | 45634 MiB | 69% | **运行中** |
| adaptive_rho06_tau07_seed123 | GPU 1 | 383947 | 45634 MiB | 100% | **运行中** |
| adaptive_rho06_tau07_seed456 | GPU 2 | 384114 | 45634 MiB | 98% | **运行中** |
| uniform_seed42_downstream (lm-eval) | GPU 3 | 384367 | 1834 MiB | 0% | **运行中**（模型加载完成，正在评估） |

- 3 个 adaptive 训练任务：模型和数据加载成功（371499 examples, max_steps=6103），正在训练中，GPU 利用率 69-100%。
- uniform_seed42_downstream：这是 lm-eval-harness 评估任务（arc_easy, arc_challenge, hellaswag, piqa, winogrande），模型已加载，显存占用较低（评估模式），刚启动正在跑。
- GPU 3 上还有一个 PID=382185 的旧 python 进程（1834 MiB），可能是之前的残留进程。

全部正常，没有 EXIT_CODE=127 或 "command not found" 错误。

---
