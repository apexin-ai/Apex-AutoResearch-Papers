# westd-16639 GPU 进程归零 — 根因分析报告

**时间**: 2026-05-19 00:37 UTC+8  
**服务器**: westd-16639 (AutoDL, 4× RTX PRO 6000 96GB)  
**项目路径**: `/root/autodl-tmp/sica_project/symb_invariant_consensus/`（注意：不是 `/root/symb_invariant_consensus/`）

---

## 1. 崩溃根因：AutoDL 平台级进程终止（两波 kill）

### 第一波 kill — 00:05:54
- exp032 vLLM (GPU 0, PID 16369) 和 exp033 vLLM (GPU 1, PID 20553) 在**同一秒**收到 SIGTERM
- 两个独立 GPU 上的独立进程同时死亡 → 排除单进程 bug，确认为外部 kill
- vLLM 日志显示 `Shutdown initiated (timeout=0)` → 收到信号后的优雅退出，不是崩溃
- exp035 (GPU 3) 的 vLLM 日志未保存到 /tmp/，但可能同时被 kill

### 第二波 kill — 00:16:16~00:16:22
- 所有剩余进程（exp032/033 的 python 重试循环、exp034 vLLM+实验、exp035 实验）同时消失
- exp034 日志在问题 4/200 中断，exp035 在问题 19/60 中断
- exp032 的 python 脚本仍在问题 519/600 无望地重试连接已死的 vLLM

### 排除的原因
| 假设 | 排除依据 |
|------|----------|
| OOM | 系统内存 956GB 可用，GPU KV cache 使用率 < 2% |
| 磁盘满 | overlay 42%, 主存储 40% |
| 内部崩溃 | 两个不同 GPU 的 vLLM 同一秒死亡，且日志无 error |
| 重启 | 容器仍可 SSH，uptime 显示 220 天 |

### 最可能原因
**AutoDL 平台资源回收或调度干预**。证据：
1. 同一秒跨 GPU 进程终止（SIGTERM，非 SIGSEGV）
2. 容器内无 dmesg/journalctl 权限（典型 AutoDL 容器限制）
3. `autopanel.monitor.db` 持续更新（AutoDL 监控活跃）
4. 无任何应用层错误先于进程死亡

---

## 2. 当前 GPU 状态

| GPU | 型号 | 温度 | 功耗 | 显存占用 | 利用率 | 状态 |
|-----|------|------|------|----------|--------|------|
| 0 | RTX PRO 6000 | 28°C | 34W/600W | 0/97887 MiB | 0% | 空闲 |
| 1 | RTX PRO 6000 | 30°C | 35W/600W | 0/97887 MiB | 0% | 空闲 |
| 2 | RTX PRO 6000 | 30°C | 34W/600W | 0/97887 MiB | 0% | 空闲 |
| 3 | RTX PRO 6000 | 30°C | 34W/600W | 0/97887 MiB | 0% | 空闲 |

4 张 GPU 全部空闲，无任何 GPU 进程。nvidia-smi 正常工作。

---

## 3. 系统资源状态

| 指标 | 值 | 状态 |
|------|-----|------|
| 内存 | 42GB used / 1.0TB total (956GB available) | 正常 |
| Swap | 0B / 0B | 无 swap |
| 磁盘 overlay | 13GB / 30GB (42%) | 正常 |
| 磁盘 /dev/sda2 | 333GB / 879GB (40%) | 正常 |
| Load average | 4.45, 4.50, 4.92 | 偏高（可能有残留 kernel threads） |
| Uptime | 220 天（宿主机，非容器） | — |
| 运行进程 | 仅 jupyter-lab + tensorboard | 无实验进程 |

---

## 4. 各实验状态汇总

| 实验 | GPU | 模型 | 数据集 | 进度 | 结果文件 | 状态 |
|------|-----|------|--------|------|----------|------|
| exp032 | 0 | Qwen2.5-14B | ProofWriter 600 | 510/600 | .polluted.bak | vLLM 00:05:54 被 kill，脚本重试至 00:16 被二次 kill |
| exp033 | 1 | Qwen3-14B | ProofWriter 600 | ~500+/600 | .polluted.bak | 同上，vLLM 同一秒被 kill |
| exp034 | 2 | Qwen2.5-14B | StrategyQA 200 | 3/200 | exp034_results.json (3条) | 00:15:17 启动，00:16:20 被 kill |
| exp035 | 3 | Qwen2.5-14B | ARC 60 | 18/60 | results.json (18条) | 运行至 00:16 被 kill |

---

## 5. exp-034 StrategyQA extraction_rate 分析

### 数据
- 处理了 3/200 题
- extraction_rate = **2.78%** (3 successes / 108 extraction attempts)
- 问题 1: 0 constraints, 问题 2: 3 constraints, 问题 3: 0 constraints

### 根因：Prompt 类型不匹配

`run_full_mvp.py` 第 264-267 行：
```python
if dataset in ("proofwriter", "folio"):
    extractor.domain = "logic"
else:
    extractor.domain = "math"  # ← StrategyQA 走这个分支
```

StrategyQA 被当作 `math` 类型，使用 `EXTRACTION_PROMPT`（期望提取 equation/inequality/predicate 类型的数学约束）。

**问题**：
- StrategyQA 是常识推理 Yes/No 题（如 "Did Mozart ever buy anything from Dolce & Gabbana?"）
- 推理 trace 包含常识知识链，不包含数学方程或不等式
- `EXTRACTION_PROMPT` 要求输出 `equation`/`inequality`/`predicate` 类型 + Z3 公式 → 对常识推理几乎完全失效
- 即使切换为 `LOGIC_EXTRACTION_PROMPT`（fact/rule/derived），其示例也是 ProofWriter 式的形式逻辑，对常识推理同样不适配

**修复建议**：StrategyQA 需要专用的 constraint extraction prompt，将常识推理步骤转化为可验证的逻辑链（如：前提真实性检查、时间线一致性、因果关系验证），而非套用数学/形式逻辑的 extraction 模板。

---

## 6. 重启建议

**可以安全重启实验**，条件如下：

1. **GPU 和系统资源正常**：4 GPU 全部空闲，内存/磁盘充足
2. **确认 AutoDL 账户状态**：先在 AutoDL 控制台检查是否有欠费/限制/维护通知，否则重启后可能再次被 kill
3. **利用 --resume**：exp032/033/035 脚本都支持 `--resume`，可从断点恢复
4. **exp034 暂不重启**：extraction prompt 未适配 StrategyQA，重启也会得到同样的低 extraction_rate，需先修改代码

### 重启优先级
1. **exp035** (ARC 60)：18/60 已完成，剩余 42 题，预计 ~20 分钟
2. **exp032** (PW 600)：510/600 已完成（但结果文件 .polluted.bak 需确认中间结果是否可恢复），剩余 90 题
3. **exp033** (PW 600)：同上
4. **exp034** (StrategyQA)：**阻塞**，需先修复 extraction prompt
