# code pgpf pipeline

**pgpf collapse filter** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pgpf_pipeline_20260513T043831_result.json`
- **Structured JSON:** [`f67ddb0c2eb306d51875.json`](../../sessions/f6/f67ddb0c2eb306d51875.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。最终文件结构：

```
artifacts/pgpf/
├── __init__.py          # 包入口
├── config.py            # PGPFConfig/LoRAConfig/TrainingConfig/GenerationConfig dataclasses
├── utils.py             # 日志、种子、路径、JSONL I/O
├── property_scorer.py   # 四属性评分: lexical_conformity, semantic_novelty, quality, confidence
├── filters.py           # 5 种过滤策略 + build_filter 工厂
├── metrics.py           # self-BLEU, vocab coverage, embedding diversity, held-out PPL
├── data_prep.py         # OpenHermes-2.5 下载/格式化/split + CLI
└── recursive_loop.py    # RecursiveTrainingLoop 主循环 + CLI
```

验证结果：
- 无 GPU/torch 环境下所有模块可 import 无报错
- 5 种 filter 逻辑全部正确（NoFilter 100/100, RandomFilter 30/100, ConfidenceFilter 50/100, PGPFStatic 14/100, LexicalOnly 50/100）
- `build_filter` 工厂函数从 config 正确实例化
- JSONL 读写 roundtrip 正确
- `extract_assistant_texts` 提取正确

GPU 就绪后可直接 `python -m pgpf.data_prep` 准备数据，然后 `python -m pgpf.recursive_loop --filter_method pgpf_static` 启动实验。

---
