# analysis mvp structural scoring v3

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_structural_scoring_v3_20260515T062101_result.json`
- **Structured JSON:** [`809916f5b93c4740de2b.json`](../../sessions/80/809916f5b93c4740de2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据已提取。

---

## mvp_structural_scoring_v3 实验结果

### 核心 Metrics

| 指标 | 值 |
|------|-----|
| Instances | 33 |
| Total segments | 566 |
| Scored (valid) | 539 |
| Keep | 41 (7.6%) |
| Drop | 498 (92.4%) |
| Failed | 27 |
| **Error rate** | **4.8%** |
| Avg confidence (keep) | 0.793 |
| Avg confidence (drop) | 0.912 |
| 耗时 | 824.1s |

### 与前次实验对比

| 指标 | v_clean (max_tokens=256) | **v3 (max_tokens=1024)** |
|------|--------------------------|--------------------------|
| Error rate | 28.5% (140/491) | **4.8% (27/566)** |
| Parse failure | 117 | 27 (全部是 parse failure) |
| API failure | 23 | 0 |
| Keep rate | — | 7.6% |

**Error rate 下降 83%**（28.5% → 4.8%）。API failure 完全消除，parse failure 从 117 降到 27。

### 假设验证

**假设成立**：error_rate = 4.8% < 5% 阈值，刚好达标。

### 需要注意的问题

1. **27 个 parse failure 全部是 JSON 格式错误**，不是 token 截断。查看 reasoning 可见 LLM 输出了接近正确的 JSON 但有语法错误（如 `confidence: 1.0.95`、重复 key `"label": "label"`、缺少引号等）。这说明 max_tokens 已不是瓶颈，剩余错误是 LLM 生成格式不稳定导致的。
2. **Keep rate 仅 7.6%**（41/539），即绝大多数 structural segments 被判定为 drop。如果这与预期一致（structural segments 大多是常规执行路径），则正常；否则需检查 prompt 是否过于严格。
3. **7 个实例被标注为 too_small/low_segment_count**（httpie_1, tqdm_2, scrapy_4, scrapy_7, luigi_5/10/14），2 个被排除（fastapi_3, fastapi_5）。
4. **进一步优化方向**：剩余 27 个 parse failure 可通过更鲁棒的 JSON 解析（如 regex fallback 或 `json_repair` 库）回收，预计可将 error rate 降到 ~0%。

---
