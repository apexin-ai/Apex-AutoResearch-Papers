# code gpu speed fix

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu-speed-fix_20260521T194005_result.json`
- **Structured JSON:** [`0720f0c60056e760a60b.json`](../../sessions/07/0720f0c60056e760a60b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Qwen 在下载中（PID 25292），两个 shard 并行下载。预计 ~8 分钟完成。

---

## 任务完成报告

### 1. 网络诊断结果
| CDN | 速度 |
|-----|------|
| HF-Mirror (代理) | 270 bytes/s — **不可用** |
| ModelScope (代理) | ~0.6 MB/s |
| **ModelScope (无代理)** | **~12 MB/s** |

**关键发现：AutoDL 的 `network_turbo` 代理反而拖慢 ModelScope（国内 CDN），去掉代理后速度提升 20 倍。**

### 2. 选择的下载方案
- 方案：**ModelScope 无代理直连**
- 杀掉所有使用代理的下载进程，重启时 `unset` 所有 proxy 环境变量
- `max_workers=4` 并行下载多个 shard
- 优先 Llama（当时最接近完成），单模型独占带宽

### 3. 实际下载速度
- 代理下：0.6-1.0 MB/s（每个 shard）
- **无代理：10-12 MB/s（总计），每 shard 5-6 MB/s**

### 4. 第一个模型标注 ✅ 已完成
- **模型**：Llama-3.1-8B-Instruct
- **状态**：标注全部完成
- **结果**：500 条推文，0 失败，17.5 秒（28.5 tweets/s）
- **输出**：`/root/work/results/exp008_checkpoint_llama-3.1-8b_balanced.csv`
- **GPU**：cuda:0（RTX PRO 6000 Blackwell 97GB）
- **修复**：transformers 5.9 兼容性问题（`apply_chat_template` 返回类型变化 + `temperature=None` 参数），已修复所有 4 个标注脚本

### 5. 第二个模型下载进度
- **Qwen2.5-7B-Instruct**（PID 25292）：
  - model-00001: ✅ 完成 (1.1G)
  - model-00002: 2.2G / 3.60G (61%)
  - model-00003: ✅ 完成 (1.7G)
  - model-00004: 237M / 3.31G (7%)
  - **预计 ~04:13 完成**，下载完即可启动标注

### 时间线
- 03:44 — 开始诊断
- 03:49 — 发现无代理快 20 倍，重启下载
- 04:00 — Llama 下载完成
- 04:03 — **Llama 标注完成**（从诊断开始 ~19 分钟）
- ~04:13 — Qwen 预计下载完成

---
