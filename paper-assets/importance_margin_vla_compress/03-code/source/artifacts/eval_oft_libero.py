"""OFT baseline eval on LIBERO — aligned with official run_libero_eval.py."""
import sys, os, math, json, time, argparse
from collections import deque

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import torch
import torch.nn as nn
from PIL import Image
import tensorflow as tf

CKPT = '/root/autodl-tmp/openvla-oft-libero-object'
ACTION_DIM = 7
NUM_ACTIONS_CHUNK = 8
PROPRIO_DIM = 8
TASK_MAX_STEPS = {
    'libero_spatial': 220,
    'libero_object': 280,
    'libero_goal': 300,
    'libero_10': 520,
    'libero_90': 400,
}
NUM_STEPS_WAIT = 10
DUMMY_ACTION = [0, 0, 0, 0, 0, 0, -1]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--suite', default='libero_object')
    p.add_argument('--gpu', type=int, default=2)
    p.add_argument('--seed', type=int, default=42)
    p.add_argument('--num_trials', type=int, default=50)
    p.add_argument('--task_ids', type=str, default=None,
                   help='Comma-separated task IDs, e.g. "0" or "0,1,2". None=all tasks.')
    p.add_argument('--dry_run', action='store_true',
                   help='Quick diagnostic: 5 episodes on task 0 with detailed logging')
    return p.parse_args()


