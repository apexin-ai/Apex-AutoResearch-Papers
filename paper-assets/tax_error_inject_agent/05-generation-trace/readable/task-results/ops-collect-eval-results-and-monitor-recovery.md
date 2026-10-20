# ops collect eval results and monitor recovery

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-eval-results-and-monitor-recovery_20260514T210128_result.json`
- **Structured JSON:** [`b0f0d1aaaa69fdd7e0ee.json`](../../sessions/b0/b0f0d1aaaa69fdd7e0ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。v4-taxei-recovery-eval 已完成（PID 87614 已退出）。

---

```
========================================================================
              v4 实验结果汇总 (valid_unseen, 47 episodes)
========================================================================

=== v4-random-seed0-eval (clean, random baseline) ===
Overall: 26/47 (55.3%)

Per-task-type:
  look_at_obj_in_light          5/6   (83.3%)
  pick_and_place_simple         4/8   (50.0%)
  pick_clean_then_place_in_recep 6/11  (54.5%)
  pick_cool_then_place_in_recep  4/7   (57.1%)
  pick_heat_then_place_in_recep  4/8   (50.0%)
  pick_two_obj_and_place         3/7   (42.9%)

Per-episode:
  ✓ AlarmClock-DeskLamp-308  ✗ Book-DeskLamp-308        ✓ Bowl-DeskLamp-308
  ✓ CD-DeskLamp-308          ✓ Mug-DeskLamp-308         ✓ Pencil-DeskLamp-308
  ✓ Mug-Desk-308             ✗ Pencil-Shelf-308         ✗ PepperShaker-Drawer-10
  ✗ SaltShaker-Cabinet-10    ✓ SaltShaker-Drawer-10     ✓ SoapBottle-Toilet-424
  ✓ Vase-Safe-219            ✗ Watch-Safe-219            ✓ Bowl-Cabinet-10
  ✗ Cloth-Cabinet-424        ✓ Cloth-CounterTop-424     ✓ Egg-Microwave-10
  ✗ Knife-CounterTop-10      ✓ Mug-CoffeeMachine-10    ✗ Pan-CounterTop-10
  ✗ Plate-CounterTop-10      ✓ SoapBar-Cabinet-424      ✓ SoapBar-CounterTop-424
  ✗ Spatula-Drawer-10        ✓ Bread-CounterTop-10      ✓ Lettuce-CounterTop-10
  ✓ Mug-Cabinet-10           ✓ Mug-CoffeeMachine-10    ✗ Pan-CounterTop-10
  ✗ Potato-Microwave-10      ✗ Tomato-Microwave-10      ✗ Apple-Fridge-10
  ✓ Apple-GarbageCan-10      ✓ Cup-Cabinet-10           ✗ Egg-GarbageCan-10
  ✓ Mug-Cabinet-10           ✓ Mug-CoffeeMachine-10    ✗ Potato-GarbageCan-10
  ✗ Tomato-GarbageCan-10     ✓ CD-Safe-308              ✗ KeyChain-Safe-219
  ✗ PepperShaker-Drawer-10   ✓ Pillow-Sofa-219          ✗ SoapBar-Cabinet-424
  ✓ SoapBar-GarbageCan-424   ✗ ToiletPaper-Cabinet-424

========================================================================

=== v4-taxei-seed0-eval (clean, taxei model) ===
Overall: 22/47 (46.8%)

Per-task-type:
  look_at_obj_in_light          5/6   (83.3%)
  pick_and_place_simple         3/8   (37.5%)  ↓ -12.5pp vs random
  pick_clean_then_place_in_recep 5/11  (45.5%)  ↓ -9.1pp
  pick_cool_then_place_in_recep  2/7   (28.6%)  ↓ -28.6pp
  pick_heat_then_place_in_recep  4/8   (50.0%)    same
  pick_two_obj_and_place         3/7   (42.9%)    same

Head-to-head vs random (taxei lost 4, gained 0):
  ✗ Vase-Safe-219 (random ✓)
  ✗ Cloth-CounterTop-424 (random ✓)
  ✗ Bread-CounterTop-10 (random ✓)
  ✗ Lettuce-CounterTop-10 (random ✓)

========================================================================

=== v4-vanilla-recovery-eval (recovery, vanilla model) ===
Overall: recovery_rate=29/47 (61.7%), detection_rate=0/47 (0.0%)

Per-operator:
  C1_context_truncation    9/12  (75.0%)  ← best
  C4_observation_masking   6/11  (54.5%)
  P1_step_order_swap       7/12  (58.3%)
  P2_sub_goal_deletion     7/12  (58.3%)

Per-task-type:
  look_at_obj_in_light          5/6   (83.3%)
  pick_and_place_simple         5/8   (62.5%)
  pick_clean_then_place_in_recep 5/11  (45.5%)
  pick_cool_then_place_in_recep  4/7   (57.1%)
  pick_heat_then_place_in_recep  6/8   (75.0%)
  pick_two_obj_and_place         4/7   (57.1%)

========================================================================

=== v4-taxei-recovery-eval (recovery, taxei model) ===
Status: COMPLETED (PID 87614 已退出)
Overall: recovery_rate=28/47 (59.6%), detection_rate=0/47 (0.0%)

Per-operator:
  C1_context_truncation    8/12  (66.7%)  ↓ -8.3pp vs vanilla
  C4_observation_masking   7/11  (63.6%)  ↑ +9.1pp vs vanilla
  P1_step_order_swap       7/12  (58.3%)    same
  P2_sub_goal_deletion     6/12  (50.0%)  ↓ -8.3pp

Per-task-type:
  look_at_obj_in_light          6/6  (100%)   ↑ +16.7pp vs vanilla
  pick_and_place_simple         4/8   (50.0%)  ↓ -12.5pp
  pick_clean_then_place_in_recep 6/11  (54.5%)  ↑ +9.1pp
  pick_cool_then_place_in_recep  3/7   (42.9%)  ↓ -14.3pp
  pick_heat_then_place_in_recep  7/8   (87.5%)  ↑ +12.5pp
  pick_two_obj_and_place         2/7   (28.6%)  ↓ -28.6pp

Head-to-head vs vanilla recovery (taxei gained 4, lost 5, net -1):
  Gained: Book-DeskLamp(P2), Mug-CoffeeMachine(C4), Spatula-Drawer(P1), Egg-GarbageCan(C4)
  Lost:   Watch-Safe(P2), Cloth-CounterTop(P1), Pan-CounterTop(P2),
          PepperShaker-Drawer(C1), Pillow-Sofa(C4)

========================================================================

=== 跨实验总结 ===

                        Clean SR    Recovery RR   Detection DR
  random baseline       55.3%       —             —
  taxei model           46.8%       —             —
  vanilla (w/ inject)   —           61.7%         0.0%
  taxei (w/ inject)     —           59.6%         0.0%

关键发现:
1. Clean eval: taxei 比 random 低 8.5pp (22 vs 26)，全部是单向损失
2. Recovery eval: taxei 比 vanilla 低 2.1pp (28 vs 29)，差异不大
3. 两个模型 detection_rate 均为 0 — 没有任何 error detection 能力
4. C1_context_truncation 在 vanilla 上恢复最好(75%)，C4 在 taxei 上恢复最好(63.6%)
5. pick_two_obj_and_place 在 taxei recovery 上表现最差(28.6%)
```

---
