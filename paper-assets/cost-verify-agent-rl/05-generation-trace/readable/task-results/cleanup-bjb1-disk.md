# cleanup bjb1 disk

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_bjb1_disk_20260521T074043_result.json`
- **Structured JSON:** [`09d6d4b8f9d10d543033.json`](../../sessions/09/09d6d4b8f9d10d543033.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 安全清理完成

| 清理项 | 释放空间 | 所在分区 |
|--------|---------|---------|
| pip cache (973 files) | ~5.4G | 根分区 |
| conda cache (373 MB) | ~0.4G | 根分区 |
| /root/autodl-tmp/tmp/ | ~467M | 数据盘 |
| /tmp/ ray/pymp 临时文件 | ~467M | 根分区 |

- **根分区**: 48% → **28%** (释放 ~6.7G)
- **数据盘**: 仍为 **93%** (231G/250G)，几乎没变

### 数据盘仍需释放 ~31G

安全清理不足以达标。以下是 >1GB 的候选项，需要你决定删哪些：

| 目录 | 大小 | 说明 |
|------|------|------|
| `checkpoints/hsweep-h2/` | **41G** | 超参搜索 |
| `checkpoints/qwen3_8b_sft_v1/` | **31G** | 旧版 SFT |
| `checkpoints/hsweep-h20/` | **21G** | 超参搜索 |
| `checkpoints/exp029/` | **21G** | seed1 训练 |
| `checkpoints/exp029-seed3/` | **21G** | seed3 训练 |
| `checkpoints/exp029-seed4/` | **21G** | seed4 训练（step 8 崩溃的） |
| `checkpoints/scienceworld_sft/` | **7.6G** | ScienceWorld SFT |
| `checkpoints/exp029_hf/` | **3.8G** | HF 格式导出 |
| `.hf_cache/` | **23G** | HuggingFace 缓存 |
| `conda-envs/` | **12G** | conda 环境 |
| `models/` | **6.7G** | 模型文件 |

**不能删**: `checkpoints/exp021_ragen_sft_v4/` (23G, SFT 基线)

请告诉我删哪些。删任意两个超参搜索目录（hsweep-h2 + hsweep-h20 = 62G）就能降到 <70%。

### Seed 4 配置确认

- **save_freq: 5** ✅
- **optimizer_offload: false** ✅

---
