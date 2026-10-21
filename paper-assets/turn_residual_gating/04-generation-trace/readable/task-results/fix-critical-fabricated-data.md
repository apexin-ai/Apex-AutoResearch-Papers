# fix critical fabricated data

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_critical_fabricated_data_20260525T210328_result.json`
- **Structured JSON:** [`8a6b2a05f4407b82a0dc.json`](../../sessions/8a/8a6b2a05f4407b82a0dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改总结：

**CRITICAL — 0.055 清除（3处）：**
- `tab_perseed_tg.tex` caption：删除 "0.055 (s123)" 和 "9.1×"，改为明确标注 s123 无 N=50 数据
- `paper/sections/appendix.tex:635`：重写 ThreadGate 段落，改用 N=5 协议真实数据（0.016 vs 0.017, gap 32.1× vs 30.6×），N=50 仅报 s42
- `docs/paper/sections/appendix.tex:635`：同步修正

**W1 — crossmodel 表：** SS AR PPL 1.441 → 1.442（来源 `d048_final_ar_eval` ppl.ss=1.442）

**W2 — perseed TG 表：** Caption 已修正为只报 s42 的 N=50 数据

**SS gap 一致性：** 全文 14 处引用逐一验证通过；s456 gap 从错误的 1.2× 修正为 1.1×（0.496/0.433=1.146）

**INFO：** Cost table 已正确（LoRA-only 5.7h, UG 6.1h），无需改动

**验证：** 0.055 搜索 0 hits，9.1× 仅存于无关的 dream_reports，crossmodel 8 行 gap 算术全部通过。

---
