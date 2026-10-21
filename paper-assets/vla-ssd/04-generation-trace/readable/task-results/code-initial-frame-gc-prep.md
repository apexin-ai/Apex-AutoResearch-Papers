# code initial frame gc prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_initial-frame-gc-prep_20260515T180438_result.json`
- **Structured JSON:** [`3008084dfed06d9dff45.json`](../../sessions/30/3008084dfed06d9dff45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。总结：

**修改文件**: `scripts/train_probes.py`，4 处改动：
1. **L71-72** — `parse_args()` 添加 `--max_frames` 参数（default=None）
2. **L916** — `run_goal_classification()` 打印 early-frame 模式信息
3. **L924-926** — 特征加载后截取 `features[:max_frames]`
4. **L975** — 结果 metadata 记录 `max_frames` 值

**验证结果**：
| 配置 | train samples | val samples | 行为 |
|------|-------------|------------|------|
| `--max_frames 1` | 400 (=400×1) | 100 (=100×1) | 每 traj 仅 t=0 |
| `--max_frames 3` | 1200 (=400×3) | 300 (=100×3) | 每 traj t=0~2 |
| 不传（兼容） | 50880 | 12848 | 全部帧，行为不变 |

**后续运行命令模板**：
```bash
# N=1,3,5 的 early-frame goal classification
for N in 1 3 5; do
  python scripts/train_probes.py \
    --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ \
    --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_maxframes${N}/ \
    --probe_type goal_classification \
    --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ \
    --max_frames $N \
    --gpu 0
done
```

---
