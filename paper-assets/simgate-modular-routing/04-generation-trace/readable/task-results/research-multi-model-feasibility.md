# research multi model feasibility

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_multi-model-feasibility_20260515T063904_result.json`
- **Structured JSON:** [`d3db0b0e71d9136d204e.json`](../../sessions/d3/d3db0b0e71d9136d204e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已收集完毕。以下是完整调研报告。

---

## Multi-model ScienceWorld 可行性报告

### 1. 服务器状态

| 项目 | 值 |
|------|-----|
| GPU | 2× RTX 5090 32GB，**全部空闲**（0MB 占用） |
| vLLM | **v0.18.1**（2025 最新版，Llama/Mistral 全支持） |
| Python | 3.12 (miniconda3) |
| 数据盘 | 250GB，已用 64GB，**剩余 187GB** |
| Qwen2.5-7B-Instruct | 权重完整（4 × safetensors，共 ~14.5GB） |
| 残留进程 | 无 GPU 进程 |

### 2. 推荐模型

#### 首选：Meta-Llama-3.1-8B-Instruct

| 维度 | 评估 |
|------|------|
| 家族差异 | Meta vs Alibaba，完全不同架构族 |
| 参数量 | 8B（与 Qwen2.5-7B 相近） |
| vLLM 支持 | v0.18.1 原生支持，day-0 兼容 |
| Chat template | tokenizer 内置，`apply_chat_template()` 自动处理 |
| ModelScope | **有镜像**：`LLM-Research/Meta-Llama-3.1-8B-Instruct` |
| BF16 显存 | ~16GB weights + ~4GB KV cache = **~20GB**，32GB 卡轻松容纳 |
| 社区验证 | 最广泛使用的开源 8B 模型之一 |

#### 备选：Mistral-7B-Instruct-v0.3

| 维度 | 评估 |
|------|------|
| 家族差异 | Mistral AI（法国），不同家族 |
| 参数量 | 7B |
| ModelScope | 有镜像：`rubraAI/Mistral-7B-Instruct-v0.3` |
| BF16 显存 | ~14GB weights，32GB 绰绰有余 |
| 劣势 | 社区规模和 benchmark 表现略逊于 Llama 3.1 |

**推荐 Llama 3.1 8B Instruct**——reviewer 更熟悉、benchmark 更有说服力、是目前引用最多的开源 baseline。

### 3. 显存评估

```
RTX 5090 VRAM:         32 GB
Llama-3.1-8B BF16:    ~16 GB (weights)
KV cache (default):   ~4-5 GB
ScienceWorld (Java):   CPU only, 0 GPU
────────────────────────────────
剩余 VRAM:            ~11-12 GB
```

**结论：单卡 BF16 完全可行，无需量化。** 比 Qwen2.5-7B（~15GB weights）略大约 1GB，毫无压力。

### 4. 代码改动量

**核心发现：几乎零改动。**

所有关键脚本（`episode_level_collection.py`、`counterfactual_labeling.py`、`collect_trajectories.py`）均已支持 `--model_path` 参数：

```bash
# 现有 Qwen 运行方式
python src/episode_level_collection.py --task_types "freeze" --gpu_id 0

# 换 Llama 只需加一个参数
python src/episode_level_collection.py --task_types "freeze" --gpu_id 0 \
  --model_path /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct
```

代码中的关键兼容点：
- `llm_agent.py` 的 `find_model_path()` 是 Qwen 专用，但 `--model_path` 传入后会跳过它
- `apply_chat_template()` 由 tokenizer 自动处理，Llama 3.1 的 chat template 内置在 `tokenizer_config.json` 中
- `SamplingParams` 的 stop tokens `["Observation:", "\nObservation"]` 是 ReAct 格式，模型无关
- System prompt / User template 是纯文本，模型无关

**唯一需要注意**：Llama 3.1 的 tokenizer 不需要 `trust_remote_code=True`（代码中已传了这个参数，对 Llama 无害但不需要）。

### 5. 模型下载方案

AutoDL 上 HuggingFace 下载极慢（~200KB/s），**必须用 ModelScope**：

```bash
source /etc/network_turbo
pip install modelscope
python -c "
from modelscope import snapshot_download
snapshot_download('LLM-Research/Meta-Llama-3.1-8B-Instruct',
                  cache_dir='/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct')
"
```

预计下载时间：~16GB，ModelScope CDN 通常 10-50MB/s → **5-30 分钟**。

### 6. 预估运行时间

现有数据：11 个 task × 20 episodes，每 episode 两种 modality（always-internal + always-deterministic）。

| 参数 | 估算 |
|------|------|
| 总 episode 数 | 11 × 20 × 2 = **440 episodes** |
| 平均步数/episode | ~25 步（17-30） |
| LLM 调用/步 | ~1 次（内部模式）或 1 次 + 3 次 fork（确定性模式，但 fork 是 CPU） |
| vLLM 推理速度 | RTX 5090 上 ~0.3-0.8s/call |
| 单 GPU 总时间 | **~4-6 小时** |
| **双 GPU 并行** | **~2-3 小时** |

run_all.sh 已有双 GPU 并行模板（GPU 0 跑一组 task，GPU 1 跑另一组），直接复用。

### 7. Blockers 和风险

| 风险 | 严重程度 | 缓解 |
|------|----------|------|
| Llama 3.1 在 ScienceWorld 上的 ReAct 能力未知 | 中 | 先跑 1 个 task × 3 eps 快速验证，确认 action parsing 正常 |
| Llama 3.1 可能有不同的 death avoidance 行为 | 低 | 这正是实验要验证的——如果 DAF 差异大反而是有趣发现 |
| ModelScope 下载偶尔限速 | 低 | 备选：HF + `network_turbo`，或预先下好 |
| `find_model_path()` fallback 会混淆 | 低 | 传 `--model_path` 绕过 |
| Llama 3.1 tokenizer 与 prompt 长度差异 | 低 | chat template 自动处理，max_tokens 已设 |

**无硬性 blocker。** 建议执行顺序：
1. 下载模型（~20 分钟）
2. 快速冒烟测试：1 task × 3 eps（~10 分钟）
3. 确认 action parsing OK 后启动全量 11 tasks × 20 eps

---
