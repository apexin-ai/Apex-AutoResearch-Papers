# ssh autodl5090 gpu cleanup and freeform

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl5090_gpu_cleanup_and_freeform_20260522T110014_result.json`
- **Structured JSON:** [`6af4221651a856b55a1b.json`](../../sessions/6a/6af4221651a856b55a1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 清理
autodl-5090 清理前: 4/4 GPU 被占用（~30GB/32GB each）
**无法清理** — 4 个进程是正在运行的 FewNERD n=32 seed=42 分片采样实验：
- PID 129317 → shard0 (0-9412), 37% 完成
- PID 130001 → shard1 (9412-18824)
- PID 130710 → shard2 (18824-28236)
- PID 131421 → shard3 (28236-37648)

当前速度 ~50 it/s，每 shard 301,184 prompts，预计还需 **~65-70 分钟**完成（约 19:30 左右释放）。

## FewNERD Free-Form 准备
已在服务器创建 `run_freeform_fewnerd.py`（参考 `run_freeform_conll.py`）。

禁用 grammar 参数: `use_grammar=False`（在脚本内硬编码，同 CoNLL free-form 模式）

完整运行命令（GPU 释放后执行）:
```bash
cd /root/autodl-tmp/struct_self_consist_ie && \
CUDA_VISIBLE_DEVICES=0 python -u run_freeform_fewnerd.py \
  --seed 42 --gpu 0 --n_samples 8 --temperature 1.0 \
  2>&1 | tee output/fewnerd_freeform_seed42.log
```

多 seed 并行（4 GPU 全空时）:
```bash
for i in 0 1 2 3; do
  seed=(42 123 456 789)
  tmux new-session -d -s fewnerd_ff_s${seed[$i]} \
    "cd /root/autodl-tmp/struct_self_consist_ie && \
     python -u run_freeform_fewnerd.py --seed ${seed[$i]} --gpu $i \
     2>&1 | tee output/fewnerd_freeform_seed${seed[$i]}.log"
done
```

目标 GPU: 待 n=32 实验完成后，autodl-5090 cuda:0-3 均可用
预估 free-form 单 seed 运行时间: ~80-90 分钟（37,648 instances × 9 prompts each）

---
