# monitor m1 disk starcoder check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_m1_disk_starcoder_check_20260513T004643_result.json`
- **Structured JSON:** [`6200f4c5d0caf612e62e.json`](../../sessions/62/6200f4c5d0caf612e62e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### M1 提取进度
- **PID 577864**: 存活，已运行 **~4 小时**
- **已完成 repo**: **21/131** 个 unique repos 已产出 JSON
- **实例数**: **4,656** 个 JSON 文件
- **当前正在处理**: cantools, oauthlib, pyupio__safety, jaraco__inflect, Cog-Creators__Red-DiscordBot, mahmoud__boltons, joke2k__faker, pygments__pygments（多个 CodeQL Java 进程并行运行中）
- **跳过**: 部分 repo（如 pdfminer__pdfminer.six）因 `clone_failed` 跳过
- **最新日志**: `2026-05-13 08:47:37`，正常推进中

### 磁盘
| 项目 | 大小 |
|------|------|
| 数据盘总量 | 169G |
| 已用 | 132G (78%) |
| 可用 | **38G** |
| m1_extraction/ | 1.8G |
| structfuse/ 总计 | 43G |

### StarCoder2-3B 模型完整性
- **HF cache** (`/root/autodl-tmp/.hf_cache/starcoder2-3b/`): **完整** — `model.safetensors` 12G + config.json + tokenizer 全在
- **MS cache** (`/root/autodl-tmp/.ms_cache/AI-ModelScope/starcoder2-3b/`): **已删除** — 被清理 Worker 移除

模型可用，MS cache 是冗余副本，删掉没问题。

### 下载进程
无任何 starcoder/modelscope/download 相关进程在运行。

---
