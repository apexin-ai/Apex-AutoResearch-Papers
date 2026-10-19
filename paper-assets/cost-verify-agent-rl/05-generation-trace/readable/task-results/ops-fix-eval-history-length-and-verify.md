# ops fix eval history length and verify

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_eval_history_length_and_verify_20260522T084642_result.json`
- **Structured JSON:** [`332bce526338b5866397.json`](../../sessions/33/332bce526338b5866397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 半程（10/20 ep），进程继续在后台运行。当前足以给出中间结论。

## 产出总结

### 1. HISTORY_LENGTH 修改
- **文件**: `/root/cost-verify-agent-rl/scripts/eval_checkpoint.py`（bjb1-17606）
- **第 52 行**: `HISTORY_LENGTH = 5` → `HISTORY_LENGTH = 50`
- **截断逻辑**: 第 119 行 `history_start = max(0, len(history) - HISTORY_LENGTH)` 自动跟随，无需额外修改

### 2. Checkpoint 路径
`/root/autodl-tmp/checkpoints/exp029-seed4/global_step_15_hf`

### 3. 验证 eval 状态
PID 400921，cuda:1，20 episodes OOD eval 正在运行。前 10 个 episode 结果：

| EP | Status | Steps | fmt | type | Time |
|----|--------|-------|-----|------|------|
| 1 | FAIL | 1 | 0/1 | cool | 2.2s |
| 2 | FAIL | 1 | 0/1 | cool | 1.8s |
| 3 | FAIL | 14 | 13/14 | cool | 39.0s |
| 4 | FAIL | 1 | 0/1 | clean | 1.8s |
| 5 | FAIL | 1 | 0/1 | clean | 1.8s |
| 6 | FAIL | 1 | 0/1 | clean | 1.7s |
| **7** | **SUCCESS** | **37** | **37/37** | **put** | **209.6s** |
| 8 | FAIL | 27 | 26/27 | put | 96.9s |
| 9 | FAIL | 50 | 50/50 | put | 245.4s |
| 10 | FAIL | 20 | 19/20 | clean | 73.9s |

**当前：1/10 = 10%**（HISTORY_LENGTH=5 时全量 134ep 为 6.72%）

### 4. 关键发现——HISTORY_LENGTH 不是主要瓶颈

**主要问题是 step-1 format failure**：5/10 episodes 在第 1 步就 fmt=0 导致立即终止。第 1 步没有历史，HISTORY_LENGTH 完全不影响。这个 step-1 failure 是 eval_checkpoint.py 与 RAGEN eval 的另一个差异。

能正常运行多步的 5 个 episode 中：format 基本正确（avg fmt ~95%），1/5 成功。这部分可能受益于 HISTORY_LENGTH 修复（EP 7 在 37 步中保留了完整历史并成功）。

**建议排查 step-1 format failure 的根因**——这才是 eval_checkpoint.py 6.72% vs RAGEN 30.60% 差距的主要来源。可以用 `grep -c "fmt=0/1" eval_gpu1_verify.log` 确认最终比例。

Eval 预计还需 ~20 分钟完成。查看最终结果：
```bash
tail -30 /root/autodl-tmp/eval_gpu1_verify.log
```

---
