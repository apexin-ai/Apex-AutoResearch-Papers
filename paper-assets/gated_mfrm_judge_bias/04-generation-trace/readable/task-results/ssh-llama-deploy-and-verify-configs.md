# ssh llama deploy and verify configs

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama_deploy_and_verify_configs_20260524T013458_result.json`
- **Structured JSON:** [`9cc30f041ec692145ff8.json`](../../sessions/9c/9cc30f041ec692145ff8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇总报告

### 任务 A: LLaMA vLLM 部署

| 步骤 | 状态 |
|------|------|
| A1 模型下载 | 9 safetensors, 0 incomplete, config.json 存在 |
| A2 cuda:1 | 空闲 → 已占用 42865 MiB |
| A3 vLLM 部署 | PID 502063, 端口 8001, HTTP 200 健康 |
| A5 Config | 已重写为正确格式（`benchmarks` key + `base_url: http://localhost:8001` + `model_name: /root/autodl-tmp/models/Llama-3.3-70B-Instruct-AWQ/`） |
| A6 Response 文件 | 全部 18 个模型存在（平铺格式 `{model}.jsonl`，非子目录格式） |
| A7 collect.py | PID 503734, 18000 total judgments, 已产出 3 条，持续运行中 |

**注意**：你提供的 config 格式与 `collect.py` 不匹配（缺少 `benchmarks` key），已自动修正为正确格式。

### 任务 B: API judges configs 验证

4 个 config 文件位于 `/root/gated_mfrm_judge_bias/exp001/`（不在 `configs/` 子目录），**target_models 全部精确匹配 18 个模型名**，无拼写差异。

| Config | target_models | 进度 |
|--------|--------------|------|
| claude-sonnet-4.6-proxy | 18/18 匹配 | 1830/18000 |
| gemini-2.5-pro-proxy | 18/18 匹配 | 1118/18000 |
| deepseek-v4-pro-proxy | 18/18 匹配 | 905/18000 |
| qwen3-235b-proxy | 18/18 匹配 | 1061/18000 |

### 任务 C: Qwen 下载

**已完成。** 11 safetensors, 39GB, `/root/autodl-tmp/models/Qwen/Qwen2.5-72B-Instruct-AWQ/`。日志显示 `DOWNLOAD_COMPLETE`。

---
