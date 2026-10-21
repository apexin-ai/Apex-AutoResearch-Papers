# ops verify processes and progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-processes-and-progress_20260514T123508_result.json`
- **Structured JSON:** [`6b4edab9b543ff71be7c.json`](../../sessions/6b/6b4edab9b543ff71be7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况与预期**完全相反**。

## 进程状态
原始进程（r4/r2/r2）：**全部已死** — PID 50534, 50675, 50946 不存在
重复进程（r5/r3/r3）：**全部存活** — PID 53066, 53144, 53287 正在运行（~4分钟）
GPU 冲突：**无**

### 详情
- 原始实验日志均显示 `Terminated` + `EXIT_CODE=129`（SIGHUP），说明 kill_job 杀掉的是原始进程而非仅 tmux wrapper
  - ced_r4: 死于 step 15/756
  - extract_r2: 死于 step 14/756
  - flatnli_r2: 死于 step 13/756
- 重复实验的 kill 未生效，子进程仍在运行：
  - 53066 → 子进程 53071 在 GPU 0（13044 MiB）
  - 53144 → 子进程 53149 在 GPU 2（13044 MiB）
  - 53287 → 子进程 53292 在 GPU 3（13044 MiB）

## GPU 占用
| GPU | PID | 实验 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| 0 | 53071 | ced_r5 | 13044 MiB | 56% |
| 1 | 45531, 47298 | eval inference ×2 | 5326 MiB ×2 | 87% |
| 2 | 53149 | extract_r3 | 13044 MiB | 64% |
| 3 | 53292 | flatnli_r3 | 13044 MiB | 58% |

## 训练进度
三个重复实验（r5/r3/r3）均刚启动，全部在 **step 1/756**，尚无 loss/reward 数据可看。

## 结论
1. **原始实验已被杀死**，不是"tmux 被杀但子进程还在"——EXIT_CODE=129 说明训练进程本身收到了 SIGHUP
2. **重复实验反而存活**，刚启动约4分钟，相当于从头重新跑。这三个实验配置与原始实验相同（都是 kl_coef=0.0），所以可以继续让它们跑
3. GPU 1 上有两个 eval inference 进程已跑了 ~48 分钟，与 GRPO 无关
4. kl_coef=0 修复是否有效需要等这三个新实验跑过 step 5 才能判断（原始实验在 step 13-15 被杀时看起来是正常运行的，没有崩溃迹象）

---
