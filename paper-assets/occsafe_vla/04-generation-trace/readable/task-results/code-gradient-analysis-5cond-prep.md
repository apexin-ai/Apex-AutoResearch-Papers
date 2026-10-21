# code gradient analysis 5cond prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient-analysis-5cond-prep_20260527T041413_result.json`
- **Structured JSON:** [`04828957caae0fff94d8.json`](../../sessions/04/04828957caae0fff94d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Confirmed: 3 checkpoints on 10894, 2 need SCP from 34685.

## 产出报告

### 脚本状态

| 脚本 | 路径 | 状态 |
|------|------|------|
| `run_gradient_analysis_v2.py` | `/root/occsafe_vla/scripts/` | 已支持 5 条件，无需修改。`--occ_norm bn/ln` + condition name 自动检测。 |
| `compare_gradient_5cond.py` | `/root/occsafe_vla/scripts/` | **新建**。5 条件对比，支持 JSON 输入和 checkpoint 输入两种模式。输出 per-layer 表格 + BN/LN 对比 + summary ratios。 |
| `run_gradient_analysis_5cond.sh` | `/root/occsafe_vla/scripts/` | **新建**。Batch runner，含 pre-flight 检查、SCP 提示、5 条件顺序执行 + 对比。 |

### Checkpoint 路径确认

| 条件 | Exp ID | 50K Checkpoint | 服务器 | 状态 |
|------|--------|---------------|--------|------|
| Full OCC BN | `mvp_occ_s3_v2` | `...--mvp_occ_s3_v2--50000_chkpt` | 10894 | ✅ 就绪 |
| Full OCC LN | `full_occ_ln_s3_v2` | `...--full_occ_ln_s3_v2--50000_chkpt` | 10894 | ✅ 就绪 |
| Detach BN | `ablation_occ_detach_s3_v2` | `...--ablation_occ_detach_s3_v2--50000_chkpt` | 10894 | ✅ 就绪 |
| Detach LN | `detach_ln_s3` | `...--detach_ln_s3--50000_chkpt` | 34685 | ⚠️ 需 SCP 到 10894 |
| Vanilla | `vanilla_v2_s1` | `...--vanilla_v2_s1--50000_chkpt` | 34685 | ⚠️ 需 SCP 到 10894 |

### 运行前需执行的 SCP

```bash
# On westd-10894:
mkdir -p /root/autodl-tmp/checkpoints/vanilla_v2_s1/
scp -r westd-34685:/root/autodl-tmp/checkpoints/vanilla_v2_s1/ /root/autodl-tmp/checkpoints/vanilla_v2_s1/

mkdir -p /root/autodl-tmp/checkpoints/detach_ln_s3/
scp -r westd-34685:/root/autodl-tmp/checkpoints/detach_ln_s3/ /root/autodl-tmp/checkpoints/detach_ln_s3/
```

### 运行命令

```bash
# GPU 释放后在 10894 上执行:
GPU=0 bash /root/occsafe_vla/scripts/run_gradient_analysis_5cond.sh
```

预估耗时：5 × ~15-20 min = ~75-100 min（单 GPU 串行）。

---
