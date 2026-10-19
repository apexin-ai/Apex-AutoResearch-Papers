# run phase0 vip gate1c

**temp adv distill vla** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_phase0-vip-gate1c_20260515T053917_result.json`
- **Structured JSON:** [`976a6ab7370b615a7ebb.json`](../../sessions/97/976a6ab7370b615a7ebb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 0 VIP Gate 1(c) 验证结果

### VIP 安装: OK (绕过 hydra，直接加载 checkpoint from download.pytorch.org)

### Gate 1(c) 结果

| Metric | Value |
|--------|-------|
| ρ Mean | 0.7197 |
| ρ Median | 0.7272 |
| ρ P25 | 0.6918 |
| ρ P75 | 0.7523 |
| ρ Min | 0.5503 |
| ρ Max | 0.8287 |
| ρ > 0.8 占比 | 8.0% |
| ρ > 0.5 占比 | 100.0% |

对比 ImageNet ResNet50（无 VIP 训练）：cos_sim ρ median=0.43, neg_L2 ρ median=0.46。VIP 训练后 ρ 从 0.43 跃升至 0.73，提升 70%。

### Gate 1(c) 判定: **PASSED** (median ρ = 0.727 > 0.5)

### 产出文件
| 文件 | 大小 |
|------|------|
| `artifacts/phase0_vip_results.json` | 22K |
| `artifacts/phase0_vip_cos_sim_vs_progress.png` | 262K |
| `artifacts/phase0_vip_spearman_boxplot.png` | 65K |

### 执行时间: 4.7 秒（推理），总耗时含 VIP 安装约 25 分钟

### 5 条代表轨迹 cos_sim 曲线特征
- **最低 ρ=0.55**（demo_46, 189帧）：前 40% 进度 cos_sim 平坦（~0.93），后半段缓慢上升，整体单调但斜率小
- **P25 ρ=0.69**（demo_45）：前期小幅波动后稳定上升
- **中位 ρ=0.73**（demo_2）：近似线性上升，cos_sim 从 0.91 到 1.0
- **P75 ρ=0.75**（demo_4）：清晰单调递增，尤其后 30% 上升明显
- **最高 ρ=0.83**（demo_0）：几乎完美单调，cos_sim 从 0.93 平滑上升到 1.0

---
