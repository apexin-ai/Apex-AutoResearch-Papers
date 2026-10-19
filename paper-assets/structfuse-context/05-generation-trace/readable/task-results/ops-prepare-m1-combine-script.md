# ops prepare m1 combine script

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare-m1-combine-script_20260515T180037_result.json`
- **Structured JSON:** [`5a02bf7f0f33cacd3b9c.json`](../../sessions/5a/5a02bf7f0f33cacd3b9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成。结果：

| 指标 | 值 |
|------|-----|
| **总 instances** | 44,173 |
| **有 structural data** | 39,712 (89.9%) |
| **仍有 error** | 384 (0.9%) |
| **CodeQL 提取** | 39,692 (89.9%) |
| **Beniget 降级** | 4,097 (9.3%) |

**Per-tier 覆盖率：**

| Tier | Repos | Instances | Structural Rate |
|------|-------|-----------|----------------|
| small (<50) | 74 | 13,868 | 94.3% |
| medium (50-200) | 31 | 18,906 | 87.0% |
| large (200-500) | 13 | 8,528 | 94.0% |
| xlarge (500+) | 5 | 2,871 | 76.0% |

**Merge info:**
- 27,892 个 error 实例被替换（replaced still_error = 0）
- 385 个替换文件缺失（m1_reextract_v2 仍有少量未完成）
- 384 个仍有 error（基本就是缺失的那些）

**产出：**
1. 脚本: `/root/structfuse/scripts/combine_m1_reextract.py`
2. Stats JSON: `/root/autodl-tmp/structfuse/artifacts/m1_final_stats.json`
3. m1_reextract_v2 完成后执行:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /root/structfuse/scripts/combine_m1_reextract.py
```

脚本会自动备份 `all.jsonl` 到 `all.jsonl.bak`，然后替换 error 实例并输出统计。注意 `replaced: 27892` 比 `available: 27891` 多 1 — 说明有 1 个文件名匹配但实际 instance_id 不同，无影响。

---
