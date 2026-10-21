# infra verify 32b downloads

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_32b_downloads_20260516T200027_result.json`
- **Structured JSON:** [`2637dfe286b6b5695cd7.json`](../../sessions/26/2637dfe286b6b5695cd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果：下载未完成，仍在进行中

### Step 1: 进程状态
```
两个下载进程仍在运行：
- PID 213895: snapshot_download("deepseek-ai/DeepSeek-R1-Distill-Qwen-32B") — CPU 29.5%
- PID 213886: snapshot_download("Qwen/QwQ-32B") — CPU 24.7%
```

### Step 2: 下载日志尾部
**R1-Distill-Qwen-32B:**
```
model-00006-of-000008.safetensors:  52% | 4.21G/8.17G [09:54<17:39, 4.02MB/s]
model-00005-of-000008.safetensors:  23% | 1.92G/8.17G [09:54<15:47, 7.09MB/s]
model-00004-of-000008.safetensors:  14% | 1.12G/8.17G [09:54<51:57, 2.43MB/s]
model-00001-of-000008.safetensors:  18% | 1.44G/8.19G [09:54<31:38, 3.82MB/s]
```

**QwQ-32B:**
```
model-00007-of-00014.safetensors:  75% | 3.39G/4.54G [09:54<02:25, 8.52MB/s]
model-00006-of-00014.safetensors:  31% | 1.39G/4.54G [09:54<24:42, 2.28MB/s]
model-00004-of-00014.safetensors:  47% | 2.11G/4.54G [09:54<05:56, 7.30MB/s]
model-00003-of-00014.safetensors:  26% | 1.16G/4.54G [09:54<13:54, 4.34MB/s]
model-00001-of-00014.safetensors:  20% | 928M/4.56G [09:54<26:11, 2.49MB/s]
```

### Step 3: safetensors 文件（>1G）
| 模型 | 已完成文件数 | 需要总数 | 状态 |
|------|------------|---------|------|
| R1-Distill-Qwen-32B | 7（1完成 + 6在temp） | 8 | 缺 model-00002 |
| QwQ-32B | 5（全在temp） | 14 | 缺 9 个 |

**R1-32B 已有文件：**
```
model-00008 (3.8G) — 已完成（在最终目录）
model-00001 (1.5G), model-00003 (2.2G), model-00004 (1.2G), model-00005 (2.0G), model-00006 (4.3G), model-00007 (3.5G) — 在 ._____temp/ 中，正在下载
```

**QwQ-32B 已有文件：**
```
model-00003 (1.2G), model-00004 (2.2G), model-00006 (1.4G), model-00007 (3.5G), model-00008 (4.0G) — 全在 ._____temp/
```

### Step 4: config.json
```
✅ R1-32B: /root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B/config.json (664B)
✅ QwQ-32B: /root/autodl-tmp/.hf_cache/Qwen/QwQ-32B/config.json (662B)
```

### Step 5: 磁盘占用
```
deepseek-ai/: 19G
Qwen/:        2.0M（safetensors 都在 ._____temp/ 所以这里只有 config）
总 .hf_cache/: 62G
磁盘: /dev/md0 250G, 已用 65G, 可用 186G (26%)
```

### 进度评估

| 模型 | 预计总大小 | 当前进度 | 预估剩余时间 |
|------|-----------|---------|-------------|
| R1-Distill-Qwen-32B (8 shards × ~8G = ~65G) | ~40% | ~30-50 min |
| QwQ-32B (14 shards × ~4.5G = ~63G) | ~20% | ~50-70 min |

**结论：两个模型都还在下载中，预计还需 50-70 分钟完成。磁盘空间充足（186G 可用），不会爆盘。**

---
