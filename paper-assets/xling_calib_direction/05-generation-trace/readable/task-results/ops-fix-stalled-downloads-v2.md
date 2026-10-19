# ops fix stalled downloads v2

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_stalled_downloads_v2_20260520T232004_result.json`
- **Structured JSON:** [`55d4269aae2679f179b8.json`](../../sessions/55/55d4269aae2679f179b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态汇总：
- 旧进程（32019, 32724）已终止
- hf_transfer 已安装，但 huggingface_hub 新版已弃用 `HF_HUB_ENABLE_HF_TRANSFER`，实际走普通 HTTP + `HF_HUB_DISABLE_XET=1`
- Llama4 下载 PID 36589（当前 33GB/63GB，需再下 30GB）
- Qwen3 下载 PID 36611（当前 19GB/120GB，需再下 101GB）
- 2.5 分钟后自动检查速度，如果慢于 2MB/s 将切换 ModelScope

---
