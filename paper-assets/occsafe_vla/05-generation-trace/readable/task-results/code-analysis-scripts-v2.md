# code analysis scripts v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis-scripts-v2_20260521T185745_result.json`
- **Structured JSON:** [`c7002b04bef991a9bec4.json`](../../sessions/c7/c7002b04bef991a9bec4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 产出清单

### 创建的文件
| 路径 | 用途 |
|------|------|
| `/root/occsafe_vla/openvla-oft/analysis/eval_utils.py` | 共用工具（数据加载、bootstrap CI、diff test） |
| `/root/occsafe_vla/openvla-oft/analysis/per_task_comparison.py` | 多条件 per-task TSR/CAR 对比 |
| `/root/occsafe_vla/openvla-oft/analysis/seed_instability.py` | 跨 seed 方差分析 |
| `/root/occsafe_vla/openvla-oft/analysis/ablation_diagnostic.py` | Ablation 诊断（4 条件 + 2×2 scatter） |

### Dry-run 验证结果

3 个脚本全部成功，共生成 19 个输出文件：

| 脚本 | 状态 | 输出 |
|------|------|------|
| `per_task_comparison.py` | **通过** | `per_task_tsr.pdf` (16K), `per_task_car.pdf` (16K), `hard_tasks.pdf` (15K), `comparison_stats.json` (122B — 单条件无 pairwise 对比，预期行为) |
| `seed_instability.py` | **通过** | `seed_variance_heatmap.pdf` (27K), `variance_ratio.pdf` (25K), `instability_stats.json` (1.4K) |
| `ablation_diagnostic.py` | **通过** | `ablation_car_comparison.pdf` (23K), `ablation_tsr_comparison.pdf` (22K), `diagnostic_matrix.pdf` (25K), `diagnostic_report.json` (2.2K) |

所有 PDF + PNG 双格式输出。

### 数据格式发现
- eval JSON 实际路径: `/root/occsafe_vla/eval_results/`（非 `/root/eval_logs/`）
- CAR 字段已是安全率（`car`），不需要 `1 - collision_rate` 转换
- 目前缺 `vanilla_s2` 的 JSON（eval_results 里只有 s0、s1）
- OCC 可用: `occ_s0_50000.json`, `occ_s2_50000.json`（另有 `occ_s0_final.json`, `occ_s2_final.json`）

---
