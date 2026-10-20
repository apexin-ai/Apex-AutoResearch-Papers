# code paperbanana fig1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paperbanana-fig1_20260529T012332_result.json`
- **Structured JSON:** [`3a12ba4d1721a2839ac3.json`](../../sessions/3a/3a12ba4d1721a2839ac3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**PaperBanana 不可用**（Gemini API 429 RESOURCE_EXHAUSTED，credits 耗尽），已回退到 matplotlib 手写脚本，经 3 轮视觉迭代。

**产出文件**（均在 `docs/paper/figures/`）：
- `fig1_architecture_pb.png` — 300 DPI, 4125×1515 px
- `fig1_architecture_pb.pdf` — PDF 版本
- `fig1_architecture_pb.py` — 源脚本，可后续微调

**3 轮迭代改进**：
1. Round 1 → 基础布局生成
2. Round 2 → 架构居中、encoder/head box 加宽、grid cell 加高、间距优化
3. Round 3 → 阴影增强、panel 分割线、gradient flow 箭头加粗、整体 polish

---
