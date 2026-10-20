# GPU Status Check — Loop 10
**Time**: 2026-05-19 19:18 UTC

## westd-25068 (4× RTX PRO 6000 Blackwell)

| GPU | 显存占用 | GPU-Util | 进程 | 实验 |
|-----|---------|----------|------|------|
| cuda:0 | 88301/97887 MiB | 96% | VLLM (PID 190753, port 8010) | **exp-065** Qwen2.5-7B PW-600 |
| cuda:1 | 88249/97887 MiB | 97% | VLLM (PID 189895, port 8011) | **exp-066** Qwen2.5-14B FOLIO seed123 |
| cuda:2 | **0/97887 MiB** | **0%** | 无 | **空闲** (exp-067 已完成) |
| cuda:3 | 88115/97887 MiB | 96% | VLLM (PID 192666, port 8003) | **exp-062** Gemma-27B FOLIO |

tmux sessions: exp062_run/vllm, exp065_run/vllm, exp066_run/vllm, exp033/034/035_run (旧), model_dl_25068

## westd-16639 (4× RTX PRO 6000 Blackwell)

| GPU | 显存占用 | GPU-Util | 进程 | 实验 |
|-----|---------|----------|------|------|
| cuda:0 | **0/97887 MiB** | **0%** | 无 | **空闲** (exp-063 已完成) |
| cuda:1 | 88287/97887 MiB | 97% | VLLM (PID 142896, port 8001) | **exp-068** Qwen3-14B LogiQA-200 |
| cuda:2 | 88255/97887 MiB | 96% | VLLM (PID 125544, port 8002) | **exp-064** DeepSeek-R1-Qwen3-8B FOLIO |
| cuda:3 | 88263/97887 MiB | 96% | VLLM (PID 76474, port 8003) | **exp-048** LLaMA-8B PW-600 |

tmux sessions: exp048_run/vllm, exp064_run/vllm, exp068_run/vllm

## 空闲 GPU 列表

| 服务器 | GPU | 状态 |
|--------|-----|------|
| westd-25068 | cuda:2 | 空闲 (exp-067 完成后释放) |
| westd-16639 | cuda:0 | 空闲 (exp-063 完成后释放) |

## 已完成实验 (本轮新发现)

### exp-063 (LLaMA-3.1-8B FOLIO-204, westd-16639)
- **SICA accuracy**: 61.8% (126/204)
- **SC accuracy**: 66.2% (135/204)
- **SICA delta**: -4.4pp
- Extraction rate: 95.7%, Contradiction rate: 5.0%
- Wall time: 155.6 min
- 结果: `results/exp-063-llama8b-folio204-16639/results.json`
- 结论: 低能力模型(SC=66.2%<70%) SICA 无增益，与 exp-020 一致

### exp-067 (Mistral-7B FOLIO seed=789, westd-25068)
- **SICA accuracy**: 53.9% (110/204)
- **SC accuracy**: 54.4% (111/204)
- **SICA delta**: -0.49pp
- Extraction rate: 97.1%, Contradiction rate: 3.3%
- Wall time: 81.8 min
- 结果: `results/exp067_mistral_folio_seed789/exp067_results.json`
- **Seed replication 汇总**: s42 +3.43pp, s123 +2.94pp, s456 0.00pp, s789 -0.49pp (mean +1.47pp, high variance)

## 仍在运行的实验

| 实验 | 模型 | 数据 | 服务器 | GPU | 启动时间 |
|------|------|------|--------|-----|---------|
| exp-062 | Gemma-3-27B-IT | FOLIO-204 | westd-25068 | cuda:3 | 17:02 |
| exp-065 | Qwen2.5-7B | PW-600 | westd-25068 | cuda:0 | 16:53 |
| exp-066 | Qwen2.5-14B | FOLIO s123 | westd-25068 | cuda:1 | 16:56 |
| exp-048 | LLaMA-3.1-8B | PW-600 | westd-16639 | cuda:3 | 10:20 |
| exp-064 | DeepSeek-R1-Qwen3-8B | FOLIO-204 | westd-16639 | cuda:2 | 16:56 |
| exp-068 | Qwen3-14B | LogiQA-200 | westd-16639 | cuda:1 | 19:13 |

## 备注
- exp-066 (Qwen2.5-14B FOLIO seed123) 在运行中，未在原始任务检查列表中
- exp-063/exp-067 注册表已更新为 DONE (success)
