# code prep eval v8 1 v8b

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_eval_v8_1_v8b_20260516T051455_result.json`
- **Structured JSON:** [`98fb6c5456bed4b34e69.json`](../../sessions/98/98fb6c5456bed4b34e69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建并通过语法检查：

**`run_v8_1_final_eval.sh`** — v8_1 (gradient isolation + λ_margin=0.2)
- Checkpoint: `checkpoints/imm_anchor_v8_1/latest`
- Config: `configs/imm_anchor_v8_1.yaml`

**`run_v8b_final_eval.sh`** — v8b (ACIS-only two-stage)
- Checkpoint: `checkpoints/imm_anchor_v8b_twostage/stage2/latest`
- Config: `configs/imm_anchor_v8b_twostage.yaml`

每个脚本流程：
1. **Phase 1**: Standard eval (500 batch, train mode soft forward) — 产出 standard + ACIS+prune 条件
2. **Phase 2**: Bypass-ACIS eval (500 batch) — 产出 bypass + random prune 条件
3. **Phase 3**: 从 standard eval 提取 ACIS-prune JSON（remap `pruneTrue→pruneFalse` 以适配 analyze_gate.py 接口）
4. **Phase 4**: Gate analysis (G1-G4，baseline=0.004077)，含 `--acis-prune` 和 `--bypass`
5. **Summary**: 打印 4 条件 clean action_loss 对比表

关键设计点：
- Train mode 通过 monkey-patch `evaluate.load_model_and_checkpoint` 实现，加载后调 `model.train()` 替代默认的 `model.eval()`
- `CUDA_VISIBLE_DEVICES=$GPU` + `--gpu 0`，默认 GPU=0，参数可覆盖
- Pre-flight 检查 checkpoint 存在性，训练未完成会报错退出

---
