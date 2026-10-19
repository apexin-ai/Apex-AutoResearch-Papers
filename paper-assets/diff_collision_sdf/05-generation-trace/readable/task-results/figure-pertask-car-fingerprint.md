# figure pertask car fingerprint

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_pertask_car_fingerprint_20260527T180722_result.json`
- **Structured JSON:** [`25a8434d5e8f57833425.json`](../../sessions/25/25a8434d5e8f57833425.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 产出总结

**图表** — `fig_pertask_car_fingerprint.pdf/.png`（服务器 `/root/autodl-tmp/artifacts/`，已注册 `art_20260527_889c4a`）
- Grouped bar chart，4 task × 4 condition
- X 轴按 CAR 降序：Choco. Pudding > Milk > Orange Juice > BBQ Sauce
- 蓝色渐变：浅→深 = λ 递增（0, 0.005, 0.01, 0.1）
- LoRA-only 和 λ=0.1 有 individual seed dots + error bars（2-seed）
- λ=0.005 和 λ=0.01 为 3-seed mean（无 per-task 逐 seed 数据）
- "highest"/"lowest" 标注 + "ordering invariant across λ" 注释框

**abstract.tex** — line 8 加了 "EE-only"：`rather than EE-only geometric supervision`

**实际数据（来自 appendix.tex Table 8）：**

| Condition | CP | Milk | OJ | BBQ |
|---|---|---|---|---|
| LoRA-only (s0/s1 mean) | 71.0 | 69.0 | 61.0 | 18.0 |
| λ=0.005 (3-seed mean) | 72.7 | 71.3 | 54.0 | 20.0 |
| λ=0.01 (3-seed mean) | 72.7 | 72.0 | 57.3 | 23.3 |
| λ=0.1 (s0/s1 mean) | 73.0 | 69.0 | 63.0 | 28.0 |

注：LoRA s2 per-task 数据不在论文 Table 8 中（仅 aggregate 55.0% 在 null distribution section）。λ=0.005/0.01 仅有 3-seed 均值。

---
