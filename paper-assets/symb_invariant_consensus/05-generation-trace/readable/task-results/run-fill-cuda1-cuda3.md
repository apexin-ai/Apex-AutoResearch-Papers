# run fill cuda1 cuda3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_fill-cuda1-cuda3_20260522T195751_result.json`
- **Structured JSON:** [`d642d47e676c5f605735.json`](../../sessions/d6/d642d47e676c5f605735.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 卡全部满载运行。

## 部署总结

### GPU 状态（4/4 满载）
| GPU | 显存 | 利用率 | 用途 |
|-----|------|--------|------|
| cuda:0 | 88239/97887 MiB | 97% | Qwen vLLM port 8001 → seed456 运行中 (不动) |
| cuda:1 | 88261/97887 MiB | 96% | **LLaMA vLLM port 8006** → PW seed123→456→789 chain |
| cuda:2 | 90451/97887 MiB | 96% | Mistral vLLM port 8003 → seed789 运行中 (不动) |
| cuda:3 | 88239/97887 MiB | 97% | **Qwen vLLM port 8005** → PW seed123 重跑 |

### 新启动实验

1. **cuda:3 — Qwen seed123 重跑** (PID 685233)
   - 独立 vLLM (port 8005)，不与 seed456 竞争 port 8001 吞吐
   - 600 samples, k=12, temperature=0.7
   - 日志: `/tmp/qwen25_pw_seed123_rerun.log`

2. **cuda:1 — LLaMA PW chain** (PID 685307)
   - 独立 vLLM (port 8006)
   - Chain: seed123 → seed456 → seed789 (各 600 samples)
   - 日志: `/tmp/multiseed_llama_pw_all.log`

### 清理
- 杀掉了 GPU 1 上遗留的 Qwen vLLM (port 8004, PID 680929)

### Tiebreaking
- 已验证 `pipeline.py:73` 和 `self_consistency.py:21` 均使用 `sorted()` — 符合 D061

### 预计完成时间
- Qwen seed123 (600 samples): ~4-6 小时 → 约 08:00-10:00
- LLaMA chain (3×600 samples): ~12-18 小时 → 约 16:00-22:00

---
