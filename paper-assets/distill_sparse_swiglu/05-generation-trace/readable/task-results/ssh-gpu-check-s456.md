# ssh gpu check s456

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-check-s456_20260515T161959_result.json`
- **Structured JSON:** [`b23fe9afe459c85b5bed.json`](../../sessions/b2/b23fe9afe459c85b5bed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| cuda:0 | 0%（瞬时） | 18.3/97.9 GB | BCE eval 链：bce_s42→**bce_s123**(进行中)→bce_s456 |
| cuda:1 | 100% | 67.6/97.9 GB | **mvp_kl_norm_v2_s456 训练** |

**s456 训练进度**：Step **630**/1000（63%），PID 74992 运行中
- loss ≈ 0.27-0.30，sparsity ≈ 0.48-0.50（接近目标 0.5）
- tau 从 0.694 降到 0.433，lr 从 8.35e-4 降到 3.62e-4
- constraint 偶发触发（~0.012），大部分步数为 0

**空闲 GPU**：无。两张卡都在工作。cuda:0 上 eval 完成后会空出来。

---
