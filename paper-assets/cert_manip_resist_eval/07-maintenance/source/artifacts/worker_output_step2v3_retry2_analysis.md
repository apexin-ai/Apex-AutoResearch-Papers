# 实验分析：mvp-step2v3-retry2

## 运行状态：**FAILED**（GPU 显存不足）

## 错误信息

脚本在 `phase1_inference()` → `judge.load()` 阶段崩溃。vLLM 尝试加载 `Qwen2.5-72B-Instruct-AWQ` 时，GPU 0 仅剩 6.62 GiB 可用（总 94.97 GiB），无法满足 `gpu_memory_utilization=0.9`（需 85.48 GiB）。

```
ValueError: Free memory on device cuda:0 (6.62/94.97 GiB) on startup is less than
desired GPU memory utilization (0.9, 85.48 GiB). Decrease GPU memory utilization or
reduce GPU memory used by other processes.
```

**根因**：GPU 0 被其他进程占用了约 88 GiB 显存。当前 `nvidia-smi` 显示 GPU 0 仍占用 89923/97887 MiB。

## 时间线

- 09:58:55 — 脚本启动，数据集加载成功（mmlu 300 samples, arc_challenge 300 samples，均从缓存读取）
- 09:58:56 — 开始加载 qwen2.5-72b 模型
- 09:59:12 — vLLM EngineCore 初始化失败，显存不足
- 09:59:13 — 脚本退出（EXIT_CODE=0，但实际是异常退出）

## Regression 结果

无。脚本在推理阶段前就崩溃了，未产出任何结果文件。

## 结论

- **conclusion**: `failed`
- **failure_type**: GPU OOM — 外部进程占用显存
- **未触及 HF xet_get 问题**：`HF_HUB_DISABLE_XET=1` 修复生效，数据集从缓存加载成功
- **需要的操作**：
  1. 清理 GPU 0 上占用显存的进程（kill 或等其结束）
  2. 或改用空闲的 GPU 1/2/3（设 `CUDA_VISIBLE_DEVICES=1`）
  3. 重新运行 step2v3

## 关键日志摘录

```
(EngineCore pid=64839) ERROR 05-22 09:59:12 [core.py:1136] EngineCore failed to start.
...
ValueError: Free memory on device cuda:0 (6.62/94.97 GiB) on startup is less than
desired GPU memory utilization (0.9, 85.48 GiB).

Traceback (most recent call last):
  File "/root/cert_manip_resist_eval/scripts/run_step2v3_regression.py", line 380, in <module>
    main()
  File "/root/cert_manip_resist_eval/scripts/run_step2v3_regression.py", line 337, in main
    clean, attacked, pairs = phase1_inference()
  File "/root/cert_manip_resist_eval/scripts/run_step2v3_regression.py", line 144, in phase1_inference
    judge.load()
  ...
RuntimeError: Engine core initialization failed.
EXIT_CODE=0
```

## GPU 现状（分析时刻 2026-05-22）

| GPU | 已用 | 总量 |
|-----|------|------|
| 0 | 89923 MiB | 97887 MiB |
| 1 | 3 MiB | 97887 MiB |
| 2 | 3 MiB | 97887 MiB |
| 3 | 3 MiB | 97887 MiB |

GPU 1/2/3 完全空闲，可用于重跑。
