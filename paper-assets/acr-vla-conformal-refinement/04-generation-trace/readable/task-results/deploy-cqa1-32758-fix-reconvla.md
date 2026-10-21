# deploy cqa1 32758 fix reconvla

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-32758-fix-reconvla_20260523T081343_result.json`
- **Structured JSON:** [`9ca595a4bce4da585e61.json`](../../sessions/9c/9ca595a4bce4da585e61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报：

### 结果

**1. 3 个 s44 实验已杀掉** — k2mean_spatial_s44, k2mean_object_s44, k2mean_goal_s44 全部终止。

**2. 3 个 Reconvla 实验已启动并正常运行：**

| Session | GPU | Python PID | tmux PID | 状态 |
|---------|-----|-----------|----------|------|
| eval-supp-reconvla-spatial-s43 | 1 | 34387 | 34363 | 10 tasks loaded, running |
| eval-supp-reconvla-spatial-s44 | 3 | 34383 | 34368 | 10 tasks loaded, running |
| eval-supp-goal-reconvla-s43 | 5 | 34385 | 34373 | 10 tasks loaded, running |

**3. 6 张卡全部在用：**
- GPU 0: k2mean_spatial_s43 (6453MiB)
- GPU 1: reconvla-spatial-s43 (6481MiB)
- GPU 2: k2mean_object_s43 (5877MiB)
- GPU 3: reconvla-spatial-s44 (6481MiB)
- GPU 4: k2mean_goal_s43 (5755MiB)
- GPU 5: goal-reconvla-s43 (5783MiB)

**4. 无报错** — 3 个 reconvla 实验无需 `--crm_checkpoint`，模型加载正常，环境已开始评估。

注：首次启动时 `CUDA_VISIBLE_DEVICES` 放在 tmux 外部没有传入 session，导致 3 个进程全跑到 GPU 0。已修复为在 `bash -c` 内部 export，GPU 分配正确。

---
