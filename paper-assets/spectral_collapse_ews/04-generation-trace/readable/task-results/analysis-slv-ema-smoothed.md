# analysis slv ema smoothed

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_slv-ema-smoothed_20260518T095452_result.json`
- **Structured JSON:** [`def905c3a9663ab3d69e.json`](../../sessions/de/def905c3a9663ab3d69e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整输出：

```
Raw 一阶 delta: ['-1.60', '28.90', '29.80', '24.50', '39.80', '19.50', '18.60', '16.70', '17.20', '12.10']

EMA-smoothed 一阶 delta (alpha=0.3):
  Gen 0->1: raw=-1.60  EMA=-1.60
  Gen 1->2: raw=+28.90  EMA=+7.55
  Gen 2->3: raw=+29.80  EMA=+14.23
  Gen 3->4: raw=+24.50  EMA=+17.31
  Gen 4->5: raw=+39.80  EMA=+24.06
  Gen 5->6: raw=+19.50  EMA=+22.69
  Gen 6->7: raw=+18.60  EMA=+21.46
  Gen 7->8: raw=+16.70  EMA=+20.03
  Gen 8->9: raw=+17.20  EMA=+19.18
  Gen 9->10: raw=+12.10  EMA=+17.06

二阶 delta2 (on EMA-smoothed):
  Gen 1->2: +9.15
  Gen 2->3: +6.68
  Gen 3->4: +3.08
  Gen 4->5: +6.75
  Gen 5->6: -1.37
  Gen 6->7: -1.23
  Gen 7->8: -1.43
  Gen 8->9: -0.85
  Gen 9->10: -2.13

Monotonicity 检查:
  EMA delta 序列: ['-1.60', '7.55', '14.23', '17.31', '24.06', '22.69', '21.46', '20.03', '19.18', '17.06']
  EMA delta 从 Gen 4->5 起严格单调递减
  二阶 delta 最长连续负值: 5 gens (从 Gen 5 起)


--- Phase 0 (r=0) EMA comparison ---
EMA delta: ['98.08', '70.21', '40.34', '17.58', '1.84', '-9.21', '-15.74', '-26.64', '-32.01', '-31.00']
二阶 EMA: ['-27.87', '-29.87', '-22.76', '-15.74', '-11.05', '-6.53', '-10.90', '-5.37', '1.02']
```

---

### 关键问题回答

**1. Gen 8→9 微弹是否被消除？**
是。Raw 一阶 delta 在 Gen 8→9 从 16.70 反弹到 17.20（+0.50），但 EMA-smoothed 序列中 Gen 8→9 = 19.18，严格小于 Gen 7→8 = 20.03。微弹完全被 EMA 吸收。

**2. EMA-smoothed 一阶 delta 是否严格单调递减？**
是，从 Gen 4→5 (24.06) 起连续 5 步严格单调递减至 Gen 9→10 (17.06)。这覆盖了后半段全部 generation。

**3. EMA-smoothed 二阶 delta 连续负值是否更长？**
是。Raw 二阶 delta 最长连续负值为 3 gens（Gen 5→7），而 EMA-smoothed 二阶 delta 从 Gen 5 起连续 5 gens 全负（-1.37, -1.23, -1.43, -0.85, -2.13），覆盖到序列末尾。

**对比 Phase 0**：Phase 0 的 EMA 二阶 delta 在最后一步（Gen 9→10）出现 +1.02 正值，说明 collapse 减速趋势在尾部有扰动，而 Phase 1 的减速信号反而更干净。

---
