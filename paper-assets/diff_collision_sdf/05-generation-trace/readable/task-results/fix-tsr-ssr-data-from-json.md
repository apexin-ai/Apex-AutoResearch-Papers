# fix tsr ssr data from json

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_tsr_ssr_data_from_json_20260527T234625_result.json`
- **Structured JSON:** [`90ba74894e66e10ab81b.json`](../../sessions/90/90ba74894e66e10ab81b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 main.tex，无法在服务器上编译。这些 section 文件可能在 Overleaf 或本地组装。

---

## 完成汇总

### 已验证数据（全部来自 reeval JSON，eval seed=7）

| 条件 | TSR (%) | CAR (%) | SSR (%) | SSR/TSR |
|------|---------|---------|---------|---------|
| Baseline | 71.5 | 28.5 | 28.0 | **0.392** |
| LoRA s0 | **51.5** | 56.5 | 29.5 | 0.573 |
| LoRA s1 | **51.5** | 52.5 | 27.0 | 0.524 |
| LoRA s2 | **51.5** | 55.0 | 26.5 | 0.515 |
| λ=0.005 s0/s1/s2 | 55.5/50.5/56.0 | 57.0/54.0/52.5 | 30.0/24.0/29.5 | 0.541/0.475/0.527 |
| λ=0.01 s0/s1/s2 | 52.5/55.5/53.5 | 57.0/57.5/54.5 | 32.5/30.0/28.0 | 0.619/0.541/0.523 |

### 关键发现
- **SSR/TSR baseline = 0.392** → appendix 的 0.39 正确，正文的 0.33 是错的
- **LoRA TSR = 51.5% 是真实数据**，三个种子碰巧都是 103/200，不是占位符
- **Threshold 表 LoRA s0 dfCAR = 56.5** 与 reeval 微平均一致，正确

### 已执行修改

| 文件 | 行 | 旧值 → 新值 |
|------|-----|-------------|
| claim3.tex | 17 | `49.7\,$\pm$\,3.2` → `51.5\,$\pm$\,0.0` |
| claim3.tex | 30 | `from 0.33 (baseline)` → `from 0.39 (baseline)` |
| claim3.tex | 30 | `21--25\,pp` → `21--23\,pp` |
| claim3.tex | 30 | `49.7--54.0\%` → `51.5--54.0\%` |
| discussion.tex | 12 | `from 0.33 to 0.51` → `from 0.39 to 0.51` |
| discussion.tex | 12 | `21--25\,pp` → `21--23\,pp` |
| appendix.tex | — | 无需修改（SSR 表和 threshold 表数据均已验证正确） |

### 未修改但需注意
- **per-task CAR 表**与 reeval 数据有微小差异（LoRA s0: 57.0% vs 56.5%），来自不同评估运行，0.5pp 差距可接受
- **λ=0.1 数据** (TSR=48.0±1.4) 未找到完整的 30k eval JSON 来验证，保持原值

---
