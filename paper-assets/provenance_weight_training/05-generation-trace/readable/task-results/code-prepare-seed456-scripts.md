# code prepare seed456 scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_seed456_scripts_20260514T122347_result.json`
- **Structured JSON:** [`032b970d80bf2f1f20b2.json`](../../sessions/03/032b970d80bf2f1f20b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过。确认无 seed456 grid_b 输出目录（前面 ls 已确认）。

脚本已创建：`/root/provenance_weight_training/scripts/submit_grid_b_seed456.sh`

用法：
```bash
cd /root/provenance_weight_training

# 单个 b 值
bash scripts/submit_grid_b_seed456.sh 2 0.5    # GPU 2 跑 b=0.5
bash scripts/submit_grid_b_seed456.sh 0 3.0    # GPU 0 跑 b=3.0

# 串行跑全部 6 个
bash scripts/submit_grid_b_seed456.sh 1 all    # GPU 1 串行跑 0.5→1.0→1.5→2.0→3.0→5.0

# 多 GPU 并行（nohup 后台）
nohup bash scripts/submit_grid_b_seed456.sh 0 0.5 > /tmp/grid_b0.5_s456.log 2>&1 &
nohup bash scripts/submit_grid_b_seed456.sh 1 1.0 > /tmp/grid_b1.0_s456.log 2>&1 &
```

与 seed123/seed42 脚本参数完全一致，仅 seed=456。现有脚本无 eval 逻辑，本脚本同样未加。`CUDA_VISIBLE_DEVICES` 通过参数控制 GPU 绑定。

---
