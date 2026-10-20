# code resume script exp007 10gen

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_resume-script-exp007-10gen_20260518T195100_result.json`
- **Structured JSON:** [`8c82c164c965d208b9ca.json`](../../sessions/8c/8c82c164c965d208b9ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并 chmod +x。

验证结果：
- **`--start_gen`** 参数已支持（`run_phase1.py` 原生支持，描述："Generation to resume from, requires checkpoint and results JSON"）
- **Gen 5 checkpoint** 存在：`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r02_seed42/gen_5/`（含 model.safetensors、config.json 等完整文件）
- **脚本参数** 与 exp_007 原始命令一致（condition=fixed_mix, seed=42, signal=log_det, tau=0.002, k=0, signal_mode=per_gen, real_ratio=0.2），`--generations` 改为 10，新增 `--start_gen 6`
- 路径：`/root/spectral_collapse_ews/scripts/resume_fixed_mix_r02_seed42_gen5to10.sh`

---
