"""Patch eval_safelibero.py with 3 fixes."""
import sys

path = "/root/colliforce-vla/scripts/eval_safelibero.py"
with open(path, "r") as f:
    content = f.read()

original = content

# === Fix 3: Replace hardcoded OBSTACLE_NAMES with per-suite mapping ===
old_obstacle = '''OBSTACLE_NAMES = [
    "moka_pot_obstacle_1",
    "white_storage_box_obstacle_1",
    "milk_obstacle_1",
    "wine_bottle_obstacle_1",
    "red_coffee_mug_obstacle_1",
    "yellow_book_obstacle_1",
]'''

new_obstacle = '''OBSTACLE_NAMES_DEFAULT = [
    "moka_pot_obstacle_1",
    "white_storage_box_obstacle_1",
    "milk_obstacle_1",
    "wine_bottle_obstacle_1",
    "red_coffee_mug_obstacle_1",
    "yellow_book_obstacle_1",
]

OBSTACLE_NAMES_LONG = [
    "moka_pot_small_obstacle_1",
    "white_storage_box_obstacle_1",
    "milk_small_obstacle_1",
    "wine_bottle_small_obstacle_1",
    "red_coffee_mug_obstacle_1",
    "yellow_book_obstacle_1",
]

SUITE_OBSTACLE_NAMES = {
    "safelibero_spatial": OBSTACLE_NAMES_DEFAULT,
    "safelibero_object": OBSTACLE_NAMES_DEFAULT,
    "safelibero_goal": OBSTACLE_NAMES_DEFAULT,
    "safelibero_long": OBSTACLE_NAMES_LONG,
}'''

content = content.replace(old_obstacle, new_obstacle)

# === Fix 1 + Fix 2: Add --no_refine, --collision_threshold, --verify_obstacles to argparse ===
old_parse_end = '''    parser.add_argument("--refine_margin", type=float, default=0.01,
                        help="A3 SDF threshold below which refinement activates")
    return parser.parse_args()'''

new_parse_end = '''    parser.add_argument("--refine_margin", type=float, default=0.01,
                        help="A3 SDF threshold below which refinement activates")
    parser.add_argument("--no_refine", action="store_true",
                        help="A3: disable inference-time SDF gradient refinement (evaluate training effect only)")
    parser.add_argument("--collision_threshold", type=float, default=COLLISION_THRESHOLD,
                        help="Obstacle displacement threshold (m) for collision detection (default: 0.001)")
    parser.add_argument("--verify_obstacles", action="store_true",
                        help="Print MuJoCo body names and verify obstacle coverage, then exit")
    return parser.parse_args()'''

content = content.replace(old_parse_end, new_parse_end)

# === Fix 1: In evaluate_task, skip refinement when --no_refine ===
old_refine_block = '            # A3: inference-time SDF gradient refinement\n            if args.model_type == "a3" and sdf_decoder is not None and suffix_hook is not None:'

new_refine_block = '            # A3: inference-time SDF gradient refinement\n            if args.model_type == "a3" and sdf_decoder is not None and suffix_hook is not None and not args.no_refine:'

content = content.replace(old_refine_block, new_refine_block)

# === A3 --no_refine: still log SDF values (like A1 does) ===
old_a1_block = '            # A1: optional SDF prediction logging (no action modification)\n            elif args.model_type == "a1" and sdf_decoder is not None and suffix_hook is not None:'

new_a1_block = '            # A1 (or A3 --no_refine): SDF prediction logging without action modification\n            elif (args.model_type == "a1" or (args.model_type == "a3" and args.no_refine)) and sdf_decoder is not None and suffix_hook is not None:'

content = content.replace(old_a1_block, new_a1_block)

# === Fix 3: In evaluate_task, use suite-specific obstacle names ===
old_obstacle_ref = '        initial_positions = get_obstacle_positions(env.sim, OBSTACLE_NAMES)'
new_obstacle_ref = '        obstacle_names = SUITE_OBSTACLE_NAMES.get(args.suite, OBSTACLE_NAMES_DEFAULT)\n        initial_positions = get_obstacle_positions(env.sim, obstacle_names)'
content = content.replace(old_obstacle_ref, new_obstacle_ref)

# Replace OBSTACLE_NAMES in collision check loop with obstacle_names + collision_threshold
content = content.replace(
    '                current_positions = get_obstacle_positions(env.sim, OBSTACLE_NAMES)\n                hit, hit_name, displacement = check_collision(\n                    initial_positions, current_positions\n                )',
    '                current_positions = get_obstacle_positions(env.sim, obstacle_names)\n                hit, hit_name, displacement = check_collision(\n                    initial_positions, current_positions, threshold=args.collision_threshold\n                )'
)

