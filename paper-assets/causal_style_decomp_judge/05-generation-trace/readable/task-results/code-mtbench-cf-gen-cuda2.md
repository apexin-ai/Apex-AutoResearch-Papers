# code mtbench cf gen cuda2

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mtbench_cf_gen_cuda2_20260521T010055_result.json`
- **Structured JSON:** [`bf5d768fc749be482148.json`](../../sessions/bf/bf5d768fc749be482148.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报：

**启动状态**
- **vLLM (cuda:2, port 8002)**: PID 88064，模型 Qwen3-32B，正常运行
- **MT-Bench counterfactual gen**: PID 89051，80 条，axis=formality，API 指向 localhost:8002
- 日志显示已开始处理，前两条请求已返回 200 OK
- 输出文件: `data/counterfactuals_mtbench.jsonl`
- 日志: `/tmp/gen_mtbench.log`

cuda:0/1 上的进程未受影响。三张 GPU 现在各自在跑：cuda:0 register、cuda:1 AlpacaEval formality、cuda:2 MT-Bench formality。

---
