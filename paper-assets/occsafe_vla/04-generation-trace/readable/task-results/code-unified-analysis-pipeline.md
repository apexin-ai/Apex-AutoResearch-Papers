# code unified analysis pipeline

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unified_analysis_pipeline_20260523T101426_result.json`
- **Structured JSON:** [`159de30e7dce391274a6.json`](../../sessions/15/159de30e7dce391274a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总如下：

### 创建的脚本

| 脚本 | 路径 | 功能 |
|------|------|------|
| `run_full_analysis.sh` | `/root/occsafe_vla/analysis/run_full_analysis.sh` | 主控 pipeline，5 阶段：scp-check → gradient → cka → figures → bootstrap。每阶段可独立运行，自动跳过已完成的分析，conda 自动激活 |
| `plot_gradient_figure.py` | `/root/occsafe_vla/analysis/plot_gradient_figure.py` | 2×2 论文级 figure：(a) action grad norms grouped bar, (b) OCC grad norms, (c) cosine similarity heatmap, (d) CKA 矩阵。支持 `--mock` 模式，兼容新旧两种 gradient stats JSON 格式 |
| `bootstrap_ci.py` | `/root/occsafe_vla/analysis/bootstrap_ci.py` | 扩展版：新增 `--add-condition NAME path1 path2 ...`（动态添加条件）、`--latex-file`（LaTeX 输出到文件）、`--dry-run`（仅验证路径），原有功能不变 |

### 验证结果
- `python plot_gradient_figure.py --mock` → 生成 PDF (40KB) + PNG (289KB)
- `bash run_full_analysis.sh --help` → 显示完整用法
- `python bootstrap_ci.py --dry-run` → 6 个条件全部 OK

### 当前阻塞
- **vanilla_retrain_s0** / **full_occ_retrain_s0**：训练中，尚无 50000_chkpt
- **ablation_occ_detach_s2** / **ablation_random_occ_s2**：需从 westd-10894 SCP checkpoint

---
