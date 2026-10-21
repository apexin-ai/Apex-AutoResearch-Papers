# code arcc benchmark prep

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_arcc-benchmark-prep_20260521T080654_result.json`
- **Structured JSON:** [`251cd2f083895356849a.json`](../../sessions/25/251cd2f083895356849a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出汇总：

**`/root/autodl-tmp/ctrl_contam_arcc/` 目录结构**：
| 文件 | 说明 |
|------|------|
| `prepare_arcc_data.py` | 数据准备脚本（已执行） |
| `train.py` | QLoRA SFT 训练脚本 |
| `eval_lz.py` | lz* 评估脚本（适配 ARC-C 变长选项） |
| `arc_c_params.csv` | 4PL IRT 参数（295 items） |
| `data/{clean_s1,clean_s2,contam_15,contam_50}/train.jsonl` | 训练数据 |
| `data/arcc_items.json` | 295 eval items |
| `data/seen_items_{15,50}pct.json` | contamination indices |

**ARC-C 数据就绪报告**：
- ARC-C test: 1172 items，IRT 参数覆盖前 295 items（294×4-choice + 1×3-choice）
- 4PL 参数可用（`/root/autodl-tmp/irt_personfit_contam/params/arc_c_params.csv`）
- 15% contam = 44 items, 50% contam = 147 items, clean = 5000 Alpaca
- 训练配置与 MMLU pilot 完全一致（QLoRA r=16, 3 epochs, lr=2e-4）
- 预期 ARC-C 检测力有限（295 items, sim_001 显示 12.9% power），但 cross-benchmark generalization 价值明确

---