# Replace OBSTACLE_NAMES in max_displacement loop
content = content.replace(
    '            current_positions = get_obstacle_positions(env.sim, OBSTACLE_NAMES)\n            for name in initial_positions:',
    '            current_positions = get_obstacle_positions(env.sim, obstacle_names)\n            for name in initial_positions:'
)

# === Fix 1: Add refine_enabled to output JSON ===
old_output_a3 = '''    # A3: include refinement config
    if args.model_type == "a3":
        output["config"]["refine_alpha"] = args.refine_alpha
        output["config"]["refine_margin"] = args.refine_margin
        output["config"]["sdf_gt_path"] = args.sdf_gt_path'''

new_output_a3 = '''    # A3: include refinement config
    if args.model_type == "a3":
        output["config"]["refine_enabled"] = not args.no_refine
        output["config"]["refine_alpha"] = args.refine_alpha
        output["config"]["refine_margin"] = args.refine_margin
        output["config"]["sdf_gt_path"] = args.sdf_gt_path'''

content = content.replace(old_output_a3, new_output_a3)

# === Fix 2: Add collision_threshold to output JSON ===
old_config_block = '        "results": all_results,'
new_config_block = '        "collision_threshold": args.collision_threshold,\n        "results": all_results,'
content = content.replace(old_config_block, new_config_block)

# === Fix 3: Add --verify_obstacles handler in main() ===
old_main_run = '    # --- Run evaluation ---\n    logging.info("Setting up SafeLIBERO benchmark: %s (level %s)", args.suite, args.safety_level)'

new_main_run = '''    # --- Verify obstacles mode ---
    if args.verify_obstacles:
        from libero.libero.benchmark import get_benchmark as _get_bm
        bm_cls = _get_bm(args.suite)
        bm = bm_cls(task_order_index=0, safety_level=args.safety_level)
        _tid = args.task_id if args.task_id is not None else 0
        _task = bm.get_task(_tid)
        _bddl = bm.get_task_bddl_file_path(_tid)
        from libero.libero.envs import OffScreenRenderEnv as _Env
        _env = _Env(bddl_file_name=_bddl, camera_heights=224, camera_widths=224)
        _env.reset()
        _init = bm.get_task_init_states(_tid)
        _env.set_init_state(_init[0])
        for _ in range(5):
            _env.step(np.zeros(7))
        all_bodies = [_env.sim.model.body_id2name(i) for i in range(_env.sim.model.nbody)]
        obs_in_sim = [b for b in all_bodies if "obstacle" in b]
        expected = SUITE_OBSTACLE_NAMES.get(args.suite, OBSTACLE_NAMES_DEFAULT)
        print(f"Suite: {args.suite}, Task: {_tid}")
        print(f"\\nAll bodies with 'obstacle': {obs_in_sim}")
        print(f"\\nExpected OBSTACLE_NAMES: {expected}")
        matched = [n for n in expected if any(n in b for b in obs_in_sim)]
        missing = [n for n in expected if n not in matched]
        extra = [b for b in obs_in_sim if not any(n in b for n in expected)]
        print(f"\\nMatched: {matched}")
        if missing:
            print(f"MISSING (in expected but not in sim): {missing}")
        if extra:
            print(f"EXTRA (in sim but not in expected): {extra}")
        _env.close()
        return

    # --- Run evaluation ---
    logging.info("Setting up SafeLIBERO benchmark: %s (level %s)", args.suite, args.safety_level)'''

content = content.replace(old_main_run, new_main_run)

# Verify all patches applied
checks = [
    ("--no_refine", "no_refine" in content),
    ("--collision_threshold", "collision_threshold" in content),
    ("--verify_obstacles", "verify_obstacles" in content),
    ("SUITE_OBSTACLE_NAMES", "SUITE_OBSTACLE_NAMES" in content),
    ("OBSTACLE_NAMES_LONG", "OBSTACLE_NAMES_LONG" in content),
    ("refine_enabled", "refine_enabled" in content),
    ("not args.no_refine", "not args.no_refine" in content),
    ("obstacle_names local var", "obstacle_names = SUITE_OBSTACLE_NAMES" in content),
    ("threshold=args.collision_threshold", "threshold=args.collision_threshold" in content),
]

all_ok = True
for name, ok in checks:
    status = "OK" if ok else "FAIL"
    print(f"  [{status}] {name}")
    if not ok:
        all_ok = False

if not all_ok:
    print("\nSome patches failed! Not writing file.")
    sys.exit(1)

if content == original:
    print("\nNo changes made!")
    sys.exit(1)

with open(path, "w") as f:
    f.write(content)

print("\nAll patches applied successfully.")
