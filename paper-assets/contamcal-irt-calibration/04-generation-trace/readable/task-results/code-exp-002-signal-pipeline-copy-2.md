# code exp 002 signal pipeline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-002-signal-pipeline_20260515T143755_result.json`
- **Structured JSON:** [`ac65d714d13c4ee7f8b8.json`](../../sessions/ac/ac65d714d13c4ee7f8b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

**结果**：
- S2 (Min-K%++) dry-run 在 gsm8k 上完成：1319 items，~40 秒（target 17s + ref 17s）
- 输出格式符合要求：`{"item_id": "gsm8k_0000", "signal": "s2_minkpp", "score": -1.734, "metadata": {...}}`
- 自动使用 base model 作为 reference（因为 d000 adapter 和 target 相同，没有更"clean"的参考）

**已部署文件**：
```
exp002/
├── compute_signals.py      # 主入口 (--signal s1/s2/s3/s4/all)
├── utils.py                # 共享工具 (模型加载、benchmark 加载、格式化)
├── signals/
│   ├── __init__.py         # SIGNAL_MAP 注册
│   ├── s1_embedding.py     # FAISS + sentence-transformers
│   ├── s2_minkpp.py        # Min-K%++ (已验证)
│   ├── s3_constat.py       # ConStat performance gap
│   └── s4_selfcritique.py  # Self-critique entropy
└── README.md
```

---
