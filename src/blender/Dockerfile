# syntax=docker/dockerfile:1.4


# Base Image
# =============================================================================

FROM ubuntu:24.04


# Environment variables
# =============================================================================

ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PATH="/usr/local/blender-2.80/python/bin:${PATH}" \
    BLENDER_VERSION="2.80" \
    BLENDER_HOME="/usr/local/blender-${BLENDER_VERSION}" \
    BLENDERPIP="${BLENDER_HOME}/python/bin/pip3" \
    BLENDERPY="${BLENDER_HOME}/python/bin/python3.7m" \
    HW="CPU"


# Install dependencies
# =============================================================================

RUN apt-get update && \
    apt-get install -y \
        wget \
        libopenexr-dev \
        bzip2 \
        build-essential \
        zlib1g-dev \
        libxmu-dev \
        libxi-dev \
        libxxf86vm-dev \
        libfontconfig1 \
        libxrender1 \
        libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*


# Download and install Blender
# =============================================================================

RUN wget https://mirror.clarkson.edu/blender/release/Blender2.80/blender-2.80-linux-glibc217-x86_64.tar.bz2 \ 
	&& tar -xjvf blender-2.80-linux-glibc217-x86_64.tar.bz2 --strip-components=1 -C /bin \ 
	&& rm -rf blender-2.80-linux-glibc217-x86_64.tar.bz2 \ 
	&& rm -rf blender-2.80-linux-glibc217-x86_64 

# RUN wget -qO- https://mirror.clarkson.edu/blender/release/Blender${BLENDER_VERSION}/blender-${BLENDER_VERSION}-linux-glibc217-x86_64.tar.bz2 \
#     | tar -xj --strip-components=1 -C ${BLENDER_HOME}


# Download the Python source since it is not bundled with Blender
# =============================================================================

RUN wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz \ 
	&& tar -xzf Python-3.7.0.tgz \ 
	&& cp -r Python-3.7.0/Include/* $BLENDER_PATH/python/include/python3.7m/ \ 
	&& rm -rf Python-3.7.0.tgz \ 
	&& rm -rf Python-3.7.0 

# RUN wget -qO- https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz \
#     | tar -xz --strip-components=1 -C ${BLENDER_HOME}/python

# # Update Python packages in Blender
# RUN ${BLENDERPY} -m ensurepip && \
#     ${BLENDERPIP} install --upgrade pip && \
#     ${BLENDERPIP} install numpy

# Blender comes with a super outdated version of numpy (which is needed for matplotlib / opencv) so override it with a modern one
# RUN rm -rf ${BLENDER_PATH}/python/lib/python3.7m/site-packages/numpy 

# Must first ensurepip to install Blender pip3 and then new numpy
# RUN ${BLENDERPY} -m ensurepip && ${BLENDERPIP} install --upgrade pip && ${BLENDERPIP} install numpy


# Set the working directory
# =============================================================================

WORKDIR /
# WORKDIR ${BLENDER_HOME}
