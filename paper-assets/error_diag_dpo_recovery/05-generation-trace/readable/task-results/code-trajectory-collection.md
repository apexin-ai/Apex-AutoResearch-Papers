# code trajectory collection

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_trajectory-collection_20260512T114358_result.json`
- **Structured JSON:** [`6ef25179527c2029f08b.json`](../../sessions/6e/6ef25179527c2029f08b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已完成并通过端到端验证。

**`src/collect_trajectories.py`** — 轨迹收集：
- Qwen3-8B 4-bit 量化加载，~7.7GB 显存
- ALFWorld 环境通过 `get_environment` API 初始化（适配 alfworld 0.4.2）
- 数据路径 `/root/autodl-tmp/alfworld_data`（已下载 json_2.1.1 game files）
- 禁用 Qwen3 thinking mode，输出干净的 `Thought:/Action:` 格式
- 支持 `--part_num/--part_idx` 分片并行
- 输出 JSONL，每行一个 episode

**`src/construct_preference.py`** — DPO pairs 构建：
- 按 game_file 分组，配对成功/失败轨迹
- rejected 截断到 chosen + 5 步
- 输出含 `prompt/chosen/rejected/error_type` 字段

**测试结果**：1 task × 40 steps，73.8 秒完成（~1.8s/step），JSONL 格式正确。环境中该 task 未成功（符合预期——需要多轮收集才能获得成功+失败 pairs）。

---
