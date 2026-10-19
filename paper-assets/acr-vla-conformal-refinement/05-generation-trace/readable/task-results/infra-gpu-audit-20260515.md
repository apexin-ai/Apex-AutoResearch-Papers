# infra gpu audit 20260515

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-audit-20260515_20260515T191007_result.json`
- **Structured JSON:** [`c502322725df1a5bdcf6.json`](../../sessions/c5/c502322725df1a5bdcf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部拿到。以下是汇总结果。

---

## GPU 利用率总览

### bjb1-32546 — 6×4090，**6/6 全部占用**

| GPU | 显存占用 | GPU利用率 | PID | 实验名 |
|-----|---------|----------|-----|--------|
| cuda:0 | 5201/24564 MiB | 23% | (截断部分) | 推断有eval进程运行 |
| cuda:1 | 4700/24564 MiB | 22% | 111718 | eval-vla-mean-object-seed43 (vla_only, mean) |
| cuda:2 | 4736/24564 MiB | 22% | 114664+ | eval-scalar-object-seed43 (crm_scalar) |
| cuda:3 | 5665/24564 MiB | 24% | 148797 | eval-obs-only-object-norm02-seed43-r2 (crm_obs_only, norm=0.2) |
| cuda:4 | 5202/24564 MiB | 23% | 134103 | eval-acr-object-obs-only-default (crm_obs_only, default norm) |
| cuda:5 | 5201/24564 MiB | 23% | (截断部分) | 推断有eval进程运行 |

> 输出中间截断了 ~4800 字符，cuda:0 和 cuda:5 的具体进程信息在截断中。但所有 6 张卡均有 ~5GB 显存占用和 ~22% GPU 利用率，确认全部在跑实验。

---

### bjb2-28827 — 6×4090，**6/6 全部占用**

| GPU | 显存占用 | GPU利用率 | PID | 实验名 |
|-----|---------|----------|-----|--------|
| cuda:0 | 5201/24564 MiB | 19% | 105946 | eval-mag-perdof-norm003-object (crm_perdof, norm=0.03) |
| cuda:1 | 5200/24564 MiB | 18% | 109655 | crm_perdof, object, norm=0.05 |
| cuda:2 | 5664/24564 MiB | 18% | 127581 | eval-mag-perdof-norm0p3-object-r2 (crm_perdof, norm=0.3) |
| cuda:3 | 5664/24564 MiB | 19% | 118886 | crm_perdof, object, norm=0.3 |
| cuda:4 | 5200/24564 MiB | 18% | **101616** | **eval-mag-obsonly-norm005-object** (crm_obs_only, norm=0.05) |
| cuda:5 | 5200/24564 MiB | 20% | **103034** | **eval-mag-obsonly-norm03-object** (crm_obs_only, norm=0.3) |

> **两个"幽灵"实验都在 bjb2-28827 上：**
> - PID 101610 (bash 包装) / 101616 (python) → cuda:4 → `eval_object_obs_only_norm005.json`
> - PID 103028 (bash 包装) / 103034 (python) → cuda:5 → `eval_object_obs_only_norm03.json`
> 
> 这两个是通过 nohup 手动启动的（非 agent-ml 框架），所以之前查不到。

---

### bjb1-18228 — 4×4090，**4/4 全部占用**

| GPU | 显存占用 | GPU利用率 | PID | 实验名 |
|-----|---------|----------|-----|--------|
| cuda:0 | 5664/24564 MiB | 20% | 390936 | crm_perdof, object, default norm, seed=42 |
| cuda:1 | 3804/24564 MiB | 16% | 365930 | eval-perdof-object-seed43 (crm_perdof, norm=0.1) |
| cuda:2 | 3342/24564 MiB | 18% | 356495 | eval-obs-only-object-seed43 (crm_obs_only, norm=0.1, seed=43) |
| cuda:3 | 3306/24564 MiB | 23% | 356701 | eval-argmin-object-seed43 (reconvla, object, seed=43) |

---

### bjb2-40593 — 1×4090D，**1/1 占用**

| GPU | 显存占用 | GPU利用率 | PID | 实验名 |
|-----|---------|----------|-----|--------|
| cuda:0 | 2499/24564 MiB | 13% | 227434 | eval-mag-obsonly-norm003-b2 (crm_obs_only, spatial, norm=0.03) |

> tmux 里还有一个 `eval-reconvla-object` 的包装进程，但其 python 子进程已结束（无高 CPU python 进程），只有 norm003 实验在跑。

---

## 结论

**空闲 GPU：0 张。** 17 张卡全部在跑 eval 实验。

- 预期 cuda:3,4 空闲的 bjb1-32546 → 实际 6/6 满载
- 预期 cuda:2-5 空闲的 bjb2-28827 → 实际 6/6 满载（含两个"幽灵"nohup 实验）
- 两个"幽灵"实验均在 **bjb2-28827** 上，PID 101610 (cuda:4) 和 PID 103028 (cuda:5)，都是活跃运行状态

---
