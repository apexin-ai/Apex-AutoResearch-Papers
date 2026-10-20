# exp aave corpus gen cuda3

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_aave-corpus-gen-cuda3_20260512T142200_result.json`
- **Structured JSON:** [`f0cc3e4cf3227ae8c06d.json`](../../sessions/f0/f0cc3e4cf3227ae8c06d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常运行。

## 汇总

| 项目 | 值 |
|------|-----|
| vLLM gen PID | 141024 (worker: 141319) |
| vLLM 端口 | 8001，served-model: `democalib-qwen-gen` |
| vLLM 额外参数 | `--enable-auto-tool-choice --tool-call-parser hermes`（脚本的 agent 端需要 tool calling） |
| Corpus gen PID | 142096 |
| 实际参数 | `--model-name democalib-qwen-gen --base-url http://localhost:8001 --dialect aave --num-tasks 20 --num-trials 5 --target-question-rate 0.10 --target-politeness-rate 0.20 --output-dir /root/democalib/synthetic_corpus --gpu-id 0` |
| GPU 2 (mvp-004) | PID 110596, 22096 MiB — 未受影响 |
| GPU 3 (corpus gen) | PID 141319, 22094 MiB |
| 日志 | `/root/democalib/results/aave_corpus_gen.log` |
| 状态 | LiteLLM 持续调用中，无报错，trace 正在生成到 `synthetic_corpus/tau_bench_logs/` |

注：首次启动未加 `--enable-auto-tool-choice --tool-call-parser hermes`，导致 agent 端 tool_choice="auto" 报 400 错误。已重启 vLLM 加上该参数，语料生成正常进行。

---
