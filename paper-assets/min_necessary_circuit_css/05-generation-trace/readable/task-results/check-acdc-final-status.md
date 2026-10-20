# check acdc final status

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_acdc-final-status_20260512T165154_result.json`
- **Structured JSON:** [`3a7c6b205b38a468749a.json`](../../sessions/3a/3a7c6b205b38a468749a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

---

## MVP ACDC 进程状态

### 进程
- **PID 98594: 存活**，已运行 3h54m，CPU 100%，内存 0.2%
- 工作目录: `/root/min_necessary_circuit_css`（不是 `/root/structfuse-mvp/`）
- 日志输出: `/root/min_necessary_circuit_css/mvp_output.log`（6.0MB，54926 行）

### GPU
- cuda:5 利用率 **99%**，显存 9311 MiB / 24564 MiB

### 整体流程进度
三阶段流水线：EAP-IG → Edge Pruning → ACDC

| 阶段 | 状态 | 耗时 |
|------|------|------|
| Phase A: EAP-IG | **完成** ✓ | ~9s，32491 edges scored |
| Phase B: Edge Pruning | **完成** ✓ | ~21s，32491 edges scored |
| Phase C: ACDC | **进行中** | 已跑 ~3h50m |

### ACDC 进度（从 tqdm 解读）
- 当前阈值: τ=0.01（第 1/5 个阈值）
- 边剪枝进度: **5239 / 32491 = 16.1%**
- 速度: ~24.3 it/s
- 已移除 5220 条边，剩余 19 条活跃边
- 预计当前阈值剩余时间: ~18m42s
- 还有 4 个阈值要跑，**总体预计还需数小时**

### 缓存文件
| 文件 | 大小 | 时间 |
|------|------|------|
| cache_eap_ig.json | 1.3M | May 12 21:04 |
| cache_edge_pruning.json | 1.3M | May 12 20:59 |
| mvp_output.log | 6.0M | May 13 00:52 |
| mvp_output_killed.log | 1.9M | May 12 19:53（上一次被 kill 的运行） |

### mvp_results.json
**不存在** — 正常，ACDC 还在跑。结果文件应该在全部 5 个阈值跑完后生成。

---
