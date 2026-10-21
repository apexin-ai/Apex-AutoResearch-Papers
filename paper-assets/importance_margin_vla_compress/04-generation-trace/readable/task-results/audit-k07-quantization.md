# audit k07 quantization

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_k07_quantization_20260528T023215_result.json`
- **Structured JSON:** [`27e353e5fe0cfd952395.json`](../../sessions/27/27e353e5fe0cfd952395.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收齐。结论如下：

## Audit 结果：无量化 bug

### 计算公式
```python
N_PATCHES = (224 // 14) ** 2  # = 256
n_keep = max(1, int(N_PATCHES * keep_ratio))  # int() = floor truncation
```

所有 pruning 模式（random/l2norm/attention）共用同一公式，**无 round-to-64、block-size 对齐或任何量化逻辑**。

### 预期 vs 实际对照表

| k | 计算 | 预期 | 实际（日志） | 匹配 |
|---|------|------|-------------|------|
| 0.50 | int(128.0) | 128 | **128** (attn, w38) | ✅ |
| 0.70 | int(179.2) | 179 | **179** (attn, w41) | ✅ |
| 0.75 | int(192.0) | 192 | **192** (attn, w41) | ✅ |
| 0.85 | int(217.6) | 217 | **217** (l2norm, w38) | ✅ |
| 0.90 | int(230.4) | 230 | **230** (attn, w38) | ✅ |
| 0.95 | int(243.2) | 243 | **243** (random w38, l2norm cqa1) | ✅ |

### k=0.7 vs k=0.75

**完全不同**：179 vs 192，差 13 tokens。不存在量化到相同值的问题。

### 混淆来源

你提供的日志路径 `eval_pi05_attn_k07_long_seed44_strict_cqa1.log` 在 westd-41074 上不存在。该服务器上 k=0.7 是 `eval_pi05_attn_k07_long_seed43_strict_w41.log`（seed43），而 seed44 的文件是 `eval_pi05_attn_k075_long_seed44_strict_w41.log`（k=0.75）。你看到 192 很可能是读到了 k=0.75 seed44 的日志。

**结论：代码正确，无需修正。所有实验的 keep 数均符合预期。**

---
