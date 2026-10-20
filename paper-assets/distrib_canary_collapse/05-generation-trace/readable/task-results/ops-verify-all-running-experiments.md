# ops verify all running experiments

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_all_running_experiments_20260521T074535_result.json`
- **Structured JSON:** [`e7af6a13f3663515ee1d.json`](../../sessions/e7/e7af6a13f3663515ee1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部进程已确认。汇总如下：

---

## westd-17855（6 个实验）

### GPU 利用率

| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| 0 | 97% | 14,237 MiB | 97,887 MiB |
| 1 | 96% | 15,269 MiB | 97,887 MiB |
| 2 | 94% | 14,237 MiB | 97,887 MiB |
| 3 | 99% | 70,763 MiB | 97,887 MiB |
| 4 | 65% | 14,535 MiB | 97,887 MiB |
| 5 | 94% | 14,237 MiB | 97,887 MiB |

### 实验进程

| GPU | 实验 | PID | 启动时间 | CPU% | 状态 |
|-----|------|-----|----------|------|------|
| cuda:0 | a000_s47_fp32 (α=0.00, s47) | 454255 | 14:57 | 235% | **正常** |
| cuda:1 | gen_gpt2m_s43_fp32 (GPT-2-medium, s43) | 442662 | ~14:04前 | — | **正常** |
| cuda:2 | a000_s45_fp32 (α=0.00, s45) | 448950 | 14:04 | 214% | **正常** |
| cuda:3 | scale_69b_bf16 (Pythia-6.9B, s43) | 400550 | 07:23 | — | **正常** (70.7G显存) |
| cuda:4 | a052_s43_fp32 (α=0.52, s43) | 454331 | 14:57 | 241% | **正常** |
| cuda:5 | a046_s43_fp32 (α=0.46, s43) | 454886 | 14:57 | 236% | **正常** |

### 异常：无

6/6 实验全部正常运行，GPU 利用率与预期匹配。cuda:4 利用率略低 (65%) 但进程活跃，可能处于数据加载/生成阶段。

---

## westd-19828（2 个实验）

### GPU 利用率

| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| 0 | **0%** | **0 MiB** | 97,887 MiB |
| 1 | 64% | 14,501 MiB | 97,887 MiB |

### 实验进程

| GPU | 实验 | PID | 启动时间 | CPU% | 状态 |
|-----|------|-----|----------|------|------|
| cuda:0 | a050_s43 | — | — | — | **无进程** |
| cuda:1 | a000_s46_fp32 (α=0.00, s46) | 647974 | 14:15 | 163% | **正常** |

### 异常

- **cuda:0 — a050_s43 无实际进程**。GPU 利用率 0%、显存 0 MiB，无任何 `iterative_train` 进程绑定该 GPU。registry 中 RUNNING 状态为虚假，需要更新为 DEAD 或重新提交。

---

**总结**：17855 的 6 个实验全部健康运行；19828 的 a000_s46_fp32 正常，但 **a050_s43 确认没有实际进程**——registry 需要修正。

---
