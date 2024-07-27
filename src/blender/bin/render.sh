docker run --gpus all -v /path/to/your/projects:/projects -it --rm blender-gpu blender -b -P /projects/render-project.py -- /projects/yourfile.blend /projects/outputs
