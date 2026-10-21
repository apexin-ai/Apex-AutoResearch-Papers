# code plan 010 download cleanup

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_010_download_cleanup_20260516T045835_result.json`
- **Structured JSON:** [`95120a55ca435f5432b2.json`](../../sessions/95/95120a55ca435f5432b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

## 报告

### 磁盘清理
删除了 4 个 instruction ablation 实验产物目录，释放 **~90 GB**：
| 目录 | 大小 |
|------|------|
| `trained_libero_goal_no_inst/` | 18G |
| `trained_libero_goal_random_s0/` | 25G |
| `trained_libero_goal_shuffled/` | 25G |
| `untrained_libero_goal_no_inst/` | 24G |

### LIBERO-Spatial 数据
- **10 tasks**，每 task **50 demos**，共 **500 demos**
- 总大小：**5.9 GB**
- 路径：`/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/`
- 数据源：`yifengzhu-hf/LIBERO-datasets`（hf-mirror.com 无代理直连）

### 当前磁盘状态
- 总容量：250G
- 已用：113G
- **可用：138G（46% 使用率）**

### 两路并行 extraction 空间评估
需要 ~50 GB，当前剩余 138 GB — **空间充足**。

---
