# analysis controller activation window

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_controller-activation-window_20260518T202743_result.json`
- **Structured JSON:** [`ca642b9d7e14ef3e993a.json`](../../sessions/ca/ca642b9d7e14ef3e993a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

## Controller Activation Table (τ=0.002, α=0.5)

| Gen | r=0 Δ_t | act? | r=0.2 Δ_t | act? | r=0.5 Δ_t | act? |
|-----|---------|------|-----------|------|-----------|------|
| 0 | --- | --- | --- | --- | --- | --- |
| 1 | -0.020721 | ✗ | -0.000164 | ✗ | +0.000333 | ✗ |
| 2 | -0.011452 | ✗ | +0.001852 | ✗ | -0.005939 | ✗ |
| 3 | +0.000477 | ✗ | +0.000035 | ✗ | -0.009270 | ✗ |
| 4 | **+0.007742** | **✓** | -0.003504 | ✗ | -0.009797 | ✗ |
| 5 | **+0.011239** | **✓** | -0.005923 | ✗ | -0.013310 | ✗ |
| 6 | **+0.013016** | **✓** | --- | --- | -0.010784 | ✗ |
| 7 | **+0.013052** | **✓** | --- | --- | -0.009314 | ✗ |
| 8 | **+0.017527** | **✓** | --- | --- | -0.008185 | ✗ |
| 9 | **+0.018175** | **✓** | --- | --- | -0.007737 | ✗ |
| 10 | **+0.015134** | **✓** | --- | --- | -0.006421 | ✗ |

## 总结

- **r=0**: 7/10 代激活（Gen 4-10 连续激活）。Gen 1-3 负 delta 反映初始 SLV 上升，之后持续正 delta = 持续 collapse 信号。
- **r=0.2**: 0/5 代激活。delta 最大仅 +0.001852（Gen 2），远低于阈值。混入 20% 真实数据即完全消除 collapse 信号。
- **r=0.5**: 0/10 代激活。所有 delta 均为负值（SLV 在上升），controller 永远看不到 collapse 信号。

**Signal attenuation paradox 完全成立**：r=0 时 controller 从 Gen 4 起持续激活且信号递增；r=0.2 时信号已衰减到阈值以下（比 r=0 弱约 4-10 倍）；r=0.5 时信号彻底反转为负（SLV 上升而非下降）。paradox 的核心机制确认——mixing ratio 越高，collapse 信号衰减越强，controller 越早失明。

输出文件：`/root/spectral_collapse_ews/results/controller_activation_analysis.json`

---
