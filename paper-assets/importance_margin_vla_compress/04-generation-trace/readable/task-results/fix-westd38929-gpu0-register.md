# fix westd38929 gpu0 register

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd38929_gpu0_register_20260527T074209_result.json`
- **Structured JSON:** [`b7826a8a08b6d8fe9ed1.json`](../../sessions/b7/b7826a8a08b6d8fe9ed1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

**结果汇总：**

| 项目 | 状态 |
|------|------|
| GPU0 状态 | **在跑** — PID 112587，已运行 1h23m |
| 实验 | OV Random k=0.95，suite=libero_10，500 episodes |
| 当前进度 | Task 2/10，~1.0 eps/min，预计还需 ~7h |
| 日志 | `eval_openvla_random_k095_long_seed42_v2.log` |
| Task 1 SR | 0.720 (36/50) |
| Registry | `eval_openvla_random_k095_long_seed42_backup` → RUNNING |
| GPU0 可用性 | **不可用**，被当前实验占用 |

注：原始提交（PID 112244）因 `--gpu 0` 参数不被脚本接受而失败，当前进程是重新启动的版本（PID 112587），使用 `CUDA_VISIBLE_DEVICES` 方式指定 GPU。

---
