# code hsweep launch infra

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hsweep_launch_infra_20260517T020741_result.json`
- **Structured JSON:** [`4e3ce96f5b8277744f5a.json`](../../sessions/4e/4e3ce96f5b8277744f5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 产出汇总

### 1. Seed 机制

| 项目 | 详情 |
|------|------|
| Config 字段 | `seed.train` (top-level，base.yaml 默认 10000) |
| Hydra override | `seed.train=20000` |
| 机制 | ESManager 用 `base_seed + seed_counter`，counter 每轮 reset +env_groups(16)。不同 base_seed → 不同 game 选择序列 |
| launch 脚本策略 | seed 1→10000, seed 2→20000, ..., seed 5→50000（间隔 10000，远超 15steps×16groups=240 的窗口） |

### 2. Trajectory Logging

**不内置。** 无 `VERL_ENABLE_TRACKER` 或 trajectory dump flag。

- `BIAVRTracker` 追踪 verify/action 指标但不落盘
- 添加改动量评估：在 `es_manager.py` 的 rollout loop 中加 ~25 行 JSONL dump（per-step action + obs + reward），非阻塞改动
- 建议 h-sweep 跑完后按需添加，不阻塞启动

### 3. launch_hsweep.sh

已创建：`/root/cost-verify-agent-rl/scripts/launch_hsweep.sh`

用法：`./launch_hsweep.sh 5 2` → 以 seed.train=20000 启动 h5 实验，wandb experiment 名 `hsweep-h5-seed2`

### 4. Tatsu Patch 部署状态

- `patches/__init__.py` ✓ 已创建
- `train.py` 第 4 行 `import patches.tatsu_parallel_fix` ✓ 已添加
- 验证: `[tatsu_parallel_fix] Patched 4 singleton parsers with thread-local instances` ✓

### 5. parallel_friendly 状态

当前 `envs.yaml` 中 `AlfworldSG`: **`parallel_friendly: false, max_workers: 1`**

Tatsu patch 已部署，parallel 执行安全。exp029 结束后执行一行即可启用：
```bash
sed -i 's/parallel_friendly: false/parallel_friendly: true/; s/max_workers: 1/max_workers: 4/' /root/cost-verify-agent-rl/RAGEN/config/envs.yaml
```

### Pre-flight (C002) 验证

- ✓ 入口点: `python train.py --config-name` (与 exp029 一致)
- ✓ 磁盘: 86GB 可用
- ✓ Model path: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4/` 存在
- ✓ 5 个 config 参数一致（h2/h5/h10/h20 用 step_independent，full 用 full mode）

---
