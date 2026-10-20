# code exp 025 pythia filtering

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_025_pythia_filtering_20260518T080547_result.json`
- **Structured JSON:** [`6c45b7458c7551a06736.json`](../../sessions/6c/6c45b7458c7551a06736.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张卡全部在训练，每卡 ~5.4GB VRAM，~3.5 it/s。一切正常。

**实验状态汇总：**

| 项目 | 状态 |
|---|---|
| **脚本** | `scripts/exp025_pythia_filtering.py` + `scripts/run_exp025.sh` |
| **模型** | Pythia-1.4B (已缓存，LoRA rank=8, alpha=16, target=`query_key_value`) |
| **数据** | `data_exp020_pythia_greedy/depth_{0-5}.jsonl`, 每层 5000 docs |
| **策略** | no_filter (30k), binary_ours K\*=2 (15k), graduated_a09 (30k, w=0.9^d) |
| **Seeds** | 42, 123, 456 |
| **调度** | 3 batches × 4 GPU 并行，共 9 runs |
| **评估** | lm-eval-harness MMLU + HellaSwag (5-shot) |

**预估时间：**
- 训练: no_filter ~9min, binary_ours ~4.5min per run
- Eval: ~30-40min per run
- 每 batch ~45min，总计 ~2-2.5h

**监控命令：**
```bash
# 总体进度
tail -20 logs/exp025/run_exp025_main.log
# 单 run 进度
tail -5 logs/exp025/&lt;strategy>_seed&lt;N>.log
# GPU 状态
nvidia-smi --query-gpu=index,memory.used --format=csv,noheader
```

结果输出在 `results/exp_025_pythia_filtering/&lt;strategy>_seed&lt;N>/eval_results.json`。训练完成后 launcher 脚本会打印汇总表。

---
