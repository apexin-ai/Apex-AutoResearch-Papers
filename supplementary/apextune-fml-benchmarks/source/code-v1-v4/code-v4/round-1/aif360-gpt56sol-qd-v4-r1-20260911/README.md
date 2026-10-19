# ApexTune AIF360 trajectory: aif360-gpt56sol-qd-v4-r1-20260911

- Code version: `code-v4`
- Experiment round: `1`
- Search strategy: `qd-v4-behaviour-frontier-stall-restart-pool-batch-bandit`
- Strategy meaning: Behaviour-axis QD frontier (abs_aod_mean x cls_acc_mean absolute bins) with stall-driven tune cooldown and alternating seed/uniform restart draws, epsilon-band elite pools sampled as parents, and one decomposed bandit observation per batch decision.
- Model: `OpenAI/gpt-5.6-sol`
- Protocol: `diagnostic`; comparable=`false`; leaderboard eligible=`false`
- LLM structure requests: `111`
- Reserved requests without a durable terminal record: `0`
- Validated structures: `91`
- Generation-failed structures: `20`
- Full validation steps: `100`
- Default structure validations: `91`
- HPO variant validations: `9`
- Stall batch decisions / cooldown batches: `39` / `15`
- Restart draws: `{'seed': 4, 'uniform_cell': 3}`
- Pool parent draws / pooled steps: `7` / `25`
- Final normalized score: `0.2287421027577004`
- Final absolute AOD: `0.011120493106355073`
- Final accuracy: `0.6429215509467989`

`APEXTUNE_STRUCTURE_INDEX.jsonl` has one row for every logical LLM request, including failed generation requests. `APEXTUNE_VALIDATION_TRAJECTORY.jsonl` has one row for every full validation. Rows sharing an `apextune_structure_id` belong to the same LLM-proposed code structure; `variant_kind=hpo_variant` marks local parameter variants of that structure. On `code-v4` rows, `admission_kind` labels the archive outcome (new_cell / displaced_elite / pooled / rejected) and `pooled=true` marks near-best variants retained by the epsilon-band elite pool. Requests reserved before a process interruption but lacking a durable terminal record are retained with `status=missing` and are not counted as successful or failed generations.
