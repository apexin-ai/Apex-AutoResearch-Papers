# d067 Seed Variance 启动报告

**服务器**: westd-21461
**时间**: 2026-05-20 07:24 CST

## 1. Cascade Kill 确认

已 kill d064 llama docred beam4 冗余 cascade（16980 已有完整结果）：

| PID | 进程 | 说明 |
|-----|-------|------|
| 122747 | `python run_constrained_extraction.py --mode unconstrained --dataset docred --model_path llama_lora_docred_merged --decoding_strategy beam --num_beams 4` | 实际 python 推理进程，已运行 4h29m |
| 99652 | `bash scripts/d064_gpu0_llama_all_with_greedy.sh` | cascade 脚本 |
| 99651 | 外层 bash wrapper | nohup 启动层 |

全部 SIGTERM 成功终止。

## 2. d067 启动

**PID**: 132647（外层 bash），实际 python PID 132661
**日志**: `/root/autodl-tmp/schema_outputs/d067_seed_variance.log`

因 GPU1 正在跑 d066 beam sweep，d067 全部 6 个配置串行在 GPU0 上运行：

```bash
nohup bash -c "
  bash d067_seed_variance.sh 0 qwen_scierc 123 &&
  bash d067_seed_variance.sh 0 qwen_scierc 456 &&
  bash d067_seed_variance.sh 0 llama_scierc 123 &&
  bash d067_seed_variance.sh 0 llama_scierc 456 &&
  bash d067_seed_variance.sh 0 qwen_docred 123 &&
  bash d067_seed_variance.sh 0 qwen_docred 456
" > /root/autodl-tmp/schema_outputs/d067_seed_variance.log 2>&1 &
```

### 脚本内容摘要

每个配置跑 2 个 pass（unconstrained + full_s1 constrained），加 violation check：

| 配置 | 模型 | 数据集 | Seeds |
|------|-------|--------|-------|
| qwen_scierc | qwen3_8b_lora_scierc_merged | SciERC test (551 samples) | 123, 456 |
| llama_scierc | llama_lora_scierc_merged | SciERC test (551 samples) | 123, 456 |
| qwen_docred | qwen_lora_docred_merged | DocRED dev | 123, 456 |

共 6 配置 × 2 passes = 12 次推理 + 12 次 violation check。
预计耗时 ~9h（串行，原双 GPU 并行估算 ~4.5h）。

## 3. GPU 分配状态

| GPU | 任务 | PID | 显存 |
|-----|------|-----|------|
| GPU0 | d067 seed variance (qwen_scierc seed123 unconstrained) | 132661 | 18990MiB / 97887MiB |
| GPU1 | d066 SciERC beam sweep (qwen_scierc beam1 unconstrained) | 132469 | 18990MiB / 97887MiB |
