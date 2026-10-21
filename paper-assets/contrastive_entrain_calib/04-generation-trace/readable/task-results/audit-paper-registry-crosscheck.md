# audit paper registry crosscheck

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper-registry-crosscheck_20260523T191603_result.json`
- **Structured JSON:** [`eb5e591a2b741e3f32cd.json`](../../sessions/eb/eb5e591a2b741e3f32cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 数据自查报告

### ⚠️ 需修复 (3 个)

**1. Abstract/Conclusion vs Discussion 分母不一致** — 最高优先
- Abstract/Conclusion: **"4/31 (12.9%)"** — 包含 gs=8 的 3 个 checkpoint (12+16+3=31)
- Discussion: **"4/28 (14.3%)"** — 仅 gs=2 (12+16=28, 3/12 s1 + 1/16 s2)
- 两个数字各自正确，但读者会以为指同一件事。审稿人很可能注意到。
- **建议**: 统一为 4/28 (14.3%) 或在 abstract 注明 "across all group sizes"

**2. gs=8 轨迹描述为 "monotonically declining"** — 实际 0.084→0.085→0.054，先微升 (+0.0001) 再降

**3. R3 饱和步数** — cosine_failure.tex 写 "by step 300"，registry 记录 step 100 (0.9998 值正确)

### ✅ 核对一致 (~65 个数字)

所有可由 Registry 追溯的核心指标均一致（仅四舍五入差异）：
- Direction quality: AUROC、per-strength、per-domain、probe ablation 全部匹配
- Vanilla baseline: SYCONScore/ToF/NoF 匹配
- R3-only GRPO: 所有 checkpoint SYCONScore + ToF/NoF + 计数 (3/12, 1/16) 匹配
- ACT: 所有 checkpoint 值 + 47/47 计数 (16+15+16) 匹配
- Probe trap: 4 个 checkpoint 的全部指标匹配
- ActAdd: alpha=5 的 3 个指标匹配
- Held-out: peak/ceiling/ratio 全部计算验证通过
- 1.7× SFT/GRPO ratio: 0.2673/0.1529=1.748 ✅

### ❌ 待确认 (9 项，需查训练日志)

1. **Direction cosine ≈ 0.96** — Registry 中 GRPO 的 cosine=0.28（这是 cosine failure），0.96 可能来自 ACT 训练但无 registry 数据
2. **Post-recalibration AUROC 0.910** — exp002v2-recalib 无 metrics 记录
3. **AUROC 0.76→0.60 (truncation)** — 独立分析脚本产出
4. **R3 ~0.98 + p=0.703** — exp-003 训练日志
5. **Probe trap entropy/reward 值** (0.702, 0.800, +0.72 等) — exp-008v3 训练日志
6. **AUROC <0.01 variation across checkpoints** — per-checkpoint AUROC 分析
7. **Failure mode taxonomy 百分比** — 手工标注 (内部算术一致: 总和 100.1%)
8. **F1c entropy 0.069 / 300 steps** — 训练日志
9. **80–84% truncation rate** — 分析脚本

完整报告已注册: `art_20260523_bf0307`

---
