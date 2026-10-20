# 诊断: eval_pi05_l2norm_k05_long_seed44_strict_w38

## 结论: 实验已成功完成，EXIT_CODE=129 为误报

### 根因

EXIT_CODE=129 (SIGHUP) 出现在实验**完成之后**。日志显示所有 10 个 task 均跑完 50 episodes，最终结果已打印并保存到 JSON 文件。SIGHUP 信号来自启动 wrapper/tmux session 在进程退出过程中发送的清理信号，不影响实验数据。

### 实验进度

- **状态**: 全部完成 (10/10 tasks × 50 episodes)
- **运行时间**: 169.8 min (~2h 50min), 03:07 → 05:59 UTC
- **总体 SR**: 52.6% (263/500)

### 逐 Task 结果

| Task | SR |
|------|-----|
| T0 alphabet soup + tomato → basket | 56% |
| T1 cream cheese + butter → basket | 66% |
| T2 stove on + moka pot | 66% |
| T3 black bowl → drawer | 48% |
| T4 white mug left + yellow mug right | 38% |
| T5 book → caddy | 62% |
| T6 white mug plate + pudding | 30% |
| T7 alphabet soup + cream cheese → basket | 54% |
| T8 both moka pots → stove | 20% |
| T9 yellow mug → microwave | 86% |

### 结果文件

已保存: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.50_libero_10_seed44.json`

内容完整，包含 config、per_task、overall_sr 等字段。

### 是否需要重跑

**不需要。** 实验数据完整，结果已保存。EXIT_CODE=129 仅为进程退出时的信号传递问题，不影响结果有效性。

### 原始启动参数

- suite=libero_10, prune=l2norm, keep=0.5, eps=50, gpu=0, seed=44
- 模型: /root/autodl-tmp/pi05_libero_finetuned
- Vision tokens: 256/image, 3 slots, keep 128/256 (50%)
