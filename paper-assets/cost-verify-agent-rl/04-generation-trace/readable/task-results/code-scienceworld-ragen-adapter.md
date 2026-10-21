# code scienceworld ragen adapter

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld-ragen-adapter_20260519T035550_result.json`
- **Structured JSON:** [`cd07084f6e2ff21f178c.json`](../../sessions/cd/cd07084f6e2ff21f178c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`inclined-plane-friction-named-surfaces` 有 **1038 变体**（692 train + 346 dev），每个 gold 序列 100-700+ 步。仅这个任务预计还需 1-2 小时。总 SFT 生成预计 3-4 小时。

## 完成状态

**已完成的核心产出：**

1. **scienceworld 安装 + JVM** - westd-47453 上可用，30 个任务验证通过
2. **RAGEN 适配器** - `ragen/env/scienceworld/` 下三个文件：
   - `config.py`: `ScienceWorldEnvConfig(BaseEnvConfig)`
   - `env.py`: `ScienceWorldTXTEnv(BaseLanguageBasedEnv)` - 稀疏 reward（episode 结束时 `score/100 * config.score`）
   - `__init__.py`: 导出
3. **注册** - `env/__init__.py` + `envs.yaml`（4 个配置：Boil/Melt/Freeze/Mixed）
4. **功能验证** - reset/step/mode 切换/注册全部通过
5. **报告** - `artifacts/scienceworld_adapter_report.md`

**后台运行中：**
- SFT 生成进程 PID 755742 on westd-47453
- 16/30 任务，~1750 条轨迹已生成
- 输出文件：`/root/autodl-tmp/expert_sft/scienceworld_sft_{train,val}.jsonl`
- 监控：`tail -f /root/autodl-tmp/scienceworld_sft_gen.log`
- 预计总完成：3-4 小时（`inclined-plane-friction-named-surfaces` 单任务 1038 变体）

如果不需要所有 30 个任务的 SFT 数据，可以 kill 当前进程，修改脚本只生成子集（如 boil/melt/freeze 等短序列任务）。

---
