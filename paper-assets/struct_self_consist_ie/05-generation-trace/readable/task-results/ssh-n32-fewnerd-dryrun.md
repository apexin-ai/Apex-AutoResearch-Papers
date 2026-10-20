# ssh n32 fewnerd dryrun

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n32_fewnerd_dryrun_20260522T024158_result.json`
- **Structured JSON:** [`f8931eaac9f097970cf0.json`](../../sessions/f8/f8931eaac9f097970cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成。汇总报告：

---

## N=32 FewNERD Dry-Run 验证报告

### 1. 环境状态
| 项目 | 状态 |
|------|------|
| GPU | 4× RTX 5090, 32GB VRAM each, 全部空闲 |
| Python | 3.12.3 (conda base) |
| vLLM | 0.18.1 |
| 磁盘 | /root/autodl-tmp 97GB 可用 (350GB 总量, 73% 已用) |

### 2. 模型/数据就绪
- **模型**: `checkpoints/qwen3-8b-fewnerd-exp021-merged/tokenizer_config.json` 存在，顶层目录正确
- **数据**: `data/fewnerd/test.json` — 37,648 instances（注意是 `.json` 不是 `.jsonl`）
- **脚本**: `code/run_mvp_pilot.py` 存在，`--n_samples` 参数无上限限制

### 3. Dry-Run 结果: **通过**
- 10 instances × 32 samples = 320 prompts，全部处理成功
- 采样吞吐: ~42.5 it/s（单 GPU）
- 模型加载 + CUDA graph 编译: ~14s
- 10 instances 总耗时: ~12s（不含模型加载）
- 输出文件: 701K（10 instances）

### 4. 全量预估
| 指标 | 预估值 |
|------|--------|
| 总 prompts | 1,204,736 (37648×32) + 37,648 greedy = ~1.24M |
| 推理时间 | ~7-8 小时（单 GPU, 42 it/s） |
| 输出大小 | ~2.6 GB（N=8 的 ~650MB × 4） |
| 磁盘足够 | 是（97GB 可用） |

### 5. 正式提交命令

```bash
cd /root/autodl-tmp/struct_self_consist_ie && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
nohup python -u code/run_mvp_pilot.py \
  --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged \
  --data_dir data/fewnerd \
  --dataset fewnerd \
  --subtask ner \
  --n_samples 32 \
  --temperature 1.0 \
  --seed 42 \
  --collect_logprobs \
  --output_dir output/fewnerd_n32_seed42 \
  > output/fewnerd_n32_seed42.log 2>&1 &
```

**注意**: 任务中 `--data_dir` 应为 `data/fewnerd`（不是 `/tmp/`），数据文件是 `.json` 格式。当前只用单 GPU，如需加速可考虑多 GPU 并行（4 卡可将时间缩短到 ~2h）。

---
