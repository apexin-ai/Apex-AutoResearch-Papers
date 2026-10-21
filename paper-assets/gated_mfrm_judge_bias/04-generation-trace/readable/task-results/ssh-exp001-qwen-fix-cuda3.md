# ssh exp001 qwen fix cuda3

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp001_qwen_fix_cuda3_20260522T025909_result.json`
- **Structured JSON:** [`0af4865fc28eaf99c4c5.json`](../../sessions/0a/0af4865fc28eaf99c4c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

主 config.yaml 端口已修正（llama→8001, qwen→8002）。

## 汇总

**模型状态**：Qwen2.5-72B-Instruct-AWQ 11/11 分片完整（每片 2.4-3.8GB），无 `.incomplete` 文件，无需修复。

**vLLM 部署**：
| GPU | 模型 | 端口 | 状态 |
|-----|------|------|------|
| GPU 2 | Llama-3.3-70B-Instruct-AWQ | 8001 | 运行中 (tmux: vllm-llama) |
| GPU 3 | Qwen2.5-72B-Instruct-AWQ | 8002 | 运行中 (后台进程) |

**数据收集**：
- **Llama 收集** (tmux: `exp001-llama`)：arena_hard pairwise，已产出 ~46 条 judgment，持续运行中
- **Qwen 收集** (tmux: `exp001-qwen`)：刚启动，已产出首条 Qwen judgment，确认端口 8002 通信正常
- 每个 judge 需完成 500 prompts × 3 target models × 2 positions = 3000 条
- 两个 judge 共写入同一 `arena_hard_judgments.jsonl`，通过 judge 字段区分

**已修复**：
- 主 config.yaml 端口配置：llama 8000→8001，qwen 8001→8002
- 创建了 `config_qwen_arena.yaml`，`model_name` 设为 vLLM 实际 served name `qwen2.5-72b-instruct`

---
