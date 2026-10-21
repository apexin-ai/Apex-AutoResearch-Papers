# code exp021 script prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp021-script-prep_20260517T114905_result.json`
- **Structured JSON:** [`6db81ed9e77306b3cc4a.json`](../../sessions/6d/6db81ed9e77306b3cc4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**

- 脚本路径：`/root/autodl-tmp/event-gated-adaptive-horizon/scripts/exp_021_full_sgs_cheetah_s1.sh`
- 已 `chmod +x`
- Dry-run 通过：`dmc_proprio` 配置存在，`full_sgs` 在 defaults 中定义为 `False`（命令行 `--full_sgs True` 会覆盖）
- `full_sgs` 逻辑在 `models.py` 中已实现（L346, L644, L648）

**与旧版脚本的变更：**
- `checkpoint_every`: 25000 → 10000（更细粒度检查点）
- 加 `set -euo pipefail`
- `CUDA_ID` 变量化（支持 `CUDA_ID=1 bash script.sh` 灵活切卡）
- `unset CUDA_VISIBLE_DEVICES` 防止环境干扰
- 环境变量用 `export` 显式导出

GPU 释放后执行：`bash /root/autodl-tmp/event-gated-adaptive-horizon/scripts/exp_021_full_sgs_cheetah_s1.sh`

---
