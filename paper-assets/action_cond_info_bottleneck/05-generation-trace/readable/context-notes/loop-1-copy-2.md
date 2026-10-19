# agent / loop_1.md

**action cond info bottleneck** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`db58266f17a1694ff8fe.json`](../../sessions/db/db58266f17a1694ff8fe.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-15T21:03:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1 @ westb-13953，不可用其他 GPU
- SSH 密码：`9ZJTsOZrkny+`，端口 13953（AutoDL 重启后端口会变，连不上先问用户）
- 所有 HF 操作必须：`source /etc/network_turbo` + `export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` + `SSL_CERT_FILE` + `HF_HUB_DISABLE_XET=1`，缺一个就 OSError
- 大文件存 `/root/autodl-tmp/`，根分区只有 ~30GB
- β=0.1 已验证导致 scorer 坍塌（step 250 后全部 ≈0.8），必须用 β=0.01 + warmup
- baseline eval 用 `lerobot/smolvla_libero`（不是 smolvla_base！之前 Worker 用错导致废弃实验）
- repo ID 是 `lerobot/smolvla_libero`（不是 `HuggingFaceVLA/smolvla_libero`，后者是早期误记）

### 2. 🖥️ 基础设施快照
- 服务器：westb-13953 (AutoDL), 2× RTX PRO 6000 Blackwell 98GB
- SSH: `ssh -p 13953 root@connect.westb.seetacloud.com`
- Python: `/root/miniconda3/bin/python` (conda base), Python 3.12.3
- 已装: lerobot 0.5.1, torch 2.10.0+cu128, transformers 5.8.1, mujoco 3.8.1
- lerobot 源码 patch: groot dataclass fix（已应用）
- 项目代码: `/root/acib/`（acib/, scripts/, configs/）
- HF cache: `/root/autodl-tmp/.hf_cache`
- 模型缓存: smolvla_base ✅, smolvla_libero ✅, smolvla_libero_plus ✅, SmolVLM2-500M ✅（processor + model 离线验证 PASSED）
- 数据集: `/root/autodl-tmp/libero_dataset/` (1.9GB, 273K frames, 完整)，但 HF cache 路径几乎为空
- 活跃进程: baseline_std eval PID 109428 (GPU 1), baseline_plus eval PID 109501 (GPU 0)
- Worker `dataset-download-hfcache` 正在解决训练数据路径问题（检查 LeRobotDataset 是否支持本地路径 or 下载到 HF cache）
- Cron: 无活跃 cron

### 3. 📊 当前状态
双 GPU baseline eval 稳定运行中，预计 ~09:30 CST 完成：
- **mvp1_baseline_std** (RUNNING, cuda:1): `lerobot/smolvla_libero`, 4 suites sequential, 早期 spatial 首 task 82% SR
- **mvp1_baseline_plus** (RUNNING, cuda:0): `lerobot/smolvla_libero_plus`, 4 suites, 早期 spatial 首 task **98%** SR
- **acib-mvp0-libero-v1** (DONE, negative): scorer 坍塌，β=0.1 太强，已确认 β warmup fix 必要性
- **acib_deploy_westb13953** (PREPARING): 历史残留，可忽略

等待中：
- Worker `dataset-download-hfcache` 回调 → 确认训练数据可用方案
- 标准 eval 完成回调 → 立即部署 perturbation eval 脚本 + 启动 LIBERO-Plus eval
- 所有 eval 完成 → ACIB v3 训练

### 4. 📋 待办（条件触发式）
- dataset Worker 回调 → 确认数据路径方案，必要时修改 `run_acib_v3_train.sh` 的数据参数
- baseline eval 完成（cron 回调或手动检查） → 收集 4 suite SR → update_registry metrics → 立即部署 `run_perturbation_eval_std.sh` (GPU 1) + `run_perturbation_eval_plus.sh` (GPU 0) 到远程并启动
- perturbation eval 完成 → 分析 robustness gap（标称 SR vs 扰动 SR） → 向 Director 汇报 gap 大小
- gap 确认 ≥10% → 启动 ACIB v3 训练（`run_acib_v3_train.sh`, seed 42 + seed 123 两轮）
- gap <10% → baseline 已鲁棒，MVP FAIL，需向 Director 报告并产出 Framing 调整提案
- ACIB v3 训练完成 → eval ACIB checkpoint on 标称+扰动 → 对比 baseline → MVP pass/fail 判定

### 5. 🎯 战略上下文
- CoRL 2026: abstract 5/26 (11天), paper 5/29 (14天)
- 核心 story: ACIB 通过 token-level soft reweighting 提升 VLA 视觉鲁棒性
- baseline_plus 98% vs baseline_std 82% 差距出乎意料 → 如果全 suite 稳定，ACIB 需定位为"与 data-aug 互补的 IB 正则化"而非替代品。Director 已注意到这个信号
- MVP pass 标准: ACIB-S 在 ≥2/4 扰动维度提升 ≥5% abs (baseline ≥10% 时)；标称回退 <2%
- 已有脚本全部就绪（perturbation eval × 2, ACIB v3 train），eval 结束后零等待
- 易踩坑：(1) 不要用 nohup 提交训练，必须用 submit_training_job (2) AutoDL 下载极慢，优先 ModelScope CDN (3) eval 脚本忘 network_turbo 会导致 processor 加载失败——已全部修复但新脚本务必包含 (4) n_episodes=50 是 per task 不是 per suite，不要改


---
