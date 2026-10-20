# diag gpu usage check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu_usage_check_20260518T084935_result.json`
- **Structured JSON:** [`e270961768203abaf830.json`](../../sessions/e2/e270961768203abaf830.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 占用汇总

| GPU | 状态 | 显存占用 | GPU 利用率 | 进程 |
|-----|------|----------|-----------|------|
| cuda:0 | **占用** | 30194 / 32607 MiB | 87% | `VLLM::EngineCore` (PID 133921) |
| cuda:1 | 空闲 | 2 / 32607 MiB | 100%* | 无 |
| cuda:2 | 空闲 | 2 / 32607 MiB | 100%* | 无 |
| cuda:3 | 空闲 | 2 / 32607 MiB | 100%* | 无 |

*cuda:1-3 GPU-Util 显示 100% 但无进程占用显存，可能是 driver 残留状态或计数器异常，实际空闲。

**LLaMA Few-NERD 训练**: 无训练进程运行，未找到训练脚本。仅有 `analyze_llama_fewnerd.py` 分析脚本。训练已结束或未启动。

**Qwen Few-NERD seed=123 推理**: 正在 cuda:0 上运行（单卡 vLLM），进度 19728/301184 (~6.5%)，预计还需 ~1-1.5 小时。运行命令:
```
python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged \
  --data_dir data/fewnerd --dataset fewnerd --subtask ner \
  --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs \
  --output_dir output/exp_021_fewnerd_n8_seed123
```

**可用于新实验: cuda:1, cuda:2, cuda:3**（3 张卡空闲）

---
