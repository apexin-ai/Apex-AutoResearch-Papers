# infra gpu check both servers

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu_check_both_servers_20260520T030822_result.json`
- **Structured JSON:** [`d9822c94ac52a51ee36f.json`](../../sessions/d9/d9822c94ac52a51ee36f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### westd-41312 (4× RTX PRO 6000 Blackwell, 96GB each)

| GPU | 显存占用 | GPU利用率 | 温度 |
|-----|---------|----------|------|
| 0 | 561 / 97887 MiB | 0% | 35°C |
| 1 | 7435 / 97887 MiB | 12% | 37°C |
| 2 | 1317 / 97887 MiB | 12% | 39°C |
| 3 | 1639 / 97887 MiB | 20% | 45°C |

**活跃进程**: 1 个 python 进程 (PID 374939) 占用全部 4 张卡（GPU1 占用最多 7.4GB）
**tmux**: 无 session
**`adaptive_fromscratch_seed42` / `pretrain_weighted`**: **未在运行**（ps grep 无结果，exit code 1）

> PID 374939 占用显存不大且 GPU 利用率低，可能是一个空闲的 Python 进程或刚结束的残留。

### westd-30476 (4× RTX PRO 6000 Blackwell, 96GB each)

| GPU | 显存占用 | GPU利用率 | 温度 |
|-----|---------|----------|------|
| 0 | 0 / 97887 MiB | 0% | 30°C |
| 1 | 0 / 97887 MiB | 0% | 30°C |
| 2 | 0 / 97887 MiB | 0% | 30°C |
| 3 | 0 / 97887 MiB | 0% | 30°C |

**活跃进程**: 无
**tmux**: 无 session
**状态**: 完全空闲

### 特别检查结果

| 检查项 | 结果 |
|--------|------|
| `adaptive_fromscratch_seed42` 在跑？ | **否** — 无匹配进程 |
| rho06 checkpoint | **存在** — `/root/autodl-tmp/.../hybrid_rho06_seed42/final/config.json` (May 17) |
| 训练脚本 | **存在** — `pretrain_weighted.py` (19KB, May 17) |
| ρ=0.6 数据文件 | **存在** — 符号链接 → `scored_data_60.jsonl`，**371,499 行** |

---
