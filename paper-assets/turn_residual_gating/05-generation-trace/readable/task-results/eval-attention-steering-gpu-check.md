# eval attention steering gpu check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_attention_steering_gpu_check_20260520T064639_result.json`
- **Structured JSON:** [`7cf03231cc99ae8ddb0e.json`](../../sessions/7c/7cf03231cc99ae8ddb0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 1. GPU 显存
| 指标 | 值 |
|------|-----|
| 总显存 | 97,887 MiB (~96 GB) |
| 已用 | 34,187 MiB (~33 GB) |
| 剩余 | **63,064 MiB (~62 GB)** |
| GPU 利用率 | 55% |

### 2. 并行可行性：**可以并行**
- 剩余 62 GB >> attention steering 推理所需 15-20 GB
- v8b 当前只用了 ~33 GB（远低于之前预估的 85 GB），留有充裕空间
- 即使 v8b 训练过程中显存波动，62 GB 余量足以容纳 7B 模型推理

### 3. LoRA rank
- `config.py`: **LORA_RANK = 16**
- `train_phase2.py` 中通过 `r=LORA_RANK` 引用，与论文修改后的 rank 16 一致

### 4. Attention steering 代码状态：**全部就绪**
| 文件 | 大小 | 修改时间 |
|------|------|----------|
| `src/attention_steering.py` | 4,371 B | May 20 14:20 |
| `src/eval_attention_steering.py` | 20,118 B | May 20 14:21 |
| `scripts/launch_attention_steering.sh` | 1,211 B | May 20 14:21 |

三个文件均存在且有实质内容，可随时启动。

---
