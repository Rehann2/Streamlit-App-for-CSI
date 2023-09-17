# Streamlit-App-for-CSI

This repository is the application implementation my internship project The Climate Stress Index. The Index provides an in detail knowledge of the situation of climate stress at a global scale on a granular level.

## Climate Stress Index
The index is a one of a kind tool that provides climate stress data at very high resolution of 1x1km, it is build by using variables from multiple domains to provide it a robust structure. The index can be used to create impact on a reasonable scale, since it is public it can be used by small and big organisations alike.

# Streamlit App Dockerized

This repository contains a Streamlit app that's been containerized with Docker for easy deployment. The app provides valuable insights into climate stress using high-resolution data.

## Getting Started

To run this app locally, you'll need to have Docker installed on your machine. If you haven't already, you can download and install Docker from [Docker's official website](https://www.docker.com/get-started).

### Clone the Repository

Clone this repository to your local environment:

```bash
git clone https://github.com/Rehann2/Streamlit-App-for-CSI.git
cd your-repo
```


## Requirements

To install requirements:

```setup
pip install -r requirements.txt
```

## Build the Docker Image
# Build the Docker image with a name of your choice (e.g., "my-streamlit-app") using the provided Dockerfile:
```bash
Copy code
docker build -t my-streamlit-app .
```

## Run the Docker Container
# Run the Docker container, specifying a name (e.g., "my-app-container"), a local port (e.g., 8501) to map to the container's port, and the container's port (typically 8501 for Streamlit):

```bash
Copy code
docker run -d --name my-app-container -p 8501:8501 my-streamlit-app
You can now access the app in your web browser at http://localhost:8501.
```

## Stopping and Removing the Container
# When you're done using the app, stop and remove the container:

```bash
Copy code
docker stop my-app-container
docker rm my-app-container
```
> This installs all the necessary libraries such as pandas,streamlit,rasterio,matplotlib etc.

## Representation
The streamlit application shows an implementation of the the Climate Stress Index for Austria specifically. Global data will be accessible in the near future.