# exp-009 状态诊断报告

**时间**: 2026-05-17 13:40 UTC

## 完成的工作

### Signals（全部完成 ✓）
| 模型 | mmlu | arc_challenge | gsm8k |
|------|------|---------------|-------|
| Qwen2.5-3B-Instruct | ✓ minkpp+selfcritique+merged | ✓ | ✓ |
| DeepSeek-R1-Distill-Qwen-1.5B | ✓ minkpp+selfcritique+merged | ✓ | ✓ |

路径: `/root/autodl-tmp/exp009/signals/`

### Eval Results（部分完成）
| 模型 | mmlu | arc_challenge | gsm8k |
|------|------|---------------|-------|
| DeepSeek-R1-Distill-Qwen-1.5B | ✓ | ✓ | ⏳ 运行中 |
| Qwen2.5-3B-Instruct | ✗ | ✗ | ✗ |

### 模型下载
- DeepSeek-R1-Distill-Qwen-1.5B: ✓ 已下载 (3.4G at `/root/autodl-tmp/models/deepseek-ai/`)

## 当前进程状态

- **GPU 3**: PID 935048 活跃，运行 DeepSeek eval（已跑 53 分钟，mmlu+arc_challenge 已完成，gsm8k 进行中）
- **GPU 5**: 空闲
- **tmux sessions**: `exp009_3b_instruct` 和 `exp009_deepseek` 均存在

## 未完成的工作

1. DeepSeek gsm8k eval — 正在自动完成（GPU 3 进程仍活跃）
2. **Qwen2.5-3B-Instruct eval（3 benchmarks）— 未启动，需要手动恢复**

## 恢复步骤

1. 等待 GPU 3 上 DeepSeek eval 自然完成（预计很快，gsm8k 是最后一个 benchmark）
2. 在空闲 GPU 上启动 Qwen2.5-3B-Instruct eval:
```bash
CUDA_VISIBLE_DEVICES=5 python /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/models/Qwen/Qwen2.5-3B-Instruct \
  --benchmarks mmlu arc_challenge gsm8k \
  --output-dir /root/autodl-tmp/exp009/eval_results/Qwen2.5-3B-Instruct \
  --instruct
```
3. 验证 Qwen 模型路径（可能在 `/root/autodl-tmp/models/Qwen/Qwen2.5-3B-Instruct` 或类似位置）
