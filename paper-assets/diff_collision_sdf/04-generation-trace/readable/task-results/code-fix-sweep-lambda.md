# code fix sweep lambda

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_sweep_lambda_20260520T121135_result.json`
- **Structured JSON:** [`6855944a892182213e23.json`](../../sessions/68/6855944a892182213e23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台内容一致。5 个修复的 diff 总结：

## 修复 Diff

| # | 问题 | 原始 | 修复后 |
|---|------|------|--------|
| 1 | `--gpu 0` 缺失 | python 调用无 `--gpu` 参数 | 添加 `--gpu 0`（CUDA_VISIBLE_DEVICES 映射后的第一张卡） |
| 2 | JAX 抢 GPU | 无 JAX 环境变量 | 循环前 `export JAX_PLATFORMS=cpu` |
| 3 | wandb 联网失败 | 无 WANDB 设置 | 循环前 `export WANDB_MODE=offline` |
| 4 | conda 未激活 | 脚本直接执行 python | `set -euo pipefail` 后加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` |
| 5 | 无时间估算 | 注释无运行时间信息 | 头部注释加 `# 时间估算: 每个 lambda 值约 29h（30K steps × ~3.5s/it），4 个 lambda 串行 ≈ 116h 单卡` |

## 验证结果
- **westd-35807**: 写入成功，内容正确
- **westd-45947**: 写入成功（原先无此文件），内容与 35807 一致

---
