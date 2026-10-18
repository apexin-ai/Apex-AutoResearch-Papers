# eval v8 eval prep dryrun

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v8-eval-prep-dryrun_20260516T001824_result.json`
- **Structured JSON:** [`fedc9bc54868f231a706.json`](../../sessions/fe/fedc9bc54868f231a706.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### P0: Dry-run eval (3/3 PASS)

| 模式 | 状态 | 条件数 | 关键指标 |
|------|------|--------|----------|
| **a) v8 标准 eval** | **PASS** | 8 | action_loss=0.0084 (clean), margin_median=0.2026, Lipschitz_emp=0.1466 |
| **b) v8 bypass-ACIS** | **PASS** | 8 | action_loss=0.0348 (clean), bypass_acis=True 确认 |
| **c) baseline eval** | **PASS** | 8 | action_loss=0.0023 (clean), imm_enabled=False 确认 |

所有 JSON 格式正确，无 NaN/Inf。

**踩坑记录**：AutoDL 上必须 `source /etc/network_turbo` + 设置 `REQUESTS_CA_BUNDLE`/`SSL_CERT_FILE`/`HF_HUB_DISABLE_XET`，否则 `SmolVLAPolicy.from_pretrained()` 和 `LeRobotDataset()` 联网检查会 hang。

### P1: Baseline 500-batch 数据

**完备** — `eval_results/eval_baseline_v5_final.json` (4147 bytes)，8 个条件 + _meta，所有 action_loss 值正常。

### P2: 全量 eval 脚本

**路径**: `/root/autodl-tmp/importance_margin_vla_compress/run_v8_final_eval.sh`

**使用方式**:
```bash
# 默认 cuda:1
nohup bash run_v8_final_eval.sh > /tmp/v8_final_eval.log 2>&1 &

# 指定 GPU
nohup bash run_v8_final_eval.sh 0 > /tmp/v8_final_eval.log 2>&1 &
```

---
