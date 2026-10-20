# ssh check autodl cuda123

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_autodl_cuda123_20260522T173820_result.json`
- **Structured JSON:** [`c62798f7b142794d25b7.json`](../../sessions/c6/c62798f7b142794d25b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 状态
| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| 0 | 0% | 0 MiB | 97,887 MiB |
| 1 | 0% | 0 MiB | 97,887 MiB |
| 2 | 0% | 0 MiB | 97,887 MiB |
| 3 | 0% | 0 MiB | 97,887 MiB |

**cuda:1/2/3 全部空闲。** 之前的 vLLM judge 评估已结束，无任何 GPU 进程。

### orchestrator2 状态
`run_remaining.sh`（exp001 小模型生成）仍在 tmux 中运行，但不占 GPU：
- **Llama-3.1-8B**: 已完成 (500/500)，进程已退出
- **Qwen2.5-7B**: 模型下载**卡住** — safetensors 文件数为 0，只有 config/tokenizer。脚本在 `wait_for_model` 循环里 sleep 30
- **Mistral-7B-v0.3**: 模型已下载完成 (3/3 safetensors)，但脚本逻辑是串行等待，要等 Qwen 先跑完

### exp-004 可行性
- `/root/gated_mfrm_judge_bias/exp004/` **不存在**，代码还未部署到服务器
- GPU 完全空闲，可以直接使用 cuda:1/2/3 跑 exp-004（包括 MCMC 方法）

### 需要决策
1. **Qwen2.5-7B 下载问题**：下载似乎挂了（只有元数据文件没有权重），orchestrator2 会无限等待。需要排查下载源或手动重新下载
2. **exp-004 部署**：需要先把 exp004 代码推到服务器，才能运行

---
