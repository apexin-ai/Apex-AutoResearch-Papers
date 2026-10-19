# diag westd34887 qwen14b v4

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd34887_qwen14b_v4_20260524T091252_result.json`
- **Structured JSON:** [`b289d8272cae7bd08c2b.json`](../../sessions/b2/b289d8272cae7bd08c2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总：

---

**Checkpoint**: 存在  
- 路径: `/root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s123/` (224MB)  
- 基础模型: `/root/autodl-tmp/models/qwen2.5-14b/` (28GB)

**v4 结果**: **已完成** — `results.json` 存在，GSM8K exact_match = **34.72%** (timestamp 2026-05-24 08:43:05)

**磁盘**:
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 22G | 8.7G | 72% |
| /root/autodl-tmp (数据盘) | 250G | 70G | 181G | 28% |

**网络**: 
- 直连 HuggingFace: 不可达（超时）
- `source /etc/network_turbo` 后: **可达** (HTTP 200)
- hf-mirror.com: 可达

**GPU**: 2× NVIDIA RTX PRO 6000 Blackwell (98GB each), 0% 利用率, 0MB 显存占用

**残留进程**: 无 gsm8k/lm_eval 相关进程

**tmux**: 无活跃 session

---

**结论**: v4 实验已成功完成，无需重跑。GSM8K eval 结果 34.72%。如需重跑其他 seed/配置，环境条件具备（GPU 空闲、磁盘充足、网络需先 `source /etc/network_turbo`）。

---
