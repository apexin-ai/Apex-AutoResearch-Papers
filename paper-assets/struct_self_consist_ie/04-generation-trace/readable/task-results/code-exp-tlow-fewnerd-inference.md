# code exp tlow fewnerd inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_tlow_fewnerd_inference_20260520T174228_result.json`
- **Structured JSON:** [`8f9c393652ecc1c7d3dd.json`](../../sessions/8f/8f9c393652ecc1c7d3dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并注册。中报告如下：

---

**exp_tlow_fewnerd_inference — 运行中**

| 项 | 值 |
|---|---|
| 运行命令 | `CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen25-7b-fewnerd-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --collect_logprobs --output_dir output/exp_tlow_fewnerd_t05_s42/` |
| Model | `checkpoints/qwen25-7b-fewnerd-merged` (Qwen2ForCausalLM, 14.25 GiB, loaded on GPU 2) |
| Data | `data/fewnerd/test.json`, 37648 instances |
| GPU | cuda:2 (RTX 5090, 30319/32607 MiB used) |
| 输出 | `output/exp_tlow_fewnerd_t05_s42/` (samples.jsonl + report.json) |
| 日志 | `output/exp_tlow_fewnerd_t05_s42.log` |
| PID | 221493 |
| 预计时长 | ~2 小时（参考 qwen3-8b FewNERD T=1.0 seed789 耗时约 2h） |
| 生成量 | 37648 × N=8 = 301,184 stochastic + 37648 greedy = ~339K generations |

脚本复用了 `code/run_mvp_pilot.py`（已有完整 FewNERD 支持），无需额外编写。vLLM 0.18.1 + XGrammar constrained decoding + logprobs 收集均已就绪。

---
