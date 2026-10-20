# ssh d062 full ft scierc recover

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d062_full_ft_scierc_recover_20260519T042307_result.json`
- **Structured JSON:** [`0c89e398e5e08b51717c.json`](../../sessions/0c/0c89e398e5e08b51717c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Inference 正在运行。Unconstrained 接近完成 (462/551)，constrained 刚开始 (17/551)。4 分钟后检查进展。

**当前状态**:
- Checkpoint 验证通过：16GB model.safetensors，399 shards 加载成功
- 训练信息：eval_loss=0.09459，3 epochs，Qwen3-8B full FT
- Unconstrained 推理：另一个 worker 已启动 (PID 83571)，462/551 完成
- Constrained (full_s1) 推理：我启动的 tmux session `d062_full_ft_infer`，17/551 完成
- GPU 使用：3 个进程共用 96GB GPU，约 57GB 已用

**LoRA FT 对比基线** (已记录):
| Metric | LoRA FT Greedy Constrained | LoRA FT Beam4 Constrained |
|--------|---------------------------|--------------------------|
| E_F1 | 67.05 | 66.88 |
| R_F1 | 43.77 | 44.23 |
| DR | 0.20% | 0% |
| CF | 1.18% | 0% |

---
