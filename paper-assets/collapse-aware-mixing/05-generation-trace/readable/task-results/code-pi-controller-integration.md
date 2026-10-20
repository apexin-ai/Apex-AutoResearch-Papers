# code pi controller integration

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pi-controller-integration_20260513T081846_result.json`
- **Structured JSON:** [`b8942a8f61610b1ad20b.json`](../../sessions/b8/b8942a8f61610b1ad20b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。文件已写入 `controlled_pipeline.py`。

核心设计：
- **`MixedDataset`**：每个样本独立以概率 `w` 采样真实数据、`(1-w)` 采样合成数据，`set_ratio()` 可在 segment 间动态更新
- **手动训练循环**：每个 segment = `save_steps` 步优化，segment 结束后暂停训练，测量 spectral rank + PPL，PI controller 输出新 `w_t`
- **Controller seeding**：训练前先测初始 rank 喂给 controller，使第一个 segment 后即产生实际控制动作
- **G0 用 `train_generation()`（标准 HF Trainer），G1+ 用 `run_controlled_generation()`（手动循环 + PI 控制）**

---
