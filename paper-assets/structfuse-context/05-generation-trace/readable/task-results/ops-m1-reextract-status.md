# ops m1 reextract status

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m1-reextract-status_20260515T204103_result.json`
- **Structured JSON:** [`0297529ba2b8edc58cd3.json`](../../sessions/02/0297529ba2b8edc58cd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 进程
提取进程仍在运行：主进程 PID 209821 + 4 个 worker（209824-209827），自 May 14 起持续运行。

### Project-MONAI/MONAI — **已完成** ✓
- 524/524 instances 全部处理完毕
- 04:29 清理了 CodeQL 数据库，标志提取结束
- 输出 527 个 json 文件

### getmoto/moto — **进行中**
- 当前进度：**200/536** (37.3%)，最近一次进度更新 02:48 (May 16)
- 速率：~50 instances / 4.25h ≈ 12/hr
- 剩余 336 instances，**预计还需 ~28 小时**（约 May 17 07:00 完成）
- 问题：**每个 instance 的 CodeQL call_graph.ql 都 timeout（exit code 33）**，但提取仍继续（只是没有 call graph 数据）
- 当前输出 225 个 json 文件

### 数据总量
| 指标 | 数值 |
|------|------|
| 总 json 文件 | **43,858** |
| 总 instances | 44,173 |
| MONAI 新增 | +527 (从 481 → 完整 524) |
| moto 当前 | 225 文件 (200/536 processed) |

### 磁盘
`/root/autodl-tmp/`: 165G used / 250G total (85G 可用, 66%)，空间充足。

### 合并判断
- MONAI 已完成，可以合入
- moto 仍需 ~28h，且 CodeQL call_graph 全部 timeout——所有 moto instance 的 structural data 将缺少 call graph
- **可选方案**：不等 moto 完成，现在用已有 43,858 个 json 执行合并（比 dry-run 的 39,712 已多出约 4,146 个），moto 剩余的 ~336 个后续补跑

---
