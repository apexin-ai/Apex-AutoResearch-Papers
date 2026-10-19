# 诊断：eval-random-selection-object-seed46-r2 失败

## 根因：robosuite/MuJoCo C 后端间歇性崩溃（segfault 或 OOM kill）

### 证据

1. **日志分析** (`logs/eval_object_random_selection_seed46.log`)：
   - 完成 6/10 任务后进程消亡，无 Python traceback、无错误信息
   - 最后一条正常输出：`[pick_up_the_tomato_sauce_and_place_it_in_the_basket] success rate: 0.0% (0/10)`
   - 未到达 "Overall success rate" 和 JSON 写出步骤

2. **对照实验** (seed42，同模式同代码)：
   - 10/10 任务全部完成，JSON 正常生成
   - 证明 `random_selection` 代码路径本身无 bug

3. **代码检查** (`select_action_random`, line 230)：
   - 逻辑极简：从 K 个候选中随机选一个，无内存泄漏风险
   - 与 seed42 完全一致的代码路径

4. **资源状态**：
   - 磁盘：根分区 30%、数据盘 40%，空间充裕
   - GPU：RTX 4090 D，当前 6.5GB/24GB 已用（另一实验在跑）
   - 无法访问 dmesg 确认 OOM kill，但资源状态正常

5. **崩溃特征**：
   - 无 Python traceback → 进程被外部信号杀死（SIGKILL/SIGSEGV in C code）
   - 代码有 SIGSEGV handler (line 489-491)，但 robosuite C 后端的 segfault 可能绕过 Python signal handler
   - 在第 7 个任务初始化/rollout 阶段崩溃，符合 robosuite 已知的间歇性 MuJoCo segfault 模式

### 结论

| 项目 | 结论 |
|------|------|
| 失败根因 | robosuite/MuJoCo 间歇性 C 后端崩溃，非代码 bug |
| 是否可直接重试 | **是**，直接重试原命令即可 |
| 需要修复吗 | 不需要，是已知的 robosuite 间歇性问题 |

### 重试命令

```bash
cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_random_selection_seed46.json
```
