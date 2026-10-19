# ops bjb2 28827 verify and rootcause

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb2-28827-verify-and-rootcause_20260515T191948_result.json`
- **Structured JSON:** [`52a5b072b3303866a81e.json`](../../sessions/52/52a5b072b3303866a81e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收集到足够信息了。汇报如下：

---

## 1. GPU 当前状态（6 块 GPU）

| GPU | PID | 显存占用 | GPU利用率 | 任务 | 启动时间 | 状态 |
|-----|-----|---------|----------|------|---------|------|
| 0 | 105947 | 5182/24564 MiB | 19% | perdof object norm=0.03 | 00:47 | ✅ 正常 |
| 1 | 109655 | 5182/24564 MiB | 18% | perdof object norm=0.05 | 00:58 | ✅ 正常 |
| 2 | 127581 | 5645 MiB | 97% | perdof object norm=0.3 r2 | 02:58 | ✅ 保留的 |
| 2 | 138867 | 5645 MiB | (共享) | perdof object norm=0.2 seed43 | 03:19 | ✅ 重新提交的 |
| 3 | 130113 | 6221/24564 MiB | 19% | obs_only spatial norm=0.3 (b2) | 03:11 | ✅ 保留的 |
| 4 | 101616 | 5182/24564 MiB | 18% | obs_only object norm=0.05 | 00:29 | ✅ 正常 |
| 5 | 103034 | 5182/24564 MiB | 18% | obs_only object norm=0.3 | 00:30 | ✅ 正常 |

**GPU 2** 共 2 个进程占用 11324/24564 MiB (46%)，利用率 97%，两个任务共存正常。其余 GPU 均单进程运行。

---

## 2. 根因分析

### 证据

`~/runs/acr-vla-conformal-refinement/` 目录下找到 3 个 obsonly-norm03 日志：

| 文件 | 创建时间 | 退出码 | 退出时间 (UTC) | 说明 |
|------|---------|--------|---------------|------|
| `eval-mag-obsonly-norm03-b2.log` | 03:11:50 | 143 (stale) | 19:23:34Z | PID 130113，当前仍在 cuda:3 运行 |
| `eval-mag-obsonly-norm03-b3.log` | 03:19 | 143+129 | 19:19:13Z | 已被 kill，输出文件错误地写为 `eval_spatial_obs_only_norm03_b2.json`（与 b2 不同命名但都指向 spatial norm=0.3 任务） |
| `eval-mag-obsonly-norm03-b4.log` | 03:19 | 143 | 19:19:14Z | 已被 kill |

关键发现：
- **b3 和 b4 在同一分钟内（03:19）创建**，间隔极短，随即被 kill
- b3 的 output_file 参数是 `eval_spatial_obs_only_norm03_b2.json`——session 名叫 b3 但输出路径写的是 b2，说明是**复制粘贴 b2 的提交命令时没改文件名**
- 所有三个 b2/b3/b4 都是通过 **agent-ml tmux framework** 提交的（带 `~/runs/` 日志 + `/tmp/agent-ml-exit/` 退出跟踪）
- b2 还有一个 stale exit file（19:23:34Z），说明 b2 session 也被重建过

### 两种提交模式共存

服务器上同时存在两种提交方式：
1. **nohup 直接提交**（PID 101616, 103034）：通过 `ssh_execute` 的 `nohup ... &` 模式，无 tmux session
2. **agent-ml tmux 框架**（其余所有）：通过 `tmux new-session -d -s NAME` 提交

### 根因推断

**obs_only spatial norm=0.3 的 4 份副本（b2 + 3 个重复）最可能原因：多个 agent 会话/worker 并发提交了相同任务。**

证据链：
1. b2 在 03:11:50 创建，分配到 cuda:3
2. b3、b4 在 03:19 密集创建（同一分钟内），且 b3 的 output_file 参数错误复制了 b2 的文件名——这是自动化脚本在生成命令时的 copy-paste bug
3. b2 的 stale exit file 表明 b2 session 本身也经历了一次 kill-recreate 循环
4. 三个重复副本都被分配到了 cuda:2（与已在运行的 perdof norm=0.3 r2 冲突），没有做 GPU 占用检查

**建议**：agent-ml 框架的 job 提交需要加 **GPU 占用检查**（提交前查 nvidia-smi）和 **session 去重**（同名任务不允许重复提交）。

---
