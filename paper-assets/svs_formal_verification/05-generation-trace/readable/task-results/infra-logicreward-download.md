# infra logicreward download

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_logicreward-download_20260514T113744_result.json`
- **Structured JSON:** [`aefc65e2300e44ebc8c5.json`](../../sessions/ae/aefc65e2300e44ebc8c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。汇报结果：

---

**模型验证结果：Aiden0526/LogicReward-Qwen3-8B**

| 项目 | 结果 |
|------|------|
| 模型存在 | 是，HuggingFace Hub 验证通过 |
| 模型类型 | **LoRA adapter**（非完整模型），83MB safetensors |
| 基座模型 | `Qwen/Qwen3-8B` |
| 训练流程 | SFT → DPO，使用 LLaMA-Factory |
| LoRA 配置 | r=8, alpha=16, target: q/k/v/o/gate/up/down_proj |
| task_type | CAUSAL_LM |
| Tokenizer | 加载成功，vocab_size=151,643 |
| 下载路径 | `/root/autodl-tmp/models/LogicReward-Qwen3-8B/` |
| 文件数 | 11 个文件（adapter_model.safetensors + tokenizer + config） |
| 论文 | LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision (ICLR 2026) |

**gpu-5090-4x-4 GPU 状态：**

| GPU | 利用率 | 显存使用 |
|-----|--------|----------|
| GPU 0 | 99% | 31,459 / 32,607 MiB |
| GPU 1 | 99% | 31,459 / 32,607 MiB |
| GPU 2 | 0% | 31,401 / 32,607 MiB（显存被占但空闲） |
| GPU 3 | 0% | 31,401 / 32,607 MiB（显存被占但空闲） |

注意：使用此 adapter 需要先下载基座模型 `Qwen/Qwen3-8B`（约 16GB）。4 张 5090 显存几乎全部被占用。

---
