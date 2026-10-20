# analysis round10 data compilation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_round10_data_compilation_20260516T002532_result.json`
- **Structured JSON:** [`4fb68aa6bbc5e3441356.json`](../../sessions/4f/4fb68aa6bbc5e3441356.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已注册为 artifact `art_20260516_c8f9bc`。

编译完成。核心结论：

**12 claims 中 8 confirmed, 2 partially confirmed, 1 gate_failed (future work), 1 confirmed (running 补充数据)**

关键数字：
- PPL dose curve (n=500): DS 0.39→1.21→3.99→8.48, QW 0.07→0.31→1.07→3.16, 两模型 Spearman ρ=1.0, 全部 imp p<1e-14
- QW accuracy: 0.40→0.36→0.36→0.33→0.19, 断崖在 s025→s030 (−14pp)
- GSM8K: phase gradient 跨 benchmark 复现, 但 strategy specificity 从 15–36× 衰减至 2.3–3.8×

待补：acc_ds_s015_8k_v2 和 acc_ds_s030_8k_v2 仍在运行（DS accuracy 5-point curve 缺 2 点，但已降为定性观察，不阻塞论文）。

---
