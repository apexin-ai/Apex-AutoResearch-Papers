# diagnose second priority batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_second_priority_batch_20260528T070145_result.json`
- **Structured JSON:** [`496900f7ce6d0cff6427.json`](../../sessions/49/496900f7ce6d0cff6427.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有三个任务完成。

---

```
[Task 1 - Attn k=0.9 s44]
搜索结果: 找到 (cqa1-33015)
log_path: ~/runs/importance_margin_vla_compress/eval_pi05_attn_k09_long_seed44_strict_w38.log
SR=64.0% (320/500), EXIT_CODE=0
Per-task: T0=48% T1=88% T2=46% T3=92% T4=60% T5=88% T6=62% T7=50% T8=16% T9=90%
Registry 已更新 (metrics + conclusion=success)

[Task 2 - w38 cuda:1 进程身份]
PID 253691: python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0
  → Random k=0.9 Long seed46, CUDA_VISIBLE_DEVICES=1

PID 261885: python -u eval_pi05_pruning_libero.py --prune_mode attention --keep_ratio 0.5 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0
  → Attention k=0.5 Long seed46, CUDA_VISIBLE_DEVICES=1

⚠️ 两个进程共享同一物理 GPU (cuda:1)，都有正确的 offline flags。

[Task 3 - cqa1 磁盘清理]
清理前: /autodl-pub 91% (6.4T/7.0T), /root/autodl-tmp 55% (136G/250G)
清理内容:
  - HF datasets/parquet cache: ~32G 已删
  - pip cache: 55M 已删
清理后: /autodl-pub 91% (6.3T/7.0T), /root/autodl-tmp 42% (104G/250G)

⚠️ 无法达到 <80% 目标: /autodl-pub 是 7T 共享盘，我们总占用 ~104G 仅为总用量 6.3T 的 ~1.6%。
剩余不可删项: LIBERO 数据集 (33G lerobot/hub)、模型文件 (pi05 21G + openvla 45G + pi05-base 14G)。
即使全删也只能从 91% 降至 ~89%。需要平台侧释放空间。
```

---
