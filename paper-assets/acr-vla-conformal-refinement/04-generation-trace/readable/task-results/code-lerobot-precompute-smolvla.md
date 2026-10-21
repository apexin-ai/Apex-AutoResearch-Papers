# code lerobot precompute smolvla

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lerobot-precompute-smolvla_20260522T141652_result.json`
- **Structured JSON:** [`33e2708a21de091a990c.json`](../../sessions/33/33e2708a21de091a990c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. 代码文件路径
- **服务器**: `/root/acr-vla-conformal-refinement/src/lerobot_precompute.py` (bjb2-28827)
- **本地**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/src/lerobot_precompute.py`

脚本基于已有的 `SmolVLAWrapper`（`smolvla_wrapper.py`），该 wrapper 已实现：
- `encode_prefix()` → VLM hidden states mean-pool 提取 obs_features
- `generate_k_samples_batched()` → 共享 KV cache 的 K 次 flow-matching 采样

### 2. obs_features 来源层和维度
- **来源**: VLM（SmolVLM2-500M-Video-Instruct，前 16 层）的 final norm output
- **提取方式**: prefix embedding（images + language + state）经 VLM forward → 对所有有效 token 的 hidden states 做 **mean-pooling**
- **维度**: **960**（与 VLM `text_config.hidden_size` 一致）

### 3. 验证结果（object benchmark, dry_run: 10 tasks × 2 demos = 20 trajectories, 3020 timesteps）

```
[precompute] object: 3020 samples in 6.3min (8.0 samples/s)

  obs_features: (3020, 960)    mean=-0.0398, std=0.7122, range=[-5.59, 6.14]
  k_samples:    (3020, 5, 5, 6) mean=0.0274, std=0.2825, range=[-1.05, 1.06]
  expert_actions: (3020, 5, 6)  mean=0.0245, std=0.2862

All 12 validation checks PASSED:
  ✓ Shape checks (obs_features, k_samples, expert_actions, manifest)
  ✓ NaN/Inf checks
  ✓ Value range reasonable
  ✓ K-sample diversity > 0 (pairwise L2 = 0.039)
```

### 4. obs_dim 确认
obs_dim = **960**，与预期一致。

---
