# director / loop_1.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`f6b1aab575f2df4ea3a1.json`](../../sessions/f6/f6b1aab575f2df4ea3a1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-15T21:02:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-13953 的 cuda:0 和 cuda:1（项目配置白名单）
- AutoDL 所有 HF/网络操作必须先 `source /etc/network_turbo` + 设置 `REQUESTS_CA_BUNDLE` 和 `SSL_CERT_FILE` 指向 `/etc/ssl/certs/ca-certificates.crt` + `HF_HUB_DISABLE_XET=1`，否则必崩
- `HF_HOME=/root/autodl-tmp/.hf_cache`，根分区只有 30GB，大文件全放 `/root/autodl-tmp/`
- LIBERO 数据集在本地路径 `/root/autodl-tmp/libero_dataset/`（1.9GB, 377 parquet + 74 mp4），HF cache 路径几乎空的——训练脚本必须指向本地路径，不能走 HF 下载
- baseline checkpoint 用 `lerobot/smolvla_libero`（fine-tuned），绝不能用 `lerobot/smolvla_base`（pretrained，0% SR）

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953，工作目录 `/root/acib/`
- Python：AutoDL 默认（未用 conda/venv，直接 pip）
- ACIB 代码：`/root/acib/acib/`（config.py, scorer.py, losses.py, acib_policy.py）
- 训练脚本：`/root/acib/scripts/train_acib.py` + `/root/acib/run_acib_v3_train.sh`
- Eval 脚本：`/root/acib/scripts/eval_baseline.py` + `run_eval_std_v3.sh` / `run_eval_plus_v2.sh` / `run_perturbation_eval_std.sh` / `run_perturbation_eval_plus.sh`
- 模型 cache：`/root/autodl-tmp/.hf_cache/`（SmolVLM2-500M-Video-Instruct 已完整缓存，离线验证通过）
- 数据集：`/root/autodl-tmp/libero_dataset/`（273,465 frames, 1,693 episodes）
- Eval 输出：`/root/acib/outputs/baseline_std/` 和 `/root/acib/outputs/baseline_plus/`
- 活跃进程：baseline_std eval PID 109428 (cuda:1), baseline_plus eval PID 109501 (cuda:0)

### 3. 📊 当前状态
双 GPU baseline eval 正在运行（修了 3 轮才跑起来：processor 缓存 → model weights → network_turbo 根因修复）。预计 ~09:30 CST 完成。

Registry:
- `mvp1_baseline_std` RUNNING — smolvla_libero 标准 eval，4 suites，spatial 首 task 82% SR
- `mvp1_baseline_plus` RUNNING — smolvla_libero_plus (data-aug) eval，4 suites，spatial 首 task 98% SR
- `acib-mvp0-libero-v1` DONE/negative — scorer 后验坍缩（β=0.1 太强），已修复为 β=0.01 + warmup
- `acib_deploy_westb13953` PREPARING

等待中：两个 eval 的 cron 完成回调。无待审批实验。

### 4. 📋 待办
- baseline eval 完成 → 收集 8 suite 结果 → 分析 baseline_std vs baseline_plus 差距 → 更新 ROADMAP
- baseline 结果收集后 → 立即部署 perturbation eval 脚本（已创建好）→ 双 GPU 跑 LIBERO-Plus 4 个视觉扰动维度 → 建立 robustness gap
- perturbation eval 完成 → 如果 robustness gap 显著 → 启动 ACIB v3 训练（β warmup, batch_size=64）
- **训练启动前必须修复**：`run_acib_v3_train.sh` 数据路径从 `lerobot/libero` 改为 `/root/autodl-tmp/libero_dataset/`（或用已有的 `train_acib_libero.py` 支持 `--data_root`）
- ACIB v3 训练完成 → 对比 baseline → MVP pass/fail 判定

### 5. 🎯 战略上下文
- 目标 CoRL 2026（abstract DDL 5/26, paper DDL 5/29，剩 11/14 天）
- 核心假设：ACIB（token-level IB 干预）能提升 VLA 对视觉扰动的鲁棒性
- **关键早期信号**：baseline_plus (data-aug) 98% vs baseline_std 82%（spatial 首 task）。如果差距在全 suite 稳定，说明 data-aug 效果极强，ACIB story 必须定位为"与 data-aug 互补的 IB 正则化"而非替代品。MVP pass/fail 标准：ACIB 至少要在 baseline_std 上显著提升
- 决策链：D001-D008，关键节点是 D005（smolvla_libero_plus 作为必选 baseline）、D006（scorer 坍缩修复 β warmup）、D008（processor 缓存根因修复）
- **易错点**：(1) 忘记 network_turbo/SSL 导致 HF 请求崩溃——这轮踩了 3 次 (2) 训练数据在本地路径不在 HF cache，直接用 dataset_id 会触发重新下载 (3) GPU 利用率低是正常的（MuJoCo CPU 仿真瓶颈），不要误判为进程挂了 (4) eval batch_size=1，GPU 只在 forward pass 短暂使用


---
