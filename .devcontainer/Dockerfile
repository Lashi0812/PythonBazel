FROM nvidia/cuda:12.1.0-devel-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
# ARG CUDA='cu121'

RUN --mount=type=cache,target=/var/cache/apt \
    apt update && \
    apt install -y bash \
                   build-essential \
                   git \
                   curl \
                   wget \
                   zsh \
                   ca-certificates \
                   unzip \
                   clang \
                   libatlas-base-dev liblapack-dev liblapacke-dev \
                   openmpi-bin libopenmpi-dev \
                   libboost-filesystem-dev libboost-python-dev libboost-test-dev \
                   gcc-mingw-w64 g++-mingw-w64 \
                   pkg-config libzmq3-dev doxygen libgraphviz-dev uuid-dev 

# instal conda 
RUN mkdir ~/miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh && \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 && \
    rm -rf ~/miniconda3/miniconda.sh 

COPY .devcontainer/environment.yml /workspace/environment.yml
RUN ~/miniconda3/bin/conda env create -f /workspace/environment.yml

# zsh plugin
ENV SHELL /bin/zsh
COPY .devcontainer/zsh-plugins/.p10k.zsh .devcontainer/zsh-plugins/ohmyzsh.sh /root/
RUN chmod +x /root/ohmyzsh.sh && sh -c /root/ohmyzsh.sh

# install cmake
ARG CMAKE_VERSION=3.27.3
RUN curl -O -L https://github.com/Kitware/CMake/releases/download/v${CMAKE_VERSION}/cmake-${CMAKE_VERSION}-linux-x86_64.sh && \
    chmod +x cmake-${CMAKE_VERSION}-linux-x86_64.sh && \
    yes | sh cmake-${CMAKE_VERSION}-linux-x86_64.sh --skip-license --prefix=/usr/local && \
    rm cmake-${CMAKE_VERSION}-linux-x86_64.sh

#* install bazel
ARG BAZEL_VERSION=6.1.2
RUN curl -O -L https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh && \
    chmod +x bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh && \
    ./bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh

# Download and install Buildifier
RUN curl -L -o /usr/local/bin/buildifier \
    https://github.com/bazelbuild/buildtools/releases/download/v6.4.0/buildifier-linux-amd64 && \
    chmod +x /usr/local/bin/buildifier

# set cuda env in .zshrc
RUN echo 'export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}' >> /root/.zshrc && \
    echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> /root/.zshrc && \
    echo 'export CUDA_HOME=/usr/local/cuda' >> /root/.zshrc