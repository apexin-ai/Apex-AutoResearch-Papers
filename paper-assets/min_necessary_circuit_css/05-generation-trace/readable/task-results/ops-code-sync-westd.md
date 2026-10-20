# ops code sync westd

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_code-sync-westd_20260513T062336_result.json`
- **Structured JSON:** [`493ef16d4b6f93115c13.json`](../../sessions/49/493ef16d4b6f93115c13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

同步完成。

### 结果汇总

**同步文件清单（22 个）：**

| 文件 | 大小 |
|------|------|
| config.py | 868B |
| css.py | 5,443B |
| circus.py | 6,001B |
| cross_tabulate.py | 4,091B |
| circuit_discovery.py | 6,533B |
| evaluation.py | 4,295B |
| run_mvp.py | 12,870B |
| edge_pruning_l0.py | 9,819B |
| ifr_discovery.py | 5,467B |
| ifr_scoring.py | 10,413B |
| analysis_fix_v3.py | 12,959B |
| eval_faithfulness.py | 5,787B |
| eval_mean_ablation.py | 15,176B |
| eval_topk_faithfulness.py | 17,573B |
| acdc_topk_sweep.py | 5,822B |
| run_arithmetic.py | 15,953B |
| run_circus_fix.py | 9,726B |
| run_phase_d_only.py | 7,277B |
| run_phase2_experiment.py | 17,344B |
| run_circus.py | 10,187B |
| run_sva.py | 21,684B |
| phase2_configs.yaml | 8,956B |

**CUDA guard 更新：**
- `os.environ["CUDA_VISIBLE_DEVICES"] = "5"` → `"0"` （11 个入口脚本）
- `os.environ.setdefault("CUDA_VISIBLE_DEVICES", "5")` → `"0"` （8 个库模块）
- `os.environ.get("CUDA_VISIBLE_DEVICES", "5")` → `"0"` （run_phase2_experiment.py 的 fallback）
- `gpu_id: "5"` → `"0"` （phase2_configs.yaml）

**Import 验证：** `circuit_discovery`, `css`, `evaluation` — ALL IMPORTS OK

**传输方式：** 临时 SSH 密钥 scp（已清理密钥和临时文件）

---
