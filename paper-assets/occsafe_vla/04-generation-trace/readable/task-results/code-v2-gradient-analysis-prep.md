# code v2 gradient analysis prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v2-gradient-analysis-prep_20260527T043305_result.json`
- **Structured JSON:** [`9bcd7e504a13baeb5e36.json`](../../sessions/9b/9bcd7e504a13baeb5e36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

执行计划已注册。总结：

**所有 5 个 50K checkpoint 均已就绪**，全部在 westd-10894 的 `/root/autodl-tmp/checkpoints/`。无需等待训练完成或跨服务器传输。

**关键发现：**
- 脚本位于 `/root/occsafe_vla/scripts/`（非 `openvla-oft/vla-scripts/`）
- 参数是 `--checkpoint_dir`（非 `--checkpoint_path`）
- Conda 环境名是 `occsafe`（非 `base`）
- 现有 `run_gradient_analysis_5cond.sh` 用了下划线条件名，会导致图例显示为 v1 标签——正确做法是用空格 + "v2" 后缀
- 预估单 GPU 串行跑 5 条件 + plot 共 ~80-105 min

GPU 空闲后可直接在 10894 上依次执行 5 条命令。

---
