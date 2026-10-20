# westd-41074 GPU 健康检查 — 2026-05-27 21:10 UTC

## GPU 状态总览

| GPU | Util | Mem (MiB) | PID | 实验 | tmux session | 进度 |
|-----|------|-----------|-----|------|-------------|------|
| 0 | 91% | 20957/97887 | 561220 | **pi05 attn k=0.75 seed42 strict** | pi05_attn_k075 | T2 ep30 (69.0%) |
| 0 | (共享) | (共享) | 568159 | **pi05 attn k=0.75 seed42 strict** ⚠️ DUPLICATE | eval_pi05_attn_k075_long_seed42_strict | 运行中(pane空) |
| 1 | 18% | 10572/97887 | 547488 | **pi05 attn k=0.5 seed42 strict** | pi05_attn_k05 | T3 ep30 (60%) |
| 2 | 0% | 10053/97887 | 610959 | **pi05 random k=0.9 seed43 strict** | pi05_rnd_k09_s43 | T0 ep20 (30%) |
| 3 | 39% | 10886/97887 | 608185 | **pi05 attn k=0.7 seed42 strict** | pi05_attn_k07 | T0 ep30 (73%) |

## 问题发现

### 1. ⚠️ GPU 0 重复实验
PID 561220 (tmux `pi05_attn_k075`) 和 PID 568159 (tmux `eval_pi05_attn_k075_long_seed42_strict`) 是完全相同的实验 (attn k=0.75 seed42 strict)，同时跑在 GPU 0 上。GPU 0 内存 20957 MiB = 两个进程各 ~10462 MiB。建议 kill 其中一个。

对应 registry:
- `eval_pi05_attn_k075_long_seed42_strict_w41` → PID 561220 (started 20:24)
- `eval_pi05_attn_k075_long_seed42_strict` → PID 568159 (started 20:29)

### 2. eval_pi05_attn_k095_long_seed42_strict_w41_v2 已完成
- 结果: **78.4%** (392/500), 132 min
- Per-task: T0=94%, T1=100%, T2=74%, T3=98%, T4=82%, T5=94%, T6=28%, T7=78%, T8=38%, T9=98%
- Registry 已更新为 DONE

### 3. cascade_gpu3.sh 等待中
tmux `pi05_l2n_k095_s43` 运行 cascade 脚本，等 PID 608185 (attn k=0.7, GPU3) 完成后自动启动 L2norm k=0.95 seed43。

## 空闲 GPU
无空闲 GPU。但 GPU 0 有一个可 kill 的重复进程。

## 实验状态一致性

| 实验 ID | Registry | 实际 | 一致? |
|---------|---------|------|------|
| eval_pi05_attn_k095_long_seed42_strict_w41_v2 | ~~RUNNING~~ → DONE | 已完成 78.4% | ✅ 已修正 |
| eval_pi05_random_k09_long_seed43_strict_w41 | RUNNING | GPU2 T0 ep20 | ✅ |
| eval_pi05_attn_k07_long_seed42_strict_w41 | RUNNING | GPU3 T0 ep30 | ✅ |
| eval_pi05_attn_k075_long_seed42_strict_w41 | RUNNING | GPU0 T2 ep30 | ✅ (有重复) |
| eval_pi05_attn_k05_long_seed42_strict_w41 | RUNNING | GPU1 T3 ep30 | ✅ |