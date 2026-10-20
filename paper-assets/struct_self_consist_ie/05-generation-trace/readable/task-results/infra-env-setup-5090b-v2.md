# infra env setup 5090b v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env_setup_5090b_v2_20260518T173626_result.json`
- **Structured JSON:** [`0dc40f9900e6f643b83b.json`](../../sessions/0d/0dc40f9900e6f643b83b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器环境搭建完成。汇总如下：

## autodl-5090-b
| 项目 | 状态 |
|------|------|
| GPU | 4x RTX 5090 (32GB each) |
| Python | 3.12.3 |
| torch | 2.10.0+cu128 |
| transformers | 4.57.1 |
| peft | 0.17.1 |
| accelerate | 1.11.0 |
| vllm | 0.18.1 |
| trl | 0.24.0 |
| bitsandbytes | 0.49.2 |
| wandb | 0.26.0 |
| 数据盘 | 350GB (403MB used) |
| 项目代码 | /root/autodl-tmp/struct_self_consist_ie/ ✓ |
| CUDA | ✓ |

## autodl-5090-c
| 项目 | 状态 |
|------|------|
| GPU | 4x RTX 5090 (32GB each) |
| Python | 3.12.3 |
| torch | 2.10.0+cu128 |
| transformers | 4.57.1 |
| peft | 0.17.1 |
| accelerate | 1.11.0 |
| vllm | 0.18.1 |
| trl | 0.24.0 |
| bitsandbytes | 0.49.2 |
| wandb | 0.26.0 |
| 数据盘 | 350GB (403MB used) |
| 项目代码 | /root/autodl-tmp/struct_self_consist_ie/ ✓ |
| CUDA | ✓ |

两台服务器的包版本与 autodl-5090 完全一致。代码、配置文件和数据已同步（不含 checkpoints/output，需要时从 HF 下载基础模型）。`env.sh` 已添加到 `.bashrc`。

---
