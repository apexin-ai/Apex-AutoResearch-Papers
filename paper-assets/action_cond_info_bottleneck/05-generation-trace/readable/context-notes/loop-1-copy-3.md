# reviewer / loop_1.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`6550dab11cfc318c70fb.json`](../../sessions/65/6550dab11cfc318c70fb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-15T21:02:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `westb-13953`，GPU 白名单 cuda:0 + cuda:1（两张 RTX PRO 6000 Blackwell 96GB）
- AutoDL 实例：eval/训练脚本必须包含 `source /etc/network_turbo` + `REQUESTS_CA_BUNDLE` + `SSL_CERT_FILE` + `HF_HUB_DISABLE_XET=1`，否则任何 HF 在线请求都会失败（已因此浪费 ~2 小时、3 轮 eval 全军覆没）
- `HF_HOME=/root/autodl-tmp/.hf_cache`（根分区只有 30GB，大文件必须在数据盘）
- SmolVLA eval 需要 `--policy.empty_cameras=1 --rename_map={"observation.images.image": "observation.images.camera1", "observation.images.image2": "observation.images.camera2"}`（3-camera → 2-camera 适配），否则加载失败

### 2. 🖥️ 基础设施快照
- 服务器：`westb-13953(root)`，工作目录 `/root/acib`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型缓存：`/root/autodl-tmp/.hf_cache/`（smolvla_libero + smolvla_libero_plus + SmolVLM2-500M-Video-Instruct 均已完整缓存）
- 训练数据：`/root/autodl-tmp/libero_dataset/`（1.9G，377 parquet + 74 mp4，273,465 frames，已验证完整）。注意 HF cache 中 `datasets--lerobot--libero` 几乎为空——训练脚本需用 `--data_root=/root/autodl-tmp/libero_dataset` 本地路径
- Eval 脚本：`/root/acib/scripts/run_eval_std_v3.sh`（GPU 1）、`run_eval_plus_v2.sh`（GPU 0）
- 训练脚本：`/root/acib/scripts/run_acib_v3_train.sh`（已部署，待启动）
- 活跃进程（截至 handoff）：PID 109428（baseline_std_v3 eval, GPU 1）、PID 109501（baseline_plus_v2 eval, GPU 0），均 03:38 CST 启动，预计 ~09:30 完成

### 3. 📊 当前状态
**刚完成**：审查 ACIB v3 dry-run（代码 OK）+ 数据集完整性验证（OK）+ baseline eval 存活确认。

**Registry**：
- `mvp1_baseline_std` — RUNNING，smolvla_libero 标称 eval（v3 脚本，4 suites × 50 ep），spatial task 0 完成 SR=82%
- `mvp1_baseline_plus` — RUNNING，smolvla_libero_plus 标称 eval（v2 脚本，同上），spatial task 0 完成 SR=98%
- `acib-mvp0-libero-v1` — DONE/negative（scorer collapsed，β=0.1 太强，已废弃）
- `acib_deploy_westb13953` — PREPARING（遗留条目，实际已被 v3 替代）

**等待**：baseline eval 完成 → 收集 SR 数据 → 启动 ACIB v3 训练

### 4. 📋 待办（条件触发式）
- baseline eval 完成通知到达 → 独立核实所有 suite 的 `eval_info.json` 存在且 SR 数字合理（spatial 预期 ~80-90%），交叉验证 registry 记录
- ACIB v3 训练启动通知 → 审查：(1) 训练数据是否走 `/root/autodl-tmp/libero_dataset` 本地路径（HF cache 里没有）；(2) β warmup 是否生效（前 1000 步 scorer_mean 不应锁在 0.8）；(3) GPU util 是否合理（batch_size=64 应比 v1 的 batch_size=8 好很多）
- ACIB v3 训练 ~2000 步时 → 检查 scorer collapse 是否复发（scorer_mean ≈ 0.8 + sparsity ≈ 0 = 复发信号）
- LIBERO-Plus 扰动 eval 启动 → 确认使用 `--env.type=libero_plus` 且按 4 维度（C/L/B/N）分别跑
- 任何论文章节审查请求 → 先查 registry 实验支撑 + paper_provenance 覆盖率

### 5. 🎯 战略上下文
- **项目定位**：ACIB = 对 VLA 视觉 token 做 IB 正则化（soft reweighting / hard pruning），目标 CoRL 2026（abstract 5/26, paper 5/29）
- **Framing 已调整**：从"robustness method"转为"与 data augmentation 互补的 regularizer"——因为发现 smolvla_libero_plus（官方 data-aug checkpoint）已存在。ACIB 必须展示在 libero_plus 之上的增量收益（complementarity）
- **MVP Pass/Fail v2**：标称 regression <2%，≥2/4 扰动维度上 ≥5% abs 提升（baseline≥10% 时），或相对 ≥50%/abs ≥3pp（baseline<10% 时），任何单维度 regression ≤10%
- **已踩的坑**：(1) v1 scorer collapsed 因 β=0.1 太强 → v3 用 β=0.01 + warmup；(2) eval 脚本不加网络配置会连环崩溃；(3) SmolVLM2 processor + model 都需要预缓存；(4) "Loading weights: 100%" 是 smolvla checkpoint 加载，不是 SmolVLM2 base model
- **易错判断**：baseline_plus SR=98% 远高于 baseline_std SR=82%——这意味着 data augmentation 效果很强，ACIB 要在此基础上再提升的空间可能有限。如果 ACIB+libero_plus 的扰动 SR 只比 libero_plus 高 1-2pp，需要诚实面对而不是包装成"重要发现"


---
