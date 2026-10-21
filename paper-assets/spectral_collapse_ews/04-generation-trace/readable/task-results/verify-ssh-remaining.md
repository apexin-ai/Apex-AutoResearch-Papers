# verify ssh remaining

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_ssh-remaining_20260525T203659_result.json`
- **Structured JSON:** [`1f12e0cff923fcf309fc.json`](../../sessions/1f/1f12e0cff923fcf309fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。所有论文数值与服务器原始数据一致：

**GPT-2-medium r=0:**
- Gen 9 SLV=415.1 ✅, PPL=328.8 ✅, σ₁=1570.7 ✅
- U-shape 确认: 6598→1191(Gen2 min)→1571(Gen9)

**Pythia-1B pilot:**
- Gen 0 SLV=2835.3/PPL=8.07 ✅, Gen 1 r_eff=570.7 ✅, Gen 2 r_eff=580.9 ✅, Gen 3 SLV=2864.8/PPL=13.44 ✅

**GPU-hours:** ~366 GPU-hours (含调试), 有效约 300-350h, 2× RTX PRO 6000 (98GB), 跨度 10 天。

报告已写入 `artifacts/server_data_verification.md`。

---
