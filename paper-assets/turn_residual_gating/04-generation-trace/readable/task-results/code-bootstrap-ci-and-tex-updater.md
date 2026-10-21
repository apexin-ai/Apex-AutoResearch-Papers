# code bootstrap ci and tex updater

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap_ci_and_tex_updater_20260522T135615_result.json`
- **Structured JSON:** [`02f2dceaf3906d2b9442.json`](../../sessions/02/02f2dceaf3906d2b9442.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**服务器上** (`westd-20861:/root/turn_residual_gating/scripts/`):
- `compute_bootstrap_ci.py` — 重写，支持 3 种 JSON 格式（标准 GAR eval、attention steering、phase1 diagnostic），输出 per-conv 和 pooled mid-turn GAR 的 bootstrap 95% CI + PPL CI。已通过 4 个代表性文件测试通过。
- `d048_number_mapping.md` — 更新为引用 bootstrap 脚本。

**本地** (`scripts/tex_number_map.md`):
- 详细映射了论文 6 个 .tex 文件中所有数值到对应的 eval JSON 文件和字段，含行号。覆盖 abstract、intro、experiments（Table 1 + §5.2 + §5.3 steering）、analysis、discussion、conclusion。

---
