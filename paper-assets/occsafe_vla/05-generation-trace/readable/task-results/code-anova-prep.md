# code anova prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_anova-prep_20260527T121225_result.json`
- **Structured JSON:** [`af15c0451bb5e7ed66bb.json`](../../sessions/af/af15c0451bb5e7ed66bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

**产出 1: ANOVA 脚本** — `/root/occsafe_vla/analysis/factorial_anova.py` (westd-34685)
- Dry-run 通过，当前数据 N=9 (3+1+4+1)
- 当前结果: gradient_flow main effect F=1.475, p=0.279 (ns, η²=0.228); norm_type F=0.512, p=0.506 (ns); interaction F=0.085, p=0.782 (ns)
- Cell 1 (Full OCC BN) vs Vanilla: Δ=-0.020, p=0.651 (ns)
- Cell 3 (Detach BN) vs Vanilla: Δ=+0.021, p=0.309 (ns)
- Cells 2/4 n=1,无法做 t-test — 等待后续 eval 补齐
- `--update-cell` 增量添加已验证可用，`--reset` 重置已验证
- statsmodels 已安装到 occsafe conda env

**产出 2: Eval 命令文档** — `artifacts/eval_commands.md`
- 4 批次 × 8 实验，所有 checkpoint 路径已 SSH 验证存在
- 关键路径修正: `full_occ_ln_v2_s1c_r2` → 实际 dir 是 `full_occ_ln_v2_s1c`; `full_occ_ln_v2_s2_r2` → 实际 dir 是 `full_occ_ln_v2_s2`
- 包含 post-eval 更新命令映射表和最终预期样本量

---
