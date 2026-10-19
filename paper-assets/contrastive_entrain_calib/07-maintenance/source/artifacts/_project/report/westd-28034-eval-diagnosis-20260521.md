# westd-28034 Eval 实验诊断报告

**日期**: 2026-05-21 15:30 (UTC+8)
**报告原因**: 报告称 3 个 eval 实验同时以 EXIT_CODE=129 (SIGHUP) 失败

---

## 结论：实际情况与报告不符

**只有 exp-003-eval-ckpt5000-v2 真正失败。ckpt6000/6500/7000 从未失败，当前正在正常运行。**

---

## 各实验实际状态

### exp-003-eval-ckpt5000-v2 — ❌ 已失败，已重试

| 项目 | 详情 |
|------|------|
| 原始 wrapper PID | 495833（已退出） |
| 子进程 PID | 495837（被 SIGKILL） |
| 启动时间 | 15:18:58 |
| 失败时间 | 15:19:24（运行 ~26 秒） |
| EXIT_CODE | 129（HUP trap 记录） |
| 日志关键行 | `bash: line 1: 495837 Killed timeout 14400 env bash -c ...` |
| 重试状态 | PID 497834 已在 GPU 0 上运行 |

**根因分析**：
- 子进程被 SIGKILL（bash 报告 "Killed"），非 SIGHUP
- wrapper 的 HUP trap 触发了 exit 129
- **排除 OOM**：系统 791GB RAM，761GB 可用，无内存压力
- **无内核日志**：容器环境无 /var/log/kern.log 或 syslog，无法确认 OOM killer 或其他内核事件
- **最可能原因**：外部干预（手动 kill / 资源管理器 / 或先前进程 GPU 残留冲突）

### exp-003-eval-ckpt6000 — ✅ 正在运行

| 项目 | 详情 |
|------|------|
| Wrapper PID | 498441（Ss+，存活） |
| Python PID | 498446（GPU 1，16834MiB，48% util） |
| 启动时间 | 15:22:02 |
| Exit 文件 | 不存在（未退出） |

### exp-003-eval-ckpt6500 — ✅ 正在运行

| 项目 | 详情 |
|------|------|
| Wrapper PID | 498579（Ss+，存活） |
| Python PID | 498584（GPU 2，16834MiB，48% util） |
| 启动时间 | 15:22:05 |
| Exit 文件 | 不存在（未退出） |

### exp-003-eval-ckpt7000 — ✅ 正在运行

| 项目 | 详情 |
|------|------|
| Wrapper PID | 498661（Ss+，存活） |
| Python PID | 498666（GPU 3，16834MiB，50% util） |
| 启动时间 | 15:22:07 |
| Exit 文件 | 不存在（未退出） |

---

## 服务器状态

| 项目 | 状态 |
|------|------|
| 可达性 | ✅ SSH 正常 |
| GPU | 4× RTX 5090 32GB，全部在用（48-50% util） |
| VRAM | 各 ~16.8GB / 32.6GB |
| 系统内存 | 791GB 总量，761GB 可用 |
| CUDA | 13.2 |
| Driver | 595.71.05 |

---

## 建议

1. **无需操作**：4 个 GPU 全部被活跃 eval 进程占用（ckpt5000-v2 重试 + ckpt6000/6500/7000），等待完成即可
2. **ckpt5000-v2 失败为孤立事件**：已自动重试，当前在 GPU 0 运行中
3. **状态报告可能有误**：ckpt6000/6500/7000 从未以 EXIT_CODE=129 失败——可能是监控系统读取了过时状态或误判
4. **结果输出目录**：`/root/contrastive_entrain_calib/results/exp003_d027_eval/` 已有 ckpt1000-5500 的结果，等待当前 4 个 eval 完成后会追加 ckpt5000-v2, 6000, 6500, 7000 的结果
