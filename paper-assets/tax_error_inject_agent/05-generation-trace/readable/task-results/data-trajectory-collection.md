# data trajectory collection

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_trajectory-collection_20260514T051511_result.json`
- **Structured JSON:** [`1920f5b0e39eb3bbe263.json`](../../sessions/19/1920f5b0e39eb3bbe263.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

alfworld-generate 87%（5562/6373），预计还需 ~25 分钟。

**当前状况总结：**

1. **ALFWorld 环境** - 完全就绪
   - alfworld 0.4.2 已安装，import 正常
   - 3895+ 个有效游戏文件（6 种任务类型均覆盖）
   - alfworld-generate 正在后台完成剩余游戏文件生成（87%）

2. **收集脚本** - 已编写、测试、验证通过
   - 路径：`/root/autodl-tmp/tax_error_inject_agent/data/collect_trajectories.py`
   - 支持多线程并行（`--workers`）、断点续传、按任务类型均匀采样
   - ReAct 格式 prompt（`&lt;think>` + `&lt;action>`），模糊匹配 action
   - 已通过 1 个完整 episode 验证：7 步完成 look_at_obj_in_light 任务（56 秒，成功）

3. **API 余额耗尽** - **阻塞项**
   - API endpoint: `http://47.94.22.126/v1`
   - 可用模型确认：`openai/gpt-5.2`（注意：原 `gpt-4o` 不在模型列表中）
   - 错误：`402 - Insufficient balance`，所有模型均受影响（包括标记为 free 的模型）
   - 测试消耗：约 10 次 API 调用（含 1 个完整 episode + 模型测试）

**需要你充值 API 余额后，执行以下命令启动正式收集：**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
source /etc/network_turbo && \
cd /root/autodl-tmp/tax_error_inject_agent && \
nohup python3 -u data/collect_trajectories.py \
  --num_trajectories 500 \
  --output_dir data/trajectories/ \
  --workers 4 \
  > /tmp/collect_500.log 2>&1 &
```

预估时间（4 并行线程）：~3.5 小时（500 条 * ~17 步 * ~6 秒/步 / 4 线程）。

---
