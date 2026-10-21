# infra scan all servers process status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_scan-all-servers-process-status_20260523T212704_result.json`
- **Structured JSON:** [`5a0ec3f4a71d085b4ac8.json`](../../sessions/5a/5a0ec3f4a71d085b4ac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

扫描完成。

## 汇总

### 存活实验 (14个进程)

**bjb2-28827** — 6/6 GPU 满载
| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval-supp-goal-vla-only-s45 | cuda:0 | 926766 | ALIVE |
| eval-supp-goal-crm-norm005-s45 | cuda:1 | 927030 | ALIVE |
| eval-supp-goal-reconvla-s45 | cuda:2 | 927237 | ALIVE |
| *eval-supp-long-reconvla-s44* | cuda:3 | 849677 | ALIVE (未预期) |
| eval-supp-long-k2mean-s45 | cuda:4 | 924226 | ALIVE |
| eval-supp-long-k2mean-s44 | cuda:5 | 850410 | ALIVE |

**bjb1-32546** — 6/6 GPU 满载
| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval-supp-crm-norm005-obj-s46 | cuda:0 | 102927 | ALIVE |
| eval-supp-long-vla-only-s45 | cuda:1 | 103128 | ALIVE |
| eval-supp-long-adapt-tau025-s45 | cuda:2 | 103397 | ALIVE |
| eval-supp-long-crm-norm005-s45 | cuda:3 | 103675 | ALIVE |
| eval-supp-long-reconvla-s45 | cuda:4 | 103942 | ALIVE |
| eval-supp-goal-adapt-tau025-s45 | cuda:5 | 104216 | ALIVE |

**cqa1-32758** — 2/6 GPU 在用
| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval-supp-reconvla-obj-s46 | cuda:2 | 380176 | ALIVE |
| *eval-reconvla-obj-s45* | cuda:4 | 377316 | ALIVE (未预期) |

**bjb2-40593** — 1/1 GPU 在用
| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval-supp-crm-norm005-obj-s45 | cuda:0 | 177824 | ALIVE |

### 已完成实验 (4个，全在 cqa1-32758)

| exp_id | 结果 | 输出文件 |
|--------|------|---------|
| eval-supp-k2mean-obj-s46 | **76.5%** (153/200) | eval_object_vla_only_seed46.json |
| eval-supp-k2mean-obj-s45 | **77.5%** (155/200) | eval_object_vla_only_seed45.json |
| eval-supp-long-crm-norm005-s44 | **56.5%** (113/200) | eval_long_crm_obs_only_norm0.05_seed44.json |
| eval-supp-long-adapt-tau025-s44 | **56.0%** (112/200) | eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json |

### 可用 GPU

cqa1-32758 有 **4 个空闲 GPU**: cuda:0, cuda:1, cuda:3, cuda:5

---
