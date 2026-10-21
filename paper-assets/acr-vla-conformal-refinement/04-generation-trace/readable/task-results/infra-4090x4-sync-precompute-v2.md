# infra 4090x4 sync precompute v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_4090x4-sync-precompute-v2_20260513T091703_result.json`
- **Structured JSON:** [`e48477d13d382110f82a.json`](../../sessions/e4/e48477d13d382110f82a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 shards actively processing. Here's the summary:

## 结果

### 1. autodl-4090x4 现状
| 项目 | 状态 |
|------|------|
| 4× RTX 4090 | 全部可用，各 ~1.4 GB 占用 |
| 源代码 (8 files) | 已有，与 autodl-4090 **完全一致** |
| LIBERO 数据 (94G) | 已有，spatial/object/goal/long/90 全部齐全 |
| SmolVLA 模型 | lerobot 格式，路径 `/root/autodl-tmp/models/SmolVLA/lerobot/smolvla_base/` |
| crm_cache | 空（无前次缓存） |
| tmux 残留 | 无 |

### 2. 代码同步
**不需要** — 两台服务器上所有 8 个源文件完全相同。

### 3. BDDL 修复
已将 `/tmp/libero_repo/libero/libero/assets` 复制到 `/root/miniconda3/lib/python3.12/site-packages/libero/assets`。验证通过：10 spatial tasks 加载成功，BDDL 文件存在。

### 4. VLM 依赖修复
- `HuggingFaceTB/SmolVLM2-500M-Video-Instruct` 通过 hf-mirror 下载到本地 HF 缓存
- 修复了 cache 目录结构（snapshot symlinks）
- 安装了缺失的 `num2words` 依赖
- SmolVLA 离线加载验证通过 (450M params)

### 5. 4-GPU 并行 precompute 状态
| Shard | GPU | 样本数 | 速度 | 预计剩余时间 |
|-------|-----|--------|------|-------------|
| 0 | GPU 0 (1419 MiB) | 3042 | **0.47 s/sample** | ~22 min |
| 1 | GPU 1 (1419 MiB) | 3042 | **0.45 s/sample** | ~22 min |
| 2 | GPU 2 (1419 MiB) | 3042 | **0.46 s/sample** | ~23 min |
| 3 | GPU 3 (1419 MiB) | 3041 | **0.43 s/sample** | ~21 min |

每个 shard 处理 spatial (3042 samples) + object 两个 benchmark。spatial 约 22 分钟完成，之后还要处理 object benchmark。

---
