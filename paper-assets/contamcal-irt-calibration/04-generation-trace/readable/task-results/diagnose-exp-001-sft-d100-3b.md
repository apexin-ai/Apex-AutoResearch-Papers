# diagnose exp 001 sft d100 3B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_d100_3B_20260514T070301_result.json`
- **Structured JSON:** [`b0f11ff9e0fc9083528f.json`](../../sessions/b0/b0f11ff9e0fc9083528f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：exp_001_sft_d100_3B 失败原因

### 失败根因：SIGKILL — 高概率 GPU 内存冲突

进程在 step 76/4159（运行约 10 分钟）被外部 SIGKILL 终止，日志无任何 Python traceback 或错误信息。

**根因判定依据：**

1. **train_sft.py 存在关键 bug**：`--gpu` 参数被 argparse 解析但代码中**从未使用**，没有任何 `os.environ["CUDA_VISIBLE_DEVICES"]` 设置逻辑。GPU 分配完全依赖外部环境变量。

2. **同服务器前车之鉴**：exp_001_sft_d100_15B 明确报错 `torch.OutOfMemoryError: CUDA out of memory` on **GPU 0**（非目标 GPU），原因是 CUDA_VISIBLE_DEVICES 未正确设置，导致模型挤入已占用 20GB 的 GPU 0。

3. **当前重启进程（PID 319555）有 `CUDA_VISIBLE_DEVICES=3`**，说明重启时修正了环境变量。但原进程 319550 很可能缺少这个设置。

4. 无 Python traceback + 训练中途突然终止 = SIGKILL（exit 137），与之前实验模式一致。

### 关键日志片段

```
# bitsandbytes 警告（非致命，训练已继续）
[ERROR] bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file

# 训练正常运行至 step 76 后突然中断，无任何错误输出
  1%|▏         | 76/4159 [10:02<4:36:30,  4.06s/it]
（日志到此结束，无 traceback）
```

**前次 15B 实验的 OOM 错误（同一模式）：**
```
torch.OutOfMemoryError: CUDA out of memory. GPU 0 has a total capacity of 23.52 GiB
of which 27.38 MiB is free. Process 248703 has 20.07 GiB memory in use.
```

### 当前 GPU 使用情况

| GPU | 显存占用 | PID | 备注 |
|-----|---------|-----|------|
| 0 | 10055/24564 MiB | 251924 | 繁忙 |
| 1 | 3593/24564 MiB | 318424 | |
| 2 | 7330/24564 MiB | 266521+266790 | 双进程 |
| 3 | 13325/24564 MiB | **319555** | 已重启的同实验（有 CUDA_VISIBLE_DEVICES=3） |
| 4 | 18547/24564 MiB | 271921 | 近满 |
| 5 | 6557/24564 MiB | 318748 | |

### 修复建议

1. **修 train_sft.py**：在 `main()` 开头添加 `--gpu` 参数的实际处理逻辑：
   ```python
   if args.gpu is not None:
       os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu
   ```

2. **确认 PID 319555 是否在正常训练**：当前该进程已在 GPU 3 上运行且 CUDA_VISIBLE_DEVICES=3 已设置正确。如果日志正常推进，无需重新提交。

3. **补充 bitsandbytes 依赖**（低优先级）：`pip install nvidia-nvjitlink-cu12` 可消除警告，但不影响训练。

---
