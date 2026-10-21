# check gemma and gpu status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gemma_and_gpu_status_20260520T073127_result.json`
- **Structured JSON:** [`cfd1d9a035db6c4e3a4b.json`](../../sessions/cf/cfd1d9a035db6c4e3a4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### Gemma 实验 (`exp_gemma2b_depth`)
| 项目 | 状态 |
|------|------|
| tmux session | **运行中** (14:34 启动) |
| 主 PID | 289968 (`run_pipeline.py`) |
| 当前进度 | **depth 2: 142/313 (45%)** |
| 速度 | ~5.5s/it |
| 预估剩余 | depth 2 剩 ~171 steps ≈ **16 min**；之后还有 depth 3-5 |
| GPU | cuda:0 |
| 参数 | gemma-2-2b, 5000 samples, max_depth=5, scorer=Qwen2.5-1.5B |

### GPU 状态
| GPU | 利用率 | 显存 | 占用进程 |
|-----|--------|------|----------|
| **0** | 71% | 6,357 / 24,564 MiB | `run_pipeline.py` (Gemma 实验) |
| **1** | 0% | 0 / 24,564 MiB | 空闲 |
| **2** | 37% | 8,679 / 24,564 MiB | `run_multi_source_unified_scorer.py` (15:24 启动) |
| **3** | 0% | 0 / 24,564 MiB | 空闲 |

### Code DeBERTa (`exp_deberta_code_qwen1b5`)
| 项目 | 状态 |
|------|------|
| tmux session | **已退出** (exit code 127) |
| 退出时间 | 2026-05-20T07:28:47Z |
| 失败原因 | **`bash: line 1: python: command not found`** |
| 根因 | 启动脚本中用了 `python` 而非 `python3`，且未激活 conda 环境（conda activate 在 `&&` 链中，但 `python` 命令找不到说明 PATH 未正确设置） |

### 额外发现
- GPU 2 上运行着 `run_multi_source_unified_scorer.py`（15:24 启动，非本次任务提交）
- `lofo_importance.py` 有多个子进程在后台运行（02:52 启动，CPU 占用近 0，可能已完成或卡住）

DeBERTa 实验需要修复启动命令后重新提交。

---
