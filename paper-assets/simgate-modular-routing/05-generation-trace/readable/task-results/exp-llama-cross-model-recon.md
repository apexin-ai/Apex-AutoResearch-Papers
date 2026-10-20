# exp llama cross model recon

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_llama-cross-model-recon_20260515T113253_result.json`
- **Structured JSON:** [`7004e72e1c2a5c10ee41.json`](../../sessions/70/7004e72e1c2a5c10ee41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。所有 5 个 task 名解析正确，每个需要收集 5 个新 episode pair。

## 侦察报告

### 1. Llama 模型
完整。4 个 safetensors shard（共 ~15GB）在 `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`，含 tokenizer 和 config。

### 2. Pipeline 代码
**可直接复用**。核心脚本 `src/episode_level_collection.py`，通过 `--model_path` 传入 Llama 路径即可。LLMAgent 使用 `apply_chat_template`（模型通用）+ vLLM 通用初始化，无 Qwen 硬编码依赖。

### 3. 环境状态
| 项目 | 状态 |
|------|------|
| GPU | 2× RTX 5090 32GB，均空闲 |
| 磁盘 | 172GB 可用 |
| vLLM | v0.18.1 已装 |
| PyTorch | 2.10.0+cu128 |
| ScienceWorld | 1.2.3 |
| vLLM 进程 | 无运行 |
| conda env | base (Python 3.10.12) |

### 4. 脚本路径
`/root/autodl-tmp/simgate-modular-routing/scripts/run_llama_expanded.sh`

逐 task 运行（错误隔离），每个 task 单独 log 到 `results/llama-expanded/logs/`。

### 5. 预估运行时间
- 5 tasks × 5 episode pairs = 25 pairs
- 基于 pilot ~4.7 min/pair → **~118 min（约 2 小时）**
- Pilot 实际数据：freeze 单个 internal episode 30步 ≈ 79s，一对 ≈ 2.7 min；但高 death tasks 可能更快（death 提前终止），保守估 2 小时

### 6. Blockers
**无。** 所有依赖就位，dry-run 通过。随时可以运行：
```bash
nohup bash scripts/run_llama_expanded.sh > results/llama-expanded/run.log 2>&1 &
```

---
