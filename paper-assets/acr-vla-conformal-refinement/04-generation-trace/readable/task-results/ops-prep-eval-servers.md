# ops prep eval servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-eval-servers_20260521T191140_result.json`
- **Structured JSON:** [`7761c403e30ad07bf4ff.json`](../../sessions/77/7761c403e30ad07bf4ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**1. git pull 结果：失败但无需操作**
- bjb2-28827：仓库存在但**没有配置 git remote**（`git remote -v` 为空），分支无 tracking。无法 git pull。
- bjb1-32546：`/root/acr-vla-conformal-refinement` **不是 git 仓库**（`fatal: not a git repository`）。

**2. evaluate.py 大小（关键发现）**
- bjb2-28827：`src/evaluate.py` 已经是 **33058 bytes**，与 bjb1-32546 目标一致。
- 任务描述的"30140 bytes 旧版"在 bjb2-28827 上已不存在 — 文件可能此前已通过其他方式同步（git status 显示 modified，疑似本地直接编辑过）。
- **结论：代码已是最新，无需同步。**

**3. π0.5 模型文件：两台均存在**
- bjb2-28827：`/root/autodl-tmp/models/pi05_libero_finetuned/model.safetensors` 7.4GB ✓
- bjb1-32546：`/root/autodl-tmp/models/pi05_libero_finetuned/model.safetensors` 7.4GB ✓
- 两台的 `policy_preprocessor.json` 大小略不同（bjb2: 1903B vs bjb1: 1937B，bjb1 日期更新到 14:31）— 可能 bjb1 上有过 preprocessor 修改，需关注。

**4. 其他问题**
- bjb2-28827 上有大量未提交修改和 `.bak` 备份文件，工作区不干净。
- bjb1-32546 完全不是 git 仓库，**未来代码同步只能用 rsync/scp，不能用 git**。
- 建议如需后续可靠同步代码：从工作机 push 到中央 remote，再在两台机器分别配 remote / 重新 `git clone`。

可以直接在 bjb2-28827 上部署 π0.5 CRM eval。

---
