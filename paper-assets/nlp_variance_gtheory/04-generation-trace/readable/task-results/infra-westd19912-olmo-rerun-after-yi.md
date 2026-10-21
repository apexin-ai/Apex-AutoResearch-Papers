# infra westd19912 olmo rerun after yi

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd19912_olmo_rerun_after_yi_20260521T183301_result.json`
- **Structured JSON:** [`2cba80247d6e07fb5041.json`](../../sessions/2c/2cba80247d6e07fb5041.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**情况与预期不同，OLMo 重跑已经在运行了。** 先详细汇报两台服务器状态。

---

## westd-19912 状态

### GPU 分配（4/4 占满）
| GPU | 任务 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | OLMo GSM8K 重跑 | 88,904/97,887 MiB | 96% |
| 1 | OLMo MATH 重跑 | 88,904/97,887 MiB | 98% |
| 2 | Yi HellaSwag (chain: MMLU→HellaSwag→MATH) | 89,094/97,887 MiB | 100% |
| 3 | Yi GSM8K (chain: ARC→GSM8K) | 89,094/97,887 MiB | 96% |

### Yi 进度
| Benchmark | 行数 | 目标 | 状态 |
|-----------|------|------|------|
| MMLU | 57,600 | 57,600 | **完成** |
| ARC | 57,600 | 57,600 | **完成** |
| HellaSwag | 19,200 | 57,600 | 33% 运行中 (GPU 2) |
| GSM8K | 2,200 | 57,600 | 4% 运行中 (GPU 3) |
| MATH | - | 57,600 | 排队中 (GPU 2 chain, HellaSwag 完成后启动) |

### OLMo 进度
| Benchmark | 行数 | 目标 | 状态 |
|-----------|------|------|------|
| MMLU | 57,600 | 57,600 | **完成** |
| ARC | 57,600 | 57,600 | **完成** |
| HellaSwag | 57,600 | 57,600 | **完成** |
| GSM8K | 6,200 | 57,600 | 11% **重跑中** (GPU 0) |
| MATH | 3,000 | 57,600 | 5% **重跑中** (GPU 1) |

### 关键发现
**OLMo GSM8K 和 MATH 已经在 GPU 0/1 上重跑了**，使用完整 design_matrix：
```
python -m src.inference.run_experiment --design results/exp002/design_matrix_olmo.csv --benchmark gsm8k --gpu-id 0 --output results/exp002_olmo/exp002_olmo_gsm8k.jsonl
python -m src.inference.run_experiment --design results/exp002/design_matrix_olmo.csv --benchmark math --gpu-id 0 --output results/exp002_olmo/exp002_olmo_math.jsonl
```
- 启动时间：02:27（约 6 分钟前）
- 不需要 shard 文件，`--benchmark` 参数已做过滤
- **yi_done_then_olmo.sh 不需要部署了**

---

## westd-32570 状态

### GPU 分配（4/4 占满）
| GPU | 任务 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | InternLM MATH | 88,472/97,887 MiB | 67% |
| 1 | InternLM GSM8K | 88,226/97,887 MiB | 97% |
| 2 | Gemma MATH (即将完成) | 88,732/97,887 MiB | 90% |
| 3 | DeepSeek GSM8K | 88,010/97,887 MiB | 88% |

### Gemma MATH
- **57,200/57,600 行 (99%)**，还差 400 行，预计几分钟内完成

### DeepSeek MATH Watcher
- **Watcher 正常运行中** (PID 188947: `gemma_to_deepseek_math.sh`)
- 最新日志 `02:33:28`: "Gemma MATH progress: 57200/57600 (99%)"
- DeepSeek MATH 尚未启动，等待 Gemma MATH 完成后接管 GPU 2

---

## 汇总

1. **westd-19912**: yi_done_then_olmo.sh **无需部署** — OLMo GSM8K/MATH 已经在独立重跑。4 GPU 全部占满，Yi 3 个 benchmark 待完成（HellaSwag 33%、GSM8K 4%、MATH 排队）
2. **westd-32570**: Gemma MATH 即将完成 (99%)，watcher 状态正常，DeepSeek MATH 将在几分钟后自动启动
3. 两台服务器共 8 GPU 全部满载运行

---
