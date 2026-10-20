# trace_distill_repair — Research Dashboard

> 最后更新: 2026-05-15 16:20 UTC | 更新原因: D033 MVP FAIL，等用户决策

## 核心方向
~~Execution trace 对 LLM 程序修复的价值不在逐行内容，而在结构。~~
**MVP FAIL (D033)**：核心假设"结构化 trace 过滤提升 LLM 修复"被两个模型一致否定。

## 当前阶段
**MVP FAIL — 等用户决策：终止 or Pivot**

### 最终实验结果

**Claude Sonnet 4（强模型，14 实例 × 4 条件）：**
| 指标 | no_trace | line | structural | full_trace |
|------|----------|------|------------|------------|
| test_pass | **42.9%** | 42.9% | 35.7% | 28.6% |
| diff_apply | **85.7%** | 71.4% | 64.3% | 57.1% |
| judge | **1.3** | 1.1 | 1.0 | 1.0 |

三项指标 no_trace 全部最优。Trace 不仅无帮助，更多 trace = 更差（full_trace 最差）。

**C001 Kill Criteria：2/3 FAIL → MVP FAIL（D019 约定，不再消歧）**

### 关键发现
1. 强模型不在 floor（42.9% test_pass），但 trace 无正向效果
2. full_trace 显著伤害修复（42.9% → 28.6%）：trace 是噪声而非信号
3. v4-pro 的微弱正向信号是 floor effect artifact——模型太弱时所有条件都在猜，trace 偶然帮忙
4. structural filtering 选错信息（scrapy_7：no_trace 通过但 structural 失败）
5. Judge 指标不可靠（功能正确的修复仍得 1/5），但不影响 test_pass 结论

### 用户决策选项
1. **终止项目** — 核心假设被否定，归档实验数据
2. **Pivot Option A: Fault Localization** — trace 不直接帮修复，但可能帮定位 bug（换研究问题）
3. **Pivot Option B: Trace Compression** — 从 binary filter 转向智能压缩（但 full_trace 最差说明 trace 本身可能就是噪声）
4. **其他方向** — 用户提出

### v2 实验（deepseek-v4-pro）
PID 131777 仍在运行（10/14），继续跑完收集完整数据但不影响 MVP 判定。

## GPU 预算
本项目分配：rtx6000-diagprobe cuda:0 + cuda:1
当前状态：两张卡均空闲（实验为 API-only）。如项目终止，GPU 可释放给其他项目。

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D033 | 2026-05-15 | MVP FAIL：强模型消歧（Claude Sonnet 4）确认 trace filtering  | mvp_strong_model_disambig, mvp_phase3_repair_v2 |
| D032 | 2026-05-15 | 修正 D028 稀释假说：Tier 1 仅 httpie_2 structural_keep=0（1 | mvp_phase3_repair_v2 |
| D031 | 2026-05-15 | 批准强模型消歧实验（Claude Sonnet 4）：单例验证 cookiecutter_1/no_ | mvp_phase3_repair_v2, mvp_strong_model_disambig |
| D030 | 2026-05-15 | 第三次修正 v2 进程误判：PID 131777 仍活跃（API retry backoff），建立 | mvp_phase3_repair_v2 |
| D029 | 2026-05-15 | 修正 D028 "重启 v2" 指令：PID 131777 仍在运行（第三次误判死亡），撤销重启。建 | mvp_phase3_repair_v2 |
| D028 | 2026-05-15 | v2 最终 9/14（进程在 scrapy_7 静默终止）。Trace 有正向信号但 structu | mvp_phase3_repair_v2 |
| D027 | 2026-05-15 | 修正 D024"各条件无差异"：v2 9/14 数据显示 trace 有正向信号（structura | mvp_phase3_repair_v2 |
| D026 | 2026-05-15 | 修正 on_complete 误触发：registry 从 ANALYZING 改回 RUNNING | mvp_phase3_repair_v2 |
| D025 | 2026-05-15 | 修正 D024：v2 实验未崩溃（PID 131777 仍活跃），等 14/14 完成再评估 C00 | mvp_phase3_repair_v2 |
| D024 | 2026-05-15 | v2 实验（deepseek-v4-pro）强烈负面信号：judge 0.6/5、0% test p | mvp_phase3_repair_v2, mvp_phase3_repair |


