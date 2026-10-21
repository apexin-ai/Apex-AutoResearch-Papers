# diagnose recent failures gpu check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_recent-failures-gpu-check_20260519T143732_result.json`
- **Structured JSON:** [`4815037ba4298b33e04b.json`](../../sessions/48/4815037ba4298b33e04b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### 5 个失败实验：统一根因

全部是 **startup recovery 清理**：实验注册到 registry 后从未实际部署（无进程、无 tmux、无日志），在 14:00-14:32 的恢复扫描中被标记为 failed。

**已全部重新启动**，当前正在运行：

| 实验 | 重部署位置 | 进度 |
|------|-----------|------|
| obs-only-spatial-k5-seed44 | bjb2-28827 | 4/10 tasks |
| obs-only-spatial-k5-seed45 | bjb2-28827 | 4/10 tasks |
| random-selection-k5-seed43 | bjb2-28827 | 3/10 tasks |
| random-selection-k5-seed44 | bjb1-32546 | 3/10 tasks |
| random-selection-k5-seed45 | bjb1-32546 | 3/10 tasks |

### GPU 共享状态

**bjb1-32546 cuda:4** — 正常。82% 利用率，显存仅用 16%，两实验都在 task 8/10，互不干扰。

**bjb2-40593 cuda:0** — 有瓶颈。99% compute 饱和，但两实验已过半（task 7/10 和 5/10），不建议中断，等自然完成。

### 空闲资源

- **bjb2-28827 cuda:3** — 完全空闲
- **bjb1-32546 cuda:1** — 完全空闲

报告已注册为 artifact：`art_20260519_912264`。

---
