import bpy
import sys
import os

def render_blender_file(blend_file_path, output_dir, resolution_x=1920, resolution_y=1080, frame_start=None, frame_end=None):
    """
    Renders a Blender file with specified output settings.

    Args:
    blend_file_path (str): Path to the .blend file.
    output_dir (str): Directory where rendered images will be saved.
    resolution_x (int): Width of the rendered image.
    resolution_y (int): Height of the rendered image.
    frame_start (int): Starting frame for rendering (optional).
    frame_end (int): Ending frame for rendering (optional).
    """

    # Load the Blender file
    bpy.ops.wm.open_mainfile(filepath=blend_file_path)

    # Set render resolution
    bpy.context.scene.render.resolution_x = resolution_x
    bpy.context.scene.render.resolution_y = resolution_y
    bpy.context.scene.render.resolution_percentage = 100

    # Set render output path
    bpy.context.scene.render.filepath = os.path.join(output_dir, "render")

    # Set the format of the output
    bpy.context.scene.render.image_settings.file_format = 'JPEG'  # Can change to PNG, TIFF, etc.

    # Set frame start and end
    if frame_start is not None:
        bpy.context.scene.frame_start = frame_start
    if frame_end is not None:
        bpy.context.scene.frame_end = frame_end

    # Render the scene
    bpy.ops.render.render(animation=True)

if __name__ == "__main__":
    # Expecting sys.argv[1] to be path to .blend file and sys.argv[2] to be output directory
    if len(sys.argv) < 4:
        print("Usage: blender -b -P this_script.py -- [path_to_blend_file] [output_directory]")
        sys.exit(1)

    blend_file_path = sys.argv[-2]
    output_dir = sys.argv[-1]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    render_blender_file(blend_file_path, output_dir)
