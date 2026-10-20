# code prepare s123 signal batch scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-s123-signal-batch-scripts_20260516T012649_result.json`
- **Structured JSON:** [`bee221838abe739327a1.json`](../../sessions/be/bee221838abe739327a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建，语法检查通过。

### 确认结果

**argparse 检查**：
- `--signal` 只接受单值 (`s1|s2|s3|s4|all`)，不支持 `s1 s2 s4`
- `--signal all` 安全：s3 在 eval paths 为 None 时返回空列表并 log warning，不会崩溃
- `--ref-model-path` 参数名确认正确

**环境**：conda（`/root/miniconda3/bin/python`），脚本开头已包含 `source conda.sh && conda activate base`

### 脚本位置

- `exp002/run_05B_s123_signals.sh` — 4 个 0.5B s123 checkpoint × 3 benchmarks = 12 runs
- `exp002/run_15B_s123_signals.sh` — 4 个 1.5B s123 checkpoint × 3 benchmarks = 12 runs

### 运行命令

```bash
# 0.5B (先确认目标 GPU 空闲，遵守 C001/C002/C004)
CUDA_VISIBLE_DEVICES=N nohup bash /root/contamcal-irt-calibration/exp002/run_05B_s123_signals.sh > /tmp/signals_05B_s123.log 2>&1 &

# 1.5B (不同 GPU)
CUDA_VISIBLE_DEVICES=M nohup bash /root/contamcal-irt-calibration/exp002/run_15B_s123_signals.sh > /tmp/signals_15B_s123.log 2>&1 &
```

### 预估时间

- 0.5B：~2-3 小时（12 runs，每个约 10-15 min）
- 1.5B：~4-6 小时（12 runs，每个约 20-30 min）

---
