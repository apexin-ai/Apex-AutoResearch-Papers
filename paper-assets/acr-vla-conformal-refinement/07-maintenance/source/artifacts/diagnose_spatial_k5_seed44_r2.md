# 诊断报告: eval-obs-only-spatial-norm02-k5-seed44-r2 及同批次 r2 实验失败

**日期**: 2026-05-19
**服务器**: bjb2-28827

## 失败根因

**根因: 实验由 untracked 手动进程完成，managed r2 重试无法检测到 sentinel/W&B 标记。**

5 个 r2 实验全部标记为 "process dead 5× with no sentinel/W&B — auto-resolved as failed"，但实际上其中 3 个实验已由手动启动的 untracked 进程成功完成。managed 系统的包装脚本在 `/tmp/agent-ml-exit/` 创建 sentinel 文件，但手动进程不写 sentinel，因此 managed 监控器检测不到。

## 各实验状态

| 实验 | JSON 存在? | 结果 | 需重试? |
|------|-----------|------|---------|
| spatial obs-only K5 seed44 | ✅ (May 19 23:45) | **37.0%** (37/100) | ❌ 不需要 |
| spatial obs-only K5 seed45 | ✅ (May 19 23:49) | **34.0%** (34/100) | ❌ 不需要 |
| object random-selection K5 seed43 | ✅ (May 20 00:03) | **11.0%** (11/100) | ❌ 不需要 |
| object random-selection K5 seed44 | ❌ 不存在 | — | ✅ 需要 |
| object random-selection K5 seed45 | ❌ 不存在 | — | ✅ 需要 |

注：`eval_object_random_selection_seed44.json` (13%) 和 `seed45.json` (10%) 是 **K=10** 的结果，不是 K=5。

## GPU 当前状态 (May 20 00:27)

| GPU | 进程 | 说明 |
|-----|------|------|
| 0 | 空闲 | tmux session `train-crm-k1-v2` 存在但 GPU 未占用 |
| 1 | PID 758237 | eval-argmin-object-k5-seed44 (reconvla mode) |
| 2 | PID 693631 | eval_object_random_selection_seed46 (K=10) |
| 3 | PID 871624 | eval-obs-only-spatial-norm02-seed46 (K=10) |
| 4 | 空闲 | |
| 5 | 空闲 | |

**ROADMAP 提到的 "GPU2 上 untracked spatial-K5-seed44 进程" 已不存在。** 该进程已完成并产生了 JSON 结果。当前 GPU2 上运行的是 random_selection seed46 (K=10)。

## Sentinel 文件检查

`/tmp/agent-ml-exit/` 中无任何 r2 批次的 sentinel 文件，进一步确认 managed 系统从未成功启动过这些进程（或进程立即退出）。

## 结论

- 3/5 个 r2 实验实际已完成，结果可直接使用
- 2/5 个实验 (object random-selection K5 seed44, seed45) 确实未完成，需要重新提交
- 重试时可用 GPU 0/4/5（当前空闲）
