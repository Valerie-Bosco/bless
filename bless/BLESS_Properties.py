import bpy


class BLESS_PG_SessionProperties(bpy.types.PropertyGroup):
    b_show_tool_box: bpy.props.BoolProperty()  # type:ignore

    b_show_object_data: bpy.props.BoolProperty()  # type:ignore
    b_show_collision_settings: bpy.props.BoolProperty()  # type:ignore


class BLESS_PG_ObjectCollisionSettings(bpy.types.PropertyGroup):
    collision_types: bpy.props.EnumProperty(
        name="Collision Type",
        description="Static level geometry.",
        default="trimesh",
        items=[
            ("trimesh", "Trimesh", "", 1),
            ("convex", "Convex", "", 1 << 1),
            ("custom", "Custom", "", 1 << 2),
            ("none", "None", "", 1 << 3),
        ])  # type: ignore

    layers = [(f"LAYER_{n}", f"{n}", "") for n in range(32)]
    collision_layers: bpy.props.EnumProperty(name="Collision Layers", options={"ENUM_FLAG"}, items=layers)  # type:ignore

    mask_layers = [(f"LAYER_{n}", f"{n}", "") for n in range(32)]
    collision_mask_layers: bpy.props.EnumProperty(name="Collision Mask Layers", options={"ENUM_FLAG"}, items=mask_layers)  # type:ignore


# Default collision type for new objects.
class BLESS_PG_DefaultCollisionType(bpy.types.PropertyGroup):
    collision_types: bpy.props.EnumProperty(
        name="Collision Type",
        description="Static level geometry.",
        default="trimesh",
        items=[
            ("trimesh", "Trimesh", "", 1),
            ("convex", "Convex", "", 1 << 1),
            ("custom", "Custom", "", 1 << 2),
            ("none", "None", "", 1 << 3),
        ])  # type: ignore
