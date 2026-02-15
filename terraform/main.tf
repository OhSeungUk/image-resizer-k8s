terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "frontend" {
  # 변수를 조합해서 이미지 이름을 만듭니다
  name         = "${var.docker_username}/${var.project_name}-frontend:latest"
  keep_locally = false
}

resource "docker_container" "frontend_server" {
  image = docker_image.frontend.image_id
  name  = "terraform-frontend"

  ports {
    internal = 3000
    external = var.external_port
  }
}