# ssh deploy fix start rgds v3

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-fix-start-rgds-v3_20260512T123235_result.json`
- **Structured JSON:** [`73a2081b36696d4d5125.json`](../../sessions/73/73a2081b36696d4d5125.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验运行正常。汇报：

**GPU 清理**：无残留实验进程。GPU 0 有 ~49GB 僵尸显存（无法 reset），剩余空间足够。

**代码部署**：
- `diversity_selection.py` — 已部署（含 PCA 对齐修复）
- `analyze_mvp.py` — 已部署

**实验启动**：
- PID: 18588
- 方法: `rgds`，双卡模式 `--gpu_ids 0,1`
- Gen-0 RankMe baseline: **983.21**
- Student 模型 Qwen3-1.7B 已加载 → GPU 1: **21633 MiB**
- Generator 模型 Qwen3-4B 已加载 → GPU 0: **58655 MiB**（含 49GB 旧残留 + ~9.5GB generator）
- gen_0 目录已创建，实验进入第一轮生成阶段

---
