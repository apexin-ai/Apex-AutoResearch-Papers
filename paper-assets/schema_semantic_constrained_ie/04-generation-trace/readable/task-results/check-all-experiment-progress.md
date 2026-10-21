# check all experiment progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_experiment_progress_20260518T175832_result.json`
- **Structured JSON:** [`6573cad275026a18515f.json`](../../sessions/65/6573cad275026a18515f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
P8c FT Latency:  unconstrained 177/551 (32%), constrained 未开始, ~3s/doc → unconstrained剩~19min, constrained ~28min, 总ETA ~47min
70B Unconstrained: 589/998 (59%), ~1.5min/doc → ETA ~10h
70B Constrained:   586/998 (59%), ~1.5min/doc → ETA ~10h
w9 sampling r2:    161/892 (18%), ~20s/doc → ETA ~4h
```

备注：
- 输出文件实际在 `/root/autodl-tmp/schema_outputs/`，不在 `/root/schema_semantic_constrained_ie/outputs/`
- 70B 两组基本同步推进，tmux pane 内容已滚空，但 jsonl 行数在增长，GPU 利用率 89%/88%，正常运行中
- P8c FT unconstrained 跑完后才会开始 constrained（constrained 文件尚不存在）
- w9 r2 每个 doc 耗时差异大（6s~65s），ETA 粗估

---
