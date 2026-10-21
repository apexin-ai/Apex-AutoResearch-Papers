# 诊断报告：cqa1-33015 seed47 实验状态

**诊断时间**: 2026-05-29 ~10:50 UTC

## 结论：两个"消失"的实验均已正常完成

进程消失原因：实验跑完后正常退出（EXIT_CODE=0），不是崩溃或 OOM。

## 实验状态

### 1. eval_pi05_attn_k07_long_seed47_cqa1 — Attn k=0.7 seed47
- **状态**: ✅ 已完成
- **SR**: 54.4% (272/500)
- **Episodes**: 500/500
- **耗时**: 250.0 min
- **EXIT_CODE**: 0
- **结果文件**: `eval_results/pi05_attention_k0.70_libero_10_seed47.json`

Per-task SR:
| Task | SR |
|------|----|
| T0 alphabet soup + tomato sauce → basket | 72% |
| T1 cream cheese + butter → basket | 72% |
| T2 stove + moka pot | 64% |
| T3 black bowl → drawer | 42% |
| T4 white mug left + yellow mug right | 46% |
| T5 book → caddy | 28% |
| T6 white mug on plate + chocolate pudding | 78% |
| T7 alphabet soup + cream cheese → basket | 44% |
| T8 both moka pots → stove | 12% |
| T9 yellow mug → microwave | 86% |

### 2. eval_pi05_l2norm_k05_long_seed47_cqa1 — L2norm k=0.5 seed47
- **状态**: ✅ 已完成
- **SR**: 50.0% (250/500)
- **Episodes**: 500/500
- **耗时**: 250.9 min
- **EXIT_CODE**: 0
- **结果文件**: `eval_results/pi05_l2norm_k0.50_libero_10_seed47.json`

Per-task SR:
| Task | SR |
|------|----|
| T0 alphabet soup + tomato sauce → basket | 56% |
| T1 cream cheese + butter → basket | 58% |
| T2 stove + moka pot | 84% |
| T3 black bowl → drawer | 38% |
| T4 white mug left + yellow mug right | 36% |
| T5 book → caddy | 58% |
| T6 white mug on plate + chocolate pudding | 30% |
| T7 alphabet soup + cream cheese → basket | 50% |
| T8 both moka pots → stove | 10% |
| T9 yellow mug → microwave | 80% |

### 3. eval_pi05_attn_k075_long_seed47_cqa1 — Attn k=0.75 seed47
- **状态**: 🔄 运行中
- **进度**: Task 9, ep 40/50（最后一个 task 的最后 10 个 episode）
- **当前累计 SR**: ~46.7% (210/450, T0-T8 完成)
- **预计剩余**: ~5 min
- **PID**: 543547 (CUDA_VISIBLE_DEVICES=2)

## cqa1-33015 当前活跃实验

| 实验 | GPU | 状态 |
|------|-----|------|
| eval_pi05_attn_k075_long_seed47_cqa1 | cuda:2 | 运行中，即将完成 |
| eval_pi05_l2norm_k07_long_seed47_w41 | tmux only | tmux session 存在 |
| eval_pi05_attn_k095_long_seed47_cqa1_v2 | cuda:0 | 运行中 |
| eval_pi05_attn_k09_long_seed47_cqa1 | cuda:1 | 运行中 |
| eval_pi05_random_k085_long_seed47_cqa1 | cuda:3 | 运行中 |