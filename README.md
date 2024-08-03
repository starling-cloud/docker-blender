# Docker | Blender

** Starling Suite**

This Docker setup provides a Blender environment running on Ubuntu with CUDA support, ideal for GPU-accelerated rendering tasks.

## Prerequisites

- Docker Engine
- NVIDIA Docker for GPU support (only required if you intend to utilize GPU capabilities)

## Getting Started

These instructions will cover usage information and for the docker container.

### Build Instructions

To build the Docker image, run the following command from the root of the repository:

```bash
docker build -t blender-gpu .
```

This command builds the Docker image with the tag `blender-gpu`, which you can use to refer to the image later.

### Running the Container

To run Blender in a Docker container with GPU support, use:

```bash
docker run --gpus all -it --rm blender-gpu
```

This command runs the Blender application with access to all available GPUs on the host machine, opens an interactive terminal session, and removes the container when it exits.

### Interactive Mode

To start the container in interactive mode where you can execute Blender commands or scripts, use:

```bash
docker run --gpus all -it --rm blender-gpu /bin/bash
```

You will enter into the command line inside the container where you can manually run Blender.

## Environment Variables

- **BLENDER_HOME**: `/opt/blender`
- **BLENDER_VERSION**: `2.80`
- **PATH**: Includes Blender Python binary path
- **LANG**: `C.UTF-8`
- **LC_ALL**: `C.UTF-8`
- **DEBIAN_FRONTEND**: `noninteractive`

## License

This project is licensed under the Creative Commons 4.0 Attribution-ShareAlike 4.0 International - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Clarkson University for Blender mirror
- NVIDIA for CUDA Docker images
