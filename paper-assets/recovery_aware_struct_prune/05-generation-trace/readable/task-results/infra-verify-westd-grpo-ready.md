# infra verify westd grpo ready

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_westd_grpo_ready_20260516T014718_result.json`
- **Structured JSON:** [`eff037988ac625ed52d6.json`](../../sessions/ef/eff037988ac625ed52d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 环境检查汇总

| 检查项 | 状态 | 详情 |
|--------|------|------|
| **SFT 模型路径** | ✓ | `/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline/` — `model.safetensors` 14.2GB |
| **GRPO 脚本** | ✓ | `/root/recovery_aware_struct_prune/src/train_grpo_v5.py` 存在 (11.7KB) |
| **eval 进程** | 运行中 | PID 74129, 已运行 8h15m, cuda:0 上评估 sft_unpruned_baseline GSM8K (1319 samples) |
| **cuda:0** | 占用 | RTX PRO 6000, 17.6GB/95.6GB used, 91% util (eval 在跑) |
| **cuda:1** | ⚠️ | RTX PRO 6000, 17.2GB/95.6GB used, **0% util** — 有显存占用但无计算 |
| **磁盘** | ❌ | 250GB 总量, **仅 38GB 可用** (项目占 199GB), 不满足 50GB 要求 |

### 需要关注的问题

1. **磁盘不足**: 38GB < 50GB 要求。GRPO 训练 save_total_limit=5 × ~12GB = 60GB 峰值。启动前需要清理空间（可清理旧 checkpoint 或已完成的实验产物）。

2. **cuda:1 显存占用 17.2GB**: 虽然 utilization 为 0%，但有 ~17GB 显存被占用。可能是之前某个进程残留。启动 GRPO 前需要释放这部分显存。

---
