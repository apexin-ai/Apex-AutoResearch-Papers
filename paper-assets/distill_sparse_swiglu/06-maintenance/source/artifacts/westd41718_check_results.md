# westd-41718 实验状态检查

**检查时间**: 2026-05-18 05:56 UTC

---

## 1. qwen14b_teal30_eval

| 项目 | 值 |
|------|-----|
| **状态** | 还在跑 |
| **进程是否存在** | 是 (PID 6896, STAT=Rl, ELAPSED=06:07:24) |
| **GPU 是否空闲** | 否 (cuda:1, 61656MiB / 97887MiB, 94% util) |
| **当前阶段** | GSM8K generate_until 87% (1153/1319), ETA ~46 min |
| **PPL (WikiText-2)** | 8.7332 |
| **ARC-c acc_norm** | 待 GSM8K 完成后统一输出 |
| **WinoGrande acc** | 待 GSM8K 完成后统一输出 |
| **MMLU acc** | 待 GSM8K 完成后统一输出 |
| **GSM8K exact_match** | 待完成 |
| **错误信息** | 无 |

**配置**: `--baseline_mode teal_vanilla --sparsity_target 0.3 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0` (实际运行在 cuda:1)

**Per-layer sparsity**: Model-level = 0.300 (global_topk allocation), 48 layers, range 0.074-0.917

**Log 最后 50 行** (qwen14b_teal30_eval.log):
```
Running generate_until requests:  81%|████████▏ | 1073/1319 [5:16:58<1:08:48, 16.78s/it]
Running generate_until requests:  82%|████████▏ | 1081/1319 [5:19:12<1:06:32, 16.77s/it]
Running generate_until requests:  83%|████████▎ | 1089/1319 [5:21:26<1:04:15, 16.76s/it]
Running generate_until requests:  83%|████████▎ | 1097/1319 [5:23:40<1:02:00, 16.76s/it]
Running generate_until requests:  84%|████████▍ | 1105/1319 [5:25:53<59:43, 16.75s/it]
Running generate_until requests:  84%|████████▍ | 1113/1319 [5:28:07<57:27, 16.73s/it]
Running generate_until requests:  85%|████████▍ | 1121/1319 [5:30:21<55:10, 16.72s/it]
Running generate_until requests:  86%|████████▌ | 1129/1319 [5:32:34<52:53, 16.70s/it]
Running generate_until requests:  86%|████████▌ | 1137/1319 [5:34:47<50:36, 16.68s/it]
Running generate_until requests:  87%|████████▋ | 1145/1319 [5:37:00<48:19, 16.67s/it]
Running generate_until requests:  87%|████████▋ | 1153/1319 [5:39:13<46:03, 16.65s/it]
```
(中间穿插 transformers max_new_tokens/max_length 警告，已省略)

---

## 2. qwen14b_dense_baseline

| 项目 | 值 |
|------|-----|
| **状态** | 还在跑 |
| **进程是否存在** | 是 (PID 18845 wrapper -> PID 18850 python, STAT=Rl, ELAPSED=03:09:22) |
| **GPU 是否空闲** | 否 (cuda:0, 59276MiB / 97887MiB, 97% util) |
| **当前阶段** | GSM8K generate_until 81% (1065/1319), ETA ~9 min |
| **PPL (WikiText-2)** | 5.1854 |
| **ARC-c acc_norm** | 待 GSM8K 完成后统一输出 |
| **WinoGrande acc** | 待 GSM8K 完成后统一输出 |
| **MMLU acc** | 待 GSM8K 完成后统一输出 |
| **GSM8K exact_match** | 待完成 |
| **错误信息** | 无 |

**配置**: `--dense --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0`

**tmux session**: `qwen14b_dense_baseline` (created Mon May 18 02:47:33 2026)

**Log 最后 50 行** (qwen14b_dense_baseline.log):
```
Running generate_until requests:  76%|███████▋  | 1009/1319 [2:38:21<43:30,  8.42s/it]
Running generate_until requests:  77%|███████▋  | 1017/1319 [2:38:37<32:51,  6.53s/it]
Running generate_until requests:  78%|███████▊  | 1025/1319 [2:38:54<25:26,  5.19s/it]
Running generate_until requests:  78%|███████▊  | 1033/1319 [2:39:11<20:21,  4.27s/it]
Running generate_until requests:  79%|███████▉  | 1041/1319 [2:39:27<16:33,  3.57s/it]
Running generate_until requests:  80%|███████▉  | 1049/1319 [2:39:36<12:47,  2.84s/it]
Running generate_until requests:  80%|████████  | 1057/1319 [2:39:51<11:10,  2.56s/it]
Running generate_until requests:  81%|████████  | 1065/1319 [2:40:00<09:01,  2.13s/it]
```
(中间穿插 transformers max_new_tokens/max_length 警告，已省略)

---

## GPU 状态

```
Mon May 18 05:56:56 2026
GPU 0: NVIDIA RTX PRO 6000 Blackwell | 62C | 397W/600W | 59285MiB/97887MiB | 97% | PID 18850
GPU 1: NVIDIA RTX PRO 6000 Blackwell | 61C | 355W/600W | 61665MiB/97887MiB | 94% | PID 6896
```

---

## 结论

- 两个实验均正常运行，无错误
- 均已完成 wikitext2 PPL + arc_challenge + winogrande + mmlu 评估，正在跑最后一个 task (gsm8k)
- **qwen14b_dense_baseline** 预计 ~9 min 内完成
- **qwen14b_teal30_eval** 预计 ~46 min 内完成
- 完整指标（ARC-c, WinoGrande, MMLU, GSM8K）将在各自 GSM8K 完成后由 benchmark_eval.py 统一输出到 log 和 results 目录
- 结果目录 (`results/benchmark/qwen14b_*/`) 当前为空，脚本在全部任务完成后才写入 JSON
