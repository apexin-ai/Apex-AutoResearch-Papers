# ops disk emergency assessment

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_emergency_assessment_20260513T013022_result.json`
- **Structured JSON:** [`fa31fcf41ba566ee0924.json`](../../sessions/fa/fa31fcf41ba566ee0924.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，以下是报告。

---

## 磁盘评估报告

### 1. 磁盘总况
```
/dev/md0  169G  154G  16G  91%  /root/autodl-tmp
```

### 2. Top-10 目录分布

| 目录 | 大小 | 说明 |
|------|------|------|
| `models/` | **57G** | 离线模型（Mistral-7B, Qwen系列等） |
| `structfuse/` | **43G** | 项目主目录 |
| `.hf_cache/` | **35G** | HuggingFace 缓存 |
| `alfworld_data/` | 2.2G | 无关项目 |
| `mvp_results/` | 1.7G | 旧 MVP 结果 |
| `gpt2-small/` | 526M | 旧模型 |
| `mvp_data/` | 295M | 旧 MVP 数据 |
| `repos/` | 170M | 旧 repo |
| `rl-active-probe-fl/` | 160M | 无关项目 |
| `/tmp/` | 52M | 临时文件 |

#### structfuse/ 内部分布

| 子目录 | 大小 |
|--------|------|
| `checkpoints/` (4个p2b_*) | **24G** |
| `m1_repos/` | **11G** |
| `models/` | **5.8G** |
| `m1_extraction/` | 2.2G |
| `dryrun_repos/` | 554M |
| `mvp_data/` | 427M |
| `m1_training_data/` | 311M |

#### models/ 详情

| 模型 | 大小 |
|------|------|
| Qwen/ | 15G |
| Qwen2.5-7B-DPO003-merged | 15G |
| Qwen2.5-7B-Instruct-DPO-merged | 15G |
| Mistral-7B-Instruct-v0.3 | 14G |
| Qwen2.5-7B-Instruct | 552M |

#### .hf_cache/ 详情

| 目录 | 大小 |
|------|------|
| starcoder2-3b/ | 12G |
| Qwen3-14B-AWQ/ | 9.4G |
| datasets/ | 4.9G |
| Qwen/ | 984M |
| hub/ | 265M |

### 3. M1 空间需求预估

- **当前**: 2.2G extraction + 11G repos = 13.2G，已完成 23/131 repos (5413 JSON files)
- **extraction 增长率**: 2.2G / 23 ≈ **96MB/repo**
- **repos 增长率**: 11G / 23 ≈ **478MB/repo**（含 codeql_db）
- **剩余 108 repos 预估**:
  - extraction: 108 × 96MB ≈ **10.3G**
  - repos (若不清理): 108 × 478MB ≈ **51.6G**
- **总需求**: 最少 10.3G（仅 extraction），最多 62G（含 repo 累积）
- **可用空间**: 16G

### 4. 结论：**空间严重不足**

即使 pipeline 每次处理完自动删除 repo 和 codeql_db，仅 extraction JSON 增长 (10.3G) 就会占掉可用空间的 64%，缓冲极小。若 pipeline 不清理 repos，16G 根本不够。

### 5. 可安全清理项（由 Director 决定）

| 优先级 | 清理项 | 可释放 | 风险 |
|--------|--------|--------|------|
| **P0** | `checkpoints/p2b_*` (4个) | **~24G** | 低 — MVP 旧 checkpoint，训练结果已提取 |
| **P1** | `models/Mistral-7B-Instruct-v0.3` | **14G** | 低 — M1 不需要 Mistral |
| **P1** | `models/Qwen2.5-7B-DPO003-merged` | **15G** | 中 — 确认 M1 是否使用 |
| **P1** | `models/Qwen2.5-7B-Instruct-DPO-merged` | **15G** | 中 — 同上 |
| **P2** | `.hf_cache/starcoder2-3b/` | **12G** | 低 — M1 用的是 Qwen，非 StarCoder |
| **P2** | `.hf_cache/Qwen3-14B-AWQ/` | **9.4G** | 中 — 确认是否 M1 当前推理模型 |
| **P3** | `alfworld_data/` | **2.2G** | 无 — 无关项目 |
| **P3** | `mvp_results/` + `gpt2-small/` + `mvp_data/` | **2.5G** | 无 — 旧数据 |

**总可释放空间**: 最高 ~94G

### 6. 建议优先级

**紧急（保 M1 不崩）**: 清 P0 checkpoints 即释放 24G，加上当前 16G = 40G，足以覆盖 extraction 增长（10.3G）且有余量。

**如 repos 会累积**: 还需清 P1 的 1-2 个模型（+14~29G），确保 m1_repos 增长不爆盘。

**最安全的最小操作**: 仅删 `checkpoints/p2b_*`（24G），立刻解除危机。

---
