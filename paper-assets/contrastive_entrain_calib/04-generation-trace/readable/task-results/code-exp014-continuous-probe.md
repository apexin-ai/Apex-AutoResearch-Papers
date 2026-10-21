# code exp014 continuous probe

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp014-continuous-probe_20260518T164640_result.json`
- **Structured JSON:** [`2b41b93b11e8caa275c4.json`](../../sessions/2b/2b41b93b11e8caa275c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入并通过语法检查：

**`probe_module.py`** — 探针模块
- `LinearProbe`: 单层线性 + sigmoid，输出 P(sycophantic)
- `train_probe()`: 从 activations.pt 提取 reward layers 的 mean hidden state，用 condition 标签（invalid_pressure=1, valid_correction=0）训练 logistic regression，200 epochs
- `save_probe()` / `load_probe()`: 序列化/反序列化

**`run_exp014_continuous_probe.py`** — 主训练脚本
- `ProbeTrainer(DCGRPOTrainer)`: 仅覆写 `compute_r1`，用冻结探针的 `1.0 - P(syc)` 替代方向投影
- 保留 `direction_path` 指向 exp-001 的 directions.pt（避免 `_DCRewardCallable` 中 `d_syc is None` 短路跳过 R1）
- 参数：R1=0.25, R2=0.0, R3=0.75, LoRA r=16/alpha=32, 8000 步, num_generations=2
- 探针训练后自动保存到 `OUTPUT_DIR/probe.pt`，下次运行直接加载

---
