# status check all gpu

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_check_all_gpu_20260519T191635_result.json`
- **Structured JSON:** [`0123d185f8d2bf1434f1.json`](../../sessions/01/0123d185f8d2bf1434f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### adaptive_fromscratch_seed42 (cuda:0)
- **进度**: step 655 / 6103 (11%)
- **速度**: ~2.23 s/step
- **ETA**: ~3h 22m
- **GPU 0**: 45643 MiB, 100% 利用率
- loss=9.955, unweighted_loss 在 1.1-2.8 范围

### Downstream eval (cuda:1/2/3)
三个 eval 刚启动 (~03:15)，都在加载模型/数据阶段：

| 任务 | GPU | 状态 | 备注 |
|------|-----|------|------|
| downstream_adaptive_ood_seed123 | cuda:1 | 进行中 | 模型已加载，正在加载 arc_easy 数据集（HF 网络不通，使用缓存） |
| downstream_adaptive_ood_seed456 | cuda:2 | 进行中 | 模型已加载，正在加载数据集（同样网络重试中） |
| downstream_uniform_ood_seed123 | cuda:3 | 进行中 | 模型已加载 |
| downstream_uniform_ood_seed456 | — | 未启动 | 无日志文件，无对应进程 |

### OOD eval（已完成）
`output/eval/` 下已有 4 个 OOD PPL 评估结果文件（May 20 02:41-02:43）：
- ood_adaptive_seed123.json
- ood_adaptive_seed456.json
- ood_uniform_seed123.json
- ood_uniform_seed456.json

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 45643 MiB | 100% |
| 1 | 1843 MiB | 0% |
| 2 | 1843 MiB | 0% |
| 3 | 1843 MiB | 0% |

GPU 1-3 显存低且利用率 0%，说明 eval 进程还在数据加载阶段，尚未开始推理。`uniform_seed456` 的 downstream eval 未启动。

---
