# check gpu 5090 4x 2 status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-5090-4x-2-status_20260514T133129_result.json`
- **Structured JSON:** [`6fac56f4446299dd033b.json`](../../sessions/6f/6fac56f4446299dd033b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## gpu-5090-4x-2 服务器状态

### GPU 状态（4x RTX 5090 32GB）

| GPU | 显存占用 | GPU利用率 | 状态 |
|-----|---------|----------|------|
| 0 | 30202/32607 MiB | 82% | **占用** — exp001_seed456 |
| 1 | 2/32607 MiB | 0% | **空闲** |
| 2 | 30154/32607 MiB | 89% | **占用** — exp001_seed123 |
| 3 | 30166/32607 MiB | 85% | **占用** — exp008_re_n16 |

### 运行中的训练任务（3个 tmux session）

| Session | GPU | 命令 | 模型 | 数据集 |
|---------|-----|------|------|--------|
| exp001_seed456 | GPU 0 | `run_mvp_pilot.py` | qwen3-8b-scierc-merged-v2 | scierc/joint, n=16, seed=456 |
| exp001_seed123 | GPU 2 | `run_mvp_pilot.py` | qwen3-8b-scierc-merged-v2 | scierc/joint, n=16, seed=123 |
| exp008_re_n16 | GPU 3 | `run_mvp_pilot.py` | qwen3-8b-scierc-merged-v2 | scierc/joint, n=16, seed=42 |

三个任务均启动于 21:27，运行约 5 分钟，各自带有 VLLM::EngineCore 进程。

### 项目环境

- **代码**：就绪，`code/` 下有完整脚本
- **数据**：就绪，`data/` 目录存在
- **Checkpoints**：9 个模型目录（qwen3-8b 多版本 + llama3.1-8b）
- **磁盘**：250GB 中已用 107GB，剩余 144GB（43%），充足
- **输出**：`output/` 目录已有 27 个子目录

### 结论

服务器正常运行，3/4 GPU 正在跑 scierc joint 实验（不同 seed 的重复实验）。**GPU 1 空闲可用。**

---
