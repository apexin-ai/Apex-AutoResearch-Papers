# infra disk cleanup

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk_cleanup_20260520T193629_result.json`
- **Structured JSON:** [`9f6f9a0910c55421ee66.json`](../../sessions/9f/9f6f9a0910c55421ee66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 磁盘清理报告

| | 清理前 | 清理后 |
|---|---|---|
| 根分区 `/` | 91% (3.0G free) | 91% (3.0G free) |
| 数据盘 `/root/autodl-tmp` | 10% (318G free) | 不变 |

**清理的内容**：27 个 pip 日志（/tmp）、5 个 `__pycache__` 目录 — 总共仅几 MB，对使用率无实质影响。

**根分区占用分布**：
- `/root/miniconda3/` — 13G（conda 环境，不可删）
- `/root/nlp_variance_gtheory/models/.hf_cache/` — **15G**（Llama-3.1-8B-Instruct 模型）

**真正能释放空间的操作**：将模型缓存迁移到数据盘。执行的话可以释放 ~15G，根分区降至约 41%：

```bash
mv /root/nlp_variance_gtheory/models/.hf_cache /root/autodl-tmp/.hf_cache
ln -s /root/autodl-tmp/.hf_cache /root/nlp_variance_gtheory/models/.hf_cache
```

需要我执行模型迁移吗？

---
