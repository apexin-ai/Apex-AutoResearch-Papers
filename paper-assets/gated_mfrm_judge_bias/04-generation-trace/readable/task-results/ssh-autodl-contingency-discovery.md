# ssh autodl contingency discovery

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_contingency_discovery_20260523T224547_result.json`
- **Structured JSON:** [`6cdeb1baaca2c0420aa1.json`](../../sessions/6c/6cdeb1baaca2c0420aa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。

---

## autodl-8gpu Discovery 报告

### 1. 代码就绪度
- **collect.py** ✓ — `exp001/collect.py`，支持 pairwise/pointwise、增量续跑、rate limiting
- **n17 configs** ✗ — exp001 中**无 n17 命名的 config**。n17 文件仅存在于 exp003/（`run_exp003_n17.py`, `run_n17_downstream.py`）
- 现有 per-judge configs（9个）：claude-opus-4.7-proxy, claude-sonnet-4.6-proxy, deepseek-v4-pro-proxy, gemini-2.5-pro-proxy, gpt-5.5-proxy, llama_arena, mistral_arena, qwen3-235b-proxy, qwen_arena
- base config.yaml 定义了 22 个 target models，per-judge proxy configs 只含 9 个

### 2. 环境就绪度
| 包 | 状态 |
|---|---|
| Python 3.12 (miniconda) | ✓ |
| vllm | ✓ |
| openai | ✓ |
| anthropic | ✓ |
| transformers | ✓ |

### 3. 模型权重
**仅有 7-9B 小模型**，无 70B/72B：

| 模型 | 路径 |
|---|---|
| Qwen3-8B | ✓ /root/autodl-tmp/models/ |
| gemma-2-9b-it | ✓ |
| Qwen2.5-7B-Instruct | ✓ |
| Llama-3.1-8B-Instruct | ✓ |
| Mistral-7B-Instruct-v0.3 | ✓ |
| **llama-3.3-70b** | ✗ 无权重 |
| **qwen2.5-72b** | ✗ 无权重 |

### 4. GPU 可用性

| GPU | 型号 | VRAM | 已用 | 利用率 | 状态 |
|---|---|---|---|---|---|
| 0 | RTX PRO 6000 Blackwell | 96 GB | 73.8 GB | 65% | **exp-017 占用** |
| 1 | RTX PRO 6000 Blackwell | 96 GB | 0 | 0% | **空闲** |
| 2 | RTX PRO 6000 Blackwell | 96 GB | 0 | 0% | **空闲** |
| 3 | RTX PRO 6000 Blackwell | 96 GB | 0 | 0% | **空闲** |

### 5. 已有 judgment 数据（exp001 arena_hard）

| Judge | 行数 | 预估完成度 |
|---|---|---|
| gpt-5.5-proxy | 3437 | ~38% |
| claude-opus-4.7-proxy | 3389 | ~38% |
| claude-sonnet-4.6-proxy | 2961 | ~33% |
| qwen3-235b-proxy | 2091 | ~23% |
| gemini-2.5-pro-proxy | 1916 | ~21% |
| deepseek-v4-pro-proxy | 1433 | ~16% |
| llama-3.3-70b | 1238 | ~14% |
| qwen2.5-72b | 915 | ~10% |
| mistral-large-2 | 583 | ~6% |

orchestrator2（response generation）**已完成**，不影响后续。

### 6. exp-017 状态
- **进度**: 165/800 iterations (20.6%)
- **速度**: ~370s/iter
- **ETA**: ~235,000s ≈ **~65 小时（约2.7天）**
- 仅占 GPU0，不影响 GPU1-3
- 类型：MCMC (numpyro)，CPU-bound sequential chains

### 7. 磁盘
- 根分区：30GB，剩余 16GB (49%)
- 数据盘：250GB，剩余 115GB (55%)

### 8. 网络
- ssh_read_only 无法测 curl，但 orchestrator2 曾成功使用 `network_turbo` 代理
- API judges 已部分产出 judgment 数据 → **API endpoint 此前可达**

---

## 结论

| 方案 | 可行性 | 说明 |
|---|---|---|
| **A: API judges only** | ✅ **立即可用** | 代码/环境/configs 就绪，collect.py 支持增量续跑，6 个 API judge 可直接继续（需确认 API key 和网络） |
| **B: API + local vLLM (70B/72B)** | ⚠️ **需数小时准备** | 无 70B/72B 权重，需下载到 autodl-tmp（AutoDL 代理下载慢，建议用 ModelScope）。3×96GB 空闲 GPU 足够托管 |
| **C: 大量准备工作** | ✗ 不适用 | 基础设施已就位，不属于此类 |

**建议**：如果只需推进 API judges（6个 proxy 系列），autodl-8gpu 可立即接手。local vLLM judges（llama-70b, qwen-72b）需要先下载权重。n17 configs 在此服务器上不存在，需从 rtx6000-4x 同步或重新生成。

---
