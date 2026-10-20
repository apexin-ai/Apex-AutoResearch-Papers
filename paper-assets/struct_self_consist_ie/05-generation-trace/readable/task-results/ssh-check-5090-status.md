# ssh check 5090 status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_5090_status_20260521T182033_result.json`
- **Structured JSON:** [`20d0fa1c2db657943662.json`](../../sessions/20/20d0fa1c2db657943662.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## 实验状态汇总

### 1. 5-epoch s42 推理
- **状态: 运行中** (PID 63198, 启动 ~25 分钟)
- GPU: cuda:1
- 进度: **19% (57352/301184 prompts)**，n_samples=8 → 301184 = 37648×8
- 预计剩余: ~1.5 小时
- 输出目录存在但 samples.jsonl 尚未写入（推理完成后才写）

### 2. 5-epoch s123 推理
- **状态: 运行中** (PID 63337, 启动 ~25 分钟)
- GPU: cuda:2
- 进度: **19% (56264/301184 prompts)**
- 预计剩余: ~1.5 小时
- 同上，samples.jsonl 尚未写入

### 3. fewnerd_n16_s456 (Qwen3-8B finetuned, n=16)
- **状态: 运行中** (PID 54277, 启动 ~3 小时)
- GPU: cuda:0
- 进度: **81% (488592/602368 prompts)**，n_samples=16 → 602368 = 37648×16
- 预计剩余: ~40 分钟
- 注意：输出目录是 `fewnerd_n16_s456`（不是 `_v2`）

### 4. e2_pretrained_fewnerd_s456 (Qwen2.5-7B pretrained, n=8)
- **状态: 运行中** (PID 47635, 启动 ~4 小时)
- GPU: cuda:3
- 进度: **82% (247824/301184 prompts)**，n_samples=8 → 301184 = 37648×8
- 预计剩余: ~50 分钟
- 输出目录为空（同样是完成后写入）

### 5. GPU 使用情况
| GPU | 型号 | 利用率 | 显存使用 |
|-----|------|--------|---------|
| 0 | RTX 5090 | 72% | 30152/32607 MiB |
| 1 | RTX 5090 | 82% | 30222/32607 MiB |
| 2 | RTX 5090 | 89% | 30194/32607 MiB |
| 3 | RTX 5090 | 77% | 29946/32607 MiB |

### 6. exp_028_fewnerd_5epoch (旧的 5-epoch 实验)
- 已完成，有 samples.jsonl，但只有 **5000 行**（不是 37648），可能是早期的 pilot 或子集运行

### 结论
- **4 个 GPU 全满载**，每个各跑一个推理任务
- 5-epoch s42/s123 **不是已完成被误报 failed**——它们是刚启动约 25 分钟的新进程，目前 19% 进度
- fewnerd_n16_s456 和 e2_pretrained_fewnerd_s456 都在 ~82%，约 40-50 分钟完成
- `fewnerd_n16_s456_v2` 目录不存在——实际运行的输出目录是 `fewnerd_n16_s456`

---
