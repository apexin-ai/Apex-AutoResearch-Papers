# code grpo training

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-training_20260513T180233_result.json`
- **Structured JSON:** [`e512127b5f0fba341c27.json`](../../sessions/e5/e512127b5f0fba341c27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No register_artifact tool available. The artifacts are already in the `artifacts/` directory.

Phase 1 GRPO 训练脚本已完成，dry-run 验证通过。

**产出文件（服务器 + 本地 artifacts/）：**

| 文件 | 服务器路径 | 说明 |
|------|-----------|------|
| `train_grpo.py` | `/root/solver-trace-ablation/scripts/train_grpo.py` | 主训练脚本，支持 `execution_only` 和 `execution_sta` 两种 reward 模式 |
| `grpo_exec_only.yaml` | `/root/solver-trace-ablation/configs/grpo_exec_only.yaml` | execution-only 配置 |
| `grpo_exec_sta.yaml` | `/root/solver-trace-ablation/configs/grpo_exec_sta.yaml` | execution+STA 配置 |
| `launch_phase1.sh` | `/root/solver-trace-ablation/scripts/launch_phase1.sh` | 双 GPU 并行启动脚本 |

**Dry-run 结果（1 步，execution_only 模式）：**
- 14.6s/step（含 generation + reward 计算 + backward）
- parse_rate=1.0, prove_rate=0.25, mean_isr=0.25
- Checkpoint 保存到 `/root/autodl-tmp/outputs/`（数据盘 232GB 可用）
- 无 OOM，94GB 显存绑绑有余

**注意事项：**
- 根分区已满（30G/30G），所有 output 写入 `/root/autodl-tmp/outputs/`
- 已设 `save_only_model=True` 避免保存 7.5GB 的 optimizer state
- 模型 shard 3 之前缺失，已通过 ModelScope 补全

---
