# ssh autodl llama judge check and orchestrator fix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_llama_judge_check_and_orchestrator_fix_20260522T112034_result.json`
- **Structured JSON:** [`0a5b791b096a47516063.json`](../../sessions/0a/0a5b791b096a47516063.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 任务 A：Llama-3.3-70B judge 数据

**实际数量** — 不是 296，是 **233**：

| 文件 | 行数 | 内容 |
|---|---|---|
| `exp001/results/llama-3.3-70b/arena_hard_judgments.jsonl` | **233** | 全部 llama-3.3-70b judge |
| `exp001/results/arena_hard_judgments.jsonl`（聚合文件） | 296 | 混合 3 judges：llama-3.3-70b ×173、qwen2.5-72b ×89、mistral-large-2 ×34 |

用户提到的 296 是**聚合文件**（混合 3 个 judge）；llama 单独文件实际是 233 条，最新更新到 15:01:45。

**target_models — 仍是旧的 3 个模型**（不是 7 个）：

```
config_llama_arena.yaml / config_qwen_arena.yaml / config_mistral_arena.yaml
target_models:
  - gpt-3.5-turbo-0125
  - gpt-4-0314
  - gpt-4-0613
```

实际 judgment 文件 model_a / model_b 列也只出现这 3 个，配对：(3.5 vs 4-0314) 78、(4-0314 vs 4-0314) 78、(4-0613 vs 4-0314) 77。

**proxy 配置同样只有 3 个旧模型**（如 `config_claude-opus-4.7-proxy_arena.yaml`），但 `exp001/config.yaml` 主配置已扩到 22 个 target_models 全集。

**结论**：autodl-8gpu 上的 Llama judge 仅覆盖旧 3 模型，**需要更新 config 为 7 模型**才能与 rtx6000-4x 对齐。
- 若 rtx6000-4x 上 llama judge 用的也是 3 模型相同 prompts，则**与本机 233 条完全重复**，不能直接合并（属于复跑）。
- 若 rtx6000-4x 已扩到 7 模型，则两边**目标不同**，可以保留本机 233 条作为子集 + 对方补完。

### 任务 B：编排脚本

**位置**：`/root/gated_mfrm_judge_bias/exp001/run_remaining.sh`（tmux session `orchestrator2` 中运行）。

**当前模式 — 已经是"下完一个跑一个"** ✅：
- `wait_for_model()` 轮询 safetensors 文件数 == index.json 期望数 且 `._____temp/` 为空 → 视为下载完成
- 完成后立即在指定 GPU 上后台启动 `generate_vllm_batch.py`（`&`），不阻塞下个模型的等待
- GPU 分配：Llama→GPU2、Qwen2.5→GPU3、Mistral→第一个空闲 GPU
- `generate_vllm_batch.py:91` 已设 `enforce_eager=True`，Blackwell OK

**唯一限制**：等待是按 llama→qwen2.5→mistral 顺序，不会"谁先下完先跑"。但本场景下 Llama (3.1G/14G) 远超 Qwen2.5 (12MB)，串行顺序与实际完成顺序一致，**无需修改**。

### 模型下载进度

| 模型 | 状态 | 大小 |
|---|---|---|
| gemma-2-9b-it | ✅ 完成 | 18GB（4 safetensors）— 响应已生成 500/500 |
| Qwen3-8B | ✅ 完成 | 16GB（5 safetensors）— 响应已生成 500/500 |
| Llama-3.1-8B-Instruct | 🔄 ~20% | 3.1GB / ~16GB（在 `._____temp/`，~400KB/s，预计还要 3-4h） |
| Qwen2.5-7B-Instruct | 🔄 启动中 | 12MB（仅 metadata，PID 102451 串行队列里） |
| Mistral-7B-Instruct-v0.3 | ⏳ 排队 | 目录不存在（等 Qwen2.5 下完才开始） |

**GPU 全部 idle**（0/97887 MiB ×4）— 编排器卡在 `wait_for_model Llama-3.1-8B-Instruct`，等下载完成。

### 建议

1. 如确认 rtx6000-4x 上 llama judge 也只用 3 模型 → autodl 的 233 条是重复，**不合并、不更新 config**；让 rtx6000-4x 完成 3 模型版后两边二选一。
2. 如计划扩到 7 模型 → 现在改 3 个 local config + 6 个 proxy config 的 `target_models`，删除旧结果重跑（233 条作废）。
3. modelscope 下载速度 ~400KB/s 偏慢，可考虑切 HF + `HF_HUB_ENABLE_HF_TRANSFER=1`，或换镜像源。

---
