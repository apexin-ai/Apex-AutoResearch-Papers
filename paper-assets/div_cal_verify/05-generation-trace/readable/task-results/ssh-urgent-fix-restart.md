# ssh urgent fix restart

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-fix-restart_20260512T144627_result.json`
- **Structured JSON:** [`5bbba0810291a0a8e9fa.json`](../../sessions/5b/5bbba0810291a0a8e9fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正在运行，模型加载完成。

**汇报：**

| 项目 | 状态 |
|------|------|
| Kill 结果 | 原 PID 42073/42079 已 kill，追杀了 44902（external_only）、42074+45088（bash+uncurated），全部清理干净 |
| 软链接状态 | **已生效**：`./results` → `/root/autodl-tmp/div_cal_verify/results/`，之前数据实际写在数据盘。但 run_all_methods.sh 现已改为显式路径，不再依赖软链接 |
| run_mvp.py patch | 成功，第 245 行插入 checkpoint 清理逻辑 |
| 新实验 PID | 45398（rgds 方法），父 bash PID 45390 |
| GPU 使用 | GPU 0: 49175 MiB（student model），GPU 1: 21633 MiB / 100% util（generator 正在生成） |
| 磁盘 | 根分区 21G/30G (68%)，数据盘 250G 几乎全空 |

---
