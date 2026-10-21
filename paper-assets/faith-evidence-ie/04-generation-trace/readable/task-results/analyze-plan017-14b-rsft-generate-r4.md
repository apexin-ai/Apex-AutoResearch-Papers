# analyze plan017 14b rsft generate r4

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan017_14b_rsft_generate_r4_20260520T180958_result.json`
- **Structured JSON:** [`351e633fddee66ff4ce3.json`](../../sessions/35/351e633fddee66ff4ce3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

**`plan017_14b_rsft_generate_r4` 成功完成。**

| 指标 | 结果 |
|------|------|
| 状态 | 正常退出 (EXIT_CODE=0) |
| 总 doc 数 | **3027**（全部完成） |
| 总生成数 | **24,216**（3027×8，符合预期） |
| 本次新增 | 474 docs（从 2553 resume） |
| 运行时间 | ~2h31m（474 docs） |
| Format OK | 24,206/24,216（**99.96%**，仅 10 条 format 失败） |
| Truncated | 1,701/24,216（7.0%，长输出被截断） |
| Diversity | mean=7.28/8, median=8.0/8 |
| 输出文件 | `generations.jsonl`，349MB |
| 磁盘剩余 | 116GB / 350GB（68% 已用） |

数据质量正常：每条包含 doc_id、generation_idx、prompt、output、format_ok、truncated、gold_triples 等完整字段，JSON 格式正确。

唯一注意点：7% 的 truncated 率和 10 条 format 失败，在 RSFT 筛选阶段会被过滤，不影响后续流程。

---
