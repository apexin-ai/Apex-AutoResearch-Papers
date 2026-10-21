# experiment 70b sica deploy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_70b-sica-deploy_20260521T122922_result.json`
- **Structured JSON:** [`c36ac7da6953cb10adb2.json`](../../sessions/c3/c36ac7da6953cb10adb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 正在处理 12 个并发请求（=K=12 traces），生成吞吐约 30 tokens/s。一切正常。

当前状态汇总：

**vLLM 服务**
- PID: 435076（EngineCore PID: 435354）
- 端口: 8002
- GPU: cuda:2，显存 ~88 GB（38.76 GiB 模型 + KV cache）
- 模型: Qwen2.5-72B-Instruct-AWQ（`--max-model-len 8192`）
- 吞吐: ~30 tokens/s，12 并发请求

**SICA Pipeline**
- PID: 436077
- 配置: FOLIO-204, K=12, T=0.7, seed=42
- 输出: `results/exp_d126_70b_sica/results.json`
- 日志: `results/exp_d126_70b_sica/pipeline.log` 和 `/tmp/sica_d126_wrapper.log`

**预计完成时间**
- 204 个问题，每个问题 K=12 traces @ ~30 tok/s
- 单问题约 1.5-3 分钟（trace generation + constraint extraction）
- 预计总时长 ~5-10 小时（204 * ~2min）

注意：最初因 `--max-model-len 4096` 与 `--max-tokens 4096` 冲突导致 400 错误，已修正为 `--max-model-len 8192`。cuda:3 保持空闲。

---
