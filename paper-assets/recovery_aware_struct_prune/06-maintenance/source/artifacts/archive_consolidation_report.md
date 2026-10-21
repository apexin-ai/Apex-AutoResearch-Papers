# 数据归档报告 — 阻塞

**状态**：阻塞，**未执行集中复制**。请用户决策后再继续。
**日期**：2026-05-25

---

## 1. 磁盘探测

| 服务器 | 路径 | 总容量 | 已用 | 可用 | Use% |
|---|---|---|---|---|---|
| westd-32935 | / (overlay) | 30G | 5.4G | 25G | 18% |
| westd-32935 | /root/autodl-tmp | 650G | 577G | **74G** | 89% |
| westb-23072 | / (overlay) | 30G | 8.2G | 22G | 28% |
| westb-23072 | /root/autodl-tmp | 250G | 221G | **30G** | 89% |

项目目录大小：

| 服务器 | 路径 | 大小 |
|---|---|---|
| westd-32935 | /root/recovery_aware_struct_prune | 21M |
| westd-32935 | /root/autodl-tmp/recovery_aware_struct_prune | **562G** |
| westb-23072 | /root/recovery_aware_struct_prune | 78M |
| westb-23072 | /root/autodl-tmp/recovery_aware_struct_prune | **205G** |

**合并需求**：562G + 205G ≈ **767G**。

---

## 2. 阻塞原因

按任务要求"必须包含所有 checkpoint"集中两台数据，无论选哪台为集中服务器都装不下：

- westd-32935：autodl-tmp 总容量只有 650G（已用 562G 是自己的项目数据），可用 74G；放不下另一台的 205G。
- westb-23072：autodl-tmp 总容量只有 250G，可用 30G；放不下另一台的 562G。

即使做"原地改名 + 仅 rsync 另一台"也不行（westd 仅剩 74G < westb 205G）。

**根本问题**：两台 autodl-tmp 单盘容量都小于联合 checkpoint 总量。

---

## 3. 数据构成（用于决策）

绝大多数空间是**模型 checkpoint 目录**（7B 模型，每个目录 11–38G）：

### westd-32935 的 562G 分解
- 大 checkpoint 目录（pruned_*/sft_*/grpo_*，~12G 每个）约 30+ 个 → **~540G**
- 其中较大异常者：`grpo_cka_only_20_floor_0.6`=38G，`grpo_standard_25_retrain`=36G，`sft_standard_25`=22G
- 非 checkpoint 数据：results 62M + logs 7.2M + wandb 30M + 评测 JSON/log ≈ **~110M**

### westb-23072 的 205G 分解
- 大 checkpoint 目录（7B 类约 15 个 × 12G = ~180G，1.5B 类约 8 个 × 2.8G = ~22G）→ **~202G**
- 其他：models/=3.4G，results 28M + logs 21M + wandb 280K + .pt 文件 → **~3.5G**

### 代码 + 实验产物（轻量）
两台合计：
- code (.git+src+scripts+脚本): ~150MB
- results JSON: ~100MB
- wandb 本地目录: ~90MB
- logs: ~30MB
- figures + paper (westb): ~1.6MB
- **轻量数据合计 < 400MB**，可轻松集中。

---

## 4. 可选方案（请用户决策）

### A. **只归档轻量数据**（推荐：保住论文/代码/可视化）
- 包含：code+.git、results JSON、logs、wandb local、figures 源数据/脚本、paper LaTeX
- 排除：所有模型 checkpoint
- 总大小：~400MB，**集中到 westd-32935 的 autodl-tmp 即可（74G 富余）**
- 后果：GPU 释放后所有 checkpoint 丢失，无法再次复跑

### B. **挑选关键 checkpoint 归档**
- 用户指定保留哪些（如每个方法只保最终 SFT/GRPO 模型，丢弃 floor/seed 变体）
- 需要用户列清单或给一个保留规则（例：只留论文表里出现的）

### C. **下载到本地/外部存储**
- 把 checkpoint 打包后 scp 到本地或 S3/OSS
- Agent 无法直接判断目的地，需要用户提供

### D. **放弃所有 checkpoint，只归档代码 + 论文 + 实验日志/结果**
- 等同方案 A

---

## 5. 暂未执行的内容

- [ ] 集中服务器选择（待方案确定）
- [ ] 本机数据复制
- [ ] 远端数据传输
- [ ] 验证

---

## 6. 两台直连测试（未执行）
按指示如选 westd 为集中点需要测 `ssh westb-23072 'echo OK'`。**等用户给方案后再测**，避免在阻塞场景下做无用功。

---

**请用户回复采用 A/B/C/D 中哪个方案**（默认建议 A），或给出其他指示后再继续操作。
