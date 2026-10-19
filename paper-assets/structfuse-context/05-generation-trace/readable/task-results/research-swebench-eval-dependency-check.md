# research swebench eval dependency check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_swebench-eval-dependency-check_20260515T181546_result.json`
- **Structured JSON:** [`1c83f8786b63ffe032dd.json`](../../sessions/1c/1c83f8786b63ffe032dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan_003 SWE-bench Eval 依赖就绪状态报告

### 1. 脚本就绪状态：✅ 已存在

| 脚本 | 路径 | 功能 |
|------|------|------|
| `eval_swebench.py` | `/root/structfuse/evaluation/` | 纯检索评估（Recall@k, MRR），**不需要 API key** |
| `eval_swebench_e2e.py` | `/root/structfuse/scripts/` | 端到端评估（检索→LLM patch→resolve rate），**需要 API key** |

e2e 脚本通过环境变量配置 LLM：
- `STRUCTFUSE_LLM_BACKEND=api`
- `STRUCTFUSE_LLM_API_BASE` / `STRUCTFUSE_LLM_API_KEY` / `STRUCTFUSE_LLM_MODEL`
- 默认 `mock` 模式（返回空 patch，用于调试流程）

### 2. 数据就绪状态：✅ 已就绪

| 数据 | 状态 | 大小 |
|------|------|------|
| SWE-bench Lite (HF cache) | ✅ | `princeton-nlp___swe-bench_lite` (dev+test) |
| SWE-bench Lite (arrow) | ✅ | `/root/autodl-tmp/swebench/swebench_lite/` (3.4MB) |
| 预克隆仓库 (12个) | ✅ | `/root/autodl-tmp/swebench/repos/` (1.7GB) |

12个仓库：astropy, django, matplotlib, seaborn, flask, requests, xarray, pylint, pytest, scikit-learn, sphinx, sympy

### 3. Checkpoint 就绪状态：⚠️ 部分就绪

| Checkpoint | 状态 |
|------------|------|
| `m2_full_qwen/dataflow_aware_s42` | ❌ 不存在（eval 示例中引用的路径） |
| `m2_full_qwen/dataflow_aware_s43/best_by_recall_at_1` | ✅ 含 model.pt + training_config.json |
| `m2_full_qwen/random_s{42,43,44}` | ✅ |
| `m2_full_qwen/embedding_distance_s{43,44}` | ✅ |

`dataflow_aware_s42` 缺失但可用 `s43` 替代，不是阻塞项。

### 4. Python 包依赖：✅ 全部已安装

torch, transformers, datasets, openai, numpy, tqdm 均可正常 import。Python 在 `/root/miniconda3/bin/python3`（conda 环境）。

### 5. API Key：❌ 未配置

- 环境变量中**无任何 API key**（无 OPENAI/ANTHROPIC/QWEN/DASHSCOPE 相关变量）
- **无 .env 文件**
- 端到端 eval 需要 OpenAI-compatible API endpoint + key（用于 Qwen3.6-27B 或其他 LLM agent）

### 6. 缺失依赖清单

| 缺失项 | 影响范围 | 优先级 |
|--------|---------|--------|
| **LLM API Key + Endpoint** | 端到端 eval 阻塞项 | **P0** |
| `dataflow_aware_s42` checkpoint | eval 示例路径不匹配 | 低（用 s43 替代） |
| Docker（待确认） | SWE-bench 标准 patch 验证可能需要 | 待查 |

### 7. 预计准备时间

| 场景 | 时间 |
|------|------|
| **纯检索 eval**（Recall@k/MRR） | **可立即运行**，0 Worker 小时准备 |
| **端到端 eval**（resolve rate） | 配置 API ~0.5h + 运行 300 instances ~2-4h = **3-5 Worker 小时** |

**结论**：检索 eval 可以立即跑。端到端 eval 唯一阻塞项是 **LLM API key/endpoint 未配置**。

---
