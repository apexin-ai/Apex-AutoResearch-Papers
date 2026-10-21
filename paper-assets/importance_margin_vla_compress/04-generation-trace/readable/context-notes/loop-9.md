# director / loop_9.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`8468ddbdd82478a30760.json`](../../sessions/84/8468ddbdd82478a30760.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-21T01:31:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-27271(0,1), westd-38929(0,1,2,3), westd-41074(0,1,2,3), cqa1-33015(0,1,2,3) — 共14卡，不可用其他
- **pip install 前必须 ps aux 确认无活跃实验进程**（M043教训：LIBERO-Plus pip install 覆盖运行中 LIBERO 包导致 4 GPU 崩溃）
- **eval 前必须验证 checkpoint 完整性**（M044教训：aria2c 下载中的 safetensors 被加载 → 0% SR）：无 .aria2 文件 + 无活跃下载进程 + safetensors 完整性检查
- **GPU 状态不可信任 get_gpu_health/list_available_gpus**（M041+3次ROADMAP误判）：必须 post_to_reviewer SSH 校验后再分配
- OpenVLA suite-specific checkpoint 必须用对应 suite 的 fine-tuned 版本（Object checkpoint 在 Spatial = 0%）
- OFT 有 **512 vision tokens**（DINOv2+SigLIP 双骨干融合），不是 256 — Reviewer 纠正过，写 adapter 和论文时必须正确处理

### 2. 🖥️ 基础设施快照
- **westd-27271** (2 GPU): 项目路径 /root/autodl-tmp/importance_margin_vla_compress。磁盘 77% (192G/250G) — VTC M32 训练中，需监控空间
- **westd-38929** (4 GPU): 同上路径。LIBERO + LIBERO-Plus 已装。环境已恢复（M043 后 Worker 切回 LIBERO-master + patch torch.load）
- **westd-41074** (4 GPU): 同上路径。OpenVLA checkpoint 下载：spatial 完成（/root/autodl-tmp/openvla-7b-finetuned-libero-spatial/），goal/10 下载中（aria2c + hf-mirror.com 16MiB/s）
- **cqa1-33015** (4 GPU): X-VLA-Libero checkpoint 覆盖全4 suite，无需额外下载
- HF 下载加速方案：`aria2c -x16` + `hf-mirror.com`（无代理），已验证 64x 加速
- OFT checkpoints: `moojink/openvla-7b-oft-finetuned-libero-{object,spatial,goal,10}` — 尚未下载
- π0.5 checkpoint: `lerobot/pi05_libero_finetuned` (~8GB) — 尚未下载

### 3. 📊 当前状态
**刚做完**：处理 Reviewer 审查报告（非单调 Goal 剪枝发现 + OFT 512 token 纠正），更新 paper_framing.md，批准 RESET_BOTH。

**RUNNING 实验**（~10/14 GPU 活跃，4 空闲）：
- westd-27271:0 — eval_openvla_prune_l2norm_k07_seed43_v2 (Object)
- westd-27271:1 — train_openvla_sc_m32_vtconly_seed42 (VTC, 36.8K/100K)
- westd-41074:0 — eval_openvla_prune_random_k05_seed42 (Object, 6/10 tasks)
- westd-41074:1 — OpenVLA Spatial baseline max_steps=600 smoke test（诊断中）
- westd-41074:2 — train_openvla_sc_m96_seed42_v3 (38.3K/100K)
- westd-41074:3 — train_openvla_sc_m64_seed42_v3 (47.4K/100K)
- cqa1:0 — X-VLA Goal k=0.9 seed42
- cqa1:1 — X-VLA Long baseline seed42 (T0=96%, T1=68%, T2=100%)
- cqa1:3 — X-VLA Goal k=0.5 seed42

**空闲 GPU**：westd-38929:2, cqa1:2, westd-38929 部分卡（v2 Object 实验可能已完成待确认）

**等待中**：
- Worker: max_steps 诊断 A/B 测试结果（westd-41074:1）
- Worker: OFT adapter 代码编写 + π0.5 pruning adapter（D120 执行指令已发）
- Worker: 空闲 GPU 审计结果
- Manager: 8×A100 扩容申请回复

### 4. 📋 待办（条件触发式）
- max_steps A/B 测试完成 → 若 600 步显著好于 280 → 更新所有 OpenVLA Spatial/Goal/Long eval 脚本的 max_steps，重启 Spatial baseline
- westd-38929 v2 Object 实验完成（k095/k07/l2norm ~2h 剩余）→ 4 GPU 释放 → SmolVLA baseline Spatial/Goal/Long + OFT/π0.5 setup
- OFT adapter 代码完成 → request_experiment_approval → Object baseline（预期 ~97%，低于 80% 说明 adapter 有 bug）
- π0.5 offline CV 分析完成 → 预期 CV≈0.038。若 CV > 0.1 → 架构和预期不同，需要深入调查
- Goal k=0.9/k=0.5 完成 → 关注 T3 非单调（k=0.9=6%, k=0.5=40%）是否在剩余 tasks 也出现。若 suite-level 聚合仍显示 Goal >> Spatial robustness → 叙事成立
- X-VLA Goal T3 非单调需多 seed 验证（seed43/44）→ 确认是真实效应还是 L2-norm scoring artifact
- Manager 批准 GPU → director_allocate_gpus 分配新卡，全面铺开 OFT+π0.5 4-suite 实验
- VTC M32/M64/M96 训练完成（M64 ~25h, M32/M96 ~35h）→ OpenVLA VTC eval

### 5. 🎯 战略上下文
**项目**：CoRL 2026 投稿。Abstract DDL 5月26日（5天），Paper DDL 5月29日（8天）。Analysis + Method paper：VLA token compressibility 由 connector architecture 决定。

**决策链**：
- D115: 扩展到 LIBERO 全 4 suite（用户指令）
- D116: SimplerEnv → LIBERO-Plus（第二 benchmark）
- D119: LIBERO-Plus 放弃（L1 SR=3.3% floor effect）→ 靠 4-suite 覆盖 RC7
- D120: 加入 π0.5 + OFT（用户指令"立即开始，卡不够向 manager 要卡"）→ 5→7 模型

**核心发现演进**：
- 原始叙事："connector type determines pruning tolerance"（4-class taxonomy: immune/threshold/graded/catastrophic）
- 升级叙事："pruning sensitivity = f(connector_type, task_semantics)" — Spatial suite（语义相同，靠空间 token 消歧）比 Goal suite（语义多样，语言消歧）敏感得多
- Goal 非单调效应：per-task 级别存在 k=0.5 > k=0.9（T1/T3），suite-level 聚合仍单调。需要多 seed 验证 T3 后决定是否升级为独立 finding

**易错点**：
- Agent 经常 idle 15-20 分钟不动 → 用 replace_agent_queue 合并指令解堵，不要一直等
- GPU 状态反复出错 → 永远先 Reviewer 校验再写 ROADMAP/发指令（已存 feedback memory）
- OFT 是 512 tokens 不是 256 — 刚纠正过，容易回退
- OpenVLA Spatial 0% 可能是 max_steps 问题（等诊断），不是 checkpoint 问题（已验证完整）
- westd-38929 环境被 LIBERO-Plus 改过，虽已恢复但注意 benign warning（datasets path not exist）


---
