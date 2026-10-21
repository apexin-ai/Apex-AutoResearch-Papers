# diagnose westd38929 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd38929_status_20260521T072618_result.json`
- **Structured JSON:** [`53c5958ff0a8605d65d4.json`](../../sessions/53/53c5958ff0a8605d65d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有部分结果文件。汇总如下：

---

## 诊断结果

### GPU 状态
4x NVIDIA RTX PRO 6000 Blackwell (98GB) **全部可用**。之前的 GPU 缩减问题已恢复。

| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 16.0 GB | 运行中 |
| 1 | 15.9 GB | 运行中 |
| 2 | ~0 GB | 空闲 |
| 3 | ~0 GB | 空闲 |

### 实验状态

| 实验 | GPU | PID | 状态 | 说明 |
|------|-----|-----|------|------|
| eval_openvla_l2norm_k07_object_seed42_v2 | 0 | 1945 | **运行中** | Task 1/10, 256→179 tokens |
| eval_openvla_random_k03_object_seed42_v2 | 1 | 2478 | **运行中** | Task 1/10, 256→76 tokens |
| eval_openvla_random_k07_object_seed42 | 2 | — | **已死** | 日志为空，进程不存在 |
| eval_openvla_l2norm_k05_object_seed42_v2 | 3 | — | **已死** | `--mode l2norm` 参数错误（应为 `l2norm_prune`） |

### 死因分析
- **l2norm_k05**: 启动命令传了 `--mode l2norm`，脚本只接受 `baseline`/`random_prune`/`l2norm_prune`，立即退出。
- **random_k07**: 日志完全为空，可能启动命令本身就失败了（进程未成功创建）。
- 两个失败实验均无部分结果产出。

---
