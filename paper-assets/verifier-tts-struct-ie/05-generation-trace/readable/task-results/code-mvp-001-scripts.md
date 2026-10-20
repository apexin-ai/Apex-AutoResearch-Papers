# code mvp 001 scripts

**verifier tts struct ie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-001-scripts_20260511T165016_result.json`
- **Structured JSON:** [`34c322c6f865c07b12c2.json`](../../sessions/34/34c322c6f865c07b12c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。文件清单：

| 文件 | 功能 |
|------|------|
| `scripts/prepare_data.py` | 加载 SciERC 数据，输出 `test_gold.jsonl` + 8 个 shard 文件 |
| `scripts/inference.py` | 调用 vLLM API，N 个候选一次返回，JSON 解析+容错 |
| `scripts/evaluate.py` | Entity-level micro-F1，exact match，per-type 分类 |
| `scripts/aggregate.py` | 3 种选择策略（self-consistency/oracle/random），汇总所有 N×seed 结果 |
| `scripts/run_experiment.sh` | 一键脚本：启动 vLLM → 数据准备 → N=1,4,8,16 推理 → 聚合评估 → 关闭 vLLM |

关键设计点：
- `inference.py` 用 vLLM 的 `n` 参数一次请求返回 N 个候选（非循环 N 次）
- N=1 时 temperature=0 greedy，只跑 seed=42；N>1 时 temp=0.7, top_p=0.9, 3 seeds
- `aggregate.py` 的 self-consistency 先用 `doc_text.find()` 定位 entity span 偏移，再算 span IoU（>=50% 匹配阈值），无偏移时回退到 text exact match
- `run_experiment.sh` 支持 `NUM_GPUS` 参数（默认 8），带 health check 超时保护

---
