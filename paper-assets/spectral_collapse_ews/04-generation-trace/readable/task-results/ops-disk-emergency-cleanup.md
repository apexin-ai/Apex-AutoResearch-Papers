# ops disk emergency cleanup

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-emergency-cleanup_20260521T113957_result.json`
- **Structured JSON:** [`56f327ad736cd74f0795.json`](../../sessions/56/56f327ad736cd74f0795.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。结果汇总：

---

### 1. 磁盘清理
- **清理前**：250G / 100% 满
- **清理后**：148G 使用 / 103G 可用 / **59%**
- **释放**：~102GB
- 保留目录正确：`fixed_mix_r025_seed42`、`fixed_mix_r025_seed43`、`fixed_mix_r025_seed44`

### 2. exp_015 状态：**存活**
- PID 516836，GPU 1，19GB 显存，94% 利用率
- 当前：**Gen 1 fine-tuning 中**（Gen 0 已完成，生成 37500 样本后正在训练）
- 磁盘清理及时，exp_015 未受影响

### 3. exp_014 崩溃详情
- **崩溃原因**：`No space left on device (os error 28)` — Gen 6 训练完成（loss=1.0873），保存 checkpoint 时磁盘满
- **数据完整性**：
  - gen_0 ~ gen_5：完整（每个目录 190 bytes 的元数据）
  - gen_6：**不完整** — 有 model.safetensors（1.3GB）和 config，但训练后的 metrics/results 未记录（崩溃在 save_pretrained）
  - gen_7 ~ gen_9：未执行

### 4. 断点续跑：**支持**
- `run_phase1.py` 支持 `--start_gen` 参数（line 100-101）
- exp_014 可从 gen 6 重跑（gen_6 checkpoint 虽然保存了 model.safetensors，但需确认完整性）
- 重启命令示例：
  ```bash
  python run_phase1.py --condition fixed_mix --seed 43 --generations 10 \
    --signal log_det --tau 0.002 --k 0 --signal_mode per_gen \
    --real_ratio 0.25 --gpu 0 --start_gen 6
  ```

### 5. exp_015 无需重启
进程正常运行，磁盘空间已充足（103GB 可用），可继续完成剩余 gen。

**建议**：等 exp_015 跑完后（占用 GPU 1），再用空闲 GPU 重启 exp_014 从 `--start_gen 6`。或者如果想并行，可在 GPU 0 上重启 exp_014。

---
