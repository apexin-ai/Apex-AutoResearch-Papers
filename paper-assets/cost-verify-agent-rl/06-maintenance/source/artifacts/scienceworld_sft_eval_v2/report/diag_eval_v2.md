# 诊断报告: scienceworld_sft_eval_v2 反复崩溃

**日期**: 2026-05-20
**服务器**: bjb1-17606
**当前状态**: 已修复并恢复运行（PID 195853, episode 465/1796）

---

## 根因 (Root Cause)

**原始脚本缺少三项关键机制，导致 Java gateway deadlock 时进程无法恢复：**

1. **无 per-episode timeout** — ScienceWorld 通过 Py4J 与 Java gateway 通信。当 `env.step()` 或 `env.get_valid_action_object_combinations()` 的 Py4J RPC 调用死锁时，Python 进程阻塞在 socket read 上，永远无法返回
2. **无 resume 能力** — 每次进程被杀后必须从 episode 1 重新开始（但 JSONL append 模式保留了已完成数据）
3. **无 error recovery** — `run_episode()` 调用未被 try/except 包裹，任何未处理异常直接终止整个进程

### 为什么进程"死亡"而无错误日志

进程并非 crash，而是 **hang**。Py4J RPC 阻塞在 Java socket read 上，Python 主线程无法继续执行。因为没有 timeout 机制，进程永远等待 Java 响应。用户或监控发现进程无输出后手动 kill，所以日志中无错误信息。

---

## 修复内容 (已应用)

对比 `eval_scienceworld.py`（421行）vs `eval_scienceworld.py.bak`（325行，原始版本），diff 显示新增：

```
+ import signal, subprocess
+ class EpisodeTimeout(Exception): pass
+ def _timeout_handler / _kill_java_gateways    # SIGALRM -> 强杀 Java -> 重建 env
+ --resume flag                                  # 从 JSONL 恢复已完成 episodes
+ --episode_timeout                              # 默认 300s per episode
+ signal.alarm(300)                              # 每个 episode 前设定
+ except EpisodeTimeout -> kill gateways -> rebuild env
+ except Exception      -> kill gateways -> rebuild env
```

---

## 日志关键片段

### 原始运行 (02:08 启动, eval_scienceworld.log)
```
Eval plan: 1796 episodes across 30 task types (split=dev, T=0.4)
[1/1796] FAIL(3) boil v14 (100 steps, valid=1%, fmt=61%, 63.4s)
...
[23/1796] FAIL(0) chemistry-mix-paint-secondary-color v18 (100 steps, valid=0%, fmt=1%, 65.0s)
# <- 日志截止，之后进程 hang，无更多输出
```
日志仅 72 行。进程反复被杀重启，每次用 `>` 覆盖日志文件，导致中间输出丢失。

### 修复后恢复运行 (07:43 启动)
```
Resuming: 439 episodes already completed, skipping to episode 440
[440/1796] OK inclined-plane-determine-angle v109 (19 steps, valid=74%, fmt=100%, 7.4s)
...
[465/1796] FAIL(10) inclined-plane-friction-named-surfaces v700 (100 steps, valid=36%, fmt=56%, 72.7s)
# <- 持续运行中，无 timeout/error
```

---

## 已完成数据可用性

**全部可用，无需从头跑。**

| 指标 | 值 |
|------|----|
| JSONL 路径 | `/root/autodl-tmp/checkpoints/scienceworld_sft/eval_results_dev_v2.jsonl` |
| 已完成 | 465 episodes（持续增长中） |
| 成功率 | 167/465 = 35.9% |
| 错误/超时 | 0 条 |
| 重复条目 | 0 条 |

Episodes 405-420 区域（含所谓的 "episode 414 deadlock" 附近）数据完整正常。原始 5 次 crash 期间的已完成 episodes 通过 JSONL append 模式全部保留。修复后的 `--resume` 从 JSONL 恢复，跳过已有条目。

---

## 剩余风险

1. **env init deadlock**：`signal.alarm` 覆盖了 `run_episode()` 内的 Py4J 调用，但 timeout/error handler 中的 `ScienceWorldEnv("")` 初始化不在 alarm 保护范围内。如果新 env init 也死锁，进程仍会 hang
2. **端口残留**：`_kill_java_gateways()` 后仅 sleep 1s，旧 Java 进程端口可能未释放，新 env 可能连接到残留 socket。建议增加至 sleep 3s 或添加端口释放检查
3. **ETA**：1796 episodes x ~50s/episode = ~25h 总时间。已完成 26%，预计还需 ~18h

---

## 总结

根因是原始脚本无 timeout/resume/error-recovery 机制，Py4J gateway deadlock 导致进程无限 hang。修复已到位（timeout + resume + error recovery），当前运行稳定。465 条已完成数据全部可用。
