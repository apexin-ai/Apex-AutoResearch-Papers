# ops 17855 cleanup deploy t15 a060 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_17855-cleanup-deploy-t15-a060-s43_20260523T024343_result.json`
- **Structured JSON:** [`a0a11fcf2ab1134cb76d.json`](../../sessions/a0/a0a11fcf2ab1134cb76d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功。

## 产出汇总

### 1. 磁盘清理
| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| Used | 335G | 319G |
| Avail | 16G | 32G |
| **释放** | **16G** | |

清理了 5 个已完成实验的中间 gen arrow 文件和 checkpoint：t10_a045/a060/a075_s42, t15_a050/a060_s42。跳过了仍在运行的 t15_a045_s42。

### 2. t15_a060_s43 部署状态
- **tmux**: `14b_t15_a060_s43` ✓
- **PID**: 749427（GPU 0, 运行中）
- **状态**: 已启动训练，160% CPU

### 3. 实际使用的命令参数
与 t15_a060_s42 config.json 一致，仅改 seed 和 output_dir：
```
CUDA_VISIBLE_DEVICES=0 python -u iterative_train.py \
  --model_name /root/autodl-tmp/.ms_cache/EleutherAI/pythia-1.4b-deduped \
  --data_dir data/wikitext103_5k \
  --synthetic_ratio 0.60 \
  --num_generations 15 \
  --steps_per_gen 5000 \
  --output_dir results/phase_diagram/t15_a060_s43_fp32_14b \
  --seed 43 \
  --batch_size 4 --max_length 512 --lr 5e-5 \
  --gen_max_new_tokens 256 --gen_batch_size 8 --top_p 0.95 \
  --optim adamw_torch --gradient_checkpointing
```

---
