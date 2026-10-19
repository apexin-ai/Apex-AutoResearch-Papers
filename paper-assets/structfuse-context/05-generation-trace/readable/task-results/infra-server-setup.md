# infra server setup

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_server_setup_20260512T102130_result.json`
- **Structured JSON:** [`56d3fd6aee4aeaf68a46.json`](../../sessions/56/56d3fd6aee4aeaf68a46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境搭建完成。汇总：

### 环境信息
| 项目 | 版本 |
|------|------|
| Python | 3.12.3 (miniconda3) |
| PyTorch | 2.10.0+cu128 |
| CUDA | 12.8 |
| GPU | 6x RTX 4090 D (24GB each) |
| transformers | 4.57.6 |
| accelerate | 1.13.0 |
| peft | 0.19.0 |
| datasets | 4.8.4 |
| wandb | 0.26.0 |
| CodeQL | 2.25.4 |

### 代码部署
10/10 文件已部署到 `/root/structfuse/`：
- `extraction/codeql_queries/call_graph.ql`
- `extraction/codeql_queries/bounded_dataflow.ql`
- `extraction/extract_dataflow.py`
- `extraction/build_training_data.py`
- `training/contrastive_model.py`
- `training/hard_negative_mining.py`
- `training/train.py`
- `evaluation/eval_retrieval.py`
- `evaluation/eval_swebench.py`
- `requirements.txt`

### 新安装的包
beniget 0.5.0, tree-sitter 0.25.2, rank-bm25 0.2.2

### 注意事项
- 分配的 GPU 是 `cuda:4`，训练时需设 `CUDA_VISIBLE_DEVICES=4`
- AutoDL 实例，使用 conda base 环境（非 venv）
- 激活环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 网络加速：`source /etc/network_turbo`（pip/git 操作前执行）
- vllm 已在 requirements.txt 中但未安装（SWE-bench 评估阶段再装）

---
