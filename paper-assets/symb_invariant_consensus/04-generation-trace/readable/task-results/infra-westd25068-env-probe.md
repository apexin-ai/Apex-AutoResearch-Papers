# infra westd25068 env probe

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd25068-env-probe_20260521T163343_result.json`
- **Structured JSON:** [`5defbbe4ef76db415fe6.json`](../../sessions/5d/5defbbe4ef76db415fe6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-25068 环境探测汇报

### 1. GPU
| 项目 | 值 |
|------|-----|
| 数量 | 4 |
| 型号 | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| 单卡显存 | 98 GB |
| 总显存 | **392 GB** |
| 当前状态 | **全部空闲**（0 MiB used, 0% util） |

### 2. Qwen-72B 权重
- **存在**：`/root/autodl-tmp/models/Qwen2.5-72B-Instruct`（100GB，37 个 safetensors shards）
- **注意：这是 BF16 全精度模型，不是 AWQ 量化版**
- 392GB 总显存远超 BF16 推理需求（~144GB），无需 AWQ

### 3. Mistral-7B
- **存在**：`/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3`（16GB）

### 4. vLLM 环境
- Python 3.12.4（conda base）
- **vLLM 0.21.0** ✓
- torch 2.11.0, transformers 5.8.1, flashinfer 0.6.8

### 5. 项目代码
- **已 sync**：`/root/symb_invariant_consensus/`，FOLIO 数据齐全

### 6. 磁盘
| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| `/`（根） | 30G | 19G | **12G** |
| `/root/autodl-tmp`（数据盘） | 250G | 250G | **845M** ⚠️ |

数据盘上模型占用明细：Qwen-72B (100G) + gemma-27b (52G) + Qwen2.5-14B (28G) + Qwen3-14B (28G) + Mistral-7B (16G) + Qwen-7B (15G) + DS-R1-8B (8.7G) + DS-R1-Llama-8B (4.3G) ≈ 252G

### 7. 70B 部署可行性评估

**结论：完全可行，无需额外下载。**

- 72B BF16 模型已在盘上，4 卡 392GB 显存绑定 tensor parallelism=2 即可（每卡约 72GB），tp=4 更宽裕（每卡约 36GB）
- vLLM 0.21.0 已装好，直接 `vllm serve` 即可启动
- 磁盘虽然满了，但不影响部署（模型已存在，vLLM 无需额外磁盘空间写临时文件，KV cache 在 GPU 内存中）
- **估算启动时间**：模型加载 2-5 分钟（100GB 从 NVMe 读入 GPU）

**唯一风险**：磁盘 845MB 余量极低，如果 vLLM 需要写日志或临时文件可能报错。建议启动前清理不需要的模型（如 gemma-27b 52G、llama-4-scout 60K 空目录等）释放空间。

---
