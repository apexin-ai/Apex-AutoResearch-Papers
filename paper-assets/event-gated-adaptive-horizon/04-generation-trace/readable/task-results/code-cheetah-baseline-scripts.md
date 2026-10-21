# code cheetah baseline scripts

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cheetah-baseline-scripts_20260517T115311_result.json`
- **Structured JSON:** [`20cecc7b8537e8aea353.json`](../../sessions/20/20cecc7b8537e8aea353.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`gate_enabled` 在 configs.yaml 默认值就是 `false`，所以 `--gate_enabled False` 是有效且冗余安全的。参数确认无误。

验证完成，汇总：

**已创建脚本：**

| 脚本 | seed | 默认 GPU | logdir |
|------|------|----------|--------|
| `exp_023a_cheetah_baseline_s0.sh` | 0 | cuda:0 | `exp_023a_cheetah_baseline_s0` |
| `exp_023b_cheetah_baseline_s1.sh` | 1 | cuda:1 | `exp_023b_cheetah_baseline_s1` |

**配置验证：**
- task: `dmc_cheetah_run` — 与 exp_021/submit_plan020 一致
- configs: `defaults dmc_proprio` — 与所有 DMC 实验一致
- `--gate_enabled False` — 显式关闭（configs.yaml 默认也是 false）
- steps: 200000，checkpoint_every: 10000
- MUJOCO_EGL_DEVICE_ID 与 CUDA_ID 联动
- `set -euo pipefail` + `unset CUDA_VISIBLE_DEVICES` 安全模式

**部署状态：**
- 本地: `artifacts/scripts/exp_023a_cheetah_baseline_s0.sh`, `exp_023b_cheetah_baseline_s1.sh`
- 远程: `/root/autodl-tmp/event-gated-adaptive-horizon/scripts/` 下已就绪，`chmod +x` 已执行

019b/022b 完成后可直接提交：
```bash
# GPU 0
CUDA_ID=0 bash scripts/exp_023a_cheetah_baseline_s0.sh
# GPU 1
CUDA_ID=1 bash scripts/exp_023b_cheetah_baseline_s1.sh
```

---
