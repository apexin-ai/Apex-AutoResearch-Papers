# code data prep

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data-prep_20260514T051737_result.json`
- **Structured JSON:** [`93cf0969da114fc82224.json`](../../sessions/93/93cf0969da114fc82224.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。文件结构：

```
compresslink_code/
├── compresslink/
│   ├── __init__.py
│   ├── data_loader.py      # NQDataLoader: JSONL加载、prompt格式化、chunk切分
│   ├── calibration.py      # KVTCCalibrator: hook收集NoPE KV → per-head SVD → save/load .pt
│   └── metrics.py          # normalize_answer, compute_exact_match, compute_f1
├── scripts/
│   ├── prepare_nq_data.py  # 流式下载NQ validation → 筛选500条 → JSONL
│   └── run_calibration.py  # CLI: 加载模型 → 校准 → 保存calibration.pt
└── tests/
    ├── __init__.py
    └── test_metrics.py      # 18个单元测试，全部通过
```

关键设计点：
- **calibration.py** 通过 `k_proj`/`v_proj` 的 forward hook 捕获 RoPE 之前的 key/value（即 NoPE 形式），无需修改模型代码
- **prepare_nq_data.py** 使用 streaming 模式加载 `natural_questions`，避免下载 42GB 全量数据；从 long_answer span 提取 context，从 short_answers 提取答案
- **data_loader.py** 的 `format_prompt` 返回 `context_end_pos` 和 `chunk_boundaries`，供后续 boundary recomputation 使用

---
