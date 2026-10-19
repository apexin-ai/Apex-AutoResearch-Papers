# Eval 实验批量失败诊断报告

**日期**: 2026-05-21  
**诊断范围**: 5 个 FAILED + 2 个 ESCALATING eval 实验

---

## 1. 根因分析

**共有两个独立根因，加一个监控误报：**

### 根因 A: bjb2-28827 SIGHUP 批量杀死进程

**影响实验**: norm005-seed62, norm01-seed61, norm005-seed63（+ 短命名 seed60, seed64）

- 5 个进程在 08:43:09.417 CST 同一微秒创建，全部在 1-11 分钟内静默退出
- 日志无 Python Traceback、无 OOM 信息、无 CUDA 错误，仅 13-14 行
- 与 bjb2-28827 历史 SIGHUP 模式一致：SSH/tmux 会话断开后，SIGHUP 信号杀死未 nohup 保护的子进程
- dmesg 不可用（AutoDL 容器限制），但从日志模式判断非 OOM

**时间线**:
| 时间 (CST) | 事件 |
|------------|------|
| 07:26 | 长命名 seed60 独立启动 (GPU 5, nohup, 存活至今) |
| 08:43:09 | 短命名批次 seed60-64 同时创建 (GPUs 0-4) |
| 08:44:12 | seed60-short, seed64 首先死亡 (~1min) |
| 08:46 | seed71-75 作为替代在 GPUs 0-4 启动 |
| 08:54:24-39 | seed61, 62, 63 死亡 (~11min) |

**关键证据**: 同一长命名 seed60 (nohup + CUDA_VISIBLE_DEVICES=5) 从 07:26 运行至今（已 >1.5h），说明问题不在 GPU/内存/磁盘，而在进程启动方式。

### 根因 B: bjb1-32546 `python` 命令不存在

**影响实验**: norm003-seed63, norm003-seed62（注册表中的 #4, #5）

- 错误信息: `nohup: failed to run command 'python': No such file or directory`
- bjb1-32546（非 bjb1-18228）上 PATH 中只有 `python3`，无 `python` symlink
- 需使用 `/root/miniconda3/bin/python` 或 `python3`
- 已重试为 seed63-r2, seed62-r2（注册表中状态 RUNNING）

### 误报: bjb1-18228 seed57/seed58 实际已完成

**影响实验**: norm01-seed57 (miss 2/5), norm005-seed58 (miss 3/5)

这两个实验**实际已成功完成**，被监控系统误报为失败：

| 实验 | 结果 | 日志证据 |
|------|------|----------|
| seed57 | 19.0% (19/100) | 日志含 "Overall success rate" + JSON 已保存 |
| seed58 | 16.0% (16/100) | 日志含 "Overall success rate" + JSON 已保存 |

**误报原因**:
1. `evaluate.py` 不含 W&B 集成（grep 确认无 wandb import）
2. 实验未通过 `tmux_wrapper.sh` 启动，因此无 sentinel 文件写入
3. 监控系统检查 "进程存活 + sentinel/W&B" → 实验完成后进程退出 + 无 sentinel → 报 miss

sentinel 目录在两台服务器上均为空：`/root/acr-vla-conformal-refinement/logs/sentinels/` 无任何文件。

---

## 2. 影响范围

### 当前正在运行的实验 — 安全

**bjb2-28827** (6 进程, 6 GPU):
| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| seed60 (长命名) | 5 | 890017 | 正在 chocolate_pudding task |
| seed71 (norm01) | 0 | 922504 | 正在 cream_cheese task |
| seed72 (norm005) | 1 | 922712 | 正在 cream_cheese task |
| seed73 (norm003) | 2 | 922982 | 正在 cream_cheese task |
| seed74 (norm01) | 3 | 923256 | 正在 cream_cheese task |
| seed75 (norm005) | 4 | 923398 | 正在 cream_cheese task |

- GPU 温度正常 (38-40°C), 内存使用 ~5.2GB/24GB
- 系统 RAM: 79GB/1TB used, 充足
- 磁盘: 根 44%, 数据盘 15%

**bjb1-18228** (1 进程, 4 GPU):
| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| seed65 (norm005) | 1 | 622484 | 正在 bbq_sauce task |

- 3 个 GPU 空闲 (0, 2, 3)
- 系统 RAM: 42GB/1TB
- 磁盘: 根 53%, 数据盘 61%

**风险评估**: 当前运行的实验均使用 nohup 或独立进程方式启动，有 CUDA_VISIBLE_DEVICES 隔离，不受 SIGHUP 影响。无风险。

---

## 3. 修复建议

### 已自动修复
- seed61/62/63 (bjb2 SIGHUP) → 已被 seed71-75 替代（不同 seed 但覆盖相同 norm 值）
- seed62-norm003/seed63-norm003 (python 不存在) → 已注册 r2 重试

### 需要修复的系统性问题

**P0: 监控误报** — seed57/seed58 结果需要从 "failed" 改为 "success"
- 结果 JSON 存在于 bjb1-18228: `logs/eval_obs_only_object_norm01_seed57.json`, `logs/eval_obs_only_object_norm005_seed58.json`
- 需更新注册表 conclusion 为 success，并录入 metrics

**P1: Sentinel/W&B 监控缺口**
- `evaluate.py` 无 W&B 集成
- 大多数实验不通过 `tmux_wrapper.sh` 启动
- 两个检测通道都失效 → 监控对 eval 实验形同虚设
- **建议**: 在 evaluate.py 结尾添加 sentinel 写入逻辑（JSON 结果已保存时同时写 sentinel），或让启动脚本统一用 tmux_wrapper.sh

**P2: 进程启动方式不统一**
- 部分用 nohup（抗 SIGHUP），部分直接 python3（不抗）
- 部分用长命名，部分用短命名
- **建议**: 统一通过 `nohup ... &` 或 `tmux_wrapper.sh` 启动

---

## 4. 是否可以直接重试

| 实验 | 可否重试 | 说明 |
|------|----------|------|
| norm005-seed62 (bjb2) | 不需要 | 已被 seed72 替代 |
| norm01-seed61 (bjb2) | 不需要 | 已被 seed71/74 替代 |
| norm005-seed63 (bjb2) | 不需要 | 已被 seed75 替代 |
| norm003-seed63 (bjb1-32546) | 已重试 | seed63-r2 已注册 |
| norm003-seed62 (bjb1-32546) | 已重试 | seed62-r2 已注册 |
| norm01-seed57 (bjb1-18228) | **不需要** | 实际已完成，需纠正注册表 |
| norm005-seed58 (bjb1-18228) | **不需要** | 实际已完成，需纠正注册表 |

**注意**: 注册表中还有 10 个 RUNNING 状态实验（seed51-r3, seed52-r3, seed62-r2, seed63-r2, seed64/65 × 3 norms）等待 GPU 资源。bjb1-18228 有 3 个空闲 GPU 可用。

---

## 5. 总结

| 根因 | 影响 | 严重度 |
|------|------|--------|
| SIGHUP 杀进程 (SSH 断连) | 3 个实验死亡，已替代 | 中 — 已恢复 |
| `python` 不在 PATH | 2 个实验未启动，已重试 | 低 — 已修复 |
| 监控误报（无 sentinel/W&B） | 2 个已完成实验被标记失败 | **高 — 系统性问题** |

最紧急的行动是：纠正 seed57/seed58 的注册表状态，以及在 eval 流程中补上 sentinel 写入机制。
