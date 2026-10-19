# infra fix resource issues

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-resource-issues_20260522T050530_result.json`
- **Structured JSON:** [`18a1b76b04f6661ae8c9.json`](../../sessions/18/18a1b76b04f6661ae8c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成。

---

## 产出报告

### Step 1: Kill 重复 probe 进程
- **PID 83019** — 已 kill (force_killed)
- **PID 83810** — 已 kill (force_killed)
- 存活进程确认：PID 82559 (bootstrap n=2000) ✓、PID 84295 (run_probes.sh) ✓

### Step 2: Gemma translate 修复
- 进度：**150/1274 (11.8%)**，< 50%，决策：kill 重启
- Bug 确认：外层 `CUDA_VISIBLE_DEVICES=1` 被内层 `bash -c` 中的 `CUDA_VISIBLE_DEVICES=0` 覆盖
- 旧进程已全部清除（包括 kill_job 未杀干净的孤儿进程 79665 等）
- 新进程 PID 85171 已启动，`CUDA_VISIBLE_DEVICES=1`，从 checkpoint 150/1274 恢复
- 运行在 tmux session `gemma_translate_zh`

### Step 3: GPU 状态快照

| GPU | 显存占用 | 利用率 | 用途 |
|-----|---------|--------|------|
| 0 | 16529 / 97887 MiB | 23% | probe 训练 |
| 1 | 16421 / 97887 MiB | 23% | **Gemma translate（已修复）** |
| 2 | 16529 / 97887 MiB | 21% | 其他任务 |
| 3 | 0 / 97887 MiB | 0% | 空闲 |

GPU 0 显存从之前的 33GB 降到 16.5GB（释放了旧 translate 占用的 ~16.5GB）。

---
