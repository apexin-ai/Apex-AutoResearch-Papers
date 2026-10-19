# ops disk cleanup urgent

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-urgent_20260521T083650_result.json`
- **Structured JSON:** [`a54a1d07173715a373e2.json`](../../sessions/a5/a54a1d07173715a373e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇报：

| 项目 | 详情 |
|------|------|
| **旧 HF 文件路径** | `/root/autodl-tmp/models/Llama4-Scout-W4A16/` 顶层 (8个 safetensors + 配置文件 + .cache/) |
| **旧 HF 文件大小** | ~44GB（218GB → 174GB used） |
| **ModelScope 下载路径** | 同目录下 `._____temp/` (13GB 临时) + `RedHatAI/` (目标) |
| **已删除** | 旧 HF safetensors、配置文件、.cache/huggingface |
| **保留** | `._____temp/`、`.lock/`、`RedHatAI/`（ModelScope 活跃使用） |
| **删除后可用空间** | **177GB**（从 133GB 增加 44GB） |

177GB 足够容纳 Qwen3 (~60GB) + Llama4 ModelScope 剩余部分 (~52GB)。

---
