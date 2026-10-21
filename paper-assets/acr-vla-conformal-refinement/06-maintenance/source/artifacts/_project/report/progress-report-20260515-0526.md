## 进度总结 (2026-05-15 05:26 UTC)

| 实验 | 服务器 | 进度 | 关键指标 | 预计完成 |
|------|--------|------|---------|---------|
| eval-vla-mean-spatial | bjb2 GPU0 | 9/10 tasks | avg 34.4% (31/90) | ~2h |
| eval-argmin-only-spatial | bjb1 GPU1 | 3/10 tasks (T4 rollout 5/10) | avg 53.3% (16/30) | ~8h |
| eval-tiny-correction-spatial | bjb1 GPU2 | 3/10 tasks (T4 rollout 5/10) | avg 53.3% (16/30) | ~8h |
| **eval-acr-spatial-v4-default** | **bjb1 GPU0** | **0/10 — 未运行!** | **无进程，需重启** | **N/A** |
| eval-acr-spatial-v4-small | bjb1 GPU3 | 1/10 tasks | T1: 60% (6/10) | ~9h |
| crm-train-v3-norm-obs-only | bjb1 GPU0 | epoch 26/50 | best val_loss=0.01669 (ep23) | ~35m |
| crm-train-v3-norm-scalar-unc | bjb1 GPU3 | epoch 26/50 | best val_loss=0.03998 (ep26, 仍在下降) | ~35m |

### Eval 详细结果（已完成 tasks）

**eval-vla-mean-spatial (K=10 mean baseline):**
| Task | Success Rate |
|------|-------------|
| T1 between_plate_ramekin | 70% (7/10) |
| T2 next_to_ramekin | 100% (10/10) |
| T3 from_table_center | 0% (0/10) |
| T4 on_cookie_box | 30% (3/10) |
| T5 in_top_drawer | 0% (0/10) |
| T6 on_ramekin | 0% (0/10) |
| T7 next_to_cookie_box | 80% (8/10) |
| T8 on_stove | 0% (0/10) |
| T9 next_to_plate | 30% (3/10) |

**eval-argmin-only-spatial (reconvla K=10 argmin):**
T1: 60%, T2: 100%, T3: 0% → avg 53.3%

**eval-tiny-correction-spatial (acr_vla max_norm=0.05):**
T1: 70%, T2: 90%, T3: 0% → avg 53.3%

**eval-acr-spatial-v4-small (v3-norm, max_norm=0.1):**
T1: 60%

## GPU 利用率

**bjb1-18228 (4× RTX 4090):**
| GPU | 利用率 | 显存 | 负载 |
|-----|--------|------|------|
| 0 | 71% | 17441/24564 MiB | crm-train-obs-only + stale v3 eval tmux |
| 1 | 20% | 1423/24564 MiB | eval-argmin-only |
| 2 | 23% | 1459/24564 MiB | eval-tiny-correction |
| 3 | 70% | 2022/24564 MiB | eval-v4-small + crm-train-scalar-unc |

**bjb2-40593 (1× RTX 4090 D):**
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 12% | 1933/24564 MiB | eval-vla-mean (近完成) |

## 异常/告警

- **🚨 eval-acr-spatial-v4-default 未运行！** Registry 标记为 RUNNING，但服务器上无对应进程、无日志文件、无 exit file。GPU 0 被旧的 eval-acr-spatial-v3 tmux 会话（crm_v2 checkpoint）占用。**需要：(1) 杀掉 stale v3 tmux 会话 (2) 等 crm-train-obs-only 完成后释放 GPU 0 显存 (3) 重新启动 v4-default eval。** 这是核心判定实验，优先级最高。
- eval-acr-spatial-v3（旧实验，tmux PID 197056）仍有 tmux 主进程但无活跃 Python 子进程，5/10 tasks 完成后似乎挂起或崩溃。建议清理。
- 两个 CRM 训练约 35 分钟后完成，完成后可释放 GPU 0 和 GPU 3 上的训练显存。
