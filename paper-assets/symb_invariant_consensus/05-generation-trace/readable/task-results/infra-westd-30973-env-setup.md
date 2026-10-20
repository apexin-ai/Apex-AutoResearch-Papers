# infra westd 30973 env setup

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-30973-env-setup_20260523T055553_result.json`
- **Structured JSON:** [`2ce56a512b4e90327473.json`](../../sessions/2c/2ce56a512b4e90327473.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-30973 环境搭建报告

### 1. 环境状态
| 项目 | 版本 |
|------|------|
| Python | 3.12.3 (Miniconda) |
| PyTorch | 2.11.0+cu130 |
| CUDA Driver | 580.82.09 (CUDA 13.0) |
| vLLM | 0.21.0 |
| transformers | 5.9.0 |
| accelerate | 1.13.0 |
| z3-solver | 4.15.4.0 |

### 2. 模型状态
- Qwen2.5-14B-Instruct: **就绪** (`/root/autodl-tmp/models/Qwen2.5-14B-Instruct/`)
- Meta-Llama-3.1-8B-Instruct: **就绪** (`/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct/`)

### 3. 代码和数据
- 15 个 run_*.py 脚本已同步
- ProofWriter 数据: 600 条

### 4. GPU 状态
| GPU | 型号 | VRAM |
|-----|------|------|
| cuda:0 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 94GB |
| cuda:1 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 94GB |
| cuda:2 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 94GB |

**注意**: 实际每卡 94GB VRAM，不是任务描述中的 48GB。

### 5. 磁盘
- 根分区: 18GB 可用 / 30GB
- 数据盘: 207GB 可用 / 250GB

### 6. env_activate 命令
`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`

---
