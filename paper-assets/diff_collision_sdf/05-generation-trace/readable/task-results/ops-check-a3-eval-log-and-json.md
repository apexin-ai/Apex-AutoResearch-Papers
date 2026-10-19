# ops check a3 eval log and json

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_a3_eval_log_and_json_20260522T062306_result.json`
- **Structured JSON:** [`2c10d9c39a2eee4c1de2.json`](../../sessions/2c/2c10d9c39a2eee4c1de2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 进程存活 + GPU 占用
- **eval 进程存活**：PID 343880，CPU 99%，启动于 14:12，正在跑
- **GPU 占用**：cuda:1 上 8617 MiB（PID 343880）
- cuda:0 上 23926 MiB 是另一个进程（a3_spatial_bowl 训练，PID 191747）
- tmux session 存活（从 ps 输出可见 tmux 进程 PID 191740）

### 2. Log 文件状态
- 最后修改时间：**14:13:14**，大小 9460 bytes，之后未再更新
- 最后内容停在模型加载完成 + benchmark 初始化阶段（Task 0 BDDL 加载、cuBLAS warning）
- **原因确认：Python stdout buffering**。进程通过 `2>&1 | tee -a` 管道输出，Python 默认 stdout 是 fully buffered（非 TTY），所以 tee 看不到实时输出。进程实际在正常跑 episode，只是 log 被 buffer 住了。

### 3. JSON 输出逻辑
- **JSON 结果独立写文件**，不依赖 stdout。脚本在 `main()` 末尾用 `json.dump()` 一次性写入 `args.save_dir`（默认 `/root/autodl-tmp/eval_results/`）
- 文件名格式：`eval_{suite}_{task_str}_level{level}_{ckpt_name}_{model_type}_seed{seed}.json`
- 当前跑的命令没指定 `--task_id`，所以会遍历所有 task，最终写 `task_str=all` 的 JSON

### 4. 已有 JSON 结果
已存在一个 **a3_refine** 的 JSON（之前跑的 task1）：
- `eval_safelibero_object_task1_levelII_best_a3_refine_seed0.json`（03:45 生成，22KB）
  - TSR=0%, CAR=0%, 所有 50 个 episode 全部 collision_step=0, refine_count=0

当前跑的是 **不指定 task_id 的全 task 跑**，完成后会生成 `eval_safelibero_object_all_levelII_best_a3_refine_seed0.json`。

### 关键问题
之前的 task1 结果中 **refine_count 全部为 0**，说明 SDF gradient refinement 根本没触发。结合 collision_step=0（第 0 步就碰撞），可能是初始状态就判定碰撞，refiner 来不及介入。

---
