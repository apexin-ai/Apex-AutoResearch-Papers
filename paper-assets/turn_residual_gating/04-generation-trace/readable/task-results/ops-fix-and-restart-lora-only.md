# ops fix and restart lora only

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_and_restart_lora_only_20260519T071950_result.json`
- **Structured JSON:** [`a10c2b1516e05aa7ead5.json`](../../sessions/a1/a10c2b1516e05aa7ead5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。汇总：

1. **修复验证**：第 128 行已修正为 `total_memory`，grep 确认无残留 `total_mem`
2. **训练状态**：已启动，Step 0 已完成，Loss=1.6080 (L_NTP=1.3786, L_GAR=0.2294)
3. **GPU 显存**：88941 MiB，利用率 97%
4. **训练配置**：
   - 总参数 7.62B，可训练 5.05M (0.07%)
   - LoRA params: 112, Gate params: 0 (gate-type=none)
   - 总步数 3000，梯度累积 8，3 epochs
   - tmux 会话: `phase2_lora_only_s42`，日志: `~/runs/turn_residual_gating/phase2_lora_only_s42.log`

---
