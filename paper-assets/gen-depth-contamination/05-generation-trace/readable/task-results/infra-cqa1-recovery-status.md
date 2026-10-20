# infra cqa1 recovery status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cqa1-recovery-status_20260519T215644_result.json`
- **Structured JSON:** [`9135c5c8e72bb05420ff.json`](../../sessions/91/9135c5c8e72bb05420ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 任务 1：实验存活状态

| 进程 | PID | 状态 | 进度 |
|------|-----|------|------|
| Wiki DeBERTa upperbound | 167144 | **已完成** | 5/5 实验全部完成，summary.json 已生成 |
| Cross-transfer GPU1 | 208306 | **存活** (1h40m) | 1/4 对完成 (wiki_pythia→wiki_olmo)，正跑第2对 |
| Cross-transfer GPU2 | 208307 | **存活** (1h40m) | 1/4 对完成 (wiki_olmo→wiki_qwen7b)，正跑第2对 |
| Cross-transfer GPU3 | 208308 | **存活** (1h40m) | 1/4 对完成 (wiki_olmo→wiki_llama8b)，第2对接近完成 |

每对约 55-60 分钟，每 GPU 剩 3 对，预计 cross-transfer 全部完成时间：**~09:00-09:30**。

### GPU 状态

| GPU | 占用 | 显存 | 任务 |
|-----|------|------|------|
| 0 | 97% | 19337/24564 MiB | **C4 1.5B DeBERTa qwen_rw** (刚启动) |
| 1 | 96% | 21213/24564 MiB | cross-transfer |
| 2 | 98% | 19665/24564 MiB | cross-transfer |
| 3 | 98% | 22635/24564 MiB | cross-transfer |

### 任务 4：C4 1.5B DeBERTa 部署

- 脚本 `run_deberta_c4_1b5.py` 已创建并部署，支持 `--config` 参数
- **qwen_rw** 已在 GPU 0 启动（PID 255066），预计 ~45 分钟完成
- **pythia_greedy** 和 **qwen_cont256** 暂无空闲 GPU，需等待：
  - 方案 A：qwen_rw 完成后在 GPU 0 上串行跑（总计 ~2.5h）
  - 方案 B：等 cross-transfer 释放 GPU 1-3 后并行跑（~3h 后可用）

建议在 qwen_rw 完成后立即在 GPU 0 上启动下一个 config，同时等 cross-transfer 释放 GPU 时启动第三个。

---
