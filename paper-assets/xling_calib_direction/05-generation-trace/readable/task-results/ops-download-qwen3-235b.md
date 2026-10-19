# ops download qwen3 235b

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download_qwen3_235b_20260520T210956_result.json`
- **Structured JSON:** [`293b8804d638e51fd17e.json`](../../sessions/29/293b8804d638e51fd17e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已清理。GPU 配置：4× RTX PRO 6000 Blackwell (96GB each)，总 VRAM 384GB。

## 报告

### 下载状态：**失败 — 磁盘空间不足**

| 项目 | 详情 |
|------|------|
| 模型 | Qwen3-235B-A22B (MoE, 235B total / 22B active) |
| BF16 大小 | ~439GB (118 shards × 3.72GB) |
| 可用磁盘 | 263GB (`/root/autodl-tmp/`) |
| **缺口** | **~176GB** |
| GPU | 4× RTX PRO 6000 Blackwell, 96GB each, 总 384GB VRAM |

### INT4 量化方案评估

bitsandbytes 和 auto-gptq 均未安装。

**推荐方案：BnB 4-bit (NF4)**
- INT4 量化后模型约 **~120GB 磁盘**，可以放下（263GB 可用）
- 4 张 96GB GPU 总 VRAM 384GB，BF16 加载都够（需 ~470GB 含 KV cache，不够），INT4 约 120GB + KV cache 完全没问题
- 不需要预先下载量化版，直接下载 BF16 权重 + `load_in_4bit=True` 在线量化即可
- 但 BF16 权重本身就需要 439GB 磁盘，**依然放不下**

### 可行方案

1. **下载预量化的 GPTQ/AWQ 版本**（如 `Qwen/Qwen3-235B-A22B-GPTQ-Int4` 或社区量化版），磁盘占用约 120GB，263GB 够用
2. **扩容数据盘**到 600GB+，再下载 BF16 原版
3. **清理现有数据**释放空间（当前已用 88GB），但仍不够补齐 176GB 缺口

建议选方案 1，下载预量化版本。需要我查找并下载 Qwen3-235B-A22B 的 INT4 量化版吗？

---
