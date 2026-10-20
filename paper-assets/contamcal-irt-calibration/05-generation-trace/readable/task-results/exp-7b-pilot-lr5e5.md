# exp 7b pilot lr5e5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_7b-pilot-lr5e5_20260518T072853_result.json`
- **Structured JSON:** [`f38a154da5eefd0c1736.json`](../../sessions/f3/f38a154da5eefd0c1736.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态：
- **模型下载**：进行中，1/4 safetensors 完成，12GB/~15GB
- **SFT 数据**：已确认，50000 行，格式正确
- **GPU 0**：空闲（0MiB 占用）
- **训练脚本**：已确认 `--lr` 参数存在，默认 2e-4，将显式传 5e-5
- **无 `--max-steps` 参数**：dry-run 将用小数据子集（head 前几行）代替

2 分钟后自动检查下载进度。

---
