# paper update results tex

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_update_results_tex_20260517T062333_result.json`
- **Structured JSON:** [`a8c437e095330eab34a4.json`](../../sessions/a8/a8c437e095330eab34a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。修改内容汇总：

**Spectral Trajectory Characterization (§4.1)**:
- 范围从 Gen 0-3 扩展到 Gen 0-5
- Stage 3 重写为 "Sustained Collapse (Gen 3→5)"，包含加速下降数据（eff_rank 每代跌幅 0.6%→1.5%→1.3%）
- 新增 "Leading Singular Value and Spectral Concentration" 段落：σ₁ 在 Gen 3 后反转上升（700.7→729.6→741.0），几何证据支持 winner-take-all 动态
- 删除 "Full-scale confirmation is pending" 等待性语言

**Table (tab:phase0_metrics)**:
- 从 4 列（Gen 0-3）扩展到 6 列（Gen 0-5）
- Gen 4: eff_rank=485.67, log_det=2405.05, ppl=19.80, distinct4=0.4679, σ₁=729.6, HellaSwag=0.3558, loss=1.098
- Gen 5: eff_rank=479.21, log_det=2370.17, ppl=24.59, distinct4=0.4630, σ₁=741.0, HellaSwag=0.3439, loss=1.047

**Cross-Validation (§4.2)**:
- Perplexity 统计更新：+116% (Gen 1→5)，加入 per-generation 加速增量
- 新增 HellaSwag 专段：pretrained 到 Gen 5 总降 16.7%，确认 downstream capability 退化
- 新增 train_loss vs ppl 交叉验证段：loss 持续降（1.623→1.047）与 ppl 持续升的 divergence 作为独立 collapse 信号
- 删除所有 Phase 0 相关 TODO（仅保留 1 个 Phase 1 TODO）

---
