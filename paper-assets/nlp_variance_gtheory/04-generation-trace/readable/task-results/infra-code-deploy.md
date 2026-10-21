# infra code deploy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_code_deploy_20260520T150135_result.json`
- **Structured JSON:** [`157bdb2444baac52cde7.json`](../../sessions/15/157bdb2444baac52cde7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码部署完成。总结：

**已完成：**
- 15 个 Python 文件 + requirements.txt + pyproject.toml + run_mvp.sh 全部部署到 `/root/nlp_variance_gtheory/`
- 目录结构 `src/{data,design,inference,analysis}`, `data/`, `results/` 已创建

**当前环境状态：**
- 服务器使用 aml-train 镜像 (conda base 环境, `/root/miniconda3/bin/python3`)
- 另一个 Worker 正在安装 vllm（PID 2546），正在下载 NVIDIA CUDA 依赖包，下载速度 ~1 MB/s
- `datasets`, `pandas` 等 CPU 依赖尚未安装，无法立即运行数据生成任务

**待 vllm 安装完成后：**
- 需要额外安装 `datasets pandas scipy seaborn statsmodels generalizit matplotlib tqdm`（这些不是 vllm 的依赖）
- 然后可以运行 CPU 数据生成步骤（sample_mmlu, few_shot, generate_design）

---
