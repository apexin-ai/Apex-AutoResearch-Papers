# code method validation scripts

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_method_validation_scripts_20260518T172526_result.json`
- **Structured JSON:** [`3d4aa5244da2d991167a.json`](../../sessions/3d/3d4aa5244da2d991167a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个脚本全部完成，dry-run + 真实数据测试均通过。

| 脚本 | 功能 | 验证 |
|------|------|------|
| `analysis_dgs_full_validation.py` | 3 数据集 DGS 全量验证 + bootstrap CI + permutation test + 退化分层 | PASS |
| `analysis_dgs_ablation.py` | 5 策略消融 (Greedy/LP-all/DGS-degen/DGS-lp/DGS-full) | PASS |
| `analysis_dgs_cross_model.py` | 跨模型验证 (LLaMA)，支持 reference 对比 | PASS |
| `analysis_dgs_multiseed.py` | 多 seed 稳定性，mean±std | PASS |

所有脚本位于 `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/code/`，使用 argparse 参数化，支持 `--dry-run`，输出 JSON + 终端报告。验证报告写入 `artifacts/method_scripts/scripts_validation_report.md`。

---
