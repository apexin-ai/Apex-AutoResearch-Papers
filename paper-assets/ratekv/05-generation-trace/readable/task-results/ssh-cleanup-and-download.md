# ssh cleanup and download

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cleanup_and_download_20260515T222523_result.json`
- **Structured JSON:** [`9fb25dc558e6e89dadc3.json`](../../sessions/9f/9fb25dc558e6e89dadc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个下载都在运行。汇总：

---

### 磁盘
- 删除 `prov_grounded_uie/` 后释放约 15G，当前 83G 可用（67% 使用）
- 两个模型合计约 ~30G（InternLM2 ~15G + Phi-3-medium ~27G safetensors），磁盘够用

### 候选模型架构

| 模型 | layers | attn | kv_heads | GQA | total_kv_heads |
|------|--------|------|----------|-----|----------------|
| **InternLM2-7B** | 32 | 32 | 8 | 4:1 | **256** |
| **Phi-3-medium** | 40 | 40 | 10 | 4:1 | **400** |
| OLMo-7B | 32 | 32 | 32 | 1:1 (MHA) | **1024** |

### 下载状态
| 模型 | PID | 来源 | 状态 |
|------|-----|------|------|
| InternLM2-7B | 379325 | HuggingFace | 下载中（14 files, ~2s/file） |
| Phi-3-medium | 379197 | ModelScope | 下载中（~1.5MB/s, 6 shards） |

### Spread 推荐

**InternLM2-7B 最有潜力**：total_kv_heads=256（GQA 4:1），KV head 数量最少，head 间异质性最高，RateKV 的 per-head 差异化分配策略收益空间最大。

**Phi-3-medium 次优**：total_kv_heads=400（GQA 4:1），且是 14B 参数量级，可以验证 scaling 效果。

**OLMo-7B 不推荐**：MHA（无 GQA），1024 个 KV heads 全等价，RateKV 的 spread 优势难以体现。

---
