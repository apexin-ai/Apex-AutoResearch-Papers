# experiment deepseek r1 distill sica

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_deepseek-r1-distill-sica_20260521T131900_result.json`
- **Structured JSON:** [`bfaf73841b4105f6da2b.json`](../../sessions/bf/bfaf73841b4105f6da2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

问题 1 完成，已进入问题 2。Pipeline 运行正常。

## 报告

| 项目 | 详情 |
|------|------|
| **模型路径** | `/root/autodl-tmp/models/deepseek-ai/DeepSeek-R1-Distill-Llama-8B/` |
| **vLLM PID** | 441147 |
| **端口** | 8003 (cuda:3) |
| **显存占用** | 83,361 / 97,887 MiB (85%) |
| **Wrapper PID** | 440997 |
| **启动命令** | `bash scripts/run_exp_r1_distill_8b_sica.sh` |
| **结果目录** | `results/exp_r1_distill_8b_sica/` |
| **Pipeline 参数** | K=12, T=0.7, seed=42, FOLIO-204, max_tokens=4096 |
| **日志文件** | wrapper: `/tmp/sica_r1_distill_wrapper.log`, vLLM: `/tmp/vllm_r1_distill.log`, pipeline: `results/exp_r1_distill_8b_sica/pipeline.log` |

**注意事项**：
- 首次启动因 FlashInfer 不兼容 Blackwell GPU (sm100) 失败，已加 `VLLM_USE_FLASHINFER_SAMPLER=0` 修复
- R1-Distill 的 `&lt;think>` 块导致部分 extraction 因 context length 超 8192 而 400 报错，pipeline 会跳过失败的 extraction 继续运行
- `_strip_thinking()` 已内置于 pipeline 中，无需额外适配
- 问题 1 耗时约 1.5 分钟，204 题预计 **5-6 小时**完成

---
