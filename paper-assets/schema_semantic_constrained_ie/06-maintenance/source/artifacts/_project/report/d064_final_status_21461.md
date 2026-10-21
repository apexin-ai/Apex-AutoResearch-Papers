# d064 Final Status — westd-21461

**检查时间**: 2026-05-20 07:19 UTC

## 文件状态

所有文件位于 `/root/autodl-tmp/schema_outputs/`

| 文件 | 行数 | 大小 | 完成时间 | 状态 | JSON 验证 |
|------|------|------|----------|------|-----------|
| d064_llama_docred_greedy_unconstrained.jsonl | 998/998 | 8.9MB | May 19 22:35 | 完成 | head/tail OK |
| d064_llama_docred_greedy_constrained.jsonl | 998/998 | 8.9MB | May 20 02:54 | 完成 | head/tail OK |
| d064_qwen_docred_beam4_unconstrained.jsonl | 998/998 | 8.6MB | May 19 23:06 | 完成 | head/tail OK |
| d064_qwen_docred_beam4_constrained.jsonl | 998/998 | 8.5MB | May 20 05:54 | 完成 | head/tail OK |
| d064_llama_docred_beam4_unconstrained.jsonl | 901/998 | 7.6MB | 运行中 | **进行中** | head OK |

## 运行中任务

- **文件**: d064_llama_docred_beam4_unconstrained.jsonl
- **进程**: PID 122747, CPU 100%, GPU0
- **进度**: 901/998 (90.3%)
- **启动时间**: May 20 02:54
- **处理速率**: ~3.4 samples/min
- **剩余**: 97 samples
- **预计完成**: ~07:48 UTC (约 28 分钟后)
- **命令**: `python run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 4 --device cuda:0`

## GPU 状态

- **GPU0**: NVIDIA RTX PRO 6000 Blackwell (96GB), 90% 利用率, 18275 MiB 已用 — 运行 d064_llama_docred_beam4_unconstrained
- **GPU1**: NVIDIA RTX PRO 6000 Blackwell (96GB), 0% 利用率, 空闲

## 其他进程

- tmux session `mistral_v3_full` 存在（旧的 wikievents 实验，进程已结束）
- cascade 脚本 `d064_gpu0_llama_all_with_greedy.sh` 仍在后台（等待当前 beam4 unconstrained 完成）

## 异常

- **额外文件**: `d064_llama_docred_beam4_unconstrained.jsonl` 不在原始预期列表中，是 cascade 脚本自动启动的额外任务
- **缺失文件**: 没有 `d064_llama_docred_beam4_constrained.jsonl` — 可能是 cascade 脚本的下一步，将在当前 unconstrained 完成后启动
- 旧路径 `/root/schema_semantic_constrained_ie/outputs/` 无 d064 文件
