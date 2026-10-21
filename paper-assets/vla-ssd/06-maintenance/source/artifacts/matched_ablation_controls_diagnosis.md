# 实验诊断报告 (2026-05-19)

## 1. matched_ablation_controls

### 状态：已正常完成

与 registry 记录不符：日志显示实验已成功完成，非"异常退出"。

### 日志证据

- 10500 forward passes 全部完成（1527s，6.9 pass/s）
- 3 个 task 均正常处理
- Metrics 已计算：
  - Random-24 mean traj_d: 0.601 +/- 0.021
  - Image-dominant-24 traj_d: 0.580
  - Instruction-dominant-24 traj_d (reference): 0.65
- 结果已保存到 `/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.json`
- return_code = 0，stderr 为空

### 无 W&B metrics 的原因

脚本未集成 W&B logging，结果只写入 JSON 文件。无 W&B metrics 是设计如此，不是故障。

### 结论

- 不需要重试，实验已成功
- Registry 状态应更新为 COMPLETED
- 如需 W&B tracking，需在脚本中添加 wandb 调用

---

## 2. behavioral_smoketest

### 状态：已正常退出（非 RUNNING）

进程已死：`ps aux` 无匹配。两张 GPU 均空闲（0% util, 0 MiB memory）。

### 运行结果

- 模型：openvla-7b-finetuned-libero-goal
- Task：open_the_middle_drawer_of_the_cabinet（task_id=0）
- Baseline 3 episodes 全部失败（SR=0.00，每 episode 跑满 400 steps）
- 脚本逻辑：baseline SR=0 时提前终止（"no point running ablation"）
- 结论字段：`"baseline_zero"`

### 分析

Baseline 0% 成功率可能原因：
1. unnorm_key (`libero_goal`) 或 checkpoint 路径配置问题
2. 3 episodes 样本量太小
3. 环境版本冲突（numpy 2.0.2 与 scipy/gym 不兼容的 warnings）

### 结论

- Registry 应更新为 COMPLETED（结果 baseline_zero）
- 如需有效 ablation 对比，需先解决 baseline SR=0 问题

---

## 环境状态

| 项目 | 状态 |
|------|------|
| GPU | 2x RTX PRO 6000 Black，均空闲 |
| 磁盘 | /root/autodl-tmp 已用 95%（剩余 15G），需关注 |
| CUDA | torch.cuda.is_available() = True |
| 进程 | 无 GPU 进程运行 |
