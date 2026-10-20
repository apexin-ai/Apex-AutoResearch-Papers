# code sica folio30 prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sica_folio30_prep_20260515T221825_result.json`
- **Structured JSON:** [`fab44a8878056ef6a0bc.json`](../../sessions/fa/fab44a8878056ef6a0bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

FOLIO SICA 实验准备完成。

## 总结

### 已就绪的组件

| 组件 | 状态 | 路径 |
|------|------|------|
| 评估脚本 | 已有且验证通过 | `/root/symb_invariant_consensus/eval_folio.py` |
| 数据加载器 | 已有 | `data/folio_loader.py` |
| 数据集 (30题) | 已有，True/False/Unknown 各10题 | `data/folio_subset.json` |
| FOLIO prompt模板 | 已有 | `sica/trace_generator.py` (FOLIO_PROMPT) |
| Pipeline FOLIO支持 | 已有 (domain auto-detect) | `sica/pipeline.py` |
| vLLM QwQ-32B | 运行中 | `localhost:8000` |

### Dry-run 结果
- 30/30 题 prompt 组装通过 (premises=Y, conclusion=Y, boxed_instr=Y)
- 6/6 答案提取测试通过 (boxed + fallback + normalization)

### Live test 结果 (2题, K=4)

| 题目 | SICA | SC | 约束数 | 去重后 | MAX-SAT | 耗时 |
|------|------|----|--------|--------|---------|------|
| folio_000 | True (V) | True (V) | 27→25 | 25/25 satisfied | 0.9ms | 288s |
| folio_001 | True (V) | True (V) | 23→17 | 16/17 satisfied | 0.7ms | 95s |

### 已更新
- `eval_folio.py` max_tokens 默认值 12288→16384
- Registry `sica_folio30` 状态更新为 QUEUED，spec 包含完整运行命令

### 正式实验启动命令
```bash
cd /root/symb_invariant_consensus && python eval_folio.py --n-problems 30 --k 12 --temperature 0.7 --max-tokens 16384 --seed 42 --save-intermediates --output results/folio_eval.json
```

预估耗时：30题 × K=12 × ~5min/题 ≈ 2.5h（受 vLLM 并发影响可能更长）。

---
