# 诊断报告：westd-38929 OpenVLA Eval 批量失败

**诊断时间**: 2026-05-21 15:05 UTC+8 (07:05 UTC)

## 根因：AutoDL 容器级重启

**不是 OOM、不是 CUDA 错误、不是代码 bug。** 是 AutoDL 平台对容器执行了重启，导致所有用户进程被 SIGKILL。

### 证据链

| 信号 | 观测 | 解释 |
|------|------|------|
| 日志无错误 | 4 个实验日志全部在 Task 4 中途截断，无异常堆栈 | 进程被外部 kill，非程序崩溃 |
| dmesg 为空 | 148 天 uptime 却无任何 dmesg 输出 | 容器重启清空了 ring buffer |
| 系统服务重启 | jupyter-lab + tensorboard 启动于 14:50（实验死亡后 1 分钟） | init 系统重新拉起了服务 |
| tmux/screen 全灭 | 无任何 session 存活 | 容器重启杀掉了所有用户会话 |
| uptime 148 天 | 宿主机未重启 | 这是容器级重启，非 host 重启 |
| 内存充裕 | 1 TB RAM，仅 46 GB used，无 OOM killer 记录 | 排除内存不足 |
| 磁盘未满 | /root/autodl-tmp 84% (41 GB 剩余) | 排除磁盘满 |

### 时间线（UTC）

```
05:03-05:05  4 个 eval 实验启动（PID 568225/568905/569611/570309）
05:03-06:45  正常运行 ~100 分钟，各完成 Tasks 1-3
06:45-06:49  日志停写（容器重启，进程被 kill）
06:50        jupyter/tensorboard 重新启动（init 系统恢复服务）
07:01-07:04  Registry reconcile 检测到进程死亡，标记 FAILED
```

## 各实验状态

### 失败实验的 Partial Results

| 实验 | 方法 | Token 压缩 | 完成进度 | 最后位置 | 已观察到的趋势 |
|------|------|-----------|----------|---------|---------------|
| eval_openvla_random_k03 | Random pruning k=0.3 | 256→76 | 170/500 eps | Task 4 Ep 20/50 | T1=14% T2=0% T3=56% |
| eval_openvla_l2norm_k07 | L2 norm k=0.7 | 256→179 | 180/500 eps | Task 4 Ep 30/50 | T1=42% T2=28% T3=54% |
| eval_openvla_l2norm_k05 | L2 norm k=0.5 | 256→128 | 160/500 eps | Task 4 Ep 10/50 | T1=56% T2=14% T3=38% |
| eval_openvla_l2norm_k03 | L2 norm k=0.3 | 256→76 | 160/500 eps | Task 4 Ep 10/50 | T1=42% T2=6% T3=28% |

### 已有完整结果（先前运行）

| 实验 | SR | 状态 | 说明 |
|------|-----|------|------|
| l2norm k=0.5 | **39.2%** | ✅ 已完成 | `openvla_l2norm_prune_k0_5_object.json` (01:35 UTC) |
| l2norm k=0.3 | **25.0%** | ✅ 已完成 | `openvla_l2norm_prune_k0_3_object.json` (02:04 UTC) |
| random k=0.3 | — | ❌ 无完整结果 | **需重跑** |
| l2norm k=0.7 | — | ❌ 无完整结果 | **需重跑** |

### 其他相关实验

| 实验 | PID | Registry 状态 | 实际状态 | 说明 |
|------|-----|--------------|---------|------|
| eval_openvla_sc_m128_object_seed42_v2 | 188248 | RUNNING (stale) | ❌ 已死 | 同样被容器重启杀死，无结果文件，Registry 需更新 |
| eval_openvla_l2norm_k03_object_seed42 | — | DONE/failed | ❌ | 同批次失败 |

## 当前 GPU 状态

```
GPU 0: NVIDIA RTX PRO 6000 Black (96 GB)
  状态: 空闲 (0 MiB / 97887 MiB)
  进程: 无
  温度: 26°C
```

**整台服务器完全空闲，可立即使用。**

## 重试建议

1. **可安全重试** — 无硬件故障、无 GPU 错误、代码无 bug
2. **只需重跑 2 个实验**：
   - `eval_openvla_random_k03_object_seed42` (Random k=0.3)
   - `eval_openvla_l2norm_k07_object_seed42` (L2 norm k=0.7)
   - l2norm k=0.5 和 k=0.3 已有完整结果，无需重跑
3. **更新 Registry**：将 `eval_openvla_sc_m128_object_seed42_v2` 标记为 FAILED
4. **防护措施**：使用 `nohup` + 定期写 checkpoint/partial results，避免容器重启导致完全数据丢失
5. **注意**：此服务器只有 1 块 GPU，4 个实验需串行或分 2 批运行（每个模型 ~15 GB，两个可并行 fit 96 GB）
