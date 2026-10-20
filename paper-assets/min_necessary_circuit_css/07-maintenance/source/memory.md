# Memory — min_necessary_circuit_css

## GPU 越界教训 (2026-05-13)

第三次 GPU 越界事件：PID 897752 占用 cuda:0（属于 rl-active-probe-fl），导致对方数据丢失。根因：旧进程或直接运行库模块时未设 CUDA_VISIBLE_DEVICES，torch 默认使用 cuda:0。

**硬规则**：
- 项目只有 cuda:5@cqa1-21977，所有 .py 文件（含库模块）必须在 import torch 前用 `os.environ.setdefault("CUDA_VISIBLE_DEVICES", "5")` 防护
- 入口脚本用 `os.environ["CUDA_VISIBLE_DEVICES"] = "5"`（强制覆盖），库模块用 `setdefault`（不覆盖入口已设的值）
- Worker 提交实验必须用 submit_training_job（自动管理 CUDA_VISIBLE_DEVICES），禁止 nohup

## ACDC isinf 退化——核心方法论问题 (2026-05-13)

ACDC binarization 用 `isinf` 只选出极少边（IOI 14, Arithmetic 17），但 ACDC 实际有 0.03-0.09 四级中间分数。isinf 导致 CSS=1.0 与 ACDC 完全重合，跨方法共识退化。top-k binarization（k=50-75）解决此问题：Arithmetic CSS 3/3 从 17→44-54。

**但 top-k 未翻转条件④**：CSS=1.0 mean CPR=0.919 < EAP-IG=0.985。

## D021: CSS-only 叙事 (2026-05-13)

放弃 CIRCUS 作为独立 claim。转 CSS-only 叙事。

## 竞争定位：CSS vs CIRCUS (2026-05-13)

- **CIRCUS (Parekh, 2026)** 最大竞争对手。CSS 差异化 = method diversity > threshold diversity
- **Mondorf et al.** direct competitor：仅 gradient 族、score averaging（非 binary consensus）
- 关键支撑：Miller et al. (COLM 2024) faithfulness 对消融敏感；Méloux et al. EAP/EAP-IG 高方差

## D026: MVP Gate 最终结论 (2026-05-13)

**Arithmetic 条件④ FAIL（CSS=1.0 < EAP-IG），IOI PASS。**

关键教训：
1. **Zero ablation 是 artifact 源**——所有小电路 zero CPR 为负，mean ablation 翻正到 0.9+
2. **节点级 ablation 的局限**——CSS=1.0 CPR 在 k=50→75 不变（节点集相同，边数变化无法区分）
3. **EAP-IG×EP 在 arithmetic 上 Jaccard=0.695**——两方法高度一致，CSS 缺少第三方视角的信息增益
4. **IOI 上 CSS 边效率极高**——14 edges CPR≈50 edges 单方法，每条边贡献远超单方法
5. **IOI CPR 不一致是误报**——mean_ablation_results.json 中标注为 IOI 的数据实际是 Arithmetic

**等待 Director 决策：edge-efficiency claim / 原 claim + 更多任务 / pivot。**

## IFR 作为第三方法——已证伪 (2026-05-13)

**phase2_qwen05b_ioi_k3 (negative)**: Qwen-2.5 0.5B 上 IFR 与 EAP-IG/EP 的 Jaccard = 0.00。

**D028 诊断结论**:
1. **Per-head 分解无效**: IFR 已经在用 per-head 分解，不是修复方向
2. **根本原因**: IFR (proximity) 度量 activation magnitude → 偏向高幅度 MLP 输出 (m2, m20, m22)；gradient 方法度量 causal influence → 偏向任务关键 attention heads (a20.h9)。两者解构的是不同维度
3. **Jaccard sweep**: 首次非零在 N=500 (J=0.045)，unique_score_rank 展开到 2191 边也仅 J=0.065
4. **Destination-side 退化 100%**: 同层头共享 residual stream，所有头得到相同 destination score

**结论**: IFR 不能作为 CSS 第三方法用于大模型。gradient 族内部仍有共识（EAP-IG×EP Jaccard=0.54）。Phase 2 需要替代第三方法（ACDC top-k 或另一个 gradient 方法）。
