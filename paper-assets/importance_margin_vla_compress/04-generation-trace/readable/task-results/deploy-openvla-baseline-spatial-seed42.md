# deploy openvla baseline spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_openvla-baseline-spatial-seed42_20260521T222156_result.json`
- **Structured JSON:** [`4557802312a53bde0e78.json`](../../sessions/45/4557802312a53bde0e78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 前置检查结果

### 1. Spatial checkpoint: **不存在**
westd-27271 上只有 Object checkpoint:
- `/root/autodl-tmp/openvla-libero-object/` (15G)
- 无任何 `*spatial*` 目录
- 数据盘剩余 96G，空间充足

### 2. 脚本参数
`--mode baseline` 可用，但脚本有 3 处 Object 硬编码需改：
- L31: `CHECKPOINT_PATH = "/root/autodl-tmp/openvla-libero-object"`
- L32: `UNNORM_KEY = "libero_object"` (影响 action denormalization)
- L276: `"model": "openvla-7b-libero-object"` (结果记录)

脚本无 `--model_path` 参数，需要修改脚本或新建 Spatial 版本。

### 3. env.seed: **已修复**
L219: `env.seed(args.seed)` — 使用 `args.seed`。

### 需要你决定的

**Spatial checkpoint 不在 westd-27271 上。** 两个获取方案：

1. **HuggingFace 下载** (`openvla/openvla-7b-finetuned-libero-spatial`)，约 15G，AutoDL 建议用 ModelScope 或开 `network_turbo` 加速
2. **从 westd-41074 拷贝**（如果那台还活着且有 `/root/autodl-tmp/openvla-7b-finetuned-libero-spatial`）

脚本修改方面，我建议**给脚本加 `--model_path` 和 `--unnorm_key` CLI 参数**（保持现有默认值不变），这样不影响已有 Object 实验，Spatial 只需命令行指定即可。

怎么处理？

---
