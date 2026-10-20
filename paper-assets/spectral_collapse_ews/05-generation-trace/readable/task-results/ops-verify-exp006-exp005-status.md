# ops verify exp006 exp005 status

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_exp006_exp005_status_20260517T174807_result.json`
- **Structured JSON:** [`50c52ef8f4924a094b43.json`](../../sessions/50/50c52ef8f4924a094b43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### exp_006 (k=10, cuda:0)
| 项目 | 状态 |
|------|------|
| 进程 | **存活** — PID 133199 (wrapper) → 133204 (python), 运行 ~16 min |
| tmux | `exp_006` session 存在 |
| GPU 0 | 19036 MiB, 79% 利用率 |
| 当前阶段 | **Gen 1 数据生成中** — 4800/25000 samples (~19%) |
| Gen 0 baseline | eff_rank=417.55, ppl=9.55, distinct4=0.7414 |
| 报错 | 无（padding_side 警告可忽略） |

启动成功，正常运行。

---

### exp_005 (k=20, cuda:1)
| 项目 | 状态 |
|------|------|
| 进程 | **存活** — PID 116947, 运行 ~4.5h |
| tmux | 无独立 session（直接后台运行） |
| GPU 1 | 25008 MiB, 94% 利用率 |
| 当前阶段 | **Gen 3 完成，Gen 4 数据生成中**（log 末尾有 padding 警告，正在生成 samples） |

**exp_005 各代指标：**

| Gen | loss | eff_rank | ppl | distinct4 |
|-----|------|----------|-----|-----------|
| 0 | — | 417.55 | 9.55 | 0.7414 |
| 1 | 1.9863 | 476.93 | 10.09 | 0.6608 |
| 2 | 1.8811 | 486.85 | 10.42 | 0.6149 |
| 3 | 1.7804 | 496.11 | 10.76 | 0.4400 |

趋势：eff_rank 持续上升（417→496），ppl 缓慢上升（9.55→10.76），distinct4 明显下降（0.74→0.44）。典型的 spectral collapse 进展特征——多样性下降伴随有效秩膨胀。

两个实验均正常运行，无报错。

---
