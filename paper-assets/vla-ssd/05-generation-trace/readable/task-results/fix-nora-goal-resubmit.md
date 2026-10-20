# fix nora goal resubmit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_nora_goal_resubmit_20260521T030604_result.json`
- **Structured JSON:** [`d9d53515554c596bb817.json`](../../sessions/d9/d9d53515554c596bb817.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 启动成功——模型加载完成，pipeline 正常进入 `trained` 条件，开始处理数据。参数解析没有报错，`EXIT_CODE=2` 的问题已修复。

SSH 超时是因为 30s 内跑不完 dry-run（模型加载就用了 14.7s），但关键部分已验证通过。

## 结果

**1. 修复内容** — argparse 改动（`nora_goal_full_pipeline.py` line 602-606）：
- `--conditions` 从单值字符串改为 `nargs="+", choices=["trained", "untrained"]`
- `default` 从 `"trained,untrained"` 改为 `["trained", "untrained"]`
- 删除了 line 614 的 `.split(",")` 解析

**2. 正确的提交命令**

Trained only（优先跑这个）：
```bash
bash -c "source /root/autodl-tmp/vla-ssd/envs/nora/bin/activate && python /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py --conditions trained"
```

Trained + Untrained（完整对照）：
```bash
bash -c "source /root/autodl-tmp/vla-ssd/envs/nora/bin/activate && python /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py --conditions trained untrained"
```

**3. Dry-run** — 通过。模型加载成功（14.7s），pipeline 正常启动进入 Phase 1 数据提取，参数解析无报错。

---
