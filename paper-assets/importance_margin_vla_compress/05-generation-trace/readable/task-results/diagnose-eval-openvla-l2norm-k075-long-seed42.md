# diagnose eval openvla l2norm k075 long seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_l2norm_k075_long_seed42_20260527T013659_result.json`
- **Structured JSON:** [`eedcf9ab0edaf4ee9178.json`](../../sessions/ee/eedcf9ab0edaf4ee9178.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

### 进度
- **完成 420/500 episodes (84%)**
- 8 个 task 已完成 (Task 1-8)，Task 9 跑到 Ep 20/50 时被 timeout 杀掉
- 剩余：Task 9 的 30 episodes + Task 10 的 50 episodes = 80 episodes

### 原因
**纯超时，无任何异常。** 无 OOM、无 error、无 traceback、无卡住迹象。全程稳定 0.9 eps/min。

### 时间分析
- 实验启动：01:30，被杀：09:30（北京时间），总运行 **8 小时 (480 min)**
- 参考：同服务器 `l2norm_k05` 完成全部 500 episodes 耗时 **666.6 min (11.1h)**
- 本实验 k=0.75（保留更多 token），速度略快（0.9 vs 0.7-0.8 eps/min）
- 预估总耗时：420 episodes / 480 min = 0.875 eps/min → 500 episodes 需 ~571 min ≈ **9.5h**
- **timeout 设了 8h，差约 1.5h**

### 已完成 Task 的成绩（可用）
| Task | SR |
|------|-----|
| 1 | 0.460 |
| 2 | 0.480 |
| 3 | 0.480 |
| 4 | 0.140 |
| 5 | 0.140 |
| 6 | 0.680 |
| 7 | 0.300 |
| 8 | 0.460 |

### 建议
重新提交时 timeout 调到 **10-11h**，或只跑剩余的 Task 9-10（如果脚本支持 `--start_task` 之类的参数）。无需修复任何代码问题。

---