# ===== Neural network modules =====
class MLPResNetBlock(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.ffn = nn.Sequential(nn.LayerNorm(dim), nn.Linear(dim, dim), nn.ReLU())
    def forward(self, x):
        return self.ffn(x) + x

class MLPResNet(nn.Module):
    def __init__(self, num_blocks, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.layer_norm1 = nn.LayerNorm(input_dim)
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.mlp_resnet_blocks = nn.ModuleList([MLPResNetBlock(hidden_dim) for _ in range(num_blocks)])
        self.layer_norm2 = nn.LayerNorm(hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
    def forward(self, x):
        x = self.relu(self.fc1(self.layer_norm1(x)))
        for b in self.mlp_resnet_blocks:
            x = b(x)
        return self.fc2(self.layer_norm2(x))

class L1RegressionActionHead(nn.Module):
    def __init__(self, input_dim=4096, hidden_dim=4096, action_dim=7):
        super().__init__()
        self.action_dim = action_dim
        self.model = MLPResNet(num_blocks=2, input_dim=input_dim*ACTION_DIM,
                               hidden_dim=hidden_dim, output_dim=action_dim)
    def predict_action(self, actions_hidden_states):
        batch_size = actions_hidden_states.shape[0]
        rearranged = actions_hidden_states.reshape(batch_size, NUM_ACTIONS_CHUNK, -1)
        return self.model(rearranged)

class ProprioProjector(nn.Module):
    def __init__(self, llm_dim, proprio_dim):
        super().__init__()
        self.fc1 = nn.Linear(proprio_dim, llm_dim, bias=True)
        self.fc2 = nn.Linear(llm_dim, llm_dim, bias=True)
        self.act_fn1 = nn.GELU()
    def forward(self, proprio):
        return self.fc2(self.act_fn1(self.fc1(proprio)))


# ===== Image preprocessing (matches official TF pipeline) =====
def resize_image_for_policy(img, resize_size=224):
    img_tf = tf.image.encode_jpeg(img)
    img_tf = tf.io.decode_image(img_tf, expand_animations=False, dtype=tf.uint8)
    img_tf = tf.image.resize(img_tf, (resize_size, resize_size), method='lanczos3', antialias=True)
    img_tf = tf.cast(tf.clip_by_value(tf.round(img_tf), 0, 255), tf.uint8)
    return img_tf.numpy()

def center_crop_image(image, crop_scale=0.9):
    image_t = tf.convert_to_tensor(np.array(image))
    orig_dtype = image_t.dtype
    image_t = tf.image.convert_image_dtype(image_t, tf.float32)
    image_t = tf.expand_dims(image_t, axis=0)
    new_h = tf.clip_by_value(tf.sqrt(crop_scale), 0, 1)
    new_w = tf.clip_by_value(tf.sqrt(crop_scale), 0, 1)
    h_off = (1 - new_h) / 2
    w_off = (1 - new_w) / 2
    boxes = tf.reshape(tf.stack([h_off, w_off, h_off + new_h, w_off + new_w]), (1, 4))
    image_t = tf.image.crop_and_resize(image_t, boxes, tf.range(1), (224, 224))
    image_t = image_t[0]
    image_t = tf.clip_by_value(image_t, 0, 1)
    image_t = tf.image.convert_image_dtype(image_t, orig_dtype, saturate=True)
    return Image.fromarray(image_t.numpy()).convert('RGB')


# ===== Observation helpers =====
def quat2axisangle(quat):
    quat = quat.copy()
    if quat[3] > 1.0:
        quat[3] = 1.0
    elif quat[3] < -1.0:
        quat[3] = -1.0
    den = np.sqrt(1.0 - quat[3] * quat[3])
    if math.isclose(den, 0.0):
        return np.zeros(3)
    return (quat[:3] * 2.0 * math.acos(quat[3])) / den

def prepare_observation(obs):
    agentview = obs['agentview_image'][::-1, ::-1]
    wrist = obs['robot0_eye_in_hand_image'][::-1, ::-1]
    agentview_pil = center_crop_image(Image.fromarray(resize_image_for_policy(agentview, 224)))
    wrist_pil = center_crop_image(Image.fromarray(resize_image_for_policy(wrist, 224)))
    proprio = np.concatenate([
        obs['robot0_eef_pos'],
        quat2axisangle(obs['robot0_eef_quat']),
        obs['robot0_gripper_qpos'],
    ])
    return agentview_pil, wrist_pil, proprio

def normalize_proprio(proprio, norm_stats):
    mask = norm_stats.get('mask', np.ones_like(norm_stats['q01'], dtype=bool))
    p_high = np.array(norm_stats['q99'])
    p_low = np.array(norm_stats['q01'])
    return np.clip(
        np.where(mask, 2 * (proprio - p_low) / (p_high - p_low + 1e-8) - 1, proprio),
        -1.0, 1.0,
    )


# ===== Action post-processing =====
def normalize_gripper_action(action, binarize=True):
    action = action.copy()
    action[..., -1] = 2 * (action[..., -1] - 0.0) / (1.0 - 0.0) - 1
    if binarize:
        action[..., -1] = np.sign(action[..., -1])
    return action

def invert_gripper_action(action):
    action = action.copy()
    action[..., -1] *= -1.0
    return action

def process_action(action):
    action = normalize_gripper_action(action, binarize=True)
    action = invert_gripper_action(action)
    return action


# ===== Get action from model =====
def get_vla_action(model, processor, agentview_pil, wrist_pil, proprio_norm, task_label,
                   unnorm_key, action_head, proprio_projector, device):
    prompt = f"In: What action should the robot take to {task_label.lower()}?\nOut:"
    inputs = processor(prompt, agentview_pil).to(device, dtype=torch.bfloat16)
    wrist_inputs = processor(prompt, wrist_pil).to(device, dtype=torch.bfloat16)
    inputs['pixel_values'] = torch.cat([inputs['pixel_values'], wrist_inputs['pixel_values']], dim=1)

    with torch.inference_mode():
        action, _ = model.predict_action(
            **inputs,
            unnorm_key=unnorm_key,
            do_sample=False,
            proprio=proprio_norm,
            proprio_projector=proprio_projector,
            action_head=action_head,
        )
    return [action[i] for i in range(len(action))]


def set_seed_everywhere(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    import random
    random.seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    os.environ['PYTHONHASHSEED'] = str(seed)


def main():
    args = parse_args()
    if args.dry_run:
        args.task_ids = '0'
        args.num_trials = 5

    os.environ['CUDA_VISIBLE_DEVICES'] = str(args.gpu)
    DEVICE = torch.device('cuda:0')

    set_seed_everywhere(args.seed)

    # ===== Load model =====
    print('=== Loading model ===')
    from transformers import AutoModelForVision2Seq, AutoProcessor
    model = AutoModelForVision2Seq.from_pretrained(
        CKPT, torch_dtype=torch.bfloat16, trust_remote_code=True, low_cpu_mem_usage=True
    )
    model.vision_backbone.set_num_images_in_input(2)
    model = model.to(DEVICE).eval()
    processor = AutoProcessor.from_pretrained(CKPT, trust_remote_code=True)

    with open(os.path.join(CKPT, 'dataset_statistics.json')) as f:
        ds_stats = json.load(f)
    model.norm_stats.update(ds_stats)
    unnorm_key = f'{args.suite}_no_noops'
    assert unnorm_key in model.norm_stats, f'{unnorm_key} not in model.norm_stats'
    proprio_stats = ds_stats[unnorm_key]['proprio']

    llm_dim = model.language_model.config.hidden_size
    print(f'Model loaded: {type(model).__name__}, LLM dim={llm_dim}')

    # ===== Load action_head =====
    action_head = L1RegressionActionHead(input_dim=llm_dim, hidden_dim=llm_dim, action_dim=ACTION_DIM)
    ah_sd = torch.load(os.path.join(CKPT, 'action_head--150000_checkpoint.pt'), weights_only=True)
    ah_sd = {k.replace('module.', ''): v for k, v in ah_sd.items()}
    action_head.load_state_dict(ah_sd)
    action_head = action_head.to(torch.bfloat16).to(DEVICE).eval()
    print(f'action_head: {sum(p.numel() for p in action_head.parameters())/1e6:.1f}M params')

    # ===== Load proprio_projector =====
    pp = ProprioProjector(llm_dim=llm_dim, proprio_dim=PROPRIO_DIM)
    pp_sd = torch.load(os.path.join(CKPT, 'proprio_projector--150000_checkpoint.pt'), weights_only=True)
    pp_sd = {k.replace('module.', ''): v for k, v in pp_sd.items()}
    pp.load_state_dict(pp_sd)
    pp = pp.to(torch.bfloat16).to(DEVICE).eval()
    print(f'proprio_projector: {sum(p.numel() for p in pp.parameters())/1e6:.1f}M params')

    # ===== Set up LIBERO =====
    sys.path.insert(0, '/root/autodl-tmp/LIBERO')
    from libero.libero import get_libero_path, benchmark
    from libero.libero.envs import OffScreenRenderEnv

    bm = benchmark.get_benchmark_dict()[args.suite]()
    num_tasks = bm.n_tasks
    max_steps = TASK_MAX_STEPS[args.suite]

    if args.task_ids is not None:
        task_ids = [int(x) for x in args.task_ids.split(',')]
    else:
        task_ids = list(range(num_tasks))

    print(f'\nSuite: {args.suite}, max_steps={max_steps}, tasks={task_ids}, '
          f'trials/task={args.num_trials}, seed={args.seed}')

    # ===== Run eval =====
    total_episodes, total_successes = 0, 0
    results = {}

    for task_id in task_ids:
        task = bm.get_task(task_id)
        task_description = task.language
        task_bddl = os.path.join(get_libero_path('bddl_files'), task.problem_folder, task.bddl_file)
        env_args = {"bddl_file_name": task_bddl, "camera_heights": 256, "camera_widths": 256}
        env = OffScreenRenderEnv(**env_args)
        env.seed(0)
        init_states = bm.get_task_init_states(task_id)

        task_successes = 0
        print(f'\n--- Task {task_id}: {task_description} ---')

        for ep in range(args.num_trials):
            env.reset()
            obs = env.set_init_state(init_states[ep % len(init_states)])

            action_queue = deque(maxlen=NUM_ACTIONS_CHUNK)
            t = 0
            success = False
            ep_actions = []

            try:
                while t < max_steps + NUM_STEPS_WAIT:
                    if t < NUM_STEPS_WAIT:
                        obs, reward, done, info = env.step(DUMMY_ACTION)
                        t += 1
                        continue

                    if len(action_queue) == 0:
                        agentview_pil, wrist_pil, raw_proprio = prepare_observation(obs)
                        proprio_norm = normalize_proprio(raw_proprio, proprio_stats)
                        actions = get_vla_action(
                            model, processor, agentview_pil, wrist_pil, proprio_norm,
                            task_description, unnorm_key, action_head, pp, DEVICE,
                        )
                        action_queue.extend(actions)

                    action = action_queue.popleft()
                    if isinstance(action, torch.Tensor):
                        action = action.cpu().numpy()
                    action = process_action(action)

                    if args.dry_run and t < NUM_STEPS_WAIT + 16:
                        ep_actions.append(action.tolist())

                    obs, reward, done, info = env.step(action.tolist())
                    if done:
                        success = True
                        break
                    t += 1

            except Exception as e:
                print(f'  Episode {ep} error: {e}')

            if success:
                task_successes += 1
                total_successes += 1
            total_episodes += 1

            status = 'SUCCESS' if success else 'FAIL'
            print(f'  Ep {ep}: {status} (steps={t})')

            if args.dry_run and ep_actions:
                print(f'    First 2 action chunks:')
                for i, a in enumerate(ep_actions[:16]):
                    print(f'      step {i}: [{", ".join(f"{x:.4f}" for x in a)}]')

        env.close()
        task_sr = task_successes / args.num_trials
        results[task_id] = {'task': task_description, 'sr': task_sr,
                            'successes': task_successes, 'trials': args.num_trials}
        print(f'  Task {task_id} SR: {task_sr:.1%} ({task_successes}/{args.num_trials})')

    # ===== Summary =====
    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0
    print(f'\n{"="*60}')
    print(f'OVERALL: {overall_sr:.1%} ({total_successes}/{total_episodes})')
    for tid, r in results.items():
        print(f'  Task {tid} [{r["task"][:50]}]: {r["sr"]:.1%}')
    print(f'{"="*60}')

    out_path = f'/root/autodl-tmp/eval_results_{args.suite}_seed{args.seed}.json'
    with open(out_path, 'w') as f:
        json.dump({'overall_sr': overall_sr, 'total_successes': total_successes,
                   'total_episodes': total_episodes, 'tasks': results,
                   'args': vars(args)}, f, indent=2, default=str)
    print(f'Results saved to {out_path}')


if __name__ == '__main__':
    main()
