# code gemma dryrun and full pipeline

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma_dryrun_and_full_pipeline_20260522T133729_result.json`
- **Structured JSON:** [`688fa50bab2d10285962.json`](../../sessions/68/688fa50bab2d10285962.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型已加载，正在生成第一条 trace。full 520 预计运行 1-3 小时（基于 dry-run 平均 ~5s/trace，thinking 模式更长）。

---

## 汇总

### Step 1: 服务器状态 ✓
- GPU: NVIDIA RTX PRO 6000 (98GB), 空闲
- 无残留进程需要清理

### Step 2: 脚本同步 ✓
- Gemma-4: `enable_thinking=True` ✓, `do_sample=True` ✓, `N_STORED_LAYERS = 42` ✓
- Gemma-2: `N_STORED_LAYERS = 42` ✓, `HIDDEN_DIM = 3584` ✓

### Step 3: Gemma-4 dry-run ✓
| 指标 | 值 |
|------|------|
| 成功/失败 | 5/0 |
| Thinking 激活 | 4/5 traces 有 `&lt;think>` 块 |
| Avg steps | 8.8 (14, 11, 11, 1, 7) |
| Hidden states shape | (T, 42, 2560) ✓ |
| 分类分布 | safe=3, JB=2 |
| 用时 | ~23s |

### Step 4: Gemma-2 dry-run ⏸ 跳过
- 下载仍在进行：shard 2/4 at 99%, shard 1/4 at 47%
- 速度极慢 (~367kB/s)，预计还需数小时

### Step 5: Gemma-4 full 520 ✓ 已启动
- tmux session: `gemma4_full` @ westd-15904
- 日志: `/tmp/gemma4_full.log`
- `--phase both`（生成 + 分析）
- 预计 1-3 小时完成

### 待办
- Gemma-2 下载完成后需要：验证模型完整性 → dry-run 5 → clean dry-run data → full 520（等 Gemma-4 跑完后再启动）

---
