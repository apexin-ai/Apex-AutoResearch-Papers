# ssh submit cf batch

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_cf_batch_20260521T210957_result.json`
- **Structured JSON:** [`a9e2878029b7eec8e917.json`](../../sessions/a9/a9e2878029b7eec8e917.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. counterfactual_batch.py 参数说明

| 参数 | 必填 | 说明 |
|------|------|------|
| `--arch` | ✓ | `openvla` / `tracvla` / `nora` |
| `--suite` | ✓ | `goal` / `spatial` / `object` / `long` |
| `--condition` | ✓ | `trained` / `untrained` |
| `--method` | | `auto`(默认) / `action_mse` / `cosine_dist`。auto 逻辑：nora 或 untrained → `cosine_dist`，其余 → `action_mse` |
| `--gpu` | | GPU 编号，默认 0 |
| `--n-demos` | | 每任务 demo 数，默认 10 |
| `--n-timesteps` | | 每 demo 时间步数，默认 50 |
| `--results-dir` | | 覆盖输出目录 |
| `--dry-run` | | 快速测试：2 tasks, 1 demo, 2 timesteps |

### 2. 缺失确认

已有 `counterfactual_combined.json` 的组合：

| 组合 | 状态 |
|------|------|
| nora_goal trained/untrained | ✓ |
| nora_spatial trained | ✓ |
| tracvla_{spatial,object,long,goal} trained | ✓ |
| openvla_{goal,spatial,long,object} trained | ✓ (旧格式) |

**确认缺失的 3 个：**
- `openvla object untrained` — checkpoint: `openvla-7b`，auto → cosine_dist ✓
- `tracvla spatial untrained` — checkpoint: `phi3v-base`，auto → cosine_dist ✓
- `tracvla object untrained` — checkpoint: `phi3v-base`，auto → cosine_dist ✓

TracVLA untrained 用 phi3v-base（纯 VLM），cosine_dist 只需隐藏层表示，不需要动作头，可以正常运行。

> 额外注意：`nora_spatial untrained`、`openvla_{goal,long} untrained`、`tracvla_{goal,long} untrained` 也没有 counterfactual 结果，但不在本次任务范围。

### 3. 提交命令

```bash
tmux new-session -d -s cf_untrained 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/vla-ssd && python scripts/counterfactual_batch.py --arch openvla --suite object --condition untrained --gpu 1 && python scripts/counterfactual_batch.py --arch tracvla --suite spatial --condition untrained --gpu 1 && python scripts/counterfactual_batch.py --arch tracvla --suite object --condition untrained --gpu 1"'
```

### 4. 预计运行时间

- openvla untrained（7B 模型，10 tasks × 10 demos × 50 timesteps × 5 conditions）：约 2-3 小时
- tracvla untrained（phi3v ~4B，同样规模）：每个约 1-2 小时
- **总计：约 4-7 小时**，取决于 GPU 型号和推理速度

---
