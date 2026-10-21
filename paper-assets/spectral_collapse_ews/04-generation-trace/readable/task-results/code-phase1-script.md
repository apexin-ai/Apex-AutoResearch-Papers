# code phase1 script

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1_script_20260516T154224_result.json`
- **Structured JSON:** [`6619571c71df38fbafee.json`](../../sessions/66/6619571c71df38fbafee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

**完成的修改：**

### `src/config.py`
- 新增 `results_filename` 字段（默认 `"phase0_results.json"`，向后兼容）
- 新增 SpectralController 参数：`controller_k`, `controller_tau`, `controller_r_min`, `controller_r_max`, `controller_r_base`

### `src/pipeline.py`
- `run_recursive_training` 新增可选参数 `results_dir`, `checkpoint_dir`, `results_filename`（None 时回退到 Config 默认值）
- Controller 创建改用 Config 中的参数（不再硬编码）
- 每代结果追加 `mix_ratio` 字段

### `run_phase1.py`（新文件）
- CLI 参数：`--condition` (pure_collapse/fixed_mix/adaptive), `--seed`, `--tau`, `--k`, `--r_min`, `--r_max`, `--gpu`, `--generations`
- 三种条件映射：pure_collapse → ratio=0.0, fixed_mix → ratio=0.5, adaptive → ratio=-1.0 + controller 参数
- Checkpoint 写入 `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/{condition}_seed{seed}/`
- 结果写入 `results/phase1_{condition}_seed{seed}_results.json`
- 训练结束后额外保存带完整元数据的 `_summary.json`
- 全链路 seed 控制（random/numpy/torch/cudnn）

---
