# 诊断报告: eval_pi05_attention_k05_long_seed42_v3

## 基本信息
- **服务器**: cqa1-33015, GPU: cuda:2 (RTX 4090 D, 24GB)
- **运行时间**: 2026-05-26 22:47 ~ 23:00 (约 13 分钟)
- **日志大小**: 31 行 / 2472 bytes（成功 run 通常 95 行 / ~7800 bytes）

## 根本原因: EGL/MuJoCo 渲染驱动层静默崩溃

**不是 OOM**，证据确凿：
- cgroup v2 `memory.events` 显示 `oom_kill 0`（零次 OOM kill）
- 系统 RAM 1TB，可用 940GB
- cgroup 内存限制 320GB，当前用量仅 45GB
- GPU 显存 10.5GB / 24GB

**不是磁盘问题**：115GB 可用（55%）

**不是代码 bug**：同 config 的 random_k05 和 attention_k075 均成功完成

## 失败模式分析

进程在 T0 ep=20 (85%) 后静默消失，无 traceback、无错误信息、无 core dump。

**同样的静默死亡模式出现在多个实验中**（不限于 attention 剪枝）：
- `eval_pi05_l2norm_k075_long_seed42.log`: 29 行，死于 T0 ep=10
- `eval_pi05_l2norm_k0925_long_seed42.log`: 32 行，死于 T0 ep=30
- `eval_pi05_attention_k05_long_seed42_v3.log`: 31 行，死于 T0 ep=20

这些实验的重试版本有时能成功完成（如 l2norm_k075_v3 完成了 4879 bytes）。

**结论**: 4 个 GPU 同时运行 eval 实验（均使用 `MUJOCO_GL=egl`），EGL 渲染在多进程共享 GPU driver 时偶发静默崩溃。进程被 driver 层 SIGKILL，Python 无法捕获也无法输出 traceback。失败点随机（ep=10/20/30），与具体剪枝方法无关。

## 日志关键片段

```
2026-05-26 22:50:20,883 Pruning: attention, keep 128/256 tokens/image (384 total, 2-layer probe)
[PRUNE-DIAG] attention: n_keep=128/256, score_range=[0.000002, 0.003847], first_indices=[1, 2, 5, 6, 7]
2026-05-26 22:55:53,938   T0 [put both the alphabet soup and the tomat] ep=10: 7/10=70%
2026-05-26 23:00:55,269   T0 [put both the alphabet soup and the tomat] ep=20: 17/20=85%
# --- 此后进程静默消失，无任何输出 ---
```

## 可否重试

**可以重试，但 cuda:2 当前被占用。**

- PID 467731 正在 cuda:2 上运行 `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7`
- 需等该实验完成后再重试

## 建议修复措施

1. **减少并发数**：避免 4 GPU 同时跑 eval（EGL 共享 driver 是根因）；2-3 个并发更稳定
2. **重试即可**：此类间歇性崩溃通过重试通常能解决
3. **可选**：在 eval 脚本中加 `faulthandler.enable()` 来捕获更多崩溃信息，便于后续诊断

## v2 日志

v2 日志文件不存在（`eval_pi05_attention_k05_long_seed42_v2.log` 未找到），说明 v2 可能连日志都没来得及写。

## 现有结果文件

`pi05_attention_k0.50_libero_10_seed42.json` 存在但**不可信**——其 `n_keep_per_image: 256`（未剪枝），是之前某次 baseline run 的残留，非本次 attention k0.5 实验的结果。
