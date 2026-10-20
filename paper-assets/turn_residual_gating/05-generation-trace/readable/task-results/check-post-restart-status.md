# check post restart status

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_post_restart_status_20260524T040056_result.json`
- **Structured JSON:** [`6138df338b3f392b472c.json`](../../sessions/61/6138df338b3f392b472c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态报告：

**GPU**: RTX PRO 6000 Black (98GB), 43% 利用率, 12GB/98GB 显存占用 — **在用**

**存活进程**:
- `gpu_chain_next.sh` (PID 108997) — **存活**
- `eval_attention_steering.py` (PID 141308) — **正在运行**，当前在做 Qwen-1.5B TG 模型的 attention steering eval（`--beta 0 3 5`, `--mode gen`, 50 convs）

**Qwen-1.5B 训练**: **已完成**
- Checkpoint 保存在 `runs/qwen15b_tg_v7_s42/`，3 个 epoch 全部完成（epoch_0/1/2 + gate_params.pt + lora/）
- 最终 checkpoint 时间 11:39
- Phase1 GAR 结果已生成（`results/qwen15b_phase1/`）

**Chain 状态**: **正在继续**
- `post_chain_queue_v2` 在等 gpu_chain 完成
- gpu_chain 已推进到 eval 阶段：base AR eval 已完成（`qwen15b_base_ar_n50.json`, 11:52），当前正在跑 TG model 的 eval
- 还差 TG eval 完成后，chain 应该还会跑后续步骤（可能还有 attention steering 分析等）

**总结**: 服务器没重启（或已自动恢复）。Qwen-1.5B 训练已完成，chain 正在自动推进 eval 阶段，当前 GPU 正在跑 TG 模型的 attention steering eval。无需干预。

---
