# audit eval script history

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_eval-script-history_20260521T172834_result.json`
- **Structured JSON:** [`2dd44252fd741e905d7a.json`](../../sessions/2d/2dd44252fd741e905d7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整结果。

## 审计结论

**所有 20r eval 均使用了正确的 `evaluate_safelibero.py`，无污染。**

唯一使用错误脚本 `eval_safelibero.py` 的是一次 50r eval（`occ_s0_50r_eval.log`），且已用正确脚本重跑。

---

### westd-34685 eval 汇总

| 实验 | Checkpoint | 日志文件 | 脚本 | 有效? | TSR |
|------|-----------|---------|------|------|-----|
| mvp_occ_s0 | 47500_chkpt (20r) | `eval_results/occ_s0_eval.log` | evaluate_safelibero.py | ✅ | 91.0% |
| mvp_occ_s0 | 47500_chkpt (50r 初次) | `eval_logs/occ_s0_50r_eval.log` | **eval_safelibero.py** | ❌ | 89.2% |
| mvp_occ_s0 | 47500_chkpt (50r 重跑) | `eval_logs/occ_s0_47500_50r_rerun.log` | evaluate_safelibero.py | ✅ | 89.2% |
| mvp_occ_s0 | 50000_chkpt (20r) | `eval_results/occ_s0_50000.log` | evaluate_safelibero.py | ✅ | 91.5% |
| mvp_occ_s1 | 30000_chkpt (20r) | `eval_results/occ_s1_30000.log` | evaluate_safelibero.py | ✅ | 80.5% |
| mvp_occ_s1 | 35000_chkpt (20r) | `eval_results/occ_s1_35000.log` | evaluate_safelibero.py | ✅ | 75.0% |
| mvp_occ_s1 | 40000_chkpt (20r) | `eval_results/occ_s1_40000.log` | evaluate_safelibero.py | ✅ | 78.5% |
| mvp_occ_s1 | 45000_chkpt (20r) | `eval_results/occ_s1_45000.log` | evaluate_safelibero.py | ✅ | 79.0% |
| mvp_occ_s1 | 45000_chkpt (auto_eval) | `eval_logs/occ_s1_45000_eval.log` | N/A | ⚠️ 失败 | N/A |
| mvp_occ_s1 | 50000_chkpt (20r) | `eval_results/occ_s1_50000_20r.log` | evaluate_safelibero.py | ✅ | 76.5% |
| mvp_occ_s2 | 47500_chkpt (20r) | `eval_results/occ_s2_eval.log` | evaluate_safelibero.py | ✅ | 91.5% |
| mvp_occ_s2 | 50000_chkpt (20r) | `eval_results/occ_s2_50000.log` | evaluate_safelibero.py | ✅ | 85.0% |

### westd-10894 eval 汇总

| 实验 | Checkpoint | 日志/JSON | 脚本 | 有效? | TSR |
|------|-----------|----------|------|------|-----|
| mvp_vanilla_s0 | 50000_chkpt (20r) | `vanilla_s0_final.json` + monitor.log | evaluate_safelibero.py | ✅ | 91.0% |
| mvp_vanilla_s1 | 50000_chkpt (20r) | `vanilla_s1_final.json` + monitor.log | evaluate_safelibero.py | ✅ | 93.5% |
| mvp_vanilla_s2 | 50000_chkpt (20r) | `vanilla_s2_final.json` + monitor.log | evaluate_safelibero.py | ✅ | 91.0% |

### 关键发现

1. **❌ 唯一受污染的 eval**：`occ_s0_50r_eval.log`（occ_s0 47500_chkpt 的 50r eval）使用了错误的 `eval_safelibero.py`（日志中行号 323/332/405/421 — 与正确脚本的 346/355/439/467 不同）。**但已用正确脚本重跑**（`occ_s0_47500_50r_rerun.log`）。

2. **⚠️ 失败的 eval**：`eval_logs/occ_s1_45000_eval.log` — `auto_eval_45K.sh` 尝试调用 `evaluate_safelibero.py`，但脚本文件当时不存在于 `/root/occsafe_vla/openvla-oft/` 路径。后来在 `eval_results/occ_s1_45000.log` 中成功重跑。

3. **所有现存 JSON 结果文件**均由正确脚本 `evaluate_safelibero.py` 产生，包含 `collision_threshold`、`safe`、`car` 等碰撞检测字段 — 碰撞检测正常工作。

---
