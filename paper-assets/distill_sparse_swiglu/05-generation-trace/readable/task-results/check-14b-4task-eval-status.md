# check 14b 4task eval status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_14b_4task_eval_status_20260518T004959_result.json`
- **Structured JSON:** [`cf5f7320ee4e7d554f89.json`](../../sessions/cf/cf5f7320ee4e7d554f89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已**崩溃**，状态如下：

## 汇总

| 实验 | 进程状态 | WikiText-2 PPL | ARC-c / WinoGrande / MMLU |
|------|----------|----------------|---------------------------|
| KL 30% | 已崩溃 | **7.6318** | 未完成 |
| TEAL 30% | 已崩溃 | **8.0054** | 未完成 |

## 崩溃原因

两个实验的失败模式完全一致：

1. WikiText-2 PPL 评估**成功完成**
2. 进入 `lm-eval` 阶段尝试运行 `arc_challenge` 时，需要从 HuggingFace Hub 下载 `allenai/ai2_arc` 数据集
3. 服务器**网络不可达**：`[Errno 101] Network is unreachable`
4. 重试 1 次后，httpx client 被关闭，抛出 `RuntimeError: Cannot send a request, as the client has been closed.`

**根因：westd-34887 外网访问被断开**，导致 lm-eval-harness 无法下载评测数据集。

## 已获得的数据

- KL 30% sparse WikiText-2 PPL = **7.6318**
- TEAL 30% sparse WikiText-2 PPL = **8.0054**
- 两者的 per-layer sparsity 也已打印（KL model-level 0.275, TEAL model-level 0.293）

## 修复方向

需要解决 lm-eval 数据集的离线可用性问题。选项：
1. 提前在有网络时缓存数据集到本地（`HF_DATASETS_OFFLINE=1` + 预下载）
2. 手动将 `ai2_arc`、`winogrande`、`cais/mmlu` 数据集文件传到服务器的 HF cache 目录
3. 恢复服务器外网访问后重跑（只需重跑 lm-eval 部分，PPL 已有结果）

---
