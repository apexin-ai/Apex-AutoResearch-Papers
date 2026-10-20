# infra cpu deps and datagen

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cpu_deps_and_datagen_20260520T155323_result.json`
- **Structured JSON:** [`cfa5b50af6a488989650.json`](../../sessions/cf/cfa5b50af6a488989650.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，三个产出文件已验证：

| 文件 | 结果 |
|------|------|
| `data/mmlu_items.json` | 50 items, 5 subjects |
| `data/few_shot_examples.json` | 5 subjects × 2 orderings |
| `design_matrix.csv` | 108 rows, 8 columns |

注意事项：
- CPU 依赖已全部预装（含 generalizit），无需额外安装
- `pip install -e .` 因 setuptools 后端问题失败，数据生成改用 `PYTHONPATH` 方式运行
- HF 数据下载需 `HF_ENDPOINT=https://hf-mirror.com` + 不走代理才稳定（直连 HF 和走代理都不行）

---
