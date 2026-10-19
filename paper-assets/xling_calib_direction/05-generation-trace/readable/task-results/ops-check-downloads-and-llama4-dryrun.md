# ops check downloads and llama4 dryrun

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_downloads_and_llama4_dryrun_20260520T225932_result.json`
- **Structured JSON:** [`3136feb6ad57aa46cce2.json`](../../sessions/31/3136feb6ad57aa46cce2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 下载状态报告

### Llama4-Scout-W4A16 (`RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized.w4a16`)
| 项目 | 值 |
|---|---|
| 进程 PID | 32019 (running since 05:49) |
| 已下载 | **29.6GB** (cache, 9 个 incomplete 文件) |
| 已完成文件 | **0/14** safetensor shards (仅小文件 config/README 已完成) |
| 当前速度 | **~2 MB/s**（仅 1 个文件在活跃下载，其余 8 个 stalled） |
| 预估总大小 | ~63GB (14 shards × ~4.5GB) |
| 预估剩余 | **4-5 小时**（按当前速度，且只有 1 个 worker 活跃） |
| 架构 | `llama4`, 48 layers, hidden_size=5120, 16 local experts (MoE) |

**问题**：hf-mirror 仍在走 xet-bridge CDN，大量文件 read timeout 后 stall，实际并发只有 1 个。

### Qwen3-235B-A22B-GPTQ-Int4 (`Qwen/Qwen3-235B-A22B-GPTQ-Int4`)
| 项目 | 值 |
|---|---|
| 进程 PID | 32724 (running since 05:52) |
| 已下载 | **14.4GB** (cache, 8 个 incomplete 文件) |
| 已完成文件 | **0/32** safetensor shards |
| 当前速度 | **0 MB/s（完全 stalled）** |
| 预估总大小 | ~120GB (32 shards) |
| 架构 | `qwen3_moe`, 94 layers, hidden_size=4096 |

### 磁盘
```
/root/autodl-tmp: 350G total, 134G used, 217G available (39%)
```
两个模型完成后约需 ~183GB，空间充足。

### 诊断

两个下载都严重 stall。`HF_HUB_DISABLE_XET=1` 没有阻止 xet-bridge 重定向，hf-mirror 在 AutoDL 网络下走 xet CDN 极慢且频繁超时。

**建议操作**：
1. **Kill 当前下载进程**，改用 ModelScope 下载（AutoDL 国内 CDN 速度快很多）
2. ModelScope 上 Llama4 Scout 量化版可能没有，需要确认；Qwen3-235B-A22B-GPTQ-Int4 大概率有
3. 或者用 `hf_transfer` + 设置 `HF_HUB_ENABLE_HF_TRANSFER=1` 绕过 xet

需要我 kill 掉当前进程并切换下载方式吗？

---
