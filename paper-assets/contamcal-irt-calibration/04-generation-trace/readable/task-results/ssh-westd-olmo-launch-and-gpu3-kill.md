# ssh westd olmo launch and gpu3 kill

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-olmo-launch-and-gpu3-kill_20260519T115322_result.json`
- **Structured JSON:** [`2759edbdd93f9cecb234.json`](../../sessions/27/2759edbdd93f9cecb234.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终状态报告

### GPU 3 冲突 — 已解除
- 杀死 PID 147606（`phase2_eval_gpu3.sh` 的 bash 进程），阻止 OLMo 自动启动
- gemma-2 d100 eval (PID 159883) 继续运行，不受影响

### OLMo eval 启动情况
| GPU | 状态 | 任务 |
|-----|------|------|
| cuda:2 | **已启动** olmo2_d100 | tmux session `olmo2_gpu2`，MMLU 评估进行中 |
| cuda:0 | **忙** — phi-4 d100 eval | 完成后才能启动 olmo2_d000+d005 |
| cuda:1 | **忙** — qwen14b d050 eval（后面还有 d100） | 完成后才能启动 olmo2_d025+d050 |

### eval_results_v2/ 已完成目录
**完成（有 results）**：gemma2_d000/d005/d025/d050, phi4_d000/d005/d025/d050, qwen14b_d000/d005/d025, qwen7b_d000/d005/d025/d050/d100

**进行中**：gemma2_d100 (GPU 3), qwen14b_d050 (GPU 1), phi4_d100 (GPU 0), olmo2_d100 (GPU 2)

### 待办
GPU 0/1 空闲后需手动启动：
- `tmux new-session -d -s olmo2_gpu0 'bash /root/contamcal-irt-calibration/exp001/olmo2_eval_gpu0.sh'`（d000+d005）
- `tmux new-session -d -s olmo2_gpu1 'bash /root/contamcal-irt-calibration/exp001/olmo2_eval_gpu1.sh'`（d025+d050）

---
