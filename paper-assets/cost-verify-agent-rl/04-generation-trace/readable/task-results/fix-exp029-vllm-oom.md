# fix exp029 vllm oom

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp029_vllm_oom_20260516T122532_result.json`
- **Structured JSON:** [`04ebc6c8850340883952.json`](../../sessions/04/04ebc6c8850340883952.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**无需修改** — 配置已经是目标状态：

| 项目 | 值 |
|------|-----|
| 文件 | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_episode_level.yaml` |
| 字段 | `actor_rollout_ref.rollout.gpu_memory_utilization` |
| 当前值 | **0.35** （已经是目标值）|
| base.yaml 默认 | 0.3 |
| YAML 验证 | 通过 |

**GPU 状态**: 两块 RTX PRO 6000 完全空闲（各 3 MiB 占用 / 97.9 GiB 总量）。

**训练命令**:
```bash
bash /root/cost-verify-agent-rl/scripts/run_exp029_episode_level.sh
```
脚本包含完整 pre-flight checklist（模型/磁盘/GPU/配置检查），最终执行 `python train.py --config-name _alfworld_exp029_episode_level`。

0.35 × 95 GiB ≈ 33 GiB，即使 FSDP actor 占了 55 GiB，剩余 40 GiB 仍够 vLLM 使用。可以直接启动。

---
