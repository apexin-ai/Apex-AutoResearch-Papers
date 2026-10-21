# code attn heads check

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_attn_heads_check_20260518T154026_result.json`
- **Structured JSON:** [`a2e01a949435cefda15c.json`](../../sessions/a2/a2e01a949435cefda15c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. attn.num_heads / attn.num_kv_heads

| 模型 | ratio | attn.num_heads | attn.num_kv_heads | num_heads(top) |
|---|---|---|---|---|
| **GDN** hybrid-3-1 | 3:1 | **16** | 8 | 8 |
| **GDN** hybrid-6-1 | 6:1 | 32 | 8 | 8 |
| **GDN** hybrid-12-1 | 12:1 | 32 | 8 | 8 |
| **GDN** hybrid-24-1 | 24:1 | 32 | 8 | 8 |
| **RetNet** hybrid-* | 全部 | 16 | 8 | 4 |
| **HGRN2** hybrid-* | 全部 | 16 | 8 | 8 |

### 2. Confound 分析

**GDN 存在 confound：** hybrid-3-1 的 `attn.num_heads=16`，其余三个 (6-1, 12-1, 24-1) 都是 `attn.num_heads=32`。不同 ratio 使用了不同的 attention head 数量。

**RetNet 和 HGRN2 无 confound：** 所有 ratio 的 attn heads 配置一致。

### 3. HGRN2 下载进度

- 下载进程仍在运行（PID 316964）
- **hybrid-12-1**: 2/2 safetensors ✅
- **hybrid-24-1**: 2/2 safetensors ✅
- **hybrid-3-1**: 2/2 safetensors ✅ (当前正在下载 shard 2)
- **hybrid-6-1**: 1/2 safetensors ⏳
- **pure**: 1/2 safetensors ⏳ (shard 1 刚下载失败，脚本应会重试)

---
