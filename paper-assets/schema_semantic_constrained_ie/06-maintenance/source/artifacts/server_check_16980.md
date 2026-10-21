# 服务器状态检查: westd-16980
**时间**: 2026-05-20 11:51 UTC

## (a) 运行中的 Python 进程

| PID | GPU | 模式 | 命令摘要 |
|-----|-----|------|----------|
| 697390 | GPU0 | unconstrained | `run_constrained_extraction.py --mode unconstrained --dataset docred --model_path llama_lora_docred_merged --output d065_llama_docred_greedy_unc_4096.jsonl --max_new_tokens 4096 --decoding_strategy greedy` |
| 698086 | GPU1 | full_s1 (constrained) | `run_constrained_extraction.py --mode full_s1 --dataset docred --model_path llama_lora_docred_merged --output d065_llama_docred_greedy_con_4096.jsonl --max_new_tokens 4096 --decoding_strategy greedy` |

## (b) nvidia-smi 输出

```
GPU 0: NVIDIA RTX PRO 6000 Blackwell
  - 温度: 56°C, 功耗: 341W/600W
  - 显存: 18275MiB / 97887MiB (18.7%)
  - 利用率: 90%
  - 进程: PID 697390 (python) - 18266MiB

GPU 1: NVIDIA RTX PRO 6000 Blackwell
  - 温度: 55°C, 功耗: 324W/600W
  - 显存: 18275MiB / 97887MiB (18.7%)
  - 利用率: 86%
  - 进程: PID 698086 (python) - 18266MiB
```

Driver: 580.95.05, CUDA: 13.0

## (c) tmux sessions

无法通过 ssh_read_only 检查（tmux 命令被拦截）。

## (d) 日志状态

两个日志文件均在 11:51 持续更新，内容为正常推理输出（transformers pad_token_id 警告），无报错。

- `d065_llama_greedy_unc.log` - 75,754 bytes
- `d065_llama_greedy_con.log` - 72,261 bytes

## (e) d065 输出文件进度

| 文件 | 行数 | 大小 | 进度 |
|------|------|------|------|
| d065_llama_docred_greedy_unc_4096.jsonl | 554 | 5.3MB | **55.5% (554/998)** |
| d065_llama_docred_greedy_con_4096.jsonl | 511 | 4.9MB | **51.2% (511/998)** |

## 结论

**两个进程均存活，服务重启后正常恢复运行。** 相比之前检查点（unc 37%, con 34%），进度分别推进到 55.5% 和 51.2%。两张 GPU 利用率 86-90%，推理正在持续进行。
