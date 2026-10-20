# ops eval file organization

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-file-organization_20260522T062950_result.json`
- **Structured JSON:** [`5a8cc3b106e185551ed8.json`](../../sessions/5a/5a8cc3b106e185551ed8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是统一后的 eval_results 文件清单：

### 标准命名文件（新建/重命名）

**Vanilla (50r, step 50000)**
| 文件 | 大小 |
|---|---|
| `vanilla_s0_50r_50000.json` | 236KB |
| `vanilla_s1_50r_50000.json` | 236KB |
| `vanilla_s2_50r_50000.json` | 236KB |

**OCC s0**
| 文件 | 大小 |
|---|---|
| `occ_s0_20r_50000.json` | 97KB |
| `occ_s0_50r_47500.json` | 236KB |
| `occ_s0_50r_50000.json` | 236KB |

**OCC s1 (old, 20r only)**
| 文件 | 大小 |
|---|---|
| `occ_s1_20r_30000.json` | 97KB |
| `occ_s1_20r_35000.json` | 97KB |
| `occ_s1_20r_40000.json` | 97KB |
| `occ_s1_20r_45000.json` | 97KB |
| `occ_s1_20r_50000.json` | 97KB |

**OCC s1_fresh (50r)**
| 文件 | 大小 |
|---|---|
| `occ_s1_fresh_50r_47500.json` | 236KB |
| `occ_s1_fresh_50r_50000.json` | 236KB |

**OCC s2**
| 文件 | 大小 |
|---|---|
| `occ_s2_20r_50000.json` | 97KB |
| `occ_s2_50r_47500.json` | 236KB |
| `occ_s2_50r_50000.json` | 236KB |

**Ablations (50r, step 50000)**
| 文件 | 大小 |
|---|---|
| `ablation_occ_detach_s0_50r_50000.json` | 236KB |
| `ablation_occ_detach_s0_20r_50000.json` | 97KB |
| `ablation_occ_detach_s1_50r_50000.json` | 236KB |
| `ablation_random_occ_s0_50r_50000.json` | 236KB |
| `ablation_random_occ_s1_50r_50000.json` | 236KB |

旧命名文件已保留未删除。

### 缺失 / 注意事项

1. **occ_s1 (old) 没有 50r eval** — 只有 20r (30K-50K step)。occ_s1_fresh 已替代，有 50r at 47500 和 50000。
2. **occ_s1_fresh 50r 已到位** — 47500 和 50000 两个 checkpoint 都有。
3. **depth_s0 / depth_s1 没有任何 eval JSON** — checkpoint 存在但未跑 eval。
4. **vanilla 没有 20r eval** — 只有 50r。
5. **occ_s0/s2 没有 47500 的 20r eval** — 只有 50r 版本。

---
