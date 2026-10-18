# diagnose eval openvla l2norm batch fail

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_l2norm_batch_fail_20260521T070451_result.json`
- **Structured JSON:** [`08f0fe08fca35f274e52.json`](../../sessions/08/08f0fe08fca35f274e52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### Root Cause: AutoDL 容器在 14:50:19 被重启，杀死了全部 4 个 eval 进程

**证据链**：
1. **PID 1** (`bash /init/boot/boot.sh`) 启动时间 = `Thu May 21 14:50:19 2026` — 容器重启
2. 4 个实验日志在 **14:45-14:49 停止更新**，与容器重启时间吻合
3. 日志末尾**无任何 error/traceback** — 进程被 SIGKILL 直接杀死，来不及写错误信息
4. 所有实验均在 **Task 4/10** 附近中断（已跑完约 40%）

### 附带问题: GPU 数量从 4 降到 1

| 项目 | 重启前 | 重启后 |
|------|--------|--------|
| GPU 数量 | 4（cuda:0-3） | **1**（仅 cuda:0, RTX PRO 6000 Blackwell 96GB） |
| eval 进程 | 4 个并行 | 全部死亡 |
| conda env | 正常 | 正常（torch=2.8.0+cu128, 1 GPU 可见） |

### 修复方案

**方案 A — 恢复 4 GPU 并行**（推荐，如果能拿到多 GPU 实例）：
- 在 AutoDL 控制台关机 → 重新开机选 4 卡实例
- 然后重新启动 4 个实验

**方案 B — 单 GPU 串行**（当前 1 卡也能跑）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/importance_margin_vla_compress

# 串行跑 4 个实验（每个约 5.5 小时 @ 1.5 eps/min × 500 eps）
for args in \
  "--mode l2norm --k_ratio 0.5" \
  "--mode random --k_ratio 0.3" \
  "--mode l2norm --k_ratio 0.7" \
  "--mode l2norm --k_ratio 0.3"; do
  python eval_openvla_l2norm_libero.py $args --suite libero_object --seed 42 --device cuda:0
done
```

**方案 C — 单 GPU 但用 tmux 防断连**（最实际）：
在 tmux 中逐个跑，这样即使 SSH 断开也不影响：
```bash
tmux new -s eval
# 在 tmux 中执行上面的 for 循环
```

需要注意：
- 如果脚本硬编码了 `--device cuda:X`（X > 0），在单卡环境下会报错，需改为 `cuda:0`
- 实验已完成约 40%，如果脚本支持 checkpoint/resume 可以从断点续跑，否则需要重头来

---
