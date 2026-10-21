# code prep exp020 folio204

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp020-folio204_20260517T084309_result.json`
- **Structured JSON:** [`06815edff2238b7a5239.json`](../../sessions/06/06815edff2238b7a5239.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪，语法检查通过。汇总：

| 项目 | 值 |
|---|---|
| 脚本路径 | `/root/symb_invariant_consensus/scripts/run_exp020_llama8b_folio204.sh` |
| 模型路径 | `/root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct` |
| 数据文件 | `data/folio_full.json`（204 题） |
| K=12, T=0.7, max-tokens=4096, max-model-len=8192 | |
| 输出目录 | `results/exp020_llama8b_folio204/` |
| 端口 | 8000 |
| seed | 42 |
| dry-run | 通过 |

脚本已经存在且配置正确（与 exp-011/exp-019 参数一致），包含 vLLM 旧进程清理 + conda 激活 + 错误退出处理。exp-019 完成后可直接用 `bash scripts/run_exp020_llama8b_folio204.sh` 提交。

预估运行时间：204 题 x K=12 x 多轮推理，参考 exp-019（200 题 StrategyQA）的速度，FOLIO 推理链更长，预计 **3-5 小时**。

---
