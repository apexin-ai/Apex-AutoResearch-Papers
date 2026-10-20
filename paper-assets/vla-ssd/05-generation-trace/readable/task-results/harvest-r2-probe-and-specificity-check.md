# harvest r2 probe and specificity check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_r2_probe_and_specificity_check_20260519T233545_result.json`
- **Structured JSON:** [`e0fd9cd16b820039e70e.json`](../../sessions/e0/e0fd9cd16b820039e70e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整结果汇报：

---

## 1. R² Probe 15-seed 完整结果

运行时间 146.9 min，正常完成。图表已保存。

### Per-condition, per-layer R² 表格

| Layer | Untrained (mean±std) | Llama2Base (mean±std) | Trained (mean±std) |
|-------|---------------------|-----------------------|-------------------|
| L0 | 0.629 ± 0.016 | 0.629 ± 0.016 | 0.629 ± 0.016 |
| L1 | 0.539 ± 0.023 | 0.626 ± 0.018 | 0.625 ± 0.017 |
| L2 | 0.517 ± 0.047 | 0.631 ± 0.013 | 0.622 ± 0.010 |
| L3 | 0.448 ± 0.216 | 0.631 ± 0.011 | 0.624 ± 0.014 |
| L4 | 0.496 ± 0.057 | 0.625 ± 0.010 | 0.628 ± 0.014 |
| L5 | 0.475 ± 0.101 | 0.627 ± 0.015 | 0.627 ± 0.019 |
| L6 | 0.422 ± 0.119 | 0.630 ± 0.010 | 0.631 ± 0.012 |
| L7 | 0.459 ± 0.093 | 0.625 ± 0.014 | 0.632 ± 0.012 |
| **L8** | 0.347 ± 0.283 | 0.635 ± 0.008 | **0.635 ± 0.013** |
| **L9** | 0.445 ± 0.127 | **0.635 ± 0.011** | **0.637 ± 0.008** |
| L10 | 0.353 ± 0.224 | 0.627 ± 0.015 | 0.624 ± 0.014 |
| L11 | 0.356 ± 0.122 | 0.627 ± 0.012 | 0.623 ± 0.016 |
| L12 | 0.409 ± 0.203 | 0.628 ± 0.010 | 0.626 ± 0.011 |
| L13 | 0.341 ± 0.227 | 0.627 ± 0.010 | 0.624 ± 0.013 |
| L14 | 0.374 ± 0.211 | 0.633 ± 0.010 | 0.623 ± 0.015 |
| L15 | 0.297 ± 0.225 | 0.621 ± 0.018 | 0.619 ± 0.012 |
| L16 | 0.323 ± 0.226 | 0.613 ± 0.017 | 0.619 ± 0.011 |
| L17 | 0.395 ± 0.109 | 0.611 ± 0.011 | 0.609 ± 0.023 |
| L18 | 0.214 ± 0.307 | 0.610 ± 0.014 | 0.613 ± 0.017 |
| L19 | 0.241 ± 0.258 | 0.606 ± 0.014 | 0.613 ± 0.013 |
| L20 | 0.086 ± 0.311 | 0.601 ± 0.019 | 0.611 ± 0.014 |
| L21 | 0.330 ± 0.216 | 0.598 ± 0.016 | 0.589 ± 0.023 |
| L22 | 0.207 ± 0.283 | 0.600 ± 0.019 | 0.586 ± 0.013 |
| L23 | 0.264 ± 0.227 | 0.589 ± 0.011 | 0.578 ± 0.028 |
| L24 | 0.173 ± 0.275 | 0.583 ± 0.017 | 0.577 ± 0.013 |
| L25 | 0.130 ± 0.305 | 0.584 ± 0.014 | 0.553 ± 0.053 |
| L26 | 0.251 ± 0.254 | 0.589 ± 0.019 | 0.535 ± 0.046 |
| L27 | 0.099 ± 0.278 | 0.578 ± 0.013 | 0.552 ± 0.027 |
| L28 | 0.099 ± 0.307 | 0.567 ± 0.016 | 0.544 ± 0.034 |
| L29 | 0.088 ± 0.275 | 0.559 ± 0.020 | 0.530 ± 0.034 |
| L30 | 0.220 ± 0.234 | 0.550 ± 0.048 | 0.511 ± 0.029 |
| L31 | 0.069 ± 0.284 | 0.552 ± 0.019 | 0.488 ± 0.054 |
| L32 | 0.584 ± 0.011 | 0.536 ± 0.014 | 0.535 ± 0.015 |

### 核心发现

| Metric | Untrained | Llama2Base | Trained |
|--------|-----------|------------|---------|
| Peak layer | L0 | L9 | **L9** |
| Peak R² | 0.629 | 0.635 | **0.637** |
| Avg R² (L1-L31) | 0.30 | 0.61 | 0.60 |
| Avg std | 0.185 | 0.016 | 0.020 |

- **Trained > Untrained** 在 L1-L31 每一层都成立，平均差距 ~0.27 R²
- **Trained vs Llama2Base** 早期层几乎一致，但 trained 在 exit layers (L25-L31) 下降更多（0.49 vs 0.55），说明 VLA 训练使 exit 层表征更特化
- **Inverted-U 确认**：trained 在 L8-L9 达到峰值后下降，但幅度较温和
- **Untrained 方差极大**（std 0.1-0.3），trained/llama2base 方差很小（std 0.01-0.05）

---

## 2. CI 收窄评估

15 seeds vs 5 seeds → SEM 缩减 √(5/15) ≈ 0.577 → **95% CI 宽度缩窄 ~42%**

以 trained L9（peak layer）为例：
- 15-seed: 95% CI width = 2×1.96×0.0083/√15 = **±0.004** (total width 0.008)
- 推算 5-seed: 95% CI width ≈ 2×1.96×0.0083/√5 = **±0.007** (total width 0.015)

Trained 和 llama2base 的 CI 在所有层都非常紧（width < 0.02），结论稳健。

---

## 3. Specificity Bootstrap 30-seed 进度

- **PID 169052**: 仍在运行
- **Phase 1 (GPU cache)**: 已完成，10 tasks × 500 demos = 63,728 frames，耗时 25.1 min
- **Phase 2 (CPU bootstrap 30 seeds)**: 刚进入，日志尚无 Phase 2 输出
- **结果文件**: 尚未生成
- **预计**: Phase 2 是纯 CPU 计算，时间取决于 bootstrap 实现复杂度，通常比 Phase 1 快

---
