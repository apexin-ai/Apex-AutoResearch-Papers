# ops exp006 gpu status check

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp006_gpu_status_check_20260521T070349_result.json`
- **Structured JSON:** [`52b2b45f56f86c5f722b.json`](../../sessions/52/52b2b45f56f86c5f722b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. GPU 状态
| GPU | Memory Used | Memory Total | Util |
|-----|------------|-------------|------|
| 0 | 0 MiB | 97887 MiB | 0% |
| 1 | 0 MiB | 97887 MiB | 0% |
| 2 | 88359 MiB | 97887 MiB | 0% |
| 3 | 0 MiB | 97887 MiB | 0% |

GPU 2 被 vLLM 占用（~90GB），其余 3 张空闲。

### 2. vLLM
**运行中** — PID 114905, Qwen3-32B on port 8002, 已运行 1h10m。当前 **空闲**（Running: 0 reqs），最后一批请求在 14:42:18 结束，之后吞吐量降至 0。

### 3. CF Gen
**已完成** — PID 115974 已退出。`counterfactuals_scaled_formality.jsonl` 有 **400/400 行**，全部生成完毕。

所有 CF 文件汇总：
| 文件 | 行数 |
|------|------|
| counterfactuals_32b.jsonl | 100 |
| counterfactuals_alpacaeval.jsonl | 100 |
| counterfactuals_mtbench.jsonl | 80 |
| counterfactuals_register.jsonl | 100 |
| counterfactuals_register_pilot.jsonl | 20 |
| counterfactuals_scaled_formality.jsonl | **400** |
| counterfactuals_tone_pilot.jsonl | 20 |
| counterfactuals_verbosity.jsonl | 100 |

### 4. Tmux Sessions
无法检查（`tmux` 被 ssh_read_only 阻止）。

### 5. 磁盘
| 分区 | 已用 | 总量 | 使用率 |
|------|------|------|--------|
| / (root) | 17G | 30G | **54%** |
| /root/autodl-tmp | 98G | 250G | **39%** |

**结论：exp-006 CF 生成已完成（400/400），vLLM 仍在运行但空闲，可以释放 GPU 2。**

---
