# code paperbanana fig2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paperbanana-fig2_20260529T013921_result.json`
- **Structured JSON:** [`f715aa4712e7a5a92219.json`](../../sessions/f7/f715aa4712e7a5a92219.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Final visual check passes:

1. **Data points**: BN OFF=0.767, BN ON=0.725, LN OFF=0.802, LN ON=0.773 — all correct
2. **Error bars**: Correct sizes (BN: ±0.024/±0.064, LN: ±0.024/±0.027)
3. **Vanilla baseline**: At 0.745, labeled correctly
4. **Colors**: BN muted red, LN gold, baseline blue
5. **"−4.2 pp" and "−2.9 pp"**: Clear, no overlap with baseline
6. **Legend**: Solid (BN) vs dashed (LN) distinguishable
7. **n-labels**: All 4 visible (n=4, n=3, n=3, n=4)
8. **Serif font, no top/right spines, 300 DPI**

产出：
- PNG: `docs/paper/figures/factorial_2x2_pb.png`
- PDF: `docs/paper/figures/factorial_2x2_pb.pdf`
- 脚本: `artifacts/figures/gen_factorial_2x2_v3.py`

LN 数据已修正（OFF: 0.826→0.802, ON: 0.777→0.773），n 值也更新（OFF: 1→3, ON: 3→4）。PaperBanana 因 Gemini API 报错无法使用，已用 matplotlib 手写脚本完成，迭代 4 轮视觉检查。

---
