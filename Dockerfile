# syntax=docker/dockerfile:1
FROM ubuntu:14.04

# Define not interactive
ENV DEBIAN_FRONTEND=noninteractive

# # Create a non-root user
# RUN useradd -G sudo --create-home --system --shell /bin/bash iibm && \
#     echo "iibm ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/iibm && \
#     chown -R iibm:iibm /home/iibm && \ 
#     echo "export PATH=/home/iibm/.local/bin:$PATH" >> /home/iibm/.bashrc

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential sudo git wget bc unzip \
    python python-wxgtk2.8 python-dev python-pip python-serial gcc g++ \
    libgif-dev libpng12-dev make bash okular libboost-thread-dev libboost-system-dev cmake && \
    ldconfig

# Copy source code to the container
WORKDIR /fabmodules
COPY . .
# Build the software
RUN make clean && make fab -j $(nproc) && make install

# Run the software
CMD ["/usr/local/bin/fab"]
