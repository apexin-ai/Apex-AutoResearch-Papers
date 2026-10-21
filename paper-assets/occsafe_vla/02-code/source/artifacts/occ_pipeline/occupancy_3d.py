import numpy as np

GEOM_PLANE = 0
GEOM_HFIELD = 1
GEOM_SPHERE = 2
GEOM_CAPSULE = 3
GEOM_ELLIPSOID = 4
GEOM_CYLINDER = 5
GEOM_BOX = 6
GEOM_MESH = 7


def _make_grid_points(grid_origin, grid_extent, resolution):
    axes = []
    for d in range(3):
        step = grid_extent[d] / resolution
        axes.append(
            np.linspace(
                grid_origin[d] + step / 2,
                grid_origin[d] + grid_extent[d] - step / 2,
                resolution,
            )
        )
    xx, yy, zz = np.meshgrid(axes[0], axes[1], axes[2], indexing="ij")
    points = np.stack([xx.ravel(), yy.ravel(), zz.ravel()], axis=-1)
    return points, (resolution, resolution, resolution)


def _world_to_local(points, geom_pos, geom_mat):
    mat = geom_mat.reshape(3, 3)
    diff = points - geom_pos[np.newaxis, :]
    local = diff @ mat
    return local


def _point_in_box(local, size):
    return np.all(np.abs(local) <= size[np.newaxis, :], axis=-1)


def _point_in_sphere(local, size):
    r = size[0]
    return np.sum(local ** 2, axis=-1) <= r * r


def _point_in_cylinder(local, size):
    r, h = size[0], size[1]
    xy_dist2 = local[:, 0] ** 2 + local[:, 1] ** 2
    return (xy_dist2 <= r * r) & (np.abs(local[:, 2]) <= h)


def _point_in_capsule(local, size):
    r, h = size[0], size[1]
    r2 = r * r
    xy_dist2 = local[:, 0] ** 2 + local[:, 1] ** 2
    z = local[:, 2]
    in_cyl = (xy_dist2 <= r2) & (np.abs(z) <= h)
    top_d2 = xy_dist2 + (z - h) ** 2
    in_top = (z > h) & (top_d2 <= r2)
    bot_d2 = xy_dist2 + (z + h) ** 2
    in_bot = (z < -h) & (bot_d2 <= r2)
    return in_cyl | in_top | in_bot


def _point_in_ellipsoid(local, size):
    scaled = local / size[np.newaxis, :]
    return np.sum(scaled ** 2, axis=-1) <= 1.0


def _get_mesh_aabb(model, geom_id):
    """Get mesh AABB half-sizes in local frame for fast box approximation."""
    raw = model._model if hasattr(model, '_model') else model
    mesh_id = raw.geom_dataid[geom_id]
    if mesh_id < 0:
        return None
    vert_start = raw.mesh_vertadr[mesh_id]
    vert_count = raw.mesh_vertnum[mesh_id]
    vertices = raw.mesh_vert[vert_start : vert_start + vert_count]
    half_sizes = np.max(np.abs(vertices), axis=0)
    return half_sizes


def build_occupancy_3d(sim, grid_origin, grid_extent, resolution, geom_class_map):
    model = sim.model
    data = sim.data

    points, shape = _make_grid_points(grid_origin, grid_extent, resolution)
    n_pts = points.shape[0]

    semantic = np.zeros(n_pts, dtype=np.uint8)
    binary = np.zeros(n_pts, dtype=bool)

    mesh_aabb_cache = {}

    for geom_id, sem_class in geom_class_map.items():
        geom_type = model.geom_type[geom_id]
        geom_size = model.geom_size[geom_id]
        geom_pos = data.geom_xpos[geom_id]
        geom_mat = data.geom_xmat[geom_id]

        if geom_type == GEOM_BOX:
            bound_r = np.linalg.norm(geom_size)
        elif geom_type == GEOM_SPHERE:
            bound_r = geom_size[0]
        elif geom_type == GEOM_CYLINDER:
            bound_r = np.sqrt(geom_size[0] ** 2 + geom_size[1] ** 2)
        elif geom_type == GEOM_CAPSULE:
            bound_r = geom_size[0] + geom_size[1]
        elif geom_type == GEOM_ELLIPSOID:
            bound_r = np.max(geom_size)
        elif geom_type == GEOM_MESH:
            if geom_id not in mesh_aabb_cache:
                mesh_aabb_cache[geom_id] = _get_mesh_aabb(model, geom_id)
            aabb = mesh_aabb_cache[geom_id]
            if aabb is None:
                continue
            bound_r = np.linalg.norm(aabb)
        else:
            continue

        dists = np.linalg.norm(points - geom_pos[np.newaxis, :], axis=-1)
        candidate_mask = dists <= bound_r * 1.05
        if not np.any(candidate_mask):
            continue

        candidate_pts = points[candidate_mask]
        local = _world_to_local(candidate_pts, geom_pos, geom_mat)

        if geom_type == GEOM_BOX:
            inside = _point_in_box(local, geom_size)
        elif geom_type == GEOM_SPHERE:
            inside = _point_in_sphere(local, geom_size)
        elif geom_type == GEOM_CYLINDER:
            inside = _point_in_cylinder(local, geom_size)
        elif geom_type == GEOM_CAPSULE:
            inside = _point_in_capsule(local, geom_size)
        elif geom_type == GEOM_ELLIPSOID:
            inside = _point_in_ellipsoid(local, geom_size)
        elif geom_type == GEOM_MESH:
            aabb = mesh_aabb_cache[geom_id]
            inside = _point_in_box(local, aabb)
        else:
            continue

        hit_indices = np.where(candidate_mask)[0][inside]
        binary[hit_indices] = True
        upgrade_mask = semantic[hit_indices] < sem_class
        semantic[hit_indices[upgrade_mask]] = sem_class

    semantic = semantic.reshape(shape)
    binary = binary.reshape(shape)

    return semantic, binary
