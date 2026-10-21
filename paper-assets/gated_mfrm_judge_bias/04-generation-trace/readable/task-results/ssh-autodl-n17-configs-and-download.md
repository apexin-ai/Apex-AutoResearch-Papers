# ssh autodl n17 configs and download

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_n17_configs_and_download_20260523T225131_result.json`
- **Structured JSON:** [`996064f10ae049923fa7.json`](../../sessions/99/996064f10ae049923fa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 产出报告

**任务 1: N=17 configs — 完成**

4 个文件已生成在 `/root/gated_mfrm_judge_bias/exp001/`：
| 文件 | Judge | Target Models |
|------|-------|--------------|
| `config_claude-sonnet-4.6-proxy_arena_n17.yaml` | claude-sonnet-4.6-proxy | 18 个 |
| `config_gemini-2.5-pro-proxy_arena_n17.yaml` | gemini-2.5-pro-proxy | 18 个 |
| `config_deepseek-v4-pro-proxy_arena_n17.yaml` | deepseek-v4-pro-proxy | 18 个 |
| `config_qwen3-235b-proxy_arena_n17.yaml` | qwen3-235b-proxy | 18 个 |

每个 config 的 `output_dir` 已加 `_n17/` 后缀以区分结果。其他配置（proxy、rpm=30、position_swap、max_retries）保持不变。

**任务 2: LLaMA-3.3-70B-AWQ 下载 — 进行中**

- 仓库：`casperhansen/Llama-3.3-70B-Instruct-AWQ`（原始 `LLM-Research` 在 ModelScope 不存在，`hugging-quants` 需要 token，改用 casperhansen 社区版本）
- PID: 478762
- 进度：1/17 文件，已下载 397MB
- 目标路径：`/root/autodl-tmp/models/Llama-3.3-70B-Instruct-AWQ/`
- 预估大小：AWQ INT4 量化约 **36-38GB**
- 预估时间：AutoDL 代理下载 HF 速度不稳定，无 token 限速，预计 **30-60 分钟**

> 注意：服务器未配置 HF_TOKEN，下载速率受限。如需加速可设置 token：`huggingface-cli login`。

---
